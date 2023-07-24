from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/new/', post_new, name='post_new'),
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),
    path('signup/', register, name='signup'),
    path('profile/<int:pk>/', ShowProfilePageView.as_view(), name='profile_view'),
    path('create_profile/', CreateProfile.as_view(), name='create_profile'),
    path('post/<int:pk>/like/', like, name='like_post'),
    path('post/<int:pk>/comment/', add_comment, name='add_comment'),
    
]
