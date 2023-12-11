from django.urls import path
from drink import views


urlpatterns = [
    path('drinks/', views.drinks, name='drinks'),
    path('drinks/<int:drink_id>', views.detail, name='detail')
]
