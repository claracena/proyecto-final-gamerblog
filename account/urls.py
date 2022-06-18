from django.urls import path, include
from account.views import registerView, logoutView, loginView, blogView, profileView

urlpatterns = [
    # path('', include('staticapp.urls'), name='home'),
    path('register/', registerView, name='register'),
    path('logout/', logoutView, name='logout'),
    path('login/', loginView, name='login'),
    path('blog/', blogView, name='blog'),
    path('profile/', profileView, name='profile'),
]