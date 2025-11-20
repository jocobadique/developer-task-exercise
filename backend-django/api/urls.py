from django.urls import path
from api.views.timezone_view import TimezoneView
from api.views.workers_view import WorkersView, WorkerDetailView
from api.views.shifts_view import ShiftsView
from api.views.shift_detail_view import ShiftDetailView  


urlpatterns = [
    path("timezone/", TimezoneView.as_view()),
    path("workers/", WorkersView.as_view()),
    path("workers/<int:worker_id>/", WorkerDetailView.as_view()),
    path("shifts/", ShiftsView.as_view()),
    path("shifts/<int:pk>/", ShiftDetailView.as_view()), 
]
