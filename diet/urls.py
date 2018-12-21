"""diet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from dietapp.views import *
from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^bitwapodgrunwaldem1410/', admin.site.urls),
    url(r'^home$', HomeView.as_view()),
    url(r'^details$', DetailsView.as_view()),
    url(r'^login$', LoginView.as_view()),
    url(r'^logout', LogoutView.as_view()),
    url(r'^registration$', RegisterUserView.as_view()),
    url(r'^bodymeasure$', BodyMeasureView.as_view()),
    url(r'^add_recipe$', MealRecipeView.as_view()),
    url(r'^diet_display$', DisplayDietView.as_view()),
    url(r'^all_recipes$', AllRecipesView.as_view()),
    url(r'^add_ingredients$', AddIngredientsView.as_view()),
    url(r'^edit/(?P<pk>\d+)$', UserUpdate.as_view()),


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)