from django.conf.urls import url

from .views import LinksIndexView, LinkDetailView, LinksByTagView


urlpatterns = [
    url(
        regex=r'^$',
        view=LinksIndexView.as_view(),
        name='index'),
    url(
        regex=r'^(?P<slug>[0-9A-Za-z-_]+)/$',
        view=LinkDetailView.as_view(),
        name='link'),
    url(
        regex=r'^tag/(?P<slug>[0-9A-Za-z-_]+)/$',
        view=LinksByTagView.as_view(),
        name='tag'),
]
