from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import HomePageView, CreatePostView, FullPostViews

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/new', CreatePostView.as_view(), name='create_post'),
    path('post/<int:pk>/', FullPostViews.as_view(), name='full_post'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
