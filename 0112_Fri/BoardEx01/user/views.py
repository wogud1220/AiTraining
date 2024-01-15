from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

class User:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.nickname = ''
        self.id = 0
    def auth(self, temp):
        if self.username == temp.username and self.password == temp.password:
            return True
        else: 
            return False
    def signUp(self,temp):
        if self.username == temp.username:
            return True
        else:
            return False

user_list=[]
a=User()
a.username='a'
a.password='a'
a.nickname='a'


user_list.append(a)

def index(request):
    context={}
    return render(request, "index.html", context)


def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    temp = User()
    temp.username = username
    temp.password = password
    for u in user_list:
        if(u.auth(temp)):
            return HttpResponse("로그인 성공")
    
    print('username: ', username)
    print('password: ', password)
    return HttpResponse("로그인 실패")



def register(request):
    context={}
    return render(request, "register.html", context)



def signUp(request):
    username = request.POST['username']
    password = request.POST['password']
    temp = User()
    temp.username = username
    temp.password = password
    for v in user_list:
        if(v.signUp(temp)==True): #이미 중복된 값이면
            return HttpResponse("회원가입 실패")
    user_list.append(temp)
    return HttpResponse("회원가입 성공")
