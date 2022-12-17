from ProjectDefence.accounts.views import SignUpView, SignInView, SignOutView, ProfileDetailsView, profile_update, \
    ProfileDeleteView

from django.urls import path

urlpatterns = (
    path('create/', SignUpView.as_view(), name='sign up'),
    path('login/', SignInView.as_view(), name='sign in'),
    path('logout/', SignOutView.as_view(), name='sign out'),
    path('profile-details/<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('profile-update/<int:pk>/', profile_update, name='profile update'),
    path('profile-delete/<int:pk>/', ProfileDeleteView.as_view(), name='profile delete'),

)
