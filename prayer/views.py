from django.shortcuts import render
import requests
from datetime import datetime

cities = [
    "Seoul","Andong","Ansan","Anseong","Anyang","Asan","Boryeong","Bucheon","Busan","Changwon","Cheonan",
    "Cheongju","Chuncheon","Chungju","Daegu","Daejeon","Dangjin","Dongducheon","Donghae","Gangneung","Geoje","Gimcheon",
    "Gimhae","Gimje","Gimpo","Gongju","Goyang","Gumi","Gunpo","Gunsan","Guri","Gwacheon","Gwangju","Gwangmyeong","Gwangyang","Gyeongju","Gyeongsan",
    "Gyeryong","Hanam","Hwaseong","Icheon","Iksan","Incheon","Jecheon","Jeongeup","Jeonju","Jeju","Jinju","Naju","Namyangju","Namwon",
    "Nonsan","Miryang","Mokpo","Mungyeong","Osan","Paju","Pocheon","Pohang","Pyeongtaek","Sacheon","Sangju","Samcheok","Sejong","Seogwipo","Seongnam",
    "Seosan","Siheung","Sokcho","Suncheon","Suwon","Taebaek","Tongyeong","Uijeongbu","Uiwang","Ulsan","Wonju","Yangju","Yangsan","Yeoju",
    "Yeongcheon","Yeongju","Yeosu","Yongin"
]

months =[ {"number":"01","value":"Yanvar"},
         {"number":"02", "value":"Fevral"},
         {"number":"03", "value":"Mart"},
         {"number":"04", "value":"Aprel"},
         {"number":"05", "value":"May"},
         {"number":"06", "value":"Iyun"},
         {"number":"07", "value":"Iyul"},
         {"number":"08", "value":"Avgust"},
         {"number":"09", "value":"Sentyabr"},
         {"number":"10", "value":"Oktyabr"},
         {"number":"11", "value":"Noyabr"},
         {"number":"12", "value":"Dekabr"},
         ]
def home(request):
     if request.method == 'POST':
        city = request.POST.get('city_select')
        mazhab = request.POST.get('mazhab_select')
        month = request.POST.get('month_select')
        year = request.POST.get('year')
        if len(year)==4:
            url = f"http://api.aladhan.com/v1/calendarByCity/{year}/{month}"
        else:
            current_year = datetime.now().year
            print(current_year)
            url = f"http://api.aladhan.com/v1/calendarByCity/{current_year}/{month}"
        

        querystring = {"country":" South Korea","city":city,"method":"1","school":mazhab}
        response = requests.get(url, params=querystring)
        context = {
            "response":response.json(),
            "cities":cities,
            "months":months
            }
        return render(request,'prayer/home.html',context=context)
     else:
         return render(request,'prayer/home.html')
