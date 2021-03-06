import rest_framework
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views
app_name = 'todoBoard_restapi_main'

router = routers.DefaultRouter()
router.register(r'todo_board', views.TodoBoard_restapi_main)

urlpatterns = [
    url('api-auth/', include('rest_framework.urls')),
    url(r'^$', views.TodoBoard_restapi_main.as_view(), name='todo'),
    url(r'^todo_list/$', views.TodoBoard_restapi_main.as_view(), name='todo_list'),
    url(r'^todo_list/create/$', views.TodoBoard_restapi_create.as_view(), name='todo_create'),
    url(r'^todo_list/(?P<no>\d+)/$', views.TodoBoard_restapi_detail.as_view(), name='todo_detail'),
    url(r'^todo_list/(?P<no>\d+)/update$', views.TodoBoard_restapi_update.as_view(), name='todo_update'),
    url(r'^todo_list/(?P<no>\d+)/delete$', views.TodoBoard_restapi_delete.as_view(), name='todo_delete')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)