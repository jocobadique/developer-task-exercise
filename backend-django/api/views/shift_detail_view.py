from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.services.shifts_service import (
    get_shift,
    update_shift,
    delete_shift,
)

class ShiftDetailView(APIView):

    def get(self, request, pk):
        shift = get_shift(pk)
        if shift is None:
            return Response({"error": "Shift not found"}, status=404)
        return Response(shift)

    def put(self, request, pk):
        worker_id = int(request.data.get("worker_id"))
        start = request.data.get("start")
        end = request.data.get("end")

        try:
            updated = update_shift(pk, worker_id, start, end)
            return Response(updated)
        except ValueError as e:
            return Response({"error": str(e)}, status=400)

    def delete(self, request, pk):
        try:
            delete_shift(pk)
            return Response(status=204)
        except ValueError as e:
            return Response({"error": str(e)}, status=400)
