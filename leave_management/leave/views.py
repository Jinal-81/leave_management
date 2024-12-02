from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, View

from .constants import ONLY_STAFF_USER_CAN_BE_APPLY_LEAVE_MSG, ONLY_HOD_CAN_BE_APPROVE_REJECT_LEAVE_MSG
from .forms import LeaveRequestForm
from .models import LeaveRequest


class ApplyLeaveView(LoginRequiredMixin, CreateView):
    """
    view for the apply the leave.staff user's acn be able to apply the leaves.
    """
    model = LeaveRequest
    form_class = LeaveRequestForm
    template_name = 'leave/apply_leave.html'
    success_url = reverse_lazy('leave_status')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        if not self.request.user.is_staff():
            return HttpResponseForbidden(ONLY_STAFF_USER_CAN_BE_APPLY_LEAVE_MSG)

        form.instance.staff = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class LeaveStatusView(LoginRequiredMixin, ListView):
    """
    view for the listing the leaves, staff can be able to view the applied leaves.
    """
    model = LeaveRequest
    template_name = 'leave/leave_status.html'

    def get_queryset(self):
        return LeaveRequest.objects.filter(staff=self.request.user)


class ApproveRejectLeaveView(LoginRequiredMixin, View):
    """
    view for the manage the leave by the hod, hod can be able to approve and reject the view.
    """
    def post(self, request, pk, action):
        if not request.user.is_hod():
            return HttpResponseForbidden(ONLY_HOD_CAN_BE_APPROVE_REJECT_LEAVE_MSG)

        leave_request = get_object_or_404(LeaveRequest, pk=pk)
        if action == 'approve':
            leave_request.status = 'approved'
        elif action == 'reject':
            leave_request.status = 'rejected'
        leave_request.save()
        return redirect('manage_leaves')


class ManageLeavesView(LoginRequiredMixin, ListView):
    """
    view for the manage the leaves, hod can be able to approve and reject the leave.
    """
    model = LeaveRequest
    template_name = 'leave/manage_leaves.html'

    def get_queryset(self):
        if not self.request.user.is_hod():
            return LeaveRequest.objects.none()
        return LeaveRequest.objects.all()

