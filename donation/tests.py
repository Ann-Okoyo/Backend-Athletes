from django.test import TestCase
from donation.models import Donation

class DonationModelTest(TestCase):
    def test_create_donation(self):
       
        donation = Donation.objects.create(amount=100.50)
        
        saved_donation = Donation.objects.get(id=donation.id)

        self.assertEqual(saved_donation.amount, 100.50)