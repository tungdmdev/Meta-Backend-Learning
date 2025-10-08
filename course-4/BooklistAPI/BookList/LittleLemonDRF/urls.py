from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('books', views.BookView.as_view()),
    path('books/<int:pk>', views.SingleBookView.as_view()),
    path('menu-items', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('categories', views.CategoriesView.as_view()),
    path('secret/',views.secret),
    path('ratings', views.RatingsView.as_view()),
]