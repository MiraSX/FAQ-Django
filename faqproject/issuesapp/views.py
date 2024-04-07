from django.shortcuts import redirect, render

from .models import Issue

from .forms import IssueForm


# Create your views here.


def issues(request):
    issues = Issue.objects.all()
    return render(
        request, "issuesapp/main.html", context={"title": "Issues", "issues": issues}
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


def show_issue(request, issue_id):
    issue = Issue.objects.get(id=issue_id)
    return render(request, "issuesapp/issue.html", context={"issue": issue})


def edit_issue(request, issue_id):
    issue = Issue.objects.get(id=issue_id)
    form = IssueForm(instance=issue)
    if request.method == "POST":
        form = IssueForm(request.POST, request.FILES, instance=issue)
        if form.is_valid():
            form.save()
            return redirect(to="issuesapp:main")
        return render(
            request, "issuesapp/edit_issue.html", context={"form": form, "issue": issue}
        )

    return render(
        request, "issuesapp/edit_issue.html", context={"form": form, "issue": issue}
    )


def delete_issue(request, issue_id):
    issue = Issue.objects.get(id=issue_id)
    issue.delete()
    return redirect(to="issuesapp:main")
