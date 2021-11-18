
from django.contrib import admin
from django.urls import path, include

import challenges 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('challenges/', include("challenges.urls"))
]
