from django.test import TestCase

_models = __import__("MVC Structure.Model.models")
_models = _models.Model.models

class CategoryTest(TestCase):
    def setUp(self):
        self.category = _models.Category.objects.create()
        self.category.title = "Electronics"
        self.category.save()
    def testTitle(self):
        expected_string = "Electronics"
        self.assertEqual(self.category.__str__(), expected_string, "String representation should be same as Category title.")
