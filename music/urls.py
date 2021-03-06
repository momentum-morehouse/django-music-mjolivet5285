"""{{ project_name }} URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from unchained_project import views as unchained_project_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', unchained_project_views.index, name='home'),
    path('unchained_project/add/', unchained_project_views.add_album, name='add_album'),
    path('unchained_project/<int:pk>/delete/', unchained_project_views.delete_album, name='delete_album'),
    path('unchained_project/<int:pk>/edit/',unchained_project_views.edit_album, name='edit_album'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
