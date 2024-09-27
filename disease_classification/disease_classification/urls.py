from django.contrib import admin
from django.urls import path, include  # Add 'include' here
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # if using authentication
    path('classification/', include('classification.urls')),  # assuming you have this
    path('', TemplateView.as_view(template_name='home.html'), name='home'),  # Add this line
]
