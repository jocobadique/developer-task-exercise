from rest_framework.views import APIView
from rest_framework.response import Response

from api.services.workers_service import (
    list_workers, create_worker, get_worker, update_worker, delete_worker
)

class WorkersView(APIView):
    def get(self, request):
        return Response(list_workers())

    def post(self, request):
        name = request.data.get("name")
        return Response(create_worker(name))


class WorkerDetailView(APIView):
    def get(self, request, worker_id):
        worker = get_worker(worker_id)
        return Response(worker or {}, status=200 if worker else 404)

    def put(self, request, worker_id):
        name = request.data.get("name")
        updated = update_worker(worker_id, name)
        return Response(updated or {}, status=200 if updated else 404)

    def delete(self, request, worker_id):
        delete_worker(worker_id)
        return Response({"status": "deleted"})
