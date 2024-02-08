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
        user_name = request.user.username if request.user.username else 'Anonymous'
        user_ip = request.META.get('HTTP_X_FORWARDED_FOR') if request.META.get('HTTP_X_FORWARDED_FOR')\
            else request.META.get('REMOTE_ADDR')
        logger.info(f'{current_time} - {user_name}|{user_ip} - {request.path}')
        response = self.get_response(request)
        return response
