from django.contrib import admin
from django.urls import path
from api import views

from rest_framework_simplejwt.views import (
    # TokenObtainPairView,
    TokenRefreshView,
)
#Our custom pair view
from .views import (
    MyTokenObtainPairView
)


AuthUrl = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
urlpatterns  = [
    *AuthUrl,
    path('', views.getAllUsers),
    path('signup', views.signup,name="sign up"),
    path('login', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('membership',views.buy_membership, name='memebership'),
    path('batch',views.getAllBatches, name='batches'),
    path('currentbatchinfo',views.getCurrentBatch, name='current batch'),
]
