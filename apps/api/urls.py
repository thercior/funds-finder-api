from django.urls import path
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
    path('funds/', FundsEstateViewSet.as_view(request_list), name='funds'),
    path('funds/{lookup}', FundsEstateViewSet.as_view(request_detail), name='funds_details_destroy'),
]

"""
from rest_framework.routers import DefaultRouter
from api.views import FundsEstateViewSet

app_name = 'API'

router = DefaultRouter(trailing_slash=False)
router.register(r'funds', FundsEstateViewSet)

urlpatterns = router.urls
"""