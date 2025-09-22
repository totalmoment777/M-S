import MS_APP.views as views
from django.urls import path

urlpatterns = [
    path('', views.SequencerView, name='sequencer'),
    path('sequences/', views.SequencesListView, name='sequences'),
    path('profile/', views.ProfileView, name='profile'),
    path('login/', views.LoginView, name='login'),
]
