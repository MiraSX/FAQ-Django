from django.forms import (
    ModelForm,
    CharField,
    TextInput,
    FileInput,
    ImageField,
    Textarea,
)

from .models import Issue


class IssueForm(ModelForm):
    title = CharField(
        max_length=100,
        min_length=5,
        required=True,
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Sort name issue"}
        ),
    )
    description = CharField(
        min_length=10,
        required=True,
        widget=Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Description",
                "cols": "40",
                "style": "min-height: 300px",
            }
        ),
    )
    image = ImageField(
        required=False, widget=FileInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Issue
        fields = ["title", "description", "image"]
