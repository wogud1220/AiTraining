from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

class User:
    def __init__(self):
        print("user()")
        self.userName = ""
        self.password = ""

userList=[]
for i in range(1,10):
    temp=User()
    temp.userName="user"+str(i)
    temp.password="111"
    userList.append(temp)


def index(request):
    print(len(userList))
    context ={"logIn": True,
              "name": '윤재형'}
    return render(request,"helloWorld/index.html",context)

def userNum(request, userNum):
    userList.append(User())
    response = "=========== %s단==========="
    response += "<br/>"
    for i in range(0,10):
        response += str(userNum) + " * "+str(i)+ " = "+ str(i*(userNum))
        response +="<br/>"
    return HttpResponse(response % userNum)

def gugugu(request):
    result=[]
    for i in range(1,10):
        result.append(i * int(request.POST['userNum']))
    return render(request, "helloWorld/gugu.html", {
        'result': result,
        'userNum': request.POST['userNum'],
    })

def bye(request):
    return HttpResponse("World!")

def bye2(request):
    name= request.POST['name']
    result = name + "님, 환영합니다.!! by python"
    return HttpResponse(result)