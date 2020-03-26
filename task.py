import requests, json, time
import os
import smtplib, ssl
import api


port = 25  # 25 110 # For SSL
smtp_server = "mail.toshiba-tsdv.com"
sender_email = "cong.leba@toshiba-tsdv.com"  # Enter your address
receiver_email = "cong.leba@toshiba-tsdv.com"  # Enter receiver address
#password = input("Type your password and press enter: ")
message = """\
Subject: Hi there

Hi there Nguyen Vu Nam. You have a new product which has now on stock at LV.

It's code is 
"""

#context = ssl.create_default_context()
#context = ssl.SSLContext(ssl.PROTOCOL_TLS)
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()
    #server.starttls()
    #server.login(sender_email,)
    server.sendmail(sender_email, receiver_email, message)



product_ids = []
f = open("product_ids.txt", "r")
for product_id in f:
    product_ids.append(product_id.rstrip())
print(product_ids)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',}

lv = api.LouisVuittonAPI("EU", False)
while True:
    print("while loop")
    for product_id in product_ids:
        print(product_id)
        api.LouisVuittonAPI.get_stock_status
        if lv.get_stock_status(product_id):
            print("inStock = true")
            # Send an email here
            product_ids.remove(product_id)
        """
        try:
            response = requests.get("https://secure.louisvuitton.com/ajaxsecure/getStockLevel.jsp?storeLang=fra-fr&pageType=storelocator_section&skuIdList={}&null&_=1583480351074".format(str(product_id)), headers=headers)
            print(response.text)
            json_data = json.loads(response.text)
            if json_data[product_id]["inStock"] == True:
                print("inStock = true")
                # Send an email here
                product_ids.remove(product_id)
        except Exception as e:
            print(e.message)
        """
    time.sleep(7)




