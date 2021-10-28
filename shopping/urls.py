from django.contrib import admin
from django.urls import path, include
import debug_toolbar

admin.site.site_header = 'Ultimate Django Part 1'
admin.site.index_title = 'Administrator'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]