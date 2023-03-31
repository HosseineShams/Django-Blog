from django.urls import path
from .views import *

app_name = 'accounts'
urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('signup/', signup_view, name='signup'),
]
