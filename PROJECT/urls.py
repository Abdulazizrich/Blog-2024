from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from mainApp.views import *
from userApp.views import *

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0)),

    #Jwt authtoken
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('maqolalar/',MaqolalarAPIView.as_view()),
    path('maqolalar/qo\'shish/', MaqolaCreateAPIView.as_view()),
    path('maqola/<int:pk>/',MaqolaAPIView.as_view()),
    path('register/', RegisterProfilAPIView.as_view()),
    path('maqolalarim/',MaqolalarimAPIView.as_view()),
]
