"""Test the django admin modifications."""
from multiprocessing.connection import Client

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self):
        """Create a test user and client for the admin site."""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            'admin@admin.com',
            'test123'
        )
        self.client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(
            email='user@user.com',
            password='test123',
            name='Test User',
        )

    def test_users_listed(self):
        """Test listing of users at user page."""
        url = reverse("admin:core_user_changelist")
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works."""
        url = reverse("admin:core_user_change", args=[self.user.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, self.user.name)

    def test_create_user_page(self):
        """Test that the create user page works."""
        url = reverse("admin:core_user_add")
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
