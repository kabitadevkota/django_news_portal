
from django.urls import path
from news import views


urlpatterns = [
   
    path('', views.NewsList.as_view(), name='index'),
    path("news/create/", views.NewsCreateView.as_view(),name='create_news'),
    path("news/<str:category>/<int:pk>/", views.NewsDetail.as_view(),name='detail_news'),
    path("news/<str:category>/<int:pk>/delete/", views.NewsDeleteView.as_view(),name='delete_news'),
    path("news/<str:category>/<int:pk>/update/", views.NewsDetail.as_view(),name='update_news')
   
]
