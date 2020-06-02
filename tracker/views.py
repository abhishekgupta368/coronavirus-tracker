from django.shortcuts import render,HttpResponse
import requests
import json
import time 

def process_number(num_dic):
    ret_dic={}
    for k,v in num_dic.items():
        if(k!='source'):
            data = str(v)[::-1]
            i=1
            ans=""
            while(i<=len(data)):
                ans+=data[i-1]
                if(i%3==0):
                    ans+=','
                i+=1
            if(ans[-1]==','):
                ans = ans[:len(ans)-1]
                ret_dic[k] = ans[::-1]
                print(ans)
            else:
                ret_dic[k] = ans[::-1]
        else:
            ret_dic[k]=v
    return ret_dic

def getRecord(request):
    api_data =  requests.get('https://api.thevirustracker.com/free-api?global=stats')
    data = api_data.json()
    if(data['stat']=='ok'):
        # process_number(data['results'][0])
        model = {'model': process_number(data['results'][0])}
        return render(request,'index.html',model)
    else:
        return HttpResponse("<h1> Data Not Found")

def update_data(request):
    # while(True):
    return getRecord(request)
        # time.sleep(5)

def showInfoByCnt(request):
    api_data = requests.get("http://newsapi.org/v2/everything?q=coronavirus&from=2020-04-12&sortBy=publishedAt&apiKey=3e4a7052c21f43e286ab2175be919f5b")
    data = api_data.json()
    news_data = []
    if(data['status']=='ok'):
        for i in range(len(data['articles'])):
            news_data.append(data['articles'][i])
        # print(data['articles'][0].keys())
        return render(request,"showInfoByCnt.html",{'news_model':news_data})
    else:
        return HttpResponse("Error in Api")
