from django.urls import path

from apps.main.api import views

urlpatterns = [
    path('register/', views.RegistrationCreateView.as_view(), name='registration-create'),
    path('reviews/', views.ReviewListView.as_view(),name='reviews-list'),
    path('history/', views.HistoryListView.as_view(), name='history-list'),
    path('video/', views.VideoListView.as_view(), name='video-list'),
]
