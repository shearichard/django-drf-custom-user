# Django-Rest-Knox Sandbox
This project is used to trial the use of customer Django Users in the context of Django Rest Framework.

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

