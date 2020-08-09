from django.urls import path

from user import views

app_user = 'user'

urlpatterns = [
  path('create/', views.CreateUserView.as_view(), name='create'),
]