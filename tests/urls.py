from django.urls import path
from tests import views

urlpatterns = [
    path('', views.tests, name='tests'),
    path('<slug:category_slug>/', views.tests, name='test_by_category'),
    path('<slug:category_slug>/<slug:test_slug>/', views.test_description, name='test_description'),
    path(
        '<slug:category_slug>/<slug:test_slug>/<int:question_id>/',
        views.question_details,
        name='question_details'
    ),
    path(
        '<slug:category_slug>/<slug:test_slug>/results/',
        views.results,
        name='results'
    )
]
