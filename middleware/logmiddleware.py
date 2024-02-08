import logging
import os
import datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('history.log')
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user_name = request.META.get('USERNAME') if request.META.get('USERNAME') else 'Anonymous'
        session_key = request.session.session_key if request.session.session_key else 'Anonymous'
        logger.info(f'{current_time} - {user_name} - {session_key} - {request.path}')

        response = self.get_response(request)
        return response
