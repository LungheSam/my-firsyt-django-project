from django.shortcuts import render
from django.http import HttpResponse
# import random
from .models import Room
# Create your views here.

# rooms=[
#     {'id':'CourseX1'+str(random.randint(1,20)),'name':'Embedded Systems','price':'$100'},
#     {'id':'CourseX1'+str(random.randrange(5)),'name':'Artificial Intelligence','price':'$200'},
#     {'id':'CourseX1'+str(random.randrange(30)),'name':'Data Science and Machine Learning','price':'$400'},
# ]
def home(request):
    # return render(request, 'home.html',{'name':'Lunghe Samuel'})
    rooms=Room.objects.all()
    context={'rooms':rooms}
    return render(request, 'home.html',context)
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def room(request,pk):
    # return HttpResponse("This is the Room page from Rooms")
    # room=None
    # for r in rooms:
    #     if r['id']==pk:
    #         room=r
    #         break
    room=Room.objects.get(id=pk)
    context={'room':room}
    return  render(request, 'room.html',context=context) 
