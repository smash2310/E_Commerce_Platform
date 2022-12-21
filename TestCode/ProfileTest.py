from django.test import TestCase

_models = __import__("MVC Structure.Model.models")
_models = _models.Model.models

class ProfileTest(TestCase):
    def setUp(self):
        self.user1 = _models.User.objects._create_user('user1@gmail.com','top_secret')
        self.user2 = _models.User.objects._create_user('user2@gmail.com','top_secret')

        self.profile1 = _models.Profile.objects.get_or_create(user=self.user1)[0]
        self.profile2 = _models.Profile.objects.get_or_create(user=self.user2)[0]

    
        self.profile1.username = "test"
        self.profile1.full_name = "test user"
        self.profile1.address_1 = "django testdb"
        self.profile1.city = "mysqli"
        self.profile1.zipcode = "8880"
        self.profile1.country = "mysqli3"
        self.profile1.phone = "127001"
        self.profile1.save()


    def test_str(self):
        expected_string = "user1@gmail.com's Profile"
        self.assertEqual(self.profile1.__str__(), expected_string, "Represent string should be user+'s profile(user1@gmail.com's Profile)")

    def test_fully_filled(self):
        self.assertTrue(self.profile1.is_fully_filled(), "User1 should be fully filled.")

    def test_not_fully_filed(self):
        self.assertFalse(self.profile2.is_fully_filled(), "User2 should not be fully filed.")
