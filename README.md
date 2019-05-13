This project is about getting posts from https://news.ycombinator.com.
It's supplied with API handling GET requests to render collections of posts' JSON representations.

Easy quick start:
- Create file named .env in the root repository and write all environmental values inside.
It's similar to local_settings.py, but cooler :) See docs: https://github.com/theskumar/python-dotenv

- In order you want to launch celery, you have to install and run redis server
(See docs: https://redis.io/topics/quickstart)

Usage tips:
- To make grabber grab news, visit '/grab_posts/' page. It initiates grabber instance and
calls its 'grab_articles' method.
