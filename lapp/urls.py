"""
URL configuration for localeaf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include, re_path
from django.views.static import serve

urlpatterns = [
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root':settings.STATIC_ROOT}),
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('supplier', views.supplier, name='supplier'),
    path('s_inventory', views.s_inventory, name='s_inventory'),

    path('buyer', views.buyer, name='buyer'),
    path('buying', views.buying, name='buying'),
    path('b_orderhistory', views.b_orderhistory, name='b_orderhistory'),

    # Buyer Options
    path('receive_order/<int:pk>/', views.receive_order, name='receive_order'),
    path('delete_order/<int:pk>/', views.delete_order, name='delete_order'),
    path('return_order/<int:pk>/', views.return_order, name='return_order'),
    path('pay_order/<int:pk>/', views.pay_order, name='pay_order'),
    
    #Supplier Options
    path('accept_order/<int:pk>/', views.accept_order, name='accept_order'),
    path('sent_order/<int:pk>/', views.sent_order, name='sent_order'),
    path('decline_order/<int:pk>/', views.decline_order, name='decline_order'),
    path('receive_payment/<int:pk>/', views.receive_payment, name='receive_payment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT)
