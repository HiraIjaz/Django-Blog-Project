from django.urls import path

from . import views

urlpatterns = [
    path('', views.login_user, name='base'),
    path('signup/', views.signup, name='signup'),
    path('updateprofile/', views.update_profile, name='updateuser'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_user, name='logout')

]
