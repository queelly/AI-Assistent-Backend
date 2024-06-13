
from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('authentication.urls')),

    path('api/ai/', include('assistent_app.urls')),


    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),


    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
