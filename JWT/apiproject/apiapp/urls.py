from django.urls import path, include
from apiapp import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

# Creating Router Object
router = DefaultRouter()

# register viewset with router
router.register('userapi', views.UserModelViewset, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('get_token/', TokenObtainPairView.as_view(), name='GetToken'),
    path('refresh_token/', TokenRefreshView.as_view(), name='RefreshToken'),
    path('verify_token/', TokenVerifyView.as_view(), name='VerifyToken'),
]
