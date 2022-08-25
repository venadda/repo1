from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from business.serializers import businessSerializer

# Serializers define the API representation.


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'vendors',businessSerializer.VendorViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('site/', include('siteapp.urls')),
    path('authapp/', include('authapp.urls')),
    path('business/',include('business.urls')),
    # path('api-auth/', include('rest_framework.urls'),namespace='restframework'),
]
