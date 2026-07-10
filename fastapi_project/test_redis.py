from redis_client import redis_client

redis_client.set("test", "Hello Redis")

value = redis_client.get("test")

print(value)
