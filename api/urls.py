from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('athletes/', views.AthleteListView.as_view(), name='user-list'),
    path('athletes/<int:id>/', views.AthleteDetailView.as_view(), name='user-list'),
    path('users/<int:id>/', views.UserDetailView.as_view(), name='user-list'),
    path('sponsors/', views.SponsorListView.as_view(), name='user-list'),
    path('sponsors/<int:id>/', views.SponsorDetailView.as_view(), name='user-list'),
    path('donations/', views.DonationListView.as_view(), name='donation-list'),
    path('donations/<int:id>/', views.DonationDetailView.as_view(), name='donation-detail'),
]
