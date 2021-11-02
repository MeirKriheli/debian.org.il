from django.conf.urls import url

from .views import PageView

app_name = 'pages'

urlpatterns = [
    url(
        regex=r'^(?P<slug>[0-9A-Za-z-_]+)/$',
        view=PageView.as_view(),
        name='page'
    ),
    url(
        regex=r'^$',
        view=PageView.as_view(),
        name='index'
    ),
]
