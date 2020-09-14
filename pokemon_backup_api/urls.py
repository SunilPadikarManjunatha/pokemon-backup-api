from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from .backup.views import BackUpView

router = routers.DefaultRouter()
router.register(r'backup/create', BackUpView, basename="create")
router.register(r'backup/delete', BackUpView, basename="delete")
router.register(r'backup/search', BackUpView, basename="query")
# router.register(r'backup/count', BackUpView, basename="count")

urlpatterns = [
    path(r'api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
