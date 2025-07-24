from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("post/<int:pk>", views.post_details, name="post-detail"),
    path("post/new/", views.PostCreateView.as_view(), name="post-create"),
    path('<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
]
