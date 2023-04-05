from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from check.models import emp_tbl
from check.serializers import emp_tbl_ser
from django.core.mail import send_mail
import secrets
import string

def generate_random_password(length=8):
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password


@api_view(['GET'])
def getData(request):
    data = emp_tbl.objects.filter(isApproved = 0)
    serializer = emp_tbl_ser(data, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def sendEmail(request):
    email = request.data["email"]
    password = generate_random_password()
    emp_tbl.objects.filter(email = email).update(password = password, isApproved = 1)
    # print(type(email))
    # print(email)
    send_mail(
        'Registration Approved',
        'YOUR CREDENTIALS : \n'+'UserName : '+email+'\nPassword : '+password,
        'onespringnight1625@gmail.com',
        [email],
        fail_silently=False
    )
    return Response(email)






