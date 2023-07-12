from django.urls import path
from.import views

urlpatterns = [
    path('',views.cat,name='hm'),
    path('<slug:c_slug>/',views.home,name='prod_cat'),
    path('proprty',views.home,name='property'),
    path('<slug:c_slug>/<slug:product_slug>',views.proddetails,name='details'),
    path('about',views.detail,name='about'),


]