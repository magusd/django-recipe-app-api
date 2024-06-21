"""
Testing models.
"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test user models"""
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@example.com'
        password = 'test123'
        user = get_user_model().objects.create_user(
            email=email,password=password
        )
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))
        self.assertNotEqual(user.id, None)

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        sample_emails = [
            ["test1@EXAMPLE.com", "test1@example.com"],
            ["Test2@example.com", "test2@example.com"],
            ["TEST3@EXAMPLE.COM", "test3@example.com"],
            ["test4@EXAMPLE.com", "test4@example.com"],
        ]
        for email, expected_email in sample_emails:
            user = get_user_model().objects.create_user(email,'sample123')
            self.assertEqual(user.email,expected_email)

    def test_new_user_without_email_raises_error(self):
        """Assert that a new user without an email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

        # get_user_model().objects.create_user("sladkfj", 'test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)