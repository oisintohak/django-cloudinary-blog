from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('detail/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('create/', views.PostCreate.as_view(), name='post_create'),
    path('new-create/', views.PostCreate.as_view(), name='new_post_create')
    # path('update/<id>', views.PostUpdate.as_view(), name='post_update'),
    # path('delete/<id>', views.PostDelete.as_view(), name='post_delete'),
]
