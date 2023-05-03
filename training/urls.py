from django.urls import path

from training.views import CourseListView, CourseDetailView, CourseCreateView

urlpatterns = [
    path('', CourseListView.as_view(), name='home'),
    path('create/', CourseCreateView.as_view(), name='course_detail'),
    path('<str:cid>/', CourseDetailView.as_view(), name='course_detail'),
]
