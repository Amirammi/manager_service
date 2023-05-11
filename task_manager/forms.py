from django import forms
from django.contrib.auth import get_user_model

from .models import Task, Project, TaskType, Position


class DateInput(forms.DateInput):
    input_type = "date"


class TaskForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        "style": "padding: 10px"
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        "style": "padding: 10px; height: 100px"
    }))
    project = forms.ModelMultipleChoiceField(
        queryset=Project.objects.all(),
        widget=forms.RadioSelect
    )
    deadline = forms.DateField(widget=DateInput(attrs={
        "style": "padding: 5px 0 0 0; width: 200px"
    }))
    priority = forms.MultipleChoiceField(
        widget=forms.RadioSelect,
        choices=Task.PRIORITY_CHOICES
    )
    task_type = forms.ModelMultipleChoiceField(
        queryset=TaskType.objects.all(),
        widget=forms.RadioSelect
    )
    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = "__all__"


class TaskTypeForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        "style": "padding: 10px"
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        "style": "padding: 10px; height: 200px"
    }))

    class Meta:
        model = TaskType
        fields = "__all__"


class TaskTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "Search by task type name...",
            "style": "padding: 10px"
        })
    )


class PositionForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        "style": "padding: 10px"
    }))
    duties = forms.CharField(widget=forms.Textarea(attrs={
        "style": "padding: 10px; height: 100px"
    }), help_text="Please, be sure to separate each duty with the symbol ' ; '")

    class Meta:
        model = Position
        fields = "__all__"


class PositionSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "Search by the position name... ",
            "style": "padding: 10px; width: 300px;"
        })
    )
