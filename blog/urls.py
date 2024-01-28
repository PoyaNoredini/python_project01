from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    # path('PostList/', views.PostList, name='Post_List'),
    path('PostList/', views.PostListView.as_view(), name='Post_List'),
    path('PostDetails/<slug:post>//<int:pk>', views.PostDetails, name='PostDetails'),
    path('account_form/', views.UserAccount, name='account_form'),
]
