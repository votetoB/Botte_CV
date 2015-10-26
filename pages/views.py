from django.shortcuts import render


def welcome(request):
    return render(request, 'pages/pages_base.html')


def contacts(request):
    pass


def hearthstone_school(request):
    pass
