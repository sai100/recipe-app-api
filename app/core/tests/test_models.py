'''
Tests for models.
'''
from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def create_user(**params):
    '''Create and returns a user.'''
    return get_user_model().objects.create_user(**params)


class ModelTests(TestCase):
    '''Test models.'''

    def test_create_user_with_email_successful(self):
        '''Test creating a user with email is successful.'''
        email = 'test@example.com'
        password = 'testpass123'

        user = create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        '''Test email is noramlized for new users.'''

        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com']
        ]

        for email, expected_email in sample_emails:
            user = create_user(email=email, password='sample123')
            self.assertEqual(user.email, expected_email)

    def test_new_user_without_email_raises_error(self):
        '''Test that creating a user without email raises ValueError.'''

        with self.assertRaises(ValueError):
            create_user(email='', password='test123')

    def test_create_superuser(self):
        '''Test creating a new super user.'''

        user = get_user_model().objects.create_superuser(
            email='test@example.com',
            password='test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe(self):
        '''Test creating a recipe.'''

        user = create_user(
            email='test@example.com',
            password='testpass123'
        )

        recipe = models.Recipe.objects.create(
            user=user,
            title='Sample recipe name',
            time_minutes=5,
            price=Decimal('5.50'),
            description='Sample recipe description,',
        )

        self.assertEqual(str(recipe), recipe.title)

    def test_create_tag(self):
        '''Test creating tag.'''

        user = create_user(
            email='user@example.com',
            password='testpass123',
        )
        tag = models.Tag.objects.create(user=user, name='Tag1')

        self.assertEqual(str(tag), tag.name)
