from django.test import TestCase

_models = __import__("MVC Structure.Model.models")
_models = _models.Model.models

class ProductTest(TestCase):
    def setUp(self):
        self.category = _models.Category()
        self.category.title = "Smartphone"
        self.category.save()

        self.product = _models.Product()
        self.product.name = "Iphone 12 pro max"
        self.product.category = self.category
        self.product.preview_text = "Iphone 12 pro max for sell"
        self.product.detail_text = "Iphone 12 pro max with 12 gb ram"
        self.product.price = 100000
        self.product.save()

    def test_oldPrice(self):
        self.assertEqual(self.product.old_price, 0, "Default old price should be 0")

    def test_str(self):
        expected_string = "Iphone 12 pro max"
        self.assertEqual(self.product.__str__(), expected_string, "String repsentation of a product should be same as product name")
