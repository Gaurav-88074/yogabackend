from django.http import HttpResponse,HttpResponseBadRequest
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
import json
# -------------------------------------------------------
from django.contrib.auth.models import User
from .models import Person
from .models import Batch
from .models import BatchesInfo

# --------serializers-----------
from .serializers import UserSerializer
from .serializers import PersonSerializer
from .serializers import BatchSerializer
from .serializers import BatchesInfoSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['user'] = user.username

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
# -----------------------------------------------

# -----------------------------------------------
@api_view(['GET'])
def index(request):
    return HttpResponse("hello")

# -----------------------------------------------
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getAllUsers(request):
    rawData = User.objects.all()
    serializedData = UserSerializer(rawData, many=True)
    return Response(serializedData.data)

# -----------------------------------------------
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def signup(request):
    try:
        # print(request.data)
        body = request.data
        # body = json.loads(json.dumps(body))
        # print(body)
        email = body['email']
        password = make_password(body['password'])
        first_name = body['firstname']
        last_name = body['lastname']
        age = body['age']

        UserObject = User.objects.create(
            username=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        UserObject.save()

        PersonObject = Person.objects.create(
            user = UserObject,
            first_name = first_name,
            last_name = last_name,
            age = age
        )
        PersonObject.save()

        rawData = Person.objects.all()
        serializedData = PersonSerializer(rawData, many=True)
        return Response(serializedData.data)
    except:
        response = {
            'status': 'error', 
            'message': "email id already exists!!"
        }
        indent = 2 
        content = json.dumps(response, indent=indent)
        return HttpResponseBadRequest(content, content_type='application/json')

#------------------------------------------
# -----------------------------------------------
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def buy_membership(request):
    try:
        body = request.data
        email = body['email']
        batch_id = body['batch_id'] 
        month = body['month'] 
        enrollDate = body['enrollDate'] 

        user   = User.objects.filter(username = email)[0]
        person = Person.objects.filter(user = user)[0]
        batch  = Batch.objects.filter(_id = batch_id)[0]
        # print(user,person,batch)
        newBatch = BatchesInfo.objects.create(
            person=person,
            batch=batch,
            month=str(month),
            enrollDate = enrollDate
        )
        newBatch.save()
        
        return Response({"message":"Payment done successfully"})
    except:
        return Response({"message":"You have already enrolled for this Month!!"})

# -----------------------------------------------
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getAllBatches(request):
    rawData = Batch.objects.all()
    serializedData = BatchSerializer(rawData, many=True)
    return Response(serializedData.data)
# -----------------------------------------------
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def getCurrentBatch(request):
    try:
        body = request.data
        
        email = body['email']
        month =str(body['month']) 

        user = User.objects.filter(username = email)[0]
        person = Person.objects.filter(user = user)[0]
        
        batch = BatchesInfo.objects.filter(person=person,month=month)[0]
        # print(batch.month)
        if(batch.month!=month):
            raise Exception("problem")

        serializedData = BatchesInfoSerializer(batch,many=False)
        return Response(serializedData.data)
    except:
        response = {
            'status': 'error', 
            'message': "batch expired"
        }
        indent = 2 
        content = json.dumps(response, indent=indent)
        return HttpResponseBadRequest(content, content_type='application/json')