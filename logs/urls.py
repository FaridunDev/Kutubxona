from django.urls import path
from .views import ActivityLogListView, ActivityLogDetailView

urlpatterns = [
    path('', ActivityLogListView.as_view(), name='activitylog-list'),
    path('<int:pk>/', ActivityLogDetailView.as_view(), name='activitylog-detail'),
]