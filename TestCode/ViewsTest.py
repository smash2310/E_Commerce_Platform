from django.test import  TestCase, RequestFactory
from django.contrib.messages.storage.fallback import FallbackStorage


_views = __import__("MVC Structure.Controller.views")
_views = _views.Controller.views

# from Model.models import User, Profile, BillingAddress
_models = __import__("MVC Structure.Model.models")
_models = _models.Model.models


class ViewsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = _models.User.objects._create_user(email="test@gmail.com",password="top_secret")
        self.category = _models.Category()
        self.category.title = "mix"
        self.category.save()
        self.product = _models.Product()
        self.product.name = "Iphone 12 pro max"
        self.product.category = self.category
        self.product.preview_text = "Iphone 12 pro max for sell"
        self.product.detail_text = "Iphone 12 pro max with 12 gb ram"
        self.product.old_price = 120000
        self.product.price = 100000
        self.product.save()

        self.request = self.factory.get('/shop/add/1')
        self.request.user = self.user
        setattr(self.request, 'session', 'session')
        messages = FallbackStorage(self.request)
        setattr(self.request, '_messages', messages)
        self.response = _views.add_to_cart(self.request,1)


    def test_add_to_cart(self):

        cart = _models.Cart.objects.get(user=self.user)
        self.assertEqual(cart.quantity, 1, "quantity of an item should be 1 at first time.")

        self.response = _views.add_to_cart(self.request,1)
        self.response = _views.add_to_cart(self.request,1)
        self.response = _views.add_to_cart(self.request,1)

        cart = _models.Cart.objects.get(user=self.user)

        self.assertEqual(self.response.status_code, 302, "Should get a successfull response.")
        self.assertEqual(cart.quantity, 4, "Same product should add to the same cart 3 time.")
        self.assertFalse(cart.purchased, "Purchased should be false by default.")
        self.assertEqual(cart.item.name, "Iphone 12 pro max", "Should add the 1st product in the cart.")

    def test_increase_cart(self):
        request = self.factory.get('/shop/increase/1')
        request.user = self.user
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)
        response = _views.increase_cart(request,1)
        cart = _models.Cart.objects.get(user=request.user)

        self.assertEqual(response.status_code, 302, "Should get a successfull response.")
        self.assertEqual(cart.quantity, 2, "quantity of an item should be zero at first time.")
        self.assertFalse(cart.purchased, "Purchased should be false by default.")
        self.assertEqual(cart.item.name, "Iphone 12 pro max", "Should add the 1st product in the cart.")

    def test_decrease_item(self):
        response = _views.add_to_cart(self.request,1)
        request = self.factory.get('/shop/decrease/1')
        request.user = self.user
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)
        response = _views.decrease_item(request,1)
        cart = _models.Cart.objects.get(user=request.user)

        self.assertEqual(response.status_code, 302, "Should get a successfull response.")
        self.assertEqual(cart.quantity, 1, "quantity of an item should be zero at first time.")
        self.assertFalse(cart.purchased, "Purchased should be false by default.")
        self.assertEqual(cart.item.name, "Iphone 12 pro max", "Should add the 1st product in the cart.")

    def test_remove_from_cart(self):
        request = self.factory.get('/shop/remove/1')
        request.user = self.user
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)
        response = _views.remove_from_cart(request,1)
        order_item = _models.Cart.objects.filter(item=self.product, user=request.user, purchased=False)

        self.assertEqual(response.status_code, 302, "Should get a successfull response.")
        self.assertEqual(len(order_item), 0 , "Cart should be remove from order")
