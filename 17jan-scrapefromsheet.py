# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 09:53:23 2022

@author: Dipen
"""

import pandas as pd
from bs4 import BeautifulSoup
import requests
import json
df = pd.read_csv('Pricing Comparision Tool.csv')
df.columns = ['Liquorkart_Product_Name', 'Liquorkart_SKU', 'Liquorkart_URL',
       'Boozebud_URL', 'Hairydog_URL', 'Dan_Murphy_URL', 'Liquorland_URL',
       'BWS_URL', 'Nicks','firstchoiceliquor', 'vintageceller',
       'kent_street_celler', 'paulsliquor', 'mr_danks_liquor', 'drink_society',
       'my_liquor_online', 'the_whiskycompany', 'devineceller']


#%%

# INDIVIDUAL

firstchoiceliquor_headers = {
    'authority': 'www.firstchoiceliquor.com.au',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    # Requests sorts cookies= alphabetically
    # 'cookie': '__uzma=7eac7273-bbc1-49ed-9417-5159ecb6661b; __uzmb=1652059114; SSID=CQCRHx0AAAAAAAD-a3hi5wpA7-preGIWAAAAAAAAAAAAKZ2BYgC7SA; SSSC=5.G7095539955602033383.22|0.0; SSRT=KZ2BYgQBAA; AMCVS_0B3D037254C7DE490A4C98A6%40AdobeOrg=1; SameSite=None; CL_FCLM_02_UBT=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjX3JvbGUiOiJBbm9ueW1vdXMiLCJjX2lkIjoiezkxMTg0NWRmLWVjYmQtNDc5MC1iOTY5LWE0MTFjYTQ4NzcyNX0iLCJjX2JyYW5kIjoiZmMiLCJjX2F4X2lkIjoiIiwibmJmIjoxNjUyNjYxNTQ3LCJleHAiOjE2NTI2OTAzNDcsImlhdCI6MTY1MjY2MTU0NywiaXNzIjoic2VsZiIsImF1ZCI6Imh0dHBzOi8vd3d3LmNvbGVzbGlxdW9yLmNvbS5hdSJ9.7v9Y_Z8PHid5uESXStFZ-TyrHWqRyBVLBJwWVXvLNNk; CL_FCLM_02_ULN=; CL_FCLM_02_UFN=; CL_FCLM_02_UAID=; CL_FCLM_02_UPOA=false; CL_FCLM_02_UDP=false; ADRUM_BTa=R:37|g:e3ef1ca1-118f-483a-b431-c02907775b5f|n:coles-prod_e0c95006-bd91-4181-bc2e-caaca584feda; ADRUM_BT1=R:37|i:490531|e:169; BVImplmain_site=18596; __uzmd=1652661556; KP_UIDz-ssn=03XkQ42UAkzUKcwBbXLJdnInWHRf4eedMVQwTcWfZ4eBfhMZzhoWjdEE0YJW6TzfvJ1Cg6eldr6rRPBdEAkVGDhhLYZ7xD4CteAhtSiW6oZZGPGIigIUaYP4O6aE44ajC3qiZmdyn60N6HsXo71vaPQeeR1; KP_UIDz=03XkQ42UAkzUKcwBbXLJdnInWHRf4eedMVQwTcWfZ4eBfhMZzhoWjdEE0YJW6TzfvJ1Cg6eldr6rRPBdEAkVGDhhLYZ7xD4CteAhtSiW6oZZGPGIigIUaYP4O6aE44ajC3qiZmdyn60N6HsXo71vaPQeeR1; AMCV_0B3D037254C7DE490A4C98A6%40AdobeOrg=-432600572%7CMCIDTS%7C19129%7CMCMID%7C65101274210646873479190368919597715077%7CMCOPTOUT-1652668757s%7CNONE%7CvVersion%7C4.5.2; __uzmc=70318142087385',
    'referer': 'https://www.firstchoiceliquor.com.au/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
}

price=[]
link=[]
firstchoice = df[['firstchoiceliquor']]
firstchoice.dropna(inplace=True)
firstchoice = firstchoice[firstchoice['firstchoiceliquor'].str.match('https://www.firstchoiceliquor.com.au/')]


s = requests.Session()
s.headers.update({'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'})

for i in firstchoice['firstchoiceliquor']:
    print(i)
    link.append(i)
    pid = i.split("/")
    cat  = pid[3]
    print(cat)
    pid = pid[-1]
    pid = pid.split("_")
    pid = pid[-1]
    if  "?uom=" in pid:
        pid = pid.replace('?uom=','_')
        pid=pid.lower()
        print(pid)
    try:
        if cat == "spirits":
            url = 'https://www.firstchoiceliquor.com.au/api/products/fc/nsw/spirits/' + pid
            print(url)
            soup = BeautifulSoup(s.get(url,headers=firstchoiceliquor_headers).text,"html.parser")
            site_json=json.loads(soup.text)
            if site_json['product']is not None:
                if site_json['product']['stock']['delivery'] == "No Stock":
                    print('OOS')
                    price.append(0)
                else:
                    print(site_json['product']['price']['normal'])
                    price.append(site_json['product']['price']['normal'])
            else:
                print('None')
                price.append(0)
        elif cat == "beer":
            url = "https://www.firstchoiceliquor.com.au/api/products/fc/nsw/beer/" + pid
            soup = BeautifulSoup(s.get(url,headers=firstchoiceliquor_headers).text,"html.parser")
            site_json=json.loads(soup.text)
            if site_json['product']is not None:
                if site_json['product']['stock']['delivery'] == "No Stock":
                    print('OOS')
                    price.append(0)
                else:
                    print(site_json['product']['price']['normal'])
                    price.append(site_json['product']['price']['normal'])
            else:
                print('None')
                price.append(0)
        else:
            print('OOS or bad connection')
            price.append(0)
    except json.JSONDecodeError:
        print('Sheild Square Captcha')
        price.append(0)
        break
    
      
firstchoice['firstchoiceliquor_price'] = price
res = pd.DataFrame()
res['firstchoiceliquor'] = firstchoice['firstchoiceliquor']
res['firstchoiceliquor_price'] = firstchoice['firstchoiceliquor_price']




df = df.join(firstchoice.set_index('firstchoiceliquor'), on='firstchoiceliquor')                                                                             
df = df.drop_duplicates()

#response = requests.get('https://www.firstchoiceliquor.com.au/api/products/fc/nsw/beer/3112135', headers=firstchoiceliquor_headers)



#%%
# INDIVIDUAL

vintage_headers = {
    'authority': 'www.vintagecellars.com.au',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    # Requests sorts cookies= alphabetically
    # 'cookie': .'__uzma=44cbccff-7c7e-4466-9d40-43abb0f58198; __uzmb=1652063515; SSID=CQAhpx0AAAAAAAAffXhiNwiAFRt9eGIDAAAAAAAAAAAAI_p5YgDRZw; SSSC=4.G7095558785380386871.3|0.0; AMCVS_0B3D037254C7DE490A4C98A6%40AdobeOrg=1; CL_VC_02_UBT=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjX3JvbGUiOiJBbm9ueW1vdXMiLCJjX2lkIjoie2EwZGVhYzFhLTJkNWUtNDg0MS05ZGM4LTdiZWM0MmY3ZjVhOH0iLCJjX2JyYW5kIjoidmMiLCJjX2F4X2lkIjoiIiwibmJmIjoxNjUyMTYxMDYyLCJleHAiOjE2NTIxODk4NjIsImlhdCI6MTY1MjE2MTA2MiwiaXNzIjoic2VsZiIsImF1ZCI6Imh0dHBzOi8vd3d3LmNvbGVzbGlxdW9yLmNvbS5hdSJ9.-LdUi5FT1BPYej3YMOvyZrCJBoCpF1aciOzcsEEJhHY; CL_VC_02_ULN=; CL_VC_02_UFN=; CL_VC_02_UAID=; CL_VC_02_UPOA=false; CL_VC_02_UDP=false; BVImplmain_site=18425; SSRT=a_p5YgQBAA; AMCV_0B3D037254C7DE490A4C98A6%40AdobeOrg=-432600572%7CMCIDTS%7C19122%7CMCMID%7C01695494457066736202469769841636932060%7CMCOPTOUT-1652168332s%7CNONE%7CvVersion%7C4.5.2; __uzmd=1652161132; __uzmc=9167429579505; KP_UIDz-ssn=03WTNsaUCzpVQ6kUIJyedFEnIXCoIl8alcED2E4kizdQD5R1GYgLOg9P8cDbpA0EK70AneJsJ32jMIKzAgrjsry9ym2pIcIFnYL0nZsyNiYUA4HWcIPYwU3o5Io40vOQfTLcYpTihRseacfutIzSwbD1lLF; KP_UIDz=03WTNsaUCzpVQ6kUIJyedFEnIXCoIl8alcED2E4kizdQD5R1GYgLOg9P8cDbpA0EK70AneJsJ32jMIKzAgrjsry9ym2pIcIFnYL0nZsyNiYUA4HWcIPYwU3o5Io40vOQfTLcYpTihRseacfutIzSwbD1lLF',
    'referer': 'https://www.vintagecellars.com.au/beer/ballistic-hawaiian-haze-pale-ale-can-375ml_3859630',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
}
price=[]
link=[]
vintage = df[['vintageceller']]
vintage.dropna(inplace=True)
vintage = vintage[vintage['vintageceller'].str.match('https://www.vintagecellars.com.au/')]

s = requests.Session()
s.headers.update({'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'})


for i in vintage['vintageceller']:
    print(i)
    link.append(i)
    pid = i.split("/")
    cat  = pid[3]
    print(cat)
    pid = pid[-1]
    pid = pid.split("_")
    pid = pid[-1]
    if  "?uom=" in pid:
        pid = pid.replace('?uom=','_')
        pid=pid.lower()
        print(pid)
    if cat == "spirits":
        url = "https://www.vintagecellars.com.au/api/products/vc/nsw/spirits/" + pid
        soup = BeautifulSoup(s.get(url,headers=vintage_headers).text,"html.parser")
        site_json=json.loads(soup.text)
        if site_json['product']is not None:
            if site_json['product']['stock']['delivery'] == "No Stock":
                print('OOS')
                price.append(0)
            else:
                print(site_json['product']['price']['current'])
                price.append(site_json['product']['price']['current'])
        else:
            print('None')
            price.append(0)
    elif cat == "beer":
        url = "https://www.vintagecellars.com.au/api/products/vc/nsw/beer/" + pid
        soup = BeautifulSoup(s.get(url,headers=vintage_headers).text,"html.parser")
        site_json=json.loads(soup.text)
        if site_json['product']is not None:
            if site_json['product']['stock']['delivery'] == "No Stock":
                print('OOS')
                price.append(0)
            else:
                print(site_json['product']['price']['current'])
                price.append(site_json['product']['price']['current'])
        else:
            print('None')
            price.append(0)
    else:
        print('OOS or bad connection')
        price.append(0)
        
        
vintage['vintageceller_price'] = price
res = pd.DataFrame()
res['vintageceller'] = vintage['vintageceller']
res['vintageceller_price'] = vintage['vintageceller_price']




df = df.join(vintage.set_index('vintageceller'), on='vintageceller')                                                                             
df = df.drop_duplicates()
#%%

# SELECT ALL AND RUN
price=[]
link=[]
kent = df[['kent_street_celler']]
kent.dropna(inplace=True)
kent = kent[kent['kent_street_celler'].str.match('https://kentstreetcellars.com.au/products/')]


for i in kent['kent_street_celler']:
    print(i)
    link.append(i)
    soup = BeautifulSoup(requests.get(i).text,"html.parser")
    p = soup.find('div',class_='price--main').text
    if soup.find('span',class_='product--badge badge--soldout'):
        print('oos')
        price.append(0)
    else :
        print('instock')
        p = p.strip()
        p = p.split("$")
        p = p[-1]
        print(p)
        price.append(p)

kent['kent_street_celler_price'] = price
res = pd.DataFrame()
res['kent_street_celler'] = kent['kent_street_celler']
res['kent_street_celler_price'] = kent['kent_street_celler_price']
df = df.join(kent.set_index('kent_street_celler'), on='kent_street_celler')                                                                             
df = df.drop_duplicates()

#%%
price=[]
link=[]
paul = df[['paulsliquor']]
paul.dropna(inplace=True)
paul = paul[paul['paulsliquor'].str.match('https://www.paulsliquor.com.au/')]

for i in paul['paulsliquor']:
    print(i)
    link.append(i)
    try:
        soup = BeautifulSoup(requests.get(i).text,"html.parser")
        if soup.find('button',class_="add-to-cart").text == "Sold Out":
            print('OOS')
            price.append(0)
        else:
            p = soup.find('span',class_="price")
            second=p.text[-2:]
            first = p.text[:-2 or None]
            pr = first + "."+second
            print(pr)
            price.append(pr)
        
    except Exception:
        price.append(0)
        
paul['paulsliquor_price'] = price
res = pd.DataFrame()
res['paulsliquor'] = link
res['paulsliquor_price'] = paul['paulsliquor_price']
df = df.join(paul.set_index('paulsliquor'), on='paulsliquor')                                                                             
df = df.drop_duplicates()

#%%

price=[]
link=[]
dank = df[['mr_danks_liquor']]
dank.dropna(inplace=True)
dank = dank[dank['mr_danks_liquor'].str.match('https://www.mrdanksliquor.com.au/product/')]

s = requests.session()
for i in dank['mr_danks_liquor']:
    print(i)
    link.append(i)
    try:
        soup = BeautifulSoup(s.get(i).text,"html.parser")
        if soup.find('p',class_="stock").text == "Out of stock":
            price.append(0)
            print('OOS')
        else:    
            print(soup.find('bdi').text)
            price.append(soup.find('bdi').text)
    except Exception:
        print('error')
        price.append(0)
        
dank['mr_danks_liquor_price'] = price
res = pd.DataFrame()
res['mr_danks_liquor'] = link
res['mr_danks_liquor_price'] = dank['mr_danks_liquor_price']
df = df.join(dank.set_index('mr_danks_liquor'), on='mr_danks_liquor')                                                                             
df = df.drop_duplicates()

#%%
price=[]
link=[]
ds = df[['drink_society']]
ds.dropna(inplace=True)
ds = ds[ds['drink_society'].str.match('https://thedrinksociety.com.au/')]
s = requests.session()

for i in ds['drink_society']:
    print(i)
    link.append(i)
    soup = BeautifulSoup(s.get(i).text,"html.parser")
    if soup.find('button',class_="btn").text.strip() == "Sold Out":
        price.append(0)
        print('OOS')
    else:
        pr = soup.find('span',class_="product__price").text
        pr = pr.strip()
        pr = pr.split("$")
        pr = "".join(pr)
        price.append(pr)

ds['drink_society_price'] = price
res = pd.DataFrame()
res['drink_society'] = link
res['drink_society_price'] = dank['mr_danks_liquor_price']
df = df.join(ds.set_index('drink_society'), on='drink_society')                                                                             
df = df.drop_duplicates()


#%%
price=[]
link=[]
myliquoronline = df[['my_liquor_online']]
myliquoronline.dropna(inplace=True)
myliquoronline = myliquoronline[myliquoronline['my_liquor_online'].str.match('https://myliquoronline.com.au/product/')]
s = requests.session()
s.headers.update({'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'})


for i in myliquoronline['my_liquor_online']:
    print(i)
    link.append(i)
    soup = BeautifulSoup(s.get(i).text,"html.parser")
    try:
        soup = BeautifulSoup(s.get(i).text,"html.parser")
        if soup.find('p',class_="stock").text == "Out of stock":
            price.append(0)
            print('OOS')
        else:    
            pr = soup.find('p',class_='price').text
            pr = pr.split("$")
            pr = pr[1]
            pr = "".join(pr)
            print(pr)
            price.append(pr)
    except Exception:
        print('error')
        price.append(0)
        
myliquoronline['my_liquor_online_price'] = price
myliquoronline['my_liquor_online_price'] = myliquoronline['my_liquor_online_price'].str.replace(r' AUD', '')
res = pd.DataFrame()
res['my_liquor_online'] = link
res['my_liquor_online_price'] = myliquoronline['my_liquor_online_price']
df = df.join(myliquoronline.set_index('my_liquor_online'), on='my_liquor_online')                                                                             
df = df.drop_duplicates()
#%%
price=[]
link=[]
whiskycompany = df[['the_whiskycompany']]
whiskycompany.dropna(inplace=True)
whiskycompany = whiskycompany[whiskycompany['the_whiskycompany'].str.match('https://www.thewhiskycompany.com.au/product/')]
s = requests.session()
s.headers.update({'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'})

for i in whiskycompany['the_whiskycompany']:
    print(i)
    link.append(i)
    soup = BeautifulSoup(s.get(i).text,"html.parser")
    try:
        soup = BeautifulSoup(s.get(i).text,"html.parser")
        if soup.find('p',class_="stock").text == "Out of stock":
            price.append(0)
            print('OOS')
        else:    
            pr = soup.find('p',class_='price').text
            pr = pr.split("$")
            pr = pr[1]
            pr = "".join(pr)
            print(pr)
            price.append(pr)
    except Exception:
        print('error')
        price.append(0)


whiskycompany['the_whiskycompany_price'] = price
whiskycompany['the_whiskycompany_price'] = whiskycompany['the_whiskycompany_price'].str.replace(r' AUD', '')
res = pd.DataFrame()
res['the_whiskycompany'] = link
res['the_whiskycompany_price'] = whiskycompany['the_whiskycompany_price']
df = df.join(whiskycompany.set_index('the_whiskycompany'), on='the_whiskycompany')                                                                             
df = df.drop_duplicates()
#%%
price=[]
link=[]
devineceller = df[['devineceller']]
devineceller.dropna(inplace=True)
devineceller = devineceller[devineceller['devineceller'].str.match('https://devinecellars.com.au/buy/')]
s = requests.session()
s.headers.update({'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'})

for i in devineceller['devineceller']:
    print(i)
    link.append(i)
    cat = []
    try:
        soup = BeautifulSoup(s.get(i).text,"html.parser")
        for j in soup.find_all('div',class_="breadcrumb-trail"):
            j = j.text.split("/")
            cat.append(j[1])
        if soup.find('p',class_="stock"):
            print('oos')
            price.append(0)
        else:
            pr = soup.find("bdi").text
            pr=pr.split("$")
            pr="".join(pr)
            print(pr)
            price.append(pr)
    except Exception:
        price.append(0)
        print('error')

devineceller['devineceller_price'] = price
res = pd.DataFrame()
res['devineceller'] = link
res['devineceller_price'] = devineceller['devineceller_price']
df = df.join(devineceller.set_index('devineceller'), on='devineceller')                                                                             
df = df.drop_duplicates()
#%%
headers = {
    'authority': 'www.boozebud.com',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'accept': 'application/json',
    'content-type': 'application/json; charset=UTF-8',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.boozebud.com/p/manlyspiritscodistillery/australiandrygin',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'STABLE_SESSION_ID=node01vnnk0hoixjnh1u5yqdndwevul155548|6e4847ca8bf31c9ecb80d99e080d3eda5694e2ced31698a5cf978fc42cdceac1; JSESSIONID=node01oinx3ik8bvx71103mqcye4pko291.node0; ab.storage.sessionId.31e1b32a-6429-4646-99ed-866675041cf0=%7B%22g%22%3A%22d4d99760-a851-9643-b36f-d99f80bee737%22%2C%22e%22%3A1642404608869%2C%22c%22%3A1642399559676%2C%22l%22%3A1642402808869%7D; ph_d5K-HmyjqsKWeaSYsWjbzyX4JOEXIeiLNu3k_GbNNS8_posthog=%7B%22distinct_id%22%3A%2217d4b5edb1017-0d1b6bfb48ab46-978183a-1fa400-17d4b5edb11e77%22%2C%22%24device_id%22%3A%2217d4b5edb1017-0d1b6bfb48ab46-978183a-1fa400-17d4b5edb11e77%22%2C%22%24search_engine%22%3A%22google%22%2C%22%24initial_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%22www.google.com%22%2C%22%24session_recording_enabled%22%3Afalse%2C%22%24active_feature_flags%22%3A%5B%5D%7D',
}

price = []
link = []
df1 = df[['Boozebud_URL']]
df1.dropna(inplace=True)
df1 = df1[df1['Boozebud_URL'].str.match('https://www.boozebud.com/')]
for i in df1['Boozebud_URL']:
    try:
        print(i)
        url = 'https://www.boozebud.com/a/producturl/' + i[25:]
        print(url)
        soup = BeautifulSoup(requests.get(url,headers=headers).text,"html.parser")
        site_json=json.loads(soup.text)
        link.append(i)
        if  site_json is not None:
            for url in site_json['variants']:
                print(url)
                if site_json['tType'] == "tspirits":
                    if url["prefix"] == "Bottle" or url["prefix"] == "Pack":
                        if url["available"] == True:
                            value = url["price"]
                        else:
                            value = 0
                else : 
                   if url["prefix"] == "Case":
                       if url['available']==True:
                           
                           value = url["price"] 
                       else :
                           value = 0
            price.append(value)
            print('price:',value)
            value = None     
        else:
            price.append(0)
            value=None
    except requests.exceptions.ConnectionError or TypeError:
       price.append(0)
       value=None
       print( "Connection refused")
df1['Boozebud_price']  = price    

res = pd.DataFrame()
res['Boozebud_URL'] = df1['Boozebud_URL']
res['Boozebud_price'] = df1['Boozebud_price']


df = df.join(df1.set_index('Boozebud_URL'), on='Boozebud_URL')                                                                             
df = df.drop_duplicates()

#%%
# =============================================================================
# proxies = {
#     'https': 'https://170.155.5.235:8080',
#     'https': 'https://8.213.129.51:80',
# }
# =============================================================================
dan_headers = {
    'authority': 'api.danmurphys.com.au',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'accept': 'application/json, text/plain, */*',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'origin': 'https://www.danmurphys.com.au',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.danmurphys.com.au/',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
}


df2 = df[['Dan_Murphy_URL']]
df2.dropna(inplace=True)

df2 = df2[df2['Dan_Murphy_URL'].str.match('https://www.danmurphys.com.au/product/')]

df2 = df2[df2['Dan_Murphy_URL'] != 'https://www.danmurphys.com.au/help/help-centre/articles/360000043436-Lowest-Liquor-Price-Guarantee']

s = requests.session()

price = []
link = []
for i in df2['Dan_Murphy_URL']:
    print(i)
    #pid = i.split('/')[-2]
    pid = i.split('/')[4]
    pid = pid[3:]
    try:
        link.append(i)
        url = 'https://api.danmurphys.com.au/apis/ui/Product/' +pid
        print(url)
        soup = BeautifulSoup(s.get(url, headers=dan_headers).text,"html.parser")
        site_json=json.loads(soup.text)
        if "Products" not in site_json or 'ResponseStatus' in site_json or site_json['Products'][0]['StockOnHand'] == 0:
            if "Products" in site_json:
                if 'availableinventoryqty' in site_json['Products'][0]['Inventory']:
                    if site_json['Products'][0]['Inventory']['availableinventoryqty'] == 0:
                        print("OOS")
                        price.append(0)
                else:
                    price.append(0)
                    print("OOS or no connection")
            else:
                price.append(0)
                print("OOS or no connection")
        else:
            if 'availableinventoryqty' in site_json['Products'][0]['Inventory']:
                if site_json['Products'][0]['Inventory']['availableinventoryqty'] == 0:
                    print("OOS")
                    price.append(0)
                else:
                    print("Stock: ",site_json['Products'][0]['StockOnHand'])
                    for element in site_json['Products'][0]['Prices']:
                        if 'promoprice' in element:
                            print(element)
                            del site_json['Products'][0]['Prices'][element]
                            break
                    if site_json['Products'][0]['Prices'] != {}:
                        temp_price = []
                        #print(site_json['Products'][0]['Prices']['caseprice']['Value'])
                        if len(site_json['Products'][0]['Prices']) == 3 and  site_json['Products'][0]['Categories'][0]['Name'] == 'Beer':
                            a = site_json['Products'][0]['Prices']['caseprice']
                            print(a['Value'])
                            price.append(a['Value'])
                        elif site_json['Products'][0]['Categories'][0]['Name'] == 'Cider':
                            a = site_json['Products'][0]['Prices']['caseprice']
                            print(a['Value'])
                            price.append(a['Value'])
                        else:
                            if len(site_json['Products'][0]['Categories']) > 1:
                                if site_json['Products'][0]['Categories'][1]['Name'] == 'Premix Drinks' or site_json['Products'][0]['Categories'][1]['Name'] == 'Seltzers' or site_json['Products'][0]['Categories'][1]['Name'] == 'Soft Drinks':
                                    for p in site_json['Products'][0]['Prices']:
                                        #print(site_json['Products'][0]['Prices'][p]['Value'])
                                        temp_price.append(site_json['Products'][0]['Prices'][p]['Value'])
                                    print(max(temp_price))
                                    price.append(max(temp_price))
                                else:
                                    for p in site_json['Products'][0]['Prices']:
                                        #print(site_json['Products'][0]['Prices'][p]['Value'])
                                        temp_price.append(site_json['Products'][0]['Prices'][p]['Value'])
                                    print(temp_price[0])
                                    price.append(temp_price[0])
                            else:
                                for p in site_json['Products'][0]['Prices']:
                                    #print(site_json['Products'][0]['Prices'][p]['Value'])
                                    temp_price.append(site_json['Products'][0]['Prices'][p]['Value'])
                                print(temp_price[0])
                                price.append(temp_price[0])
                    else:
                        print(0)
                        price.append(0)       
            else:
                print("Stock: ",site_json['Products'][0]['StockOnHand'])
                for element in site_json['Products'][0]['Prices']:
                    if 'promoprice' in element:
                        print(element)
                        del site_json['Products'][0]['Prices'][element]
                        break
                if site_json['Products'][0]['Prices'] != {}:
                    temp_price = []
                    #print(site_json['Products'][0]['Prices']['caseprice']['Value'])
                    if len(site_json['Products'][0]['Prices']) == 3 and  site_json['Products'][0]['Categories'][0]['Name'] == 'Beer':
                        a = site_json['Products'][0]['Prices']['caseprice']
                        print(a['Value'])
                        price.append(a['Value'])
                    elif site_json['Products'][0]['Categories'][0]['Name'] == 'Cider':
                        a = site_json['Products'][0]['Prices']['caseprice']
                        print(a['Value'])
                        price.append(a['Value'])
                    else:
                        if len(site_json['Products'][0]['Categories']) > 1:
                            if site_json['Products'][0]['Categories'][1]['Name'] == 'Premix Drinks' or site_json['Products'][0]['Categories'][1]['Name'] == 'Seltzers' or site_json['Products'][0]['Categories'][1]['Name'] == 'Soft Drinks':
                                for p in site_json['Products'][0]['Prices']:
                                    #print(site_json['Products'][0]['Prices'][p]['Value'])
                                    temp_price.append(site_json['Products'][0]['Prices'][p]['Value'])
                                print(max(temp_price))
                                price.append(max(temp_price))
                            else:
                                for p in site_json['Products'][0]['Prices']:
                                    #print(site_json['Products'][0]['Prices'][p]['Value'])
                                    temp_price.append(site_json['Products'][0]['Prices'][p]['Value'])
                                print(temp_price[0])
                                price.append(temp_price[0])
                        else:
                            for p in site_json['Products'][0]['Prices']:
                                #print(site_json['Products'][0]['Prices'][p]['Value'])
                                temp_price.append(site_json['Products'][0]['Prices'][p]['Value'])
                            print(temp_price[0])
                            price.append(temp_price[0])
                else:
                    print(0)
                    price.append(0)
                    
    except json.JSONDecodeError or KeyError:
        price.append(0)
        link.append(i)
        print( "Connection refused")
            
            
            
df2['Dan_murphy_price'] = price


res = pd.DataFrame()
res['Dan_Murphy_URL'] = df2['Dan_Murphy_URL']
res['Dan_murphy_price'] = df2['Dan_murphy_price']

df = df.join(res.set_index('Dan_Murphy_URL'), on='Dan_Murphy_URL')
df = df.drop_duplicates()

#%%
df3 = df[['Liquorland_URL']]
df3.dropna(inplace=True)
df3 = df3[df3['Liquorland_URL'].str.match('https://www.liquorland.com.au/')]
df3 = df3.drop_duplicates()
#there is search url and not product url in url
import re
sku_list=[]
import time



liqland_headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36', 'Accept-Encoding': 'gzip, deflate, br', 'accept': 'application/json, text/plain, */*', 'Connection': 'keep-alive', 'authority': 'www.liquorland.com.au', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"', 'ai-score-cluster': '', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'referer': 'https://www.liquorland.com.au/', 'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7', 'cookie': '__uzma=0faa5823-9a8c-4848-ad23-6711182ba7db; __uzmb=1641801157; AMCVS_0B3D037254C7DE490A4C98A6%40AdobeOrg=1; CL_LL_02_UBT=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjX3JvbGUiOiJBbm9ueW1vdXMiLCJjX2lkIjoiezM1ZDU5M2Q0LWQ4MjItNDAzNi1iZWIzLWE4ZDg1MjJjNGQ4Y30iLCJjX2JyYW5kIjoibGwiLCJjX2F4X2lkIjoiIiwibmJmIjoxNjQ0MDI5NTIwLCJleHAiOjE2NDQwNTgzMjAsImlhdCI6MTY0NDAyOTUyMCwiaXNzIjoic2VsZiIsImF1ZCI6Imh0dHBzOi8vd3d3LmNvbGVzbGlxdW9yLmNvbS5hdSJ9.rb5KTMYQxaUeM4ESCOW7nijInhxWFXfG2sYWmm-v6HU; CL_LL_02_ULN=; CL_LL_02_UFN=; CL_LL_02_UAID=; CL_LL_02_UPOA=false; CL_LL_02_UDP=false; SSID=CQDf4R0AAAAAAADX5dthgSsAU8Xl22EmAAAAAAAAAAAAxgL-YQBuOg; SSSC=6.G7051482354551892865.38|0.0; KP_UIDz-ssn=0Kjcug7FcGHUzVZwQjoBSQb7NEc8auIgDvbA3FIndq2slbBNd3vN8rc8pEmoyMn7vxaWLdUq2uJqtDPNxLLGFzfTBNf4K03R3rBMijsUf73MxfFomFZwaGE12S7Lhr1wOMQjD1VNK4VlHUVufgQVqXHBC; KP_UIDz=0Kjcug7FcGHUzVZwQjoBSQb7NEc8auIgDvbA3FIndq2slbBNd3vN8rc8pEmoyMn7vxaWLdUq2uJqtDPNxLLGFzfTBNf4K03R3rBMijsUf73MxfFomFZwaGE12S7Lhr1wOMQjD1VNK4VlHUVufgQVqXHBC; SSRT=8Qj-YQQBAA; AMCV_0B3D037254C7DE490A4C98A6%40AdobeOrg=1075005958%7CMCIDTS%7C19028%7CMCMID%7C78088235673109503290195770817961978732%7CMCOPTOUT-1644045590s%7CNONE%7CvVersion%7C4.4.1; __uzmd=1644038391; __uzmc=83778142034736'}

price = []
link = []
for i in df3['Liquorland_URL']:
    o = i.split('/')
    o = o[-1]
    o = re.findall('(?<=_).*$', str(o))
    if o != []:
        print(i)
        #print(o)
        url = 'https://www.liquorland.com.au/api/products/ll/nsw/beer/' + ''.join(o)
        if "?uom=" in url:
            url = url.replace("?uom=", "_")
            url = url.lower()
        print(url)
        soup = BeautifulSoup(requests.get(url, headers=liqland_headers,timeout=10).text,"html.parser")
        title = soup.title
        try:
            site_json=json.loads(soup.text)
            if soup.title == "" or site_json['product'] == None:
                print('bad gateway')
                price.append(0)
                link.append(i)
            else:
                
                site_json=json.loads(soup.text)
                print(site_json['product']['price']['normal'])
                price.append(site_json['product']['price']['normal'])
                link.append(i)
        except json.JSONDecodeError:
            print("Too many requests, Please open https://www.liquorland.com.au in browser and solve captcha , then try again.")
            break
        
res = pd.DataFrame()
res['Liquorland_URL'] = link
res['Liquorland_price'] = price
df = df.join(res.set_index('Liquorland_URL'), on='Liquorland_URL')
df = df.drop_duplicates()

import requests

headers = {
    'authority': 'www.liquorland.com.au',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'accept': 'application/json, text/plain, */*',
    'ai-score-cluster': '',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.liquorland.com.au/',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': '__uzma=0faa5823-9a8c-4848-ad23-6711182ba7db; __uzmb=1641801157; AMCVS_0B3D037254C7DE490A4C98A6%40AdobeOrg=1; CL_LL_02_UBT=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjX3JvbGUiOiJBbm9ueW1vdXMiLCJjX2lkIjoiezM1ZDU5M2Q0LWQ4MjItNDAzNi1iZWIzLWE4ZDg1MjJjNGQ4Y30iLCJjX2JyYW5kIjoibGwiLCJjX2F4X2lkIjoiIiwibmJmIjoxNjQ0MDI5NTIwLCJleHAiOjE2NDQwNTgzMjAsImlhdCI6MTY0NDAyOTUyMCwiaXNzIjoic2VsZiIsImF1ZCI6Imh0dHBzOi8vd3d3LmNvbGVzbGlxdW9yLmNvbS5hdSJ9.rb5KTMYQxaUeM4ESCOW7nijInhxWFXfG2sYWmm-v6HU; CL_LL_02_ULN=; CL_LL_02_UFN=; CL_LL_02_UAID=; CL_LL_02_UPOA=false; CL_LL_02_UDP=false; SSID=CQDf4R0AAAAAAADX5dthgSsAU8Xl22EmAAAAAAAAAAAAxgL-YQBuOg; SSSC=6.G7051482354551892865.38|0.0; KP_UIDz-ssn=0Kjcug7FcGHUzVZwQjoBSQb7NEc8auIgDvbA3FIndq2slbBNd3vN8rc8pEmoyMn7vxaWLdUq2uJqtDPNxLLGFzfTBNf4K03R3rBMijsUf73MxfFomFZwaGE12S7Lhr1wOMQjD1VNK4VlHUVufgQVqXHBC; KP_UIDz=0Kjcug7FcGHUzVZwQjoBSQb7NEc8auIgDvbA3FIndq2slbBNd3vN8rc8pEmoyMn7vxaWLdUq2uJqtDPNxLLGFzfTBNf4K03R3rBMijsUf73MxfFomFZwaGE12S7Lhr1wOMQjD1VNK4VlHUVufgQVqXHBC; SSRT=8Qj-YQQBAA; AMCV_0B3D037254C7DE490A4C98A6%40AdobeOrg=1075005958%7CMCIDTS%7C19028%7CMCMID%7C78088235673109503290195770817961978732%7CMCOPTOUT-1644045590s%7CNONE%7CvVersion%7C4.4.1; __uzmd=1644038391; __uzmc=83778142034736',
}

response = requests.get('https://www.liquorland.com.au/api/campaign/ll/nsw/home')
response.text
         
#%%%
df4 = df[['BWS_URL']]
df4.dropna(inplace=True)
df4 = df4[df4['BWS_URL'].str.match('https://bws.com.au/product/')]

bws_headers = {
    'authority': 'api.bws.com.au',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'accept': 'application/json, text/plain, */*',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'origin': 'https://bws.com.au',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://bws.com.au/',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
}


price = []
pr=[]
link=[]
for i in df4['BWS_URL']:
    print(i)
    pid = i.split('/')
    url = 'https://api.bws.com.au/apis/ui/Product/' + pid[4]
    soup = BeautifulSoup(requests.get(url, headers=bws_headers,timeout=10).text,"html.parser")
    site_json=json.loads(soup.text)
    for p in site_json['Products']: 
        del p['RecommendedProducts']
        del p['ProductsInSameOffer']
        del p['BundleContent']
        del p['Categories']
        del p['ImageTag']
        del p['FooterTag']
        del p['PercentageOffTag']
        del p['FixedPricePromoTag']
        del p['AdditionalDetails']
        del p['Tags']
        print(p['IsAvailable'])
        if p['IsAvailable'] == True:
            pr.append(p['Price'])
        else:
            print('OOS')
            pr.append(0)
    print(pr)
    if pr == []:
        price.append(0)
    else:
        print(max(pr))
        price.append(max(pr))
    link.append(i)
    pr = []

res = pd.DataFrame()
res['BWS_URL'] = link
res['BWS_Price'] = price

df = df.join(res.set_index('BWS_URL'), on='BWS_URL')
df = df.drop_duplicates()
#%%

df5 = df[['Nicks']]
df5.dropna(inplace=True)
df5 = df5[df5['Nicks'].str.match('https://www.nicks.com.au/products/')]



nicks_headers = {
    'authority': 'www.nicks.com.au',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'upgrade-insecure-requests': '1',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'empty',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
}

price = []
link=[]
for i in df5['Nicks']:
    pid = i.split('/')
    url = 'https://www.nicks.com.au/products/' + pid[4]
    print(url)
    link.append(i)
    try:
        soup = BeautifulSoup(requests.get(url, headers=nicks_headers,timeout=10).text,"html.parser")
        if "Page Not Found | Nicks Wine Merchants" in soup.title:
            price.append(0)
        else :
            data = json.loads(soup.find('script', type='application/ld+json').text)    
            if data !=[]:
                if data[0]['offers']['availability'] == "https://schema.org/OutOfStock":
                    print(data[0]['offers']['availability'])
                    price.append(0)
                    print(0)
                else:
                    print(data[0]['offers']['price'])
                    price.append(data[0]['offers']['price'])
    except ConnectionError:
        price.append(0)
            
res = pd.DataFrame()
res['Nicks'] = link
res['Nicks_price'] = price

df = df.join(res.set_index('Nicks'), on='Nicks')
df = df.drop_duplicates()

    
#%%

df6 = df[['Hairydog_URL']]
df6.dropna(inplace=True)
df6 = df6[df6['Hairydog_URL'].str.match('https://www.hairydog.com.au/product/')]

import requests

hairy_headers = {
    'authority': 'www.hairydog.com.au',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.hairydog.com.au/category/all-beer',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
}


price = []
link = []
for i in df6['Hairydog_URL']:
    print(i)
    link.append(i)
    soup = BeautifulSoup(requests.get(i, headers=headers,timeout=20).text,"lxml")
    try:
        if soup.find('button',class_="ProductDetails_product-desktop-cart__button__3puKK").text=="Out of Stock":
            print ('OOS')
            price.append(0)
        else:
            if soup.find_all('div',class_="ProductPage_productpage__price-section__1VlWR"):
                category = soup.find_all('div',class_="Navigation_view-cart-link__home__D7I_h")[1].text
                category = category.split(">")
                category = category[0].strip()
                prices = soup.find_all('div',class_="ProductDetails_product-desktop-cart__was-price-wrapper__EGTnp")
                if category == "Spirits" or category == "Non-Alcoholic":
                    pr = prices[0].text.split("$")
                    price.append(pr[-1])
                    print(pr[-1])
                else:
                    pr = prices[1].text.split("$")
                    price.append(pr[-1])
                    print("Tag Found")
                    print(pr[-1])
            else:
                print(0)
                price.append(0)
    except Exception:
        price.append(0)
        print(Exception)

    
    
res = pd.DataFrame()
res['Hairydog_URL'] = link
res['Hairydog_Price'] = price           
        
df = df.join(res.set_index('Hairydog_URL'), on='Hairydog_URL')      
df = df.drop_duplicates()
#%%


lq = df[['Liquorkart_URL']]
lq.dropna(inplace=True)

lq = lq[lq['Liquorkart_URL'].str.match('https://www.liquorkart.com.au/products/')]

#lq = lq[lq['Liquorkart_URL'] != 'https://www.danmurphys.com.au/help/help-centre/articles/360000043436-Lowest-Liquor-Price-Guarantee']


price = []
link = []



for i in  lq['Liquorkart_URL']:
    link.append(i)
    print(i)
    try: 
        soup = BeautifulSoup(requests.get(i,timeout=10).text,"lxml")
        cur_price = soup.find_all("span", class_= "current_price")
        if cur_price == []:
            print('0')
            price.append(0)
        else:
            for i in cur_price:
                print(i.text)
                price.append(i.text)
    except Exception:
        print('eror')
        price.append(0)
        
lq['Liquorkart_Price'] = price

res = pd.DataFrame()
res['Liquorkart_URL'] = lq['Liquorkart_URL']
res['Liquorkart_Price'] = lq['Liquorkart_Price']

df = df.join(res.set_index('Liquorkart_URL'), on='Liquorkart_URL')
df = df.drop_duplicates()

#%%

dff =df[['Liquorkart_Product_Name', 'Liquorkart_SKU','Liquorkart_Price', 'Hairydog_Price', 'Boozebud_price','Dan_murphy_price', 'Liquorland_price', 'BWS_Price', 'Nicks_price','firstchoiceliquor_price','vintageceller_price', 'kent_street_celler_price', 'paulsliquor_price',
'mr_danks_liquor_price', 'drink_society_price',
'my_liquor_online_price', 'the_whiskycompany_price',
'devineceller_price']]

dff.to_csv('prices.csv')

