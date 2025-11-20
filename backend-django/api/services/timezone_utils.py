# api/services/timezone_utils.py
from datetime import datetime
from zoneinfo import ZoneInfo
import dateutil.parser

def validate_timezone(tz: str):
    try:
        ZoneInfo(tz)
        return True
    except:
        return False

def to_utc(dt_iso: str, tz_str: str):
    dt = dateutil.parser.isoparse(dt_iso)

    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=ZoneInfo(tz_str))

    dt_utc = dt.astimezone(ZoneInfo("UTC"))
    return dt_utc.isoformat()

def from_utc(utc_iso: str, tz_str: str):
    dt_utc = dateutil.parser.isoparse(utc_iso)
    return dt_utc.astimezone(ZoneInfo(tz_str)).isoformat()
