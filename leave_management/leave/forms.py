# forms.py
from django import forms
from django.core.exceptions import ValidationError

from .constants import START_END_DATE_REQUIRED_MSG, ALREADY_APPLIED_LEAVE_MSG
from .models import LeaveRequest


class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ['reason', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        user = self.user

        # Check if start_date and end_date are provided
        if not start_date or not end_date:
            raise ValidationError(START_END_DATE_REQUIRED_MSG)

        # Check if the user has already applied for leave for the same date range
        existing_leave = LeaveRequest.objects.filter(
            staff=user,
            start_date__lte=end_date,
            end_date__gte=start_date
        )

        if existing_leave.exists():
            raise ValidationError(ALREADY_APPLIED_LEAVE_MSG)

        return cleaned_data
