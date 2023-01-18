'''
URL mappings for Recipe app.
'''

from rest_framework.routers import DefaultRouter

from django.urls import (
    path,
    include,
)

from recipe import views


router = DefaultRouter()
router.register('recipes', views.RecipeView)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]
