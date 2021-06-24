# blog.urls.py

from django.urls import path

from blog import views


app_name = 'blog'
urlpatterns = [
    path(route="sport/", view=views.post_sport_view, name='post_sport_list'),
    path(route="politique/", view=views.post_politique_view, name='post_politique_list'),
    path(route="religion/", view=views.post_religion_view, name='post_religion_list'),
    path(route="communique/", view=views.post_communique_view, name='post_communique_list'),
    path(route="societe/", view=views.post_societe_view, name='post_societe_list'),
    path(route="bouake-news/", view=views.post_bknews_view, name='post_bknews_list'),
    path(route="international/", view=views.post_international_view, name='post_international_list'),
    path(route='article/<date>-<slug>-<pk>/', view=views.post_detail_view, name='post_detail')
]
