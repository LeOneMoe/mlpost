from django.conf.urls import url
from django.contrib import admin
from mostlikes import views


urlpatterns = [
    url('^api/mlpost$', views.MLPostView),
    url(r'^admin/', admin.site.urls),
    url(r'^', views.IndexView),
]
