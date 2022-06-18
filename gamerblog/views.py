from django.shortcuts import render

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def page_unauthorized(request, exception):
    return render(request, '401.html', status=401)

def page_bad_request(request, exception):
    return render(request, '400.html', status=400)

def page_forbidden(request, exception):
    return render(request, '403.html', status=403)

def internal_server_error(request, *args, **argv):
    return render(request, '500.html', status=500)