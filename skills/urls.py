from django.urls import path
from .views import (
    SkillListView, SkillDetailView, SkillCreateView, 
    SkillUpdateView, SkillDeleteView, DashboardView,
    BookingCreateView, ReviewCreateView, BookingStatusUpdateView
)

urlpatterns = [
    path('', SkillListView.as_view(), name='skill_list'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('skill/<int:pk>/', SkillDetailView.as_view(), name='skill_detail'),
    path('skill/new/', SkillCreateView.as_view(), name='skill_create'),
    path('skill/<int:pk>/edit/', SkillUpdateView.as_view(), name='skill_update'),
    path('skill/<int:pk>/delete/', SkillDeleteView.as_view(), name='skill_delete'),
    
    # New features
    path('skill/<int:pk>/book/', BookingCreateView.as_view(), name='booking_create'),
    path('skill/<int:pk>/review/', ReviewCreateView.as_view(), name='review_create'),
    path('booking/<int:pk>/status/<str:status>/', BookingStatusUpdateView.as_view(), name='booking_status_update'),
]
