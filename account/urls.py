from django.urls import path, include
from account.views import registerView, logoutView, loginView, profileView, profileEdit, userProfile

urlpatterns = [
    # path('', include('staticapp.urls'), name='home'),
    path('register/', registerView, name='register'),
    path('logout/', logoutView, name='logout'),
    path('login/', loginView, name='login'),
    path('profile/', profileView, name='profile'),
    path('user-profile/<str:pk>', userProfile, name='user-profile'),
    path('profile/edit', profileEdit, name='profile-edit'),
]