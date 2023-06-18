from django.urls import include, path
from rest_framework import routers
from apps.members import viewsets as view_member
from apps.foods import viewsets as view_food
app_name = 'apps'
router = routers.DefaultRouter()

router.register(r'members', view_member.MembersViewSet, basename='members')
router.register(r'foods', view_food.FoodsViewSet, basename='foods')

urlpatterns = [
    path('', include(router.urls), name='main')
]
