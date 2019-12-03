from django.conf.urls import url, include
from django.urls import path
from rest_framework.authtoken import views
from .views import UserCreateView, UserListView, ApiRootView, DoctorListView, PrzychodniaCreateView, GetAuthTokenView, DoctorCreateView, UserEditProfileView, DoctorEditProfileView


urlpatterns = [
    path('create/user/', UserCreateView.as_view(), name=UserCreateView.name),
    path('create/doctor/', DoctorCreateView.as_view(), name=DoctorCreateView.name),
    path('create/przychodnia/', PrzychodniaCreateView.as_view(), name=PrzychodniaCreateView.name),
    path('users/patient/profile/', UserEditProfileView.as_view(), name=UserEditProfileView.name),
    path('users/patient/list/', UserListView.as_view(), name=UserListView.name),
    path('users/doctor/profile/', DoctorEditProfileView.as_view(), name=DoctorEditProfileView.name),
    path('users/doctor/list/', DoctorListView.as_view(), name=DoctorListView.name),
    url(r'^$', ApiRootView.as_view(), name=ApiRootView.name),
    url(r'^login_user/', GetAuthTokenView.as_view(), name=GetAuthTokenView.name),
    url(r'^api-auth/', include('rest_framework.urls')),
]
