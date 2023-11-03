def session_key_middleware(get_response):

    def middleware(request):
        if not request.session.session_key:         #* request altında session'ın session key'i yok ise request'in session key'in kaydet
            request.session.save()
        print(f"SESSION KEY : {request.session.session_key}")

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware