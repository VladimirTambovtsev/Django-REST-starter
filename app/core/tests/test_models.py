

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successfull(self):
        """Create new user with new email"""
        email = 'test@email.com'
        password = '1234567890'
        user = get_user_model().objects.create_user(
          email=email, password=password
          )
        self.assertEqual(user.email, email)
        self.assertEqual(user.check_password(password))
