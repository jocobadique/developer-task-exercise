# api/services/timezone_settings_service.py
from google.cloud import datastore
from .datastore import client

SETTINGS_KEY = ("Settings", "global")

def get_timezone():
    key = client.key(*SETTINGS_KEY)
    ent = client.get(key)
    if not ent:
        return "UTC"
    return ent.get("timezone", "UTC")

def set_timezone(tz: str):
    key = client.key(*SETTINGS_KEY)
    ent = datastore.Entity(key=key)
    ent.update({"timezone": tz})
    client.put(ent)
    return tz
