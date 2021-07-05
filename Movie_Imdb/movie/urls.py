from django.conf.urls import url
from django.urls import path
from .views import index, search_movie, allmovies, registerMovie, handlelogin, handlelogout, delete_data,update_data

urlpatterns = [
    # url(r'^movies', IndexView.as_view(), name='index'),
    path('', index, name='index'),
    path('search_movie/', search_movie, name='search_movie'),
    path('allmovies/', allmovies, name='allmovies'),
    path('registerMovie/', registerMovie, name='registerMovie'),
    path('login', handlelogin, name="login"),
    path('logout', handlelogout, name="logout"),
    path('delete/<int:id>/', delete_data, name='delete'),
    path('<int:id>/', update_data, name='update')
]
