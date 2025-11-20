from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.services.timezone_utils import validate_timezone
from api.services.timezone_settings_service import get_timezone, set_timezone


class TimezoneView(APIView):
    def get(self, request):
        return Response({"timezone": get_timezone()})

    def put(self, request):
        tz = request.data.get("timezone")
        if not tz or not validate_timezone(tz):
            return Response({"error": "Invalid timezone"}, status=400)
        set_timezone(tz)
        return Response({"timezone": tz})
