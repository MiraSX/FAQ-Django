from django.shortcuts import render


# Create your views here.
def main(request):
    return render(request, "issuesapp/base.html", context={"title": "Main"})


def issues(request):
    return render(request, "issuesapp/issues.html", context={"title": "Issues"})


def create_issue(request):
    return render(request, "issuesapp/create.html", context={"title": "Create Issue"})
