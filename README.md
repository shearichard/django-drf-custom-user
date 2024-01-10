# Django-Rest-Knox Sandbox
This project is used to trial the use of [django-rest-knox](https://pypi.org/project/django-rest-knox/). It's starting point is a cutdown version of [drf-tut-baseline](https://github.com/shearichard/drf-tut-baseline).

## Installation
Take note of the comments in the django-rest-knox documentation regarding [operating system prerequisites](https://jazzband.github.io/django-rest-knox/installation/).

## Example Transactions
### Before any authorisation applied
Add a snippet.
```
$ echo -n '{"id": 1,"title": "","code": "foo = \"bar\"\n","linenos": false,"language": "python","style": "friendly"}' | http POST localhost:8000/snippets/
```
View all snippets.
```
$ http http://localhost:8000/snippets/
```

