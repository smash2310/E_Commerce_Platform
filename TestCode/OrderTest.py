from django.test import TestCase

_models = __import__("MVC Structure.Model.models")
_models = _models.Model.models

class OrderTest(TestCase):
    def setUp(self):
        self.user = _models.User.objects._create_user('user1@gmail.com','top_secret')

        self.category = _models.Category()
        self.category.title = "Bike & Accessories"
        self.category.save()

        self.product1 = _models.Product()
        self.product1.name = "Yamha R15"
        self.product1.category = self.category
        self.product1.preview_text = "Yamha R15 2021 Indonesian Verson"
        self.product1.detail_text = "Yamha R15 150cc with 45 mileage."
        self.product1.price = 525000
        self.product1.save()

        self.cart1 = _models.Cart()
        self.cart1.user = self.user
        self.cart1.item = self.product1
        self.cart1.quantity = 1
        self.cart1.save()

        self.product2 = _models.Product()
        self.product2.name = "Vemos Helmet250"
        self.product2.category = self.category
        self.product2.preview_text = "Helmet 250 with indicator light"
        self.product2.detail_text = "A helmet with more safety as well as comfortable"
        self.product2.price = 5000
        self.product2.save()

        self.cart2 = _models.Cart()
        self.cart2.user = self.user
        self.cart2.item = self.product2
        self.cart2.quantity = 2
        self.cart2.save()

        self.order = _models.Order()
        self.order.user = self.user
        self.order.save()
        self.order.orderitems.add(self.cart1)
        self.order.orderitems.add(self.cart2)


    def testGet_total(self):
        expcted_result = "535000"
        self.assertEqual(self.order.get_total(), expcted_result, "Total amount should be 525000 + 5000 = 530000.")

    def testGet_total(self):
        expcted_result = "10000.00"
        self.assertEqual(self.cart2.get_total(), expcted_result, "Total amount should be 2* 5000 = 10000.")
