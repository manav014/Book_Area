from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Areas
from math import ceil
from django.core.mail import send_mail


# Create your views here.

def index(request):
    # areas = Areas.objects.all()
    # print(areas)
    # n = len(areas)
    # slides = n // 4 + ceil((n / 4) - (n // 4))
    # params={'areas' : areas, 'no_of_slides' : slides, 'range' : range(1,slides)}
    # allAreas = [[areas, range(1, slides), slides], [areas, range(1, slides), slides]]
    allAreas = []
    collegeAreas = Areas.objects.values('Area_college', 'id')
    college = {item['Area_college'] for item in collegeAreas}
    for col in college:
        area = Areas.objects.filter(Area_college=col)
        n = len(area)
        slides = n // 4 + ceil((n / 4) - (n // 4))
        allAreas.append([area, range(1, slides), slides])
    params = {'allAreas': allAreas}
    return render(request, "areas/index.html", params)


def sendMail(request):
    if request.method == 'POST':
        email = request.POST['email']
        area_name = request.POST['area_name']
        from_email = request.POST['from_email']
        send_mail('Booking Request!!!',
                  'Hey!! There is a request to book your' + str(area_name) + "from " + str(from_email), str(email),
                  [str(email)], fail_silently=False)
        messages.success(request, "mail sent")
        return redirect('/areas')
    else:
        return HttpResponse("404 not found")

# def listing(request):
#     return HttpResponse("LIST")
#
#
# def details(request):
#     return HttpResponse("areaview")
#
#
# def search(request):
#     return HttpResponse("search")
#
#
# def book(request):
#     return HttpResponse("book")
