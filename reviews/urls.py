from django.urls import path
from .views import ReviewListCreateView, ReviewDetailView

urlpatterns = [
    path('books/<int:book_pk>/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
]