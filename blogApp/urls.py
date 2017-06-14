from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^blogs', views.show_blogs, name='index1'),
    url(r'^submit', views.submit, name='submit'),
    url(r'^blogApp/investigate', views.investigate, name='investigate'),
    url(r'^blogApp/train_ticket', views.stores, name='train'),
    url(r'^blogApp/flight', views.flight, name='flight'),
]