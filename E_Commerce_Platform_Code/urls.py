
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns


# app_name = 'Route'
views = __import__("MVC Structure.Controller.views")
views = views.Controller.views
# from MVC_Structure.Controller.views import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/signup/',views.sign_up,name='signup'),
    path('account/login/', views.login_user, name='login'),
    path('account/logout/', views.logout_user, name='logout'),
    path('account/profile/',views.user_profile, name='profile'),
    path('shop/add/<pk>', views.add_to_cart, name="add"),
    path('shop/remove/<pk>',views.remove_from_cart, name='remove'),
    path('shop/increase/<pk>', views.increase_cart, name='increase'),
    path('shop/decrease/<pk>', views.decrease_item, name='decrease'),
    path('shop/cart/',views.cart_view, name='cart'),
    path('payment/checkout/', views.checkout, name='checkout'),
    path('payment/pay/',views.payment, name="payment"),
    path('payment/status/',views.complete, name='complete'),
    path('payment/purchase/<val_id>/<tran_id>/', views.purchase, name='purchase'),
    path('payment/orders/', views.order_view, name='orders'),
    path('', views.Home.as_view(), name='home'),
    path('product/<pk>',views.ProductDetail.as_view(), name="product_detail"),
    # path('',include('App_Shop.urls')),
    # path('shop/', include('App_Order.urls')),
    # path('payment/', include('App_Payment.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
