from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('chome',HomeView.as_view(),name="chome"),
    path('prod/<str:cat>',ProductView.as_view(),name="prod"),
    path('proddet/<int:pid>',ProductDetailsView.as_view(),name="det"),
    path('addtocart/<int:pid>',addtoCart,name="acart"),
    path('cartlist',CartListView.as_view(),name="clist"),
    path('dcart/<int:id>',Deletecart,name="dcart"),
    path('checkout/<int:cid>',CheckoutView.as_view(),name="cout"),
    path('orderlist',OrderListView.as_view(),name="olist"),
    path('cancelorder/<int:oid>',cancelorder,name="cancel")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)