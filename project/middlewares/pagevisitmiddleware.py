import requests
from datetime import datetime

from django.conf import settings

class PageVisitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        user_ip = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('HTTP_X_REAL_IP') or request.META.get('REMOTE_ADDR')
        user_agent = request.META.get('HTTP_USER_AGENT')
        timestamp = datetime.now()
        page = request.path

        endpoint = f'http://:{settings.EXTERNAL_SERVICE_IP}/api/pagevisits/'
        data = {
            'user_ip': user_ip,
            'user_agent': user_agent,
            'timestamp': timestamp.isoformat(),
            'page': page,
        }

        res = requests.post(endpoint, data)

        return response 

