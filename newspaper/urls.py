from django.urls import path
from .views import PostsList, PostDetails, Search, PostCreateView, PostEditView, PostDeleteView

urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>', PostDetails.as_view(), name='newsone'),
    path('search', Search.as_view()),
    path('add', PostCreateView.as_view(), name='news_create'),
    path('edit/<int:pk>', PostEditView.as_view(), name='news_update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='news_delete'),
]
