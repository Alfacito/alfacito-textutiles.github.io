#i have created this file
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter =request.POST.get('charcounter', 'off')
    if removepunc =='on':
        punctuations= '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzee= ""
        for char in djtext:
            if char not in punctuations:
                analyzee= analyzee + char
        params= {'purpose':'Remove punctuations','analyzed_text':analyzee}
        return render(request,'analyze.html',params)

    elif fullcaps=='on':
        analyzee=""
        for char in djtext:
            analyzee = analyzee+char.upper()
        params ={'purpose':'Change to upper case ','analyzed_text':analyzee}
        return render(request,'analyze.html',params)


    elif (newlineremover == "on"):
        analyzee=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzee=analyzee + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzee}
        return render(request, 'analyze.html', params)

    elif extraspaceremover=='on':
        import re
        djtext=re.sub(' +', ' ',djtext)
        analyzee = djtext
        params= {'purpose':'remove extra space','analyzed_text':analyzee}
        return render(request,'analyze.html',params)

    elif charcounter=='on':
        analyzee=len(djtext.split())
        params = {'purpose': 'no. of characters in text ', 'analyzed_text': analyzee}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("error")


def aboutus(request):
    return render(request,'aboutus.html')