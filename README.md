
# Weather API Wrapper Service

Get weather data based on location given by user from https://weather.visualcrossing.com 

Store the data in redis cache for faster response.


## Skills Learned

Third-party API integration, **caching** strategy, environment variable management.


## API Reference

#### Get weather data

```http
GET /weather/ 
Host: localhost
Port: 8000
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `location` | `string` | default = Tehran |

## Installation

```bash
  pip install django djangorestframework requests redis django-redis
  python manage.py runserver
```
    
## Tech Stack


**Server:** Django, DRF

**Caching:** Redis

