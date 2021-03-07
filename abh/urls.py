
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from store import views as users_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('users/', include('users.urls')),
    path('search/', users_views.SearchView, name='search'),
	path('about/', users_views.about, name="about"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
