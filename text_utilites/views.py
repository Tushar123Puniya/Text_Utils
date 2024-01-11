from  django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def aboutus(request):
    return render(request,'aboutus.html')

def contactus(request):
    return render(request,'contact.html')

def modifications(request):
    got_text=request.POST.get('text','default')
    can_remove=request.POST.get('remove extra spaces','off')
    can_capitalize=request.POST.get('capitalize all','off')
    char_count=request.POST.get('count number of charachters','off')
    
    analzed_text_=got_text
    measures=""
    
    # print(can_remove)
    # print(can_capitalize)
    # print(char_count)
    # print(got_text)
    
    if(can_capitalize == 'off' and can_remove=='off' and char_count=='off'):
        return render(request,'notanalyzed.html')
    
    if can_remove=="on":
        analzed_text_=''''''
        for index,char in enumerate(got_text):
            if index!=len(got_text)-1 and char ==' ' and got_text[index+1]==' ':
                pass
            else:
                analzed_text_=analzed_text_+char
        measures=measures+"Remove extra spaces "
                
    if can_capitalize=="on":
        analzed_text_=analzed_text_.upper()
        measures=measures+"Capitalize all charachters "
        
    if not(char_count =='on'):
        variables={
            "applied_actions" : measures,
            "analyzed_text" :   analzed_text_
        }
        
        return render(request,'analyzed.html',variables)
    
    else:
        measures = measures + "Count number of Charachters"
        u=set()
        for char in analzed_text_:
            u.add(char)
            
        len_ = len(u)
        analzed_text_ = analzed_text_ + f'''\nNumber of distinct charachters in modified text = {len_}'''
        variables={
            "applied_actions" : measures,
            "analyzed_text" :   analzed_text_
        }
        return render(request,'analyzed.html',variables)
    
    
def personal_navigator(request):
    s='''<h1>These Below are some of my favourite websites</h1>:
        <ul>
            <li> <a href="https://codeforces.com/">CODEFORCES</a></li>
            <li> <a href="https://atcoder.jp/home/">ATCODER</a></li>
            <li> <a href="https://cses.fi/problemset/">CSES</a></li>
            <li> <a href="https://cp-algorithms.com/">CP ALGORITHMS</a></li>
            <li> <a href="https://leetcode.com/problemset/">LEETCODE</a></li>
        </ul>
    '''
    return HttpResponse(s)