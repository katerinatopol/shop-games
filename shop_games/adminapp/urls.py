import adminapp.views as adminapp
from django.urls import path

app_name = 'adminapp'

urlpatterns = [
    path('users/create/', adminapp.user_create, name='user_create'),
    path('users/read/', adminapp.users, name='users'),
    path('users/update/<int:pk>/', adminapp.user_update, name='user_update'),
    path('users/delete/<int:pk>/', adminapp.user_delete, name='user_delete'),

    path('categories/create/', adminapp.category_create, name='category_create'),
    path('categories/read/', adminapp.categories, name='categories'),
    path('categories/update/<int:pk>/', adminapp.category_update, name='category_update'),
    path('categories/delete/<int:pk>/', adminapp.category_delete, name='category_delete'),

    path('games/create/category/<int:pk>/', adminapp.game_create, name='gamet_create'),
    path('games/read/category/<int:pk>/', adminapp.games, name='games'),
    path('games/read/<int:pk>/', adminapp.game_read, name='game_read'),
    path('games/update/<int:pk>/', adminapp.game_update, name='game_update'),
    path('games/delete/<int:pk>/', adminapp.game_delete, name='game_delete'),
]
