# AuthTokenCache: A Caching Solution for Authentication Tokens

This project implements a local caching mechanism using Django and Redis to store authentication tokens. By caching tokens locally, we minimize the need to frequently interact with a third-party authentication service, reducing latency and improving API performance.

## Features

- **In-Memory Token Caching**: Tokens are stored in a local cache for quick access.
- **FIFO Eviction Strategy**: When the cache reaches its capacity, the oldest token is removed to make space for new ones.
- **Configurable Cache Size**: The maximum number of tokens to store in the cache can be specified.

## Prerequisites

- Python 3.6+
- Django 3.0+
- Redis server
- `django-redis` package

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/AuthTokenCache.git
   cd AuthTokenCache
Set Up a Virtual Environment

2. **Create and activate a virtual environment:**
   ```bash
      python -m venv venv
      source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install Django and django-redis:**
    ```bash
      pip install django django-redis


4. **Usage:**
Initialize and Use the Cache
```bash
      from auth_token_cache import AuthTokenCache
      
      # Initialize the cache with a maximum size (e.g., 100 tokens)
      auth_token_cache = AuthTokenCache(max_size=100)
      
      # Store a token in the cache
      auth_token_cache.setToken('user_123', 'sample_token_abc123')
      
      # Retrieve a token from the cache
      token = auth_token_cache.getToken('user_123')
      
      if token:
          print("Token found:", token)
      else:
          print("Token not found or expired.")
