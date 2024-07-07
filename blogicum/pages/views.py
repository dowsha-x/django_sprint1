from django.shortcuts import render


def about(request):
    """Отоброжает страницу - о компании."""
    return render(request, 'pages/about.html')


def rules(request):
    """Отоброжает страницу - правила."""
    return render(request, 'pages/rules.html')
