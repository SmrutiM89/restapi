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
        user = User(name=body['name'], email=body['email'],age=body['age'])
        user.save()
        return HttpResponse(json.dumps({'id': user.id,'name':user.name}))