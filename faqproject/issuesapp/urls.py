from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = "issuesapp"

urlpatterns = [
    path("", views.issues, name="main"),
    path(
        "create/",
        views.create_issue,
        name="create",
    ),
    path(
        "issue/<int:issue_id>",
        views.show_issue,
        name="issue",
    ),
    path(
        "edit/<int:issue_id>",
        views.edit_issue,
        name="edit",
    ),
    path(
        "delete/<int:issue_id>",
        views.delete_issue,
        name="delete",
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
