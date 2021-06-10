from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})


def object_detail(request, id):
    return render(request, 'index.html', {})


def post_detail(request, id):
    return render(request, 'index.html', {})
