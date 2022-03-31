from . import views
from django.urls import path

urlpatterns = [
    path('', views.AdvList.as_view(), name='get_post_adv'),
    path('rate/', views.RateCreate.as_view(), name='post_adv'),
    path('upd/<str:pk>', views.UpdateAdv.as_view(), name='get_update_adv'),
    path('search/<str:city>/<str:town>', views.AdvSearch.as_view(), name='search_adv'),
    path('detail/<str:id>', views.AdvDetail.as_view(), name='detail_adv'),
    
]

