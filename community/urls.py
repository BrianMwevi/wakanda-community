from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls

# schema_view = get_swagger_view(title='Polls API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'), name="api"),
    # path(r'swagger-docs/', schema_view),
    # path(r'', include_docs_urls(title='Polls API')),

]
