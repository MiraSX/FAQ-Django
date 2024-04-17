from django.forms import (
    ModelForm,
    CharField,
    SelectMultiple,
    TextInput,
    FileInput,
    ImageField,
    Textarea,
    MultipleChoiceField,
)

from .models import Issue, Tag


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

    tags = MultipleChoiceField(
        choices=Tag.objects.all().values_list("id", "name"),
        widget=SelectMultiple(attrs={"class": "form-control"}),
        required=True,  # You can set it to False if you prefer
    )

    class Meta:
        model = Issue
        fields = ["title", "description", "image", "tags"]
