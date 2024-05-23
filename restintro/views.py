from django.http import HttpRequest, HttpResponse
from .models import User
import json


def users(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        users = User.objects.all()
        serialized_user = [user.name for user in users]
        return HttpResponse(json.dumps(serialized_user))

    if request.method == 'POST':
        body = json.loads(request.body)
        user = User(name=body['name'], email=body['email'], age=body['age'])
        user.save()
        return HttpResponse(json.dumps({'id': user.id, 'name': user.name}))


def get_or_update_or_delete_user(request: HttpRequest, id: int) -> HttpResponse:
    if request.method == 'PUT':
        body = json.loads(request.body)
        user = User.objects.get(id=id)
        user.name = body['name']
        user.email = body['email']
        user.age = body['age']
        user.save()
        return HttpResponse(json.dumps({'id': user.id, 'name': user.name}))

    if request.method == 'DELETE':
        # body = json.loads(request.body)
        user = User.objects.get(id=id)
        user.delete()
        return HttpResponse(json.dumps({'id': user.id, 'deleted': True}))

    if request.method == 'GET':
        user = User.objects.get(id=id)
        return HttpResponse(json.dumps({'id': user.id, 'name': user.name, 'age': user.age, 'email': user.email}))