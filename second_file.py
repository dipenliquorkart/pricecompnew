# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 06:06:42 2022

@author: Dipen
"""
import pandas as pd
import numpy as np 
from datetime import date
date = date.today()
d4 = date.strftime("%b-%d")

df = pd.read_csv('prices.csv',index_col=0,encoding='utf-8-sig')


lqprice = pd.read_csv('products.csv',index_col=0)

lqprice = lqprice[['Variant SKU','Cost per item','Variant Inventory Qty']]

df = df.join(lqprice.set_index('Variant SKU'), on='Liquorkart_SKU')     

df.columns =['Liquorkart_Product_Name', 'Liquorkart_SKU', 'liquorkart_selling_price',
       'Hairydog_Price', 'Boozebud_price', 'Dan_murphy_price',
       'Liquorland_price', 'BWS_Price', 'Nicks_price',
       'firstchoiceliquor_price','vintageceller_price', 'kent_street_celler_price',
       'paulsliquor_price', 'mr_danks_liquor_price', 'drink_society_price',
       'my_liquor_online_price', 'the_whiskycompany_price',
       'devineceller_price', 'liquorkart_cost_price', 'Variant Inventory Qty']



df['liquorkart_selling_price'] = df['liquorkart_selling_price'].str.replace(r'$', '')
df['liquorkart_selling_price'] = df['liquorkart_selling_price'].str.replace(r',', '')
df['liquorkart_selling_price'] = df['liquorkart_selling_price'].astype(float)

df['kent_street_celler_price'] = df['kent_street_celler_price'].str.replace(r'$', '')
df['kent_street_celler_price'] = df['kent_street_celler_price'].str.replace(r',', '')
df['kent_street_celler_price'] = df['kent_street_celler_price'].astype(float)

df['mr_danks_liquor_price'] = df['mr_danks_liquor_price'].str.replace(r'$', '')
df['mr_danks_liquor_price'] = df['mr_danks_liquor_price'].str.replace(r',', '')
df['mr_danks_liquor_price'] = df['mr_danks_liquor_price'].astype(float)

df['drink_society_price'] = df['drink_society_price'].str.replace(r'$', '')
df['drink_society_price'] = df['drink_society_price'].str.replace(r',', '')
df['drink_society_price'] = df['drink_society_price'].astype(float)

df['my_liquor_online_price'] = df['my_liquor_online_price'].str.replace(r'$', '')
df['my_liquor_online_price'] = df['my_liquor_online_price'].str.replace(r',', '')
df['my_liquor_online_price'] = df['my_liquor_online_price'].astype(float)

df['the_whiskycompany_price'] = df['the_whiskycompany_price'].str.replace(r'$', '')
df['the_whiskycompany_price'] = df['the_whiskycompany_price'].str.replace(r',', '')
df['the_whiskycompany_price'] = df['the_whiskycompany_price'].astype(float)

df['devineceller_price'] = df['devineceller_price'].str.replace(r'$', '')
df['devineceller_price'] = df['devineceller_price'].str.replace(r',', '')
df['devineceller_price'] = df['devineceller_price'].astype(float)


df.drop_duplicates(inplace=True)
df.dropna(subset=['Liquorkart_SKU'], inplace=True)


def get_change(current, previous):                                   
    if current == previous:
        0
    try:
        return (abs(current - previous) / previous) * 100.0
    except ZeroDivisionError:
        return 0

for i,row in df.iterrows():
    if row['Boozebud_price'] > row['liquorkart_selling_price']:
        df.loc[i,'Boozebud_actual_difference'] = int(row['Boozebud_price']) - int(row['liquorkart_selling_price'])
        df.loc[i,'Boozebud_status'] = "lower"
    elif row['Boozebud_price'] < row['liquorkart_selling_price']:
        df.loc[i,'Boozebud_actual_difference'] = int(row['liquorkart_selling_price']) - int(row['Boozebud_price'])
        df.loc[i,'Boozebud_status'] = "higher"
    elif row['Boozebud_price'] == row['liquorkart_selling_price']:
        df.loc[i,'Boozebud_actual_difference'] = int(row['liquorkart_selling_price']) - int(row['Boozebud_price'])
        df.loc[i,'Boozebud_status'] = "same"

for i,row in df.iterrows():
    if row['Boozebud_price'] > row['liquorkart_selling_price']:
        df.loc[i,'Boozebud_%_difference'] = get_change(row['Boozebud_price'], row['liquorkart_selling_price'])
    elif row['Boozebud_price'] < row['liquorkart_selling_price']:
        df.loc[i,'Boozebud_%_difference'] = get_change(row['liquorkart_selling_price'], row['Boozebud_price'])
        

#%%%%
for i,row in df.iterrows():
    if row['Hairydog_Price'] > row['liquorkart_selling_price']:
        df.loc[i,'Hairydog_actual_difference'] = int(row['Hairydog_Price']) - int(row['liquorkart_selling_price'])
        df.loc[i,'Hairydog_status'] = "lower"
    elif row['Hairydog_Price'] < row['liquorkart_selling_price']:
        df.loc[i,'Hairydog_actual_difference'] = int(row['liquorkart_selling_price']) - int(row['Hairydog_Price'])
        df.loc[i,'Hairydog_status'] = "higher"
    elif row['Hairydog_Price'] == row['liquorkart_selling_price']:
        df.loc[i,'Hairydog_actual_difference'] = int(row['liquorkart_selling_price']) - int(row['Hairydog_Price'])
        df.loc[i,'Hairydog_status'] = "same"

for i,row in df.iterrows():
    if row['Hairydog_Price'] > row['liquorkart_selling_price']:
        df.loc[i,'Hairydog_%_difference'] = get_change(row['Hairydog_Price'], row['liquorkart_selling_price'])
    elif row['Hairydog_Price'] < row['liquorkart_selling_price']:
        df.loc[i,'Hairydog_%_difference'] = get_change(row['liquorkart_selling_price'], row['Hairydog_Price'])
        
#%%

for i,row in df.iterrows():
    if row['Dan_murphy_price'] > row['liquorkart_selling_price']:
        df.loc[i,'Dan_murphy_actual_difference'] = int(row['Dan_murphy_price']) - int(row['liquorkart_selling_price'])
        df.loc[i,'Dan_murphy_status'] = "lower"
    elif row['Dan_murphy_price'] < row['liquorkart_selling_price']:
        df.loc[i,'Dan_murphy_actual_difference'] = int(row['liquorkart_selling_price']) - int(row['Dan_murphy_price'])
        df.loc[i,'Dan_murphy_status'] = "higher"
    elif row['Dan_murphy_price'] == row['liquorkart_selling_price']:
        df.loc[i,'Dan_murphy_actual_difference'] = int(row['liquorkart_selling_price']) - int(row['Dan_murphy_price'])
        df.loc[i,'Dan_murphy_status'] = "same"

for i,row in df.iterrows():
    if row['Dan_murphy_price'] > row['liquorkart_selling_price']:
        df.loc[i,'Dan_murphy_%_difference'] = get_change(row['Dan_murphy_price'], row['liquorkart_selling_price'])
    elif row['Dan_murphy_price'] < row['liquorkart_selling_price']:
        df.loc[i,'Dan_murphy_%_difference'] = get_change(row['liquorkart_selling_price'], row['Dan_murphy_price'])
    
#%%


for i,row in df.iterrows():
    if row['Liquorland_price'] > row['liquorkart_selling_price']:
        df.loc[i,'Liquorland_actual_difference'] = int(row['Liquorland_price']) - int(row['liquorkart_selling_price'])
        df.loc[i,'Liquorland_status'] = "lower"
    elif row['Liquorland_price'] < row['liquorkart_selling_price']:
        df.loc[i,'Liquorland_actual_difference'] = int(row['liquorkart_selling_price']) - int(row['Liquorland_price'])
        df.loc[i,'Liquorland_status'] = "higher"
    elif row['Liquorland_price'] == row['liquorkart_selling_price']:
        df.loc[i,'Liquorland_actual_difference'] = int(row['liquorkart_selling_price']) - int(row['Liquorland_price'])
        df.loc[i,'Liquorland_status'] = "same"

for i,row in df.iterrows():
    if row['Liquorland_price'] > row['liquorkart_selling_price']:
        df.loc[i,'Liquorland_%_difference'] = get_change(row['Liquorland_price'], row['liquorkart_selling_price'])
    elif row['Liquorland_price'] < row['liquorkart_selling_price']:
        df.loc[i,'Liquorland_%_difference'] = get_change(row['liquorkart_selling_price'], row['Liquorland_price'])
        
        
#%%
for i,row in df.iterrows():
    if row['BWS_Price'] > row['liquorkart_selling_price']:
        df.loc[i,'BWS_actual_difference'] = int(row['BWS_Price']) - int(row['liquorkart_selling_price'])
        df.loc[i,'BWS_status'] = "lower"
    elif row['BWS_Price'] < row['liquorkart_selling_price']:
        df.loc[i,'BWS_actual_difference'] = int(row['liquorkart_selling_price']) - int(row['BWS_Price'])
        df.loc[i,'BWS_status'] = "higher"
    elif row['BWS_Price'] == row['liquorkart_selling_price']:
        df.loc[i,'BWS_actual_difference'] = int(row['liquorkart_selling_price']) - int(row['BWS_Price'])
        df.loc[i,'BWS_status'] = "same"

for i,row in df.iterrows():
    if row['BWS_Price'] > row['liquorkart_selling_price']:
        df.loc[i,'BWS_%_difference'] = get_change(row['BWS_Price'], row['liquorkart_selling_price'])
    elif row['BWS_Price'] < row['liquorkart_selling_price']:
        df.loc[i,'BWS_%_difference'] = get_change(row['liquorkart_selling_price'], row['BWS_Price'])
        
#%%

for i,row in df.iterrows():
    if row['Nicks_price'] > row['liquorkart_selling_price']:
        df.loc[i,'Nicks_actual_difference'] = int(row['Nicks_price']) - int(row['liquorkart_selling_price'])
        df.loc[i,'Nicks_status'] = "lower"
    elif row['Nicks_price'] < row['liquorkart_selling_price']:
        df.loc[i,'Nicks_actual_difference'] = int(row['liquorkart_selling_price']) - int(row['Nicks_price'])
        df.loc[i,'Nicks_status'] = "higher"
    elif row['Nicks_price'] == row['liquorkart_selling_price']:
        df.loc[i,'Nicks_actual_difference'] = int(row['liquorkart_selling_price']) - int(row['Nicks_price'])
        df.loc[i,'Nicks_status'] = "same"

for i,row in df.iterrows():
    if row['Nicks_price'] > row['liquorkart_selling_price']:
        df.loc[i,'Nicks_%_difference'] = get_change(row['Nicks_price'], row['liquorkart_selling_price'])
    elif row['Nicks_price'] < row['liquorkart_selling_price']:
        df.loc[i,'Nicks_%_difference'] = get_change(row['liquorkart_selling_price'], row['Nicks_price'])
        

#%%

for i,row in df.iterrows():
    if row['firstchoiceliquor_price'] > row['liquorkart_selling_price']:
        df.loc[i,'firstchoiceliquor_actual_difference'] = int(row['firstchoiceliquor_price']) - int(row['liquorkart_selling_price'])
        df.loc[i,'firstchoiceliquor_status'] = "lower"
    elif row['firstchoiceliquor_price'] < row['liquorkart_selling_price']:
        df.loc[i,'firstchoiceliquor_difference'] = int(row['liquorkart_selling_price']) - int(row['firstchoiceliquor_price'])
        df.loc[i,'firstchoiceliquor_status'] = "higher"
    elif row['firstchoiceliquor_price'] == row['liquorkart_selling_price']:
        df.loc[i,'firstchoiceliquor_actual_difference'] = int(row['liquorkart_selling_price']) - int(row['firstchoiceliquor_price'])
        df.loc[i,'firstchoiceliquor_status'] = "same"

for i,row in df.iterrows():
    if row['firstchoiceliquor_price'] > row['liquorkart_selling_price']:
        df.loc[i,'firstchoiceliquor_%_difference'] = get_change(row['firstchoiceliquor_price'], row['liquorkart_selling_price'])
    elif row['firstchoiceliquor_price'] < row['liquorkart_selling_price']:
        df.loc[i,'firstchoiceliquor_%_difference'] = get_change(row['liquorkart_selling_price'], row['firstchoiceliquor_price'])

#%%

for i,row in df.iterrows():
    if row['vintageceller_price'] > row['liquorkart_selling_price']:
        df.loc[i,'vintageceller_actual_difference'] = int(row['vintageceller_price']) - int(row['liquorkart_selling_price'])
        df.loc[i,'vintageceller_status'] = "lower"
    elif row['vintageceller_price'] < row['liquorkart_selling_price']:
        df.loc[i,'vintageceller_actual_difference'] = int(row['liquorkart_selling_price']) - int(row['vintageceller_price'])
        df.loc[i,'vintageceller_status'] = "higher"
    elif row['vintageceller_price'] == row['liquorkart_selling_price']:
        df.loc[i,'vintageceller_actual_difference'] = int(row['liquorkart_selling_price']) - int(row['vintageceller_price'])
        df.loc[i,'vintageceller_status'] = "same"

for i,row in df.iterrows():
    if row['vintageceller_price'] > row['liquorkart_selling_price']:
        df.loc[i,'vintageceller_%_difference'] = get_change(row['vintageceller_price'], row['liquorkart_selling_price'])
    elif row['vintageceller_price'] < row['liquorkart_selling_price']:
        df.loc[i,'vintageceller_%_difference'] = get_change(row['liquorkart_selling_price'], row['vintageceller_price'])
        
#%%

for i,row in df.iterrows():
    if row['kent_street_celler_price'] > row['liquorkart_selling_price']:
        df.loc[i,'kent_street_celler_actual_difference'] = int(row['kent_street_celler_price']) - int(row['liquorkart_selling_price'])
        df.loc[i,'kent_street_celler_status'] = "lower"
    elif row['kent_street_celler_price'] < row['liquorkart_selling_price']:
        df.loc[i,'kent_street_celler_actual_difference'] = int(row['liquorkart_selling_price']) - int(row['kent_street_celler_price'])
        df.loc[i,'kent_street_celler_status'] = "higher"
    elif row['kent_street_celler_price'] == row['liquorkart_selling_price']:
        df.loc[i,'kent_street_celler_actual_difference'] = int(row['liquorkart_selling_price']) - int(row['kent_street_celler_price'])
        df.loc[i,'kent_street_celler_status'] = "same"

for i,row in df.iterrows():
    if row['kent_street_celler_price'] > row['liquorkart_selling_price']:
        df.loc[i,'kent_street_celler_%_difference'] = get_change(row['kent_street_celler_price'], row['liquorkart_selling_price'])
    elif row['kent_street_celler_price'] < row['liquorkart_selling_price']:
        df.loc[i,'kent_street_celler_%_difference'] = get_change(row['liquorkart_selling_price'], row['kent_street_celler_price'])
        
#%%

for i,row in df.iterrows():
    if row['paulsliquor_price'] > row['liquorkart_selling_price']:
        df.loc[i,'paulsliquor_actual_difference'] = int(row['paulsliquor_price']) - int(row['liquorkart_selling_price'])
        df.loc[i,'paulsliquor_status'] = "lower"
    elif row['paulsliquor_price'] < row['liquorkart_selling_price']:
        df.loc[i,'paulsliquor_actual_difference'] = int(row['liquorkart_selling_price']) - int(row['paulsliquor_price'])
        df.loc[i,'paulsliquor_status'] = "higher"
    elif row['paulsliquor_price'] == row['liquorkart_selling_price']:
        df.loc[i,'paulsliquor_actual_difference'] = int(row['liquorkart_selling_price']) - int(row['paulsliquor_price'])
        df.loc[i,'paulsliquor_status'] = "same"

for i,row in df.iterrows():
    if row['paulsliquor_price'] > row['liquorkart_selling_price']:
        df.loc[i,'paulsliquor_%_difference'] = get_change(row['paulsliquor_price'], row['liquorkart_selling_price'])
    elif row['paulsliquor_price'] < row['liquorkart_selling_price']:
        df.loc[i,'paulsliquor_%_difference'] = get_change(row['liquorkart_selling_price'], row['paulsliquor_price'])

#%%

for i,row in df.iterrows():
    if row['mr_danks_liquor_price'] > row['liquorkart_selling_price']:
        df.loc[i,'mr_danks_liquor_actual_difference'] = int(row['mr_danks_liquor_price']) - int(row['liquorkart_selling_price'])
        df.loc[i,'mr_danks_liquor_status'] = "lower"
    elif row['mr_danks_liquor_price'] < row['liquorkart_selling_price']:
        df.loc[i,'mr_danks_liquor_actual_difference'] = int(row['liquorkart_selling_price']) - int(row['mr_danks_liquor_price'])
        df.loc[i,'mr_danks_liquor_status'] = "higher"
    elif row['mr_danks_liquor_price'] == row['liquorkart_selling_price']:
        df.loc[i,'mr_danks_liquor_actual_difference'] = int(row['liquorkart_selling_price']) - int(row['mr_danks_liquor_price'])
        df.loc[i,'mr_danks_liquor_status'] = "same"

for i,row in df.iterrows():
    if row['mr_danks_liquor_price'] > row['liquorkart_selling_price']:
        df.loc[i,'mr_danks_liquor_%_difference'] = get_change(row['mr_danks_liquor_price'], row['liquorkart_selling_price'])
    elif row['mr_danks_liquor_price'] < row['liquorkart_selling_price']:
        df.loc[i,'mr_danks_liquor_%_difference'] = get_change(row['liquorkart_selling_price'], row['mr_danks_liquor_price'])

#%%

for i,row in df.iterrows():
    if row['drink_society_price'] > row['liquorkart_selling_price']:
        df.loc[i,'drink_society_actual_difference'] = int(row['drink_society_price']) - int(row['liquorkart_selling_price'])
        df.loc[i,'drink_society_status'] = "lower"
    elif row['drink_society_price'] < row['liquorkart_selling_price']:
        df.loc[i,'drink_society_actual_difference'] = int(row['liquorkart_selling_price']) - int(row['drink_society_price'])
        df.loc[i,'drink_society_status'] = "higher"
    elif row['drink_society_price'] == row['liquorkart_selling_price']:
        df.loc[i,'drink_society_actual_difference'] = int(row['liquorkart_selling_price']) - int(row['drink_society_price'])
        df.loc[i,'drink_society_status'] = "same"

for i,row in df.iterrows():
    if row['drink_society_price'] > row['liquorkart_selling_price']:
        df.loc[i,'drink_society_%_difference'] = get_change(row['drink_society_price'], row['liquorkart_selling_price'])
    elif row['drink_society_price'] < row['liquorkart_selling_price']:
        df.loc[i,'drink_society_%_difference'] = get_change(row['liquorkart_selling_price'], row['drink_society_price'])

#%%

for i,row in df.iterrows():
    if row['my_liquor_online_price'] > row['liquorkart_selling_price']:
        df.loc[i,'my_liquor_online_actual_difference'] = int(row['my_liquor_online_price']) - int(row['liquorkart_selling_price'])
        df.loc[i,'my_liquor_online_status'] = "lower"
    elif row['my_liquor_online_price'] < row['liquorkart_selling_price']:
        df.loc[i,'my_liquor_online_actual_difference'] = int(row['liquorkart_selling_price']) - int(row['my_liquor_online_price'])
        df.loc[i,'my_liquor_online_status'] = "higher"
    elif row['my_liquor_online_price'] == row['liquorkart_selling_price']:
        df.loc[i,'my_liquor_online_actual_difference'] = int(row['liquorkart_selling_price']) - int(row['my_liquor_online_price'])
        df.loc[i,'my_liquor_online_status'] = "same"

for i,row in df.iterrows():
    if row['my_liquor_online_price'] > row['liquorkart_selling_price']:
        df.loc[i,'my_liquor_online_%_difference'] = get_change(row['my_liquor_online_price'], row['liquorkart_selling_price'])
    elif row['my_liquor_online_price'] < row['liquorkart_selling_price']:
        df.loc[i,'my_liquor_online_%_difference'] = get_change(row['liquorkart_selling_price'], row['my_liquor_online_price'])

#%%

for i,row in df.iterrows():
    if row['the_whiskycompany_price'] > row['liquorkart_selling_price']:
        df.loc[i,'the_whiskycompany_actual_difference'] = int(row['the_whiskycompany_price']) - int(row['liquorkart_selling_price'])
        df.loc[i,'the_whiskycompany_status'] = "lower"
    elif row['the_whiskycompany_price'] < row['liquorkart_selling_price']:
        df.loc[i,'the_whiskycompany_actual_difference'] = int(row['liquorkart_selling_price']) - int(row['the_whiskycompany_price'])
        df.loc[i,'the_whiskycompany_status'] = "higher"
    elif row['the_whiskycompany_price'] == row['liquorkart_selling_price']:
        df.loc[i,'the_whiskycompany_actual_difference'] = int(row['liquorkart_selling_price']) - int(row['the_whiskycompany_price'])
        df.loc[i,'the_whiskycompany_status'] = "same"

for i,row in df.iterrows():
    if row['the_whiskycompany_price'] > row['liquorkart_selling_price']:
        df.loc[i,'the_whiskycompany_%_difference'] = get_change(row['the_whiskycompany_price'], row['liquorkart_selling_price'])
    elif row['the_whiskycompany_price'] < row['liquorkart_selling_price']:
        df.loc[i,'the_whiskycompany_%_difference'] = get_change(row['liquorkart_selling_price'], row['the_whiskycompany_price'])
        
#%%

for i,row in df.iterrows():
    if row['devineceller_price'] > row['liquorkart_selling_price']:
        df.loc[i,'devineceller_actual_difference'] = int(row['devineceller_price']) - int(row['liquorkart_selling_price'])
        df.loc[i,'devineceller_status'] = "lower"
    elif row['devineceller_price'] < row['liquorkart_selling_price']:
        df.loc[i,'devineceller_actual_difference'] = int(row['liquorkart_selling_price']) - int(row['devineceller_price'])
        df.loc[i,'devineceller_status'] = "higher"
    elif row['devineceller_price'] == row['liquorkart_selling_price']:
        df.loc[i,'devineceller_actual_difference'] = int(row['liquorkart_selling_price']) - int(row['devineceller_price'])
        df.loc[i,'devineceller_status'] = "same"

for i,row in df.iterrows():
    if row['devineceller_price'] > row['liquorkart_selling_price']:
        df.loc[i,'devineceller_%_difference'] = get_change(row['devineceller_price'], row['liquorkart_selling_price'])
    elif row['devineceller_price'] < row['liquorkart_selling_price']:
        df.loc[i,'the_whiskycompany_%_difference'] = get_change(row['liquorkart_selling_price'], row['devineceller_price'])

#%%



df['freight'] = 9
df['liquorkart_cost_price'] = df['liquorkart_cost_price'].apply(lambda x: float(x))
df['liquorkart_margin']=(df['liquorkart_selling_price'] -df['liquorkart_cost_price']) + 9
df.to_csv(f"Price_comparison-{d4}.csv",encoding='utf-8-sig')
print('File Created')

# =============================================================================
# df = df[['Liquorkart_Product_Name', 'Liquorkart_SKU', 'liquorkart_selling_price',
#        'liquorkart_margin','Hairydog_Price', 'Boozebud_price', 'Dan_murphy_price',
#        'Liquorland_price', 'BWS_Price', 'Nicks_price', 'liquorkart_cost_price',
#        'Variant Inventory Qty', 'Boozebud_actual_difference',
#        'Boozebud_status', 'Boozebud_%_difference',
#        'Hairydog_actual_difference', 'Hairydog_status',
#        'Hairydog_%_difference', 'Dan_murphy_actual_difference',
#        'Dan_murphy_status', 'Dan_murphy_%_difference',
#        'Liquorland_actual_difference', 'Liquorland_status',
#        'Liquorland_%_difference', 'BWS_actual_difference', 'BWS_status',
#        'BWS_%_difference', 'Nicks_actual_difference', 'Nicks_status',
#        'Nicks_%_difference', 'freight']]
# 
# df.columns = ['liquorkart_product_name', 'liquorkart_sku', 'liquorkart_selling_price',
#        'liquorkart_margin', 'hairydog_price', 'boozebud_price',
#        'dan_murphy_price', 'liquorland_price', 'bws_Price', 'nicks_Price',
#        'liquorkart_cost_price', 'variant_inventory_qty',
#        'boozebud_actual_difference', 'boozebud_status',
#        'boozebud_percent_difference', 'hairydog_actual_difference',
#        'hairydog_status', 'hairydog_percent_difference',
#        'dan_murphy_actual_difference', 'dan_murphy_status',
#        'dan_murphy_percent_difference', 'liquorland_actual_difference',
#        'liquorland_status', 'liquorland_percent_difference',
#        'bws_actual_difference', 'bws_status', 'bws_percent_difference',
#        'nicks_actual_difference', 'nicks_status', 'nicks_percent_difference',
#        'freight']
# 
# url='https://staging.liquorkart.com.au/marketplace/csv/index'
# 
# params = {
#     "auth_token": "b7ead240-2b11-483e-b872-4941ec3d2133",
# 
# }
# df_out = df.to_csv()
# 
# files = {
#     "csv_file": (
#         "test.csv",
#         df_out,
#         "text/csv",
#         {"Expires": "0"},
#     )
# }
# 
# print('Pushing to data base .... please wait')
# import requests
# r = requests.post(url, files=files,params=params)
# print('Database Updated')
# 
# =============================================================================
        

