from django.test import TestCase

_models = __import__("MVC Structure.Model.models")
_models = _models.Model.models

class CartTest(TestCase):
    def setUp(self):
        self.user = _models.User.objects._create_user('user1@gmail.com','top_secret')

        self.category = _models.Category()
        self.category.title = "Laptop"
        self.category.save()

        self.product = _models.Product()
        self.product.name = "Apple Macbook pro 13"
        self.product.category = self.category
        self.product.preview_text = "Apple Macbook pro 13 for sell"
        self.product.detail_text = "Apple Macbook pro 13 with 12 gb ram"
        self.product.price = 100000
        self.product.save()

        self.cart = _models.Cart()
        self.cart.user = self.user
        self.cart.item = self.product
        self.cart.quantity = 2
        self.cart.save()

    def testGet_total(self):
        expcted_result = "200000.00"
        self.assertEqual(self.cart.get_total(), expcted_result, "Total amount should be 2*100000 = 200000.")

    def testStr(self):
        expected_string = "2 X Apple Macbook pro 13"
        self.assertEqual(self.cart.__str__(), expected_string, "String representation should be quantity X item name(2 X Apple Macbook pro 13)")
