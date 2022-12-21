
from django.test import TestCase


_models = __import__("MVC Structure.Model.models")
_models = _models.Model.models


class MyUserManagerTest(TestCase):
    def setUp(self):
        self.user = _models.User.objects._create_user('user@gmail.com','top_secret')
        self.super_user = _models.User.objects.create_superuser('super_user@gmail.com','top2_secret')

    def test_get_full_name_user(self):
        expcted_result = 'user@gmail.com'
        self.assertEqual(self.user.get_full_name(), expcted_result, 'Full name for user should be test1@gmail.com')

    def test_get_full_name_super(self):
        expcted_result = 'super_user@gmail.com'
        self.assertEqual(self.super_user.get_full_name(), expcted_result, 'Full name for super user should be test2@gmail.com')

    def test_get_short_name_user(self):
        expcted_result = 'user@gmail.com'
        self.assertEqual(self.user.get_short_name(), expcted_result, 'Short name for user should be test1@gmail.com')

    def test_get_short_name_super(self):
        expcted_result = 'super_user@gmail.com'
        self.assertEqual(self.super_user.get_short_name(), expcted_result, 'Short name for super user should be test2@gmail.com')

    def test_is_staff(self):
        self.assertFalse(self.user.is_staff, "Normal user should not be an staff,")
        self.assertTrue(self.super_user.is_staff, "Super user is also an staff.")

    def test_is_active(self):
        self.assertTrue(self.user.is_active, "Normal user should be an active user.")
        self.assertTrue(self.super_user.is_active, "Super user should be always an active user.")

    def test_is_superuser(self):
        self.assertTrue(self.super_user.is_superuser, "A super user must have activate super user functionallity")
