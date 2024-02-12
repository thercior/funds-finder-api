"""from django.urls import path
from api.views import *

app_name = 'API'

request_list = {
    'get': 'list',
    'post': 'create',
    'options': 'options',
    'head':'list'
}

request_detail = {
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'delete'
}

urlpatterns = [
    path('funds/<str:lookup>', FundsEstateViewSet.as_view(request_detail), name='funds_details_destroy'),
    path('funds/', FundsEstateViewSet.as_view(request_list), name='funds'),
]"""


from rest_framework.routers import DefaultRouter
from api.views import FundsEstateViewSet

app_name = 'API'

router = DefaultRouter(trailing_slash=True)
router.register(r'funds', FundsEstateViewSet)

urlpatterns = router.urls
