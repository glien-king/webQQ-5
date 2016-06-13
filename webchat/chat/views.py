from django.shortcuts import render, HttpResponse

# Create your views here.


def dashboard(request):
    print(request.user.userprofile)
    print(request.user.userprofile.group_members.select_related())
    return render(request, 'chat/webchat.html')


def send_msg(request):
    print(request.POST)
    return HttpResponse('d')