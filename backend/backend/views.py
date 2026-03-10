from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import *
from .models import Job, Application

@api_view(['GET'])
def hello_api(request):
    return Response({"message":"hello from Django API"})

@api_view(['POST'])
def register_user(request):
    serializer= RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"User Registered Successfully!"},status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def basic_login(request):
    username=request.data.get('username')
    password=request.data.get('password')
    user = authenticate(username=username, password=password)
    try:
        user = User.objects.get(username=username,password=password)
        return Response({"user_id": user.id,"username":user.username, 'message':"Login Successful"},status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'message':"Invalid Credentials"},status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def job_list(request):
    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def apply_job(request):
    serializer=ApplicationSerializer(data=request.data)
    job_id= request.data.get("job")
    applicant_id=request.data.get("applicant")
    #check application exists
    if Application.objects.filter(job_id=job_id,applicant_id=applicant_id).exists():
        return Response({"message":"You already have applied!"},status=status.HTTP_400_BAD_REQUEST)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"Application submitted"},status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

 

