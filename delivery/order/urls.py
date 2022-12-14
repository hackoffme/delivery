from django.urls import path

from order import view_rest


urlpatterns = [
    path('tg_users/<tg_id>/', view_rest.CustomerViewDetail.as_view({'get':'retrieve', 'put':'update'})),
    path('tg_users/', view_rest.CustomerViewDetail.as_view({'post':'create'})),
    path('order/', view_rest.OrderCreate.as_view()),
    path('order/tg/<tg_id>', view_rest.OrderViewList.as_view({'get': 'list'}))
]
