from google.cloud import datastore
from datetime import datetime, timezone
import dateutil.parser

from .datastore import client
from .timezone_settings_service import get_timezone
from .timezone_utils import to_utc, from_utc


def format_shift(entity):
    tz = get_timezone()
    return {
        "id": entity.key.id,
        "worker_id": entity["worker_id"],
        "start": from_utc(entity["start_utc"], tz),
        "end": from_utc(entity["end_utc"], tz),
        "duration_hours": _calculate_duration(entity["start_utc"], entity["end_utc"])
    }


def _parse(dt):
    return dateutil.parser.isoparse(dt)


def list_shifts():
    query = client.query(kind="Shift")
    entities = list(query.fetch())

    tz = get_timezone()

    result = []
    for e in entities:
        result.append({
            "id": e.key.id,
            "worker_id": e["worker_id"],
            "start": from_utc(e["start_utc"], tz),
            "end": from_utc(e["end_utc"], tz),
            "duration_hours": _calculate_duration(e["start_utc"], e["end_utc"])
        })
    return result


def _calculate_duration(start_utc, end_utc):
    s = _parse(start_utc)
    e = _parse(end_utc)
    return (e - s).total_seconds() / 3600.0


def _check_overlap(worker_id, start_dt, end_dt):
    query = client.query(kind="Shift")
    query.add_filter("worker_id", "=", worker_id)
    query.add_filter("end_utc", ">", start_dt.isoformat())

    for s in query.fetch():
        existing_start = _parse(s["start_utc"])
        existing_end = _parse(s["end_utc"])

        if existing_start < end_dt and existing_end > start_dt:
            return s.key.id
    return None


def create_shift(worker_id, start_local_iso, end_local_iso):
    tz = get_timezone()

    start_utc = to_utc(start_local_iso, tz)
    end_utc = to_utc(end_local_iso, tz)

    start_dt = _parse(start_utc)
    end_dt = _parse(end_utc)

    if end_dt <= start_dt:
        raise ValueError("End must be after start")

    duration = (end_dt - start_dt).total_seconds() / 3600
    if duration > 12:
        raise ValueError("Shift exceeds 12 hours")

    overlap = _check_overlap(worker_id, start_dt, end_dt)
    if overlap:
        raise ValueError(f"Shift overlaps with shift ID {overlap}")

    key = client.key("Shift")
    ent = datastore.Entity(key=key)
    ent.update({
        "worker_id": worker_id,
        "start_utc": start_utc,
        "end_utc": end_utc
    })
    client.put(ent)

    return {"id": ent.key.id}



def get_shift(pk):
    key = client.key("Shift", pk)
    entity = client.get(key)

    if entity is None:
        return None

    return format_shift(entity)



def update_shift(pk, worker_id, start_local_iso, end_local_iso):
    tz = get_timezone()

    # Convert to UTC same as create
    new_start_utc = to_utc(start_local_iso, tz)
    new_end_utc = to_utc(end_local_iso, tz)

    new_start_dt = _parse(new_start_utc)
    new_end_dt = _parse(new_end_utc)

    key = client.key("Shift", pk)
    shift = client.get(key)

    if shift is None:
        raise ValueError("Shift not found")

    # Validation
    if new_end_dt <= new_start_dt:
        raise ValueError("End must be after start")

    duration = (new_end_dt - new_start_dt).total_seconds() / 3600
    if duration > 12:
        raise ValueError("Shift exceeds 12 hours")

    # Check for overlap (exclude itself)
    query = client.query(kind="Shift")
    query.add_filter("worker_id", "=", worker_id)
    query.add_filter("end_utc", ">", new_start_utc)

    for s in query.fetch():
        if s.key.id != pk:
            existing_start = _parse(s["start_utc"])
            existing_end = _parse(s["end_utc"])

            if existing_start < new_end_dt and existing_end > new_start_dt:
                raise ValueError(f"Shift overlaps with shift ID {s.key.id}")

    # Update record
    shift["worker_id"] = worker_id
    shift["start_utc"] = new_start_utc
    shift["end_utc"] = new_end_utc

    client.put(shift)

    # Return formatted like list_shifts()
    return {
        "id": shift.key.id,
        "worker_id": worker_id,
        "start": from_utc(new_start_utc, tz),
        "end": from_utc(new_end_utc, tz),
        "duration_hours": (new_end_dt - new_start_dt).total_seconds() / 3600
    }



def delete_shift(pk):
    key = client.key("Shift", pk)
    shift = client.get(key)

    if shift is None:
        raise ValueError("Shift not found")

    client.delete(key)