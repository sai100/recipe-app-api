'''
Tests for Django admin modifications.
'''


from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import Client


class AdminSiteTests(TestCase):
    '''Tests for django admin.'''

    def setUp(self):
        '''Setup '''

        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='password'
        )

        self.client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='testpass123',
            name='Test User'
        )

    def test_users_list(self):
        '''Test that users are listed on page.'''

        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_edit_user_page(self):
        '''Tests the edit user page works.'''

        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        '''Tests the create user page works.'''

        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
