from datetime import datetime
from random import randint

import json
import redis
from django.conf import settings
from django.http import JsonResponse

redis_cache = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DATABASE)


class Push:

    def __init__(self):
        pass

    def push_in_queue(self, payload):
        redis_cache_key = "dakiya_payload_" + str(int(datetime.timestamp(datetime.now()))) + str(randint(100, 999))
        redis_cache.set(redis_cache_key, json.dumps(payload))
        response = {'status': True, 'redis_cache_key': redis_cache_key}
        return response

