# api/services/workers_service.py
from .datastore import client
from google.cloud import datastore

def list_workers():
    query = client.query(kind="Worker")
    entities = list(query.fetch())
    return [{"id": e.key.id, "name": e["name"]} for e in entities]

def create_worker(name: str):
    key = client.key("Worker")
    ent = datastore.Entity(key=key)
    ent.update({"name": name})
    client.put(ent)
    return {"id": ent.key.id, "name": name}

def get_worker(worker_id: int):
    key = client.key("Worker", worker_id)
    ent = client.get(key)
    if not ent:
        return None
    return {"id": ent.key.id, "name": ent["name"]}

def update_worker(worker_id: int, name: str):
    key = client.key("Worker", worker_id)
    ent = client.get(key)
    if not ent:
        return None
    ent["name"] = name
    client.put(ent)
    return {"id": worker_id, "name": name}

def delete_worker(worker_id: int):
    key = client.key("Worker", worker_id)
    client.delete(key)
    return True
