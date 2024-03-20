from django.forms import ModelForm, CharField, TextInput, FileInput, ImageField

from .models import Issue


class IssueForm(ModelForm):
    title = CharField(
        max_length=50,
        min_length=5,
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Sort name issue"}
        ),
    )
    description = CharField(
        max_length=200,
        min_length=10,
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Description",
                "style": "min-height: 300px",
            }
        ),
    )
    image = ImageField(widget=FileInput(attrs={"class": "form-control"}))

    class Meta:
        model = Issue
        fields = ["title", "description", "image"]
