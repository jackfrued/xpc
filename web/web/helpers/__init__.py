import redis
from django.conf import settings

r = redis.Redis(host=settings.REDIS_HOST)
