from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('showroom',views.Showroom_ViewSet,basename='showroom')

urlpatterns = [
    path("list", views.car_list_view, name="car_list"),
    path("<int:pk>",views.car_detail_view, name="car_detail"  ),
    path('',include(router.urls)),
    # path("showroom", views.Showroom_View.as_view() , name ="showroom_view"), #asview is used to convert class based view to function based
    # path('showroom/<int:pk>',views.Showroom_Details.as_view(),name="showroom_details"),
    # path('review/' ,views.ReviewList.as_view(), name="review_lists"),
    # path('review/<int:pk>' ,views.ReviewDetail.as_view(), name="review_details")

    path('showroom/<int:pk>/review-create',views.ReviewCreate.as_view(),name ='review-create'),
    path('showroom/<int:pk>/review',views.ReviewList.as_view(),name="review-list"),
    path('showroom/review/<int:pk>',views.ReviewDetail.as_view(),name='review-detail'),
]
