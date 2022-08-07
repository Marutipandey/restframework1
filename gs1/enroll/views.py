import json
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render


from enroll.models import Student
from enroll.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
# Create your views here.
def home(request):
    stu = Student.objects.all()
    seri=StudentSerializer(stu,many=True)
    # json_data=JSONRenderer().render(seri.data)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(seri.data,safe=False)
    
