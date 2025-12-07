from django.urls import path
from .views import ContentModerationListCreateView, ContentModerationDetailUpdateView

urlpatterns = [
    path('', ContentModerationListCreateView.as_view(), name='moderation-list-create'),
    path('<int:pk>/', ContentModerationDetailUpdateView.as_view(), name='moderation-detail-update'),
]