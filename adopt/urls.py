from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('adopt',views.AdoptViewSet)
router.register('quiz',views.QuizViewSet)

urlpatterns = [
    path('' ,include(router.urls)),
]