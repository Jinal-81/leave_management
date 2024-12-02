from django.urls import path
from .views import ApplyLeaveView, LeaveStatusView, ManageLeavesView, ApproveRejectLeaveView

urlpatterns = [
    path('apply-leave/', ApplyLeaveView.as_view(), name='apply_leave'),
    path('leave-status/', LeaveStatusView.as_view(), name='leave_status'),
    path('manage-leaves/', ManageLeavesView.as_view(), name='manage_leaves'),
    path('approve-reject-leave/<int:pk>/<str:action>/', ApproveRejectLeaveView.as_view(), name='approve_reject_leave'),
]
