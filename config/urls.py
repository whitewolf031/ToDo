from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # urls
    path('api/', include('api.urls')),
    
    # Swagger va ReDoc uchun
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # # auth
    # path('auth/', include('djoser.urls.base')),
    # path('auth/', include('djoser.urls.jwt')),


    # create todo
    # path('todo/', include('todo.urls')),  

    # # auth
    # path('accounts/', include('django.contrib.auth.urls')),  
    # path('users/', include('users.urls')),  
]
