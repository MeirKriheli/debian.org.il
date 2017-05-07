from django.conf.urls import url

from .views import TipsIndexView, TipDetailView, TipsByTagView


urlpatterns = [
    url(
        regex=r'^$',
        view=TipsIndexView.as_view(),
        name='index'),
    url(
        regex=r'^(?P<slug>[0-9A-Za-z-_]+)/$',
        view=TipDetailView.as_view(),
        name='tip'),
    url(
        regex=r'^tag/(?P<slug>[0-9A-Za-z-_]+)/$',
        view=TipsByTagView.as_view(),
        name='tag'),
]
