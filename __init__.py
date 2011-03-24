#!/usr/bin/env python2

statuscode = {
        'continue': 100,
        'switching protocols': 101,
        'ok': 200,
        'created': 201,
        'accepted': 202,
        'non-authoritative information': 203,
        'no content': 204,
        'reset content': 205,
        'partial content': 206,
        'multiple choices': 300,
        'moved permanently': 301,
        'found': 302,
        'see other': 303,
        'not modified': 304,
        'use proxy': 305,
        'temporary redirect': 307,
        'bad request': 400,
        'unauthorized': 401,
        'payment required': 402,
        'forbidden': 403,
        'not found': 404,
        'method not allowed': 405,
        'not acceptable': 406,
        'proxy authentication required': 407,
        'request timeout': 408,
        'request time-out': 408,
        'conflict': 409,
        'gone': 410,
        'length required': 411,
        'precondition failed': 412,
        'request entity too large': 413,
        'request-uri too large': 414,
        'unsupported media type': 415,
        'requested range not satisfiable': 416,
        'expectation failed': 417,
        'internal server error': 500,
        'not implemented': 501,
        'bad gateway': 502,
        'service unavailable': 503,
        'gateway timeout': 504,
        'gateway time-out': 504,
        'http version not supported': 505
    }

def HttpStatus(status):
    """
    Return a function on a HttpResponse to set its status code to a given
    `status` number or reason phrase as specified by RFC 2616.

    Example:

        >>> def view(request):
                return HttpStatus('Created')(
                           render_to_response(...)
                       )
    """
    def status_setter(response):
        if isinstance(status, int):
            response.status_code = status
        elif isinstane(status, basestring):
            try:
                response.status_code = statuscode[status.lower()]
            except KeyError:
                raise ValueError("unknown reason phrase")
        else:
            raise TypeError("code must be int or str")
        return response
    return status_setter
