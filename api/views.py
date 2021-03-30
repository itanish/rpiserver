from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import UploadSerializer
from django.core.files.storage import default_storage
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import requests
import json

# ViewSets define the view behavior.
class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        return Response("GET API")

    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        content_type = file_uploaded.content_type
        file_name = default_storage.save(file_uploaded.name, file_uploaded)
        response = "POST API and you have uploaded a {} file".format(content_type)
        return Response(response)


def getimage(request):

    url = "http://127.0.0.1:8000/upload/"

    payload={}
    files=[
    ('file_uploaded',('avatar.png',open('/Users/tanishsehgal/Documents/avatar.png','rb'),'image/png'))
    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    # print(response.text)

    return HttpResponse(response.text)
