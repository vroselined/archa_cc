from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from django.test import TestCase

from .models import Transaction


class TransactionAPITests(APITestCase):
    # Set up test data before tests run
    def setUp(self):
        self.transaction_data = {
            "transaction_type": "DEPOSIT",
            "amount": 100.00,
            "description": "Initial deposit"
        }
        # This URL should correspond to your endpoint
        self.url = reverse('transaction')

    def test_create_transaction(self):
        # Test POST request to create a new transaction
        response = self.client.post(self.url, self.transaction_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Check if status is 201
        self.assertEqual(response.data['transaction_type'], "DEPOSIT")  # Check if data matches

    def test_get_transaction(self):
        # First, create a transaction
        post_response = self.client.post(self.url, self.transaction_data, format='json')
        transaction_id = post_response.data['id']

        # Now test GET request to retrieve the transaction
        response = self.client.get(reverse('transaction-detail', args=[transaction_id]), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Check if status is 200
        self.assertEqual(response.data['transaction_type'], "DEPOSIT")  # Check if data matches
        self.assertEqual(response.data['amount'], "100.00")  # Check if amount is correct



class TransactionModelTest(TestCase):
    
    def setUp(self):
        # Create a deposit transaction instance
        self.transaction = Transaction.objects.create(
            transaction_type=Transaction.DEPOSIT,
            amount=100.00,
            description="Initial deposit"
        )
        
        # Create a withdrawal transaction instance
        self.withdrawal = Transaction.objects.create(
            transaction_type=Transaction.WITHDRAWAL,
            amount=50.00,
            description="Withdrawal"
        )

    def test_transaction_creation(self):
        """Test that a transaction is created correctly"""
        self.assertEqual(self.transaction.transaction_type, Transaction.DEPOSIT)
        self.assertEqual(self.transaction.amount, 100.00)
        self.assertEqual(self.transaction.description, "Initial deposit")
        
