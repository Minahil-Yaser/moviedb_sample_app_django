from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'movietv'

urlpatterns = [
    path('', views.index, name='index'),
    path("home", views.index, name='index'),
    path("search/", views.search, name='search'),
    path("movie/<int:movie_id>/", views.movie_detail, name="moviedetail"),
    path("tv/<int:tv_id>/", views.tv_detail, name="tvdetail"),
    path("tv/<int:tv_id>/season/<int:season_number>/", views.season_detail, name="seasondetail"),
    path("tv/<int:tv_id>/season/<int:season_number>/episode/<int:episode_number>/", views.episode_detail, name="episodedetail"),
    path("movies", views.movies, name='movies'),
    path("tv", views.tv, name='tv'),
    path("person/<int:person_id>/", views.people, name='people'),
    path("people",views.ppeople, name='ppeople')
] 

urlpatterns += staticfiles_urlpatterns()