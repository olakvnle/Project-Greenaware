from django.test import TestCase
from .models import UserAccount
from django.core.exceptions import ValidationError

class UserAccountModelTests(TestCase):

    def test_create_user(self):
        # Test the user creation with minimum required fields
        user = UserAccount.objects.create_user(email='normal@user.com', password='foo')
        self.assertEqual(user.email, 'normal@user.com')
        self.assertTrue(user.check_password('foo'))
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_observer)

    def test_create_user_without_email(self):
        # Test creating a user without an email raises a ValueError
        with self.assertRaises(ValueError):
            UserAccount.objects.create_user(email=None, password='foo')

    def test_create_superuser(self):
        # Test creating a superuser
        superuser = UserAccount.objects.create_superuser(email='super@user.com', password='foo')
        self.assertEqual(superuser.email, 'super@user.com')
        self.assertTrue(superuser.check_password('foo'))
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)

    def test_get_full_name(self):
        # Test the get_full_name method
        user = UserAccount.objects.create_user(email='test@user.com', first_name='John', last_name='Doe', password='foo')
        self.assertEqual(user.get_full_name(), 'John Doe')

    def test_str_representation(self):
        # Test the __str__ method
        user = UserAccount.objects.create_user(email='test@user.com', password='foo')
        self.assertEqual(str(user), 'test@user.com')
