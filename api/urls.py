from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('todos',views.TodosView,basename='todos')#todosview viewset il ninnu import cheythukond


urlpatterns=[
    path('register/',views.RegistrationView.as_view())
]+router.urls