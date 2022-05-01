from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string

from django.urls import reverse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User , auth
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile
from django.http.response import StreamingHttpResponse
import threading
# from .forms import FaceAdditionForm
import datetime
import os
import numpy as np
import face_recognition
import cv2
import numpy as np
from imutils.video import VideoStream
import imutils
import cv2,os,urllib.request
import numpy as np
from django.conf import settings
from subprocess import check_output, CalledProcessError,STDOUT
import pytesseract
from PIL import Image
import datetime
import cv2
import sys
import os
import os.path
import re
import numpy as np
from pyzbar.pyzbar import decode

# @login_required(login_url='/authentication/login')
# class KYCView(View):
#     def post(self,request):
#         email = request.POST.get('email')
#         name = request.POST.get('uname')

#         print("email")
#         print(name)
#         return render(request, 'KYC/KYC2.html')

#     def get(self, request):
#         return render(request, 'KYC/KYC1.html')
aadhar=""
name2=""
def KYC(request):
    if request.method == 'POST':
        email = request.POST.get('uemail')
        name = request.POST.get('uname')
        print(email)
        print(name)
        return render(request, 'KYC/KYC1.html')

    return render(request, 'KYC/KYC1.html')


# @login_required(login_url='/authentication/login')

def KYC2(request):
     if request.method == 'POST':
        email = request.POST.get('uemail')
        name = request.POST.get('uname')
        print(email)
        print(name)

   

     return render(request, 'KYC/KYC2.html')




def KYC3(request):

     if request.method == 'POST':
        aadhar_number = request.POST.get('fname')
        aadhar=aadhar_number
       
        print(aadhar_number)
        
        return render(request, 'KYC/KYC3.html')
# @login_required(login_url='/authentication/login')
def KYC4(request):
     if request.method == 'POST':
      aadhar_photo = request.FILES['aadharpic']
      df=Profile(pic=aadhar_photo)
      df.save()
      data="media/images/"+str(aadhar_photo)

      print(data)

      dd,d=readBarcodeQRcode(data)
      x=extractFace(data)
      fut=True
      print(aadhar+"1231456")
      print(name2)
      if aadhar == dd[d.index("uid")] and name2 == dd[d.index("name")]:
        print("Data match")
        fut= True
      else:
        
        fut =False
      
      print("Data matched")
      context ={'name' : dd[d.index("name")] , 'aadhar' : dd[d.index("uid")] }
    
        
      return render(request, 'KYC/KYC4.html',context)


def readBarcodeQRcode(img):
    # img = cv2.imread('test1_back.png')
    img = cv2.imread(img)
    for barcode in decode(img):
        data = barcode.data
        myData = barcode.data.decode('utf-8')
        # print(myData)
    # myData = myData.split()
    print("List: ", myData)
    d = ["uid", "name", "gender", "yob", "gname", "co", "house", "lm", "loc", "vtc", "po", "dist", "subdist", "state",
         "pc"]
    def stringToList(string):
        l = []
        flag = 0
        for c in string:
            if flag:
                if c != '"':
                    str += c
                else:
                    l.append(str)
                    flag = 0
            elif c == '"':
                str = ''
                flag = 1
        return l
    df = stringToList(myData)
    del df[0:2]
    print(df)
    print(df[d.index("name")])
    return df, d

def extractFace(img):
    img = cv2.imread(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        faces = img[y:y + h, x:x + w]
        cv2.imshow("face", faces)
        cv2.imwrite('face.jpg', faces)
    cv2.imwrite('detcted.jpg', img)
    cv2.imshow('img', img)
      