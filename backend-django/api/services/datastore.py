# api/services/datastore.py
from google.cloud import datastore
import os

def get_client():
    # When running locally with emulator:
    # DATASTORE_EMULATOR_HOST and DATASTORE_PROJECT_ID must be set
    project = os.getenv("DATASTORE_PROJECT_ID", "fc-itw-joco")
    return datastore.Client(project=project)

client = get_client()
