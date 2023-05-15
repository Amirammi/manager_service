from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from taggit.forms import TagField

from .models import Task, Project, TaskType, Position, Worker, Team


class DateInput(forms.DateInput):
    input_type = "date"


class WorkerCreateForm(UserCreationForm):
    username = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            "placeholder": "Username*",
            "style": "padding: 10px"
        }),
        label="",
        required=True
    )
    first_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            "placeholder": "First Name*",
            "style": "padding: 10px"
        }),
        label="",
        required=True
    )
    last_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            "placeholder": "Last Name*",
            "style": "padding: 10px"
        }),
        label="",
        required=True
    )
    email = forms.EmailField(widget=forms.EmailInput(attrs={
            "placeholder": "Email*",
            "style": "padding: 10px"
        }),
        required=True,
        label=""
    )
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "placeholder": "Password*",
            "style": "padding: 10px"
        }),
        label="",
        required=True
    )
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "placeholder": "Confirm password*",
            "style": "padding: 10px"
        }),
        label="",
        required=True
    )
    position = forms.ModelChoiceField(
        widget=forms.Select(attrs={"style": "padding: 10px;"}),
        queryset=Position.objects.all(),
        required=False
    )
    team = forms.ModelChoiceField(
        widget=forms.Select(attrs={"style": "padding: 10px;"}),
        queryset=Team.objects.all(),
        required=False
    )

    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "position", "team")


class TaskForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Name*",
        "style": "padding: 10px"
    }),
        label="",
        required=True
    )
    description = forms.CharField(widget=forms.Textarea(attrs={
        "placeholder": "Description",
        "style": "padding: 10px; height: 100px"
    }),
        label=""
    )
    project = forms.ModelChoiceField(
        widget=forms.Select(attrs={"style": "padding: 10px;"}),
        queryset=Project.objects.all()
    )
    deadline = forms.DateField(widget=DateInput(attrs={
        "style": "padding: 8px 0 0 55px; height: 43px; width: 200px"
    }))
    priority = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=Task.PRIORITY_CHOICES
    )
    task_type = forms.ModelChoiceField(
        queryset=TaskType.objects.all(),
        widget=forms.Select(attrs={"style": "padding: 10px;"}),
    )
    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    tags = TagField(required=False)

    class Meta:
        model = Task
        fields = "__all__"


class TaskTypeForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Name*",
        "style": "padding: 10px"
    }),
        label="",
        required=True
    )
    description = forms.CharField(widget=forms.Textarea(attrs={
        "placeholder": "Description",
        "style": "padding: 10px; height: 200px"
    }),
        label=""
    )

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
        "placeholder": "Name*",
        "style": "padding: 10px"
    }))
    duties = forms.CharField(widget=forms.Textarea(attrs={
        "placeholder": "Description",
        "style": "padding: 10px; height: 100px"
    }),
        help_text="Please, separate each duty with the symbol ' ; '",
        label=""
    )

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
