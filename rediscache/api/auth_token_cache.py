from django.core.cache import cache


class AuthTokenCache:
    def __init__(self, max_size=100):
        self.cache_key = "auth_token_cache"
        self.max_size = max_size

    def getToken(self, key):
        """
        Fetch the token from the cache based on the key (e.g., user_id or session_id).
        """
        token = cache.get(f"{self.cache_key}:{key}")
        return token

    def setToken(self, key, token):
        """
        Add a new token to the cache. If the cache exceeds its max size, evict the oldest token.
        """
        current_cache = cache.get(self.cache_key, [])

        # Remove the oldest token if the cache is full
        if len(current_cache) >= self.max_size:
            oldest_key = current_cache.pop(0)
            cache.delete(f"{self.cache_key}:{oldest_key}")

        # Add the new token
        current_cache.append(key)
        cache.set(f"{self.cache_key}:{key}", token)
        cache.set(self.cache_key, current_cache)
