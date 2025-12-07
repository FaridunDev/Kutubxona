from django.urls import path
from .views import BorrowingListCreateView, BorrowingReturnView

urlpatterns = [
    path('', BorrowingListCreateView.as_view(), name='borrowing-list-create'),
    path('<int:pk>/return/', BorrowingReturnView.as_view(), name='borrowing-return'),
]