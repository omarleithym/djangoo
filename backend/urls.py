from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from django.contrib import admin
import api.views
import posts.views
from rest_framework.authtoken.views import ObtainAuthToken

router = routers.DefaultRouter()
router.register(r'users', api.views.UserViewSet)
router.register(r'posts', posts.views.PostViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', api.views.CustomObtainAuthToken.as_view()),
]