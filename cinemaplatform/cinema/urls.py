from django.urls import path, include
from . import views
from . views import HomeViewSet, PresentationDetail, BookingViewSet, BookingCreate, BookingList, LoginView,UserRegisterView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('booking', BookingViewSet, basename='boking')

urlpatterns = [
    path('', HomeViewSet.as_view(), name="home"),
    path('detail/<int:pk>', PresentationDetail.as_view(), name="detail"),
    # path('booking', views.booking, name="booking"),
    path('vset/', include(router.urls)),
    # path('vset/<int:>', include(router.urls)),
    path('create', BookingCreate.as_view(), name="booking_create"),
    path('list', BookingList.as_view(), name="booking_List"),
    path('login', LoginView.as_view(), name="login"),
    path('register', UserRegisterView.as_view(), name="register"),
 
]