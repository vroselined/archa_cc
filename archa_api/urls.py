from django.urls import path
from .views import TransactionView
from .views import TransactionDetailView

urlpatterns = [
    path('transactions/', TransactionView.as_view(), name='transaction'),
    path('transactions/<int:id>', TransactionDetailView.as_view(), name='transaction-detail'),
]
