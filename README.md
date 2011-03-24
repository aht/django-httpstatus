    from django.http import HttpResponse
    from django_httpstatus import HttpStatus, statuscode

    def view1(request):
        return HttpResponse("Hello!", status=statuscode["ok"])

    def view2(request):
        return HttpStatus('Created')(
                   render_to_response(...)
               )
