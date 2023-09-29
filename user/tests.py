from django.test import TestCase
from django.contrib.auth.models import Group
from phonenumber_field.modelfields import PhoneNumber
from .models import CustomUser

class CustomUserModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            username='testuser',
            email='test@example.com',
            role='regular_user',
            password='testpassword',
        )
        self.group = Group.objects.create(name='Test Group')

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.role, 'regular_user')
        self.assertEqual(self.user.password, 'testpassword')

    def test_user_string_representation(self):
        self.assertEqual(str(self.user), 'test@example.com')

    def test_user_group_membership(self):
        self.user.groups.add(self.group)
        self.assertIn(self.group, self.user.groups.all())

    def test_user_phone_number_field(self):
        self.user.phone_number = PhoneNumber.from_string('+1234567890')
        self.assertEqual(self.user.phone_number.as_e164, '+1234567890')

    def test_user_confirm_password_field(self):
        self.user.confirm_password = 'testpassword'
        self.assertEqual(self.user.confirm_password, 'testpassword')

    def test_user_role_choices(self):
        self.assertEqual(self.user.role, 'regular_user')
        self.user.role = 'athlete'
        self.assertEqual(self.user.role, 'athlete')
        self.user.role = 'admin'
        self.assertEqual(self.user.role, 'admin')

