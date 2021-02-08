from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter


# Using router
router = DefaultRouter()
#router.register('items', ItemsViewSet, basename='items', )


urlpatterns = [
    #path('item_detail/<str:item_id>/', views.ItemApiView.as_view()),
]


# Add routers to urls form urlpatterns
urlpatterns += router.urls