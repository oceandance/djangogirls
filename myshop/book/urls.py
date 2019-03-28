from django.conf.urls import url
from django.urls import path

from book import views

urlpatterns = [
    path('', views.all_book_list, name='all_book_list'),
    path('book/<int:pk>/', views.book_info, name='book_info'),
    path('author/<int:pk>/', views.author_info, name='author_info'),
    path('user/<int:pk>/library', views.order_list, name='order_list'),
    path('', views.add_book, name='add_book'),

    # path('post/new/',views.post_new,name = 'post_new'),
    # path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    # path('drafts/', views.post_draft_list, name='post_draft_list'),
    # path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    # path('post/<pk>/remove/', views.post_remove, name='post_remove'),

]