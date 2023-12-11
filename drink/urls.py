from django.urls import path
from drink import views

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('drinks/', views.drinks, name='drinks'),
    path('drinks/<int:drink_id>', views.detail, name='detail')
]

# allows display of data in json format in the browser, instead of the default HTML view provided by Django REST Framework
urlpatterns = format_suffix_patterns(urlpatterns)
