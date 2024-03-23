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
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
