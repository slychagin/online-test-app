from django.urls import path
from tests import views

urlpatterns = [
    path('', views.tests, name='tests'),
    path('<slug:category_slug>/', views.tests, name='test_by_category'),
]
