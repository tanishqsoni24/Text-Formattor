from concurrent.futures import process
import imp
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request , 'index.html')  #yeh serve krta hai '.html' wali file pr
    # print("print hoja bhai")
    # return HttpResponse('''Hello World <a href="http://127.0.0.1:8000/about">Click Here</a>''')

def about(request):
    print(request.POST.get('name','Kuch Ni Daala'))
    print(request.POST.get('email','Kuch Ni Daala'))
    print(request.POST.get('password','Kuch Ni Daala'))
    check = request.POST.get('check')
    if check=='on':
        return render(request, 'about_us.html')
    else:
        return HttpResponse('Please check the checkbox first!')
    # return HttpResponse("about section hai bhai")  #Yeh us screen pr 'yeh wala' content display krdega!

def analyzer(request):
    text_container = request.POST.get('textarea','empty')
    puncheck = request.POST.get('puncremove','off')
    upconvert = request.POST.get('upcase','off')
    lowconvert = request.POST.get('lowconvert','off')
    istitle = request.POST.get('istitle','off')
    chrcount = request.POST.get('chrcount','off')
    if puncheck=='on':
        processed=""
        punctuations = '''!()-[]{};:'""\,<>./?@#$%^&*_~'''
        for i in text_container:
            if i not in punctuations:
                processed=processed+i
        input = {'purpose':text_container , 'result': processed }
        text_container = processed  
        # return render(request, 'result.html', input)
    if upconvert=='on':
        processed=""
        text_container = str(text_container)
        processed = text_container.upper()
        input = {'purpose':text_container , 'result': processed }
        text_container = processed  
        # return render(request, 'result.html', input)
    if(lowconvert=='on'):
        processed=""
        text_container = str(text_container)
        processed = text_container.lower()
        input = {'purpose':text_container , 'result': processed }
        text_container = processed  
        # return render(request, 'result.html', input)
    if(istitle=='on'):
        processed=""
        text_container = str(text_container)
        processed = text_container.istitle()
        input = {'purpose':text_container , 'result': processed }
        text_container = processed  
        # return render(request, 'result.html', input)
    if(chrcount=='on'):
        text_container = str(text_container)
        processed = len(text_container)
        input = {'purpose':text_container , 'result': processed }
        text_container = processed  
    if (upconvert!='on' and lowconvert!='on' and istitle!='on' and chrcount!='on'):
        return HttpResponse('Please check the check box first!')
    if(upconvert=='on' and lowconvert=='on'):
        return HttpResponse('You can not select both Uppercase and lowercase simultaneously')
        
    else:
        return render(request, 'result.html', input)
    # return HttpResponse("Welcome")