from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('add/listing', views.create_listing, name="add-listing"),
    path('add/category', views.add_category, name="add-category"),
    path('categoryList/', views.category_list, name="category-list"),
    path('categoryList/show/<id>', views.show_category, name="show-category"),
 
   

]