from django.shortcuts import redirect, render

from .models import Issue

from .forms import IssueForm


# Create your views here.
def main(request):
    return render(request, "issuesapp/base.html", context={"title": "Main"})


def issues(request):
    issues = Issue.objects.all()
    return render(
        request, "issuesapp/issues.html", context={"title": "Issues", "issues": issues}
    )


def create_issue(request):
    form = IssueForm()
    if request.method == "POST":
        form = IssueForm(request.POST, request.FILES, instance=Issue())
        if form.is_valid():
            form.save()
            return redirect(to="issuesapp:main")
        return render(request, "issuesapp/create.html", context={"form": form})

    return render(request, "issuesapp/create.html", context={"form": IssueForm()})
