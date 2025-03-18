from django.shortcuts import HttpResponse

data="<hr><a href='/'>Home</a>    <a href='/signin'>SignIn</a>    <a href='/signup'>Signup</a>"

def index(request):
    return HttpResponse(f"<center><h1>Welcome To My Page!!!{data}</h1></center>")

def signup(request):
    global username
    username=input("Enter username=")
    return HttpResponse(f"<center><h1>Sign Up page{data}</h1></center>")


def signin(request):
    checkusername=input("Enter username to signin=")
    if checkusername==username:
        next=f"<hr><h1><a href='/'>Logout!!</a></h1>"
        return HttpResponse(f"<center><h1>Welcome{checkusername}!!{next}</h1></center>")
    else:
        msg=f"<center><h1>Incorrect username !! Try Again...</h1></center>"
        next=f"<hr><h1><a href='/'>click here to go Back</a></h1>"
        return HttpResponse(f"{msg}{next}")