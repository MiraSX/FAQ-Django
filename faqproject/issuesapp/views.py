from django.shortcuts import redirect, render

from .forms import IssueForm


# Create your views here.
def main(request):
    return render(request, "issuesapp/base.html", context={"title": "Main"})


def issues(request):
    return render(request, "issuesapp/issues.html", context={"title": "Issues"})


def create_issue(request):
    if request.method == "POST":
        form = IssueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="issuesapp:main")
        return render(request, "issuesapp/create.html", context={"form": form})

    return render(request, "issuesapp/create.html", context={"form": IssueForm()})
