from django.shortcuts import render
from django.views.decorators.cache import cache_control

@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def page_unauthorized(request, exception):
    return render(request, '401.html', status=401)

@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def page_bad_request(request, exception):
    return render(request, '400.html', status=400)

@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def page_forbidden(request, exception):
    return render(request, '403.html', status=403)

@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def internal_server_error(request, *args, **argv):
    return render(request, '500.html', status=500)