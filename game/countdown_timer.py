import time

class CountdownTimerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not hasattr(request, 'session'):
            # Ensure the session is available
            return self.get_response(request)

        if 'start_countdown' in request.session:
            # Check if the countdown should start
            if request.session['start_countdown']:
                request.session['countdown_start'] = time.time()
                request.session['start_countdown'] = False

        if 'countdown_start' not in request.session:
            # Initialize the countdown timer if it hasn't started yet
            request.session['countdown_start'] = None
            request.session['start_countdown'] = False

        elapsed_time = 0
        if request.session['countdown_start']:
            elapsed_time = time.time() - request.session['countdown_start']

        remaining_time = max(0, 600 - elapsed_time)  # 10 minutes in seconds

        # Add the remaining time to the request context
        request.remaining_time = remaining_time

        response = self.get_response(request)
        return response
