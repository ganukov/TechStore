from ProjectDefence.errors import page_not_found_404, forbidden_response_403, internal_server_error_500


def error_handlers(get_response):
    def handlers(request):
        response = get_response(request)
        if response.status_code == 404:
            return page_not_found_404(request)
        if response.status_code == 403:
            return forbidden_response_403(request)
        if response.status_code == 500:
            return internal_server_error_500(request)
        return response
    return handlers
