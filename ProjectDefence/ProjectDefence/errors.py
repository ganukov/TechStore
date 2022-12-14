from django.shortcuts import render


def page_not_found_404(request):
    return render(request, 'errors/404.html', status=404)


def forbidden_response_403(request):
    return render(request, 'errors/403.html', status=403)


def internal_server_error_500(request):
    return render(request, 'errors/500.html', status=500)
