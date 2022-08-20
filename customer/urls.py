from django.urls import path
from customer import views
urlpatterns=[
    path("all",views.ViewAllBook.as_view(),name="c_name"),
    path("account/signup",views.SignUpView.as_view(),name="signup"),
    path("account/signin", views.SignInView.as_view(), name="signin"),
    path("account/signout",views.Sign_Out,name="signout"),
    path("customers/item/carts/add/<int:id>",views.AddToCartView.as_view(),name="addtocart"),
    path("customer/carts/items",views.CartItem.as_view(),name="listcardsitem"),
    path("customer/carts/items/remove/<int:id>",views.RemoveCartItem.as_view(),name="removecartitem"),
    path("customer/order/add/<int:p_id>/<int:c_id>",views.OrderView.as_view(),name="ordercreate"),
    path("customer/orders/",views.MyOrders.as_view(),name="myorders"),
    path("customers/orders/myorders/<int:id>",views.CancelOrder.as_view(),name="cancelorder")

]