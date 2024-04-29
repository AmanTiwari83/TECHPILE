from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def home(request):
    return  render(request,'user/home.html')

def register(request):
    if request.method=="POST":
        enroll=request.POST.get('enroll')
        name = request.POST.get('name')
        apply = request.POST.get('apply')
        college = request.POST.get('college')
        course = request.POST.get('course')
        year = request.POST.get('year')
        contact = request.POST.get('mobile')
        email = request.POST.get('email')
        amount = request.POST.get('amount')
        signup(enroll=enroll,name=name,apply=apply,college=college,course=course,year=year,contact=contact,email=email,date=datetime.now().date()).save()
        return HttpResponse(
            "<script>alert('You Are Registered Successfully..');location.href='/register/' </script>")
    rdata=signup.objects.all().order_by('-id')[0:1]
    md={"rdata":rdata}
    return  render(request,'user/register.html',md)

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        contact=request.POST.get('contact')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contactus(name=name,contact=contact,email=email,message=message).save()
        return  HttpResponse("<script> alert('Thank You For Contacting Us..'); location.href='/contact/'</script>")
    return  render(request,'user/contact.html')

def feedback(request):
    if request.method=="POST":
        name=request.POST.get('name')
        picture=request.FILES.get('picture')
        college=request.POST.get('college')
        feedback=request.POST.get('feedback')
        feed(name=name,picture=picture,college=college,feedback=feedback).save()
        return  HttpResponse('<script> alert("Thank You For Your Valuable Feedback..");location.href="/feedback/"</script>')
    return  render(request,'user/feedback.html')

def aboutus(request):
    return  render(request,'user/aboutus.html')

def placement(request):
    pdata=placements.objects.all().order_by('-id')
    mydict={"pdata":pdata}
    return  render(request,'user/placement.html',mydict)

def policy(request):
    return  render(request,'user/policy.html')

def course(request):
    cdata=courses.objects.all().order_by('-id')
    md={"cdata":cdata}
    return  render(request,'user/course.html',md)

def image(request):
    cid=request.GET.get('cid')
    if cid is not None:
        idata=imagegallery.objects.filter(category=cid)
    else:
        idata=imagegallery.objects.all().order_by('-id')
    cdata=category.objects.all().order_by('-id')
    mydict={"idata":idata,"cdata":cdata}
    return render(request,'gallery/image.html',mydict)

def video(request):
    cid=request.GET.get('cid')
    if cid is not None:
        vdata=videogallery.objects.filter(category=cid)
    else:
        vdata=videogallery.objects.all().order_by('-id')
    cdata=category.objects.all().order_by('-id')
    mydict={"vdata":vdata,"cdata":cdata}
    return render(request,'gallery/video.html',mydict)

def summer(request):
    return  render(request,'training/summer.html')

def winter(request):
    return  render(request,'training/winter.html')

def apprenticeship(request):
    return  render(request,'training/apprenticeship.html')

def syllabus(request):
    return  render(request,'training/syllabus.html')

def industrial(request):
    return  render(request,'training/industrial.html')

def python(request):
    return  render(request,'courses/python.html')

def php(request):
    return  render(request,'courses/php.html')

def java(request):
    return  render(request,'courses/java.html')

def android(request):
    return  render(request,'courses/android.html')

def html(request):
    return  render(request,'courses/html.html')

def css(request):
    return  render(request,'courses/css.html')

def c(request):
    return  render(request,'courses/c.html')

def net(request):
    return  render(request,'courses/net.html')