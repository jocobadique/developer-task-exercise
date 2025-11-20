from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.services.shifts_service import list_shifts, create_shift

class ShiftsView(APIView):
    def get(self, request):
        return Response(list_shifts())

    def post(self, request):
        worker_id = int(request.data.get("worker_id"))
        start = request.data.get("start")
        end = request.data.get("end")

        try:
            shift = create_shift(worker_id, start, end)
            return Response(shift, status=201)
        except ValueError as e:
            return Response({"error": str(e)}, status=400)
