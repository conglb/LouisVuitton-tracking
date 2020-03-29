import requests, json, time
import os
import smtplib, ssl


port = 25  # 25 110 # For SSL
smtp_server = "mail.toshiba-tsdv.com"
sender_email = "cong.leba@toshiba-tsdv.com"  # Enter your address
receiver_email = "congmb@gmail.com"  # Enter receiver address
#password = input("Type your password and press enter: ")
message = """\
Subject: Hi there

Hi there Nguyen Vu Nam. You have a new product which has now on stock at LV.

It's code is 
"""

#context = ssl.create_default_context()
#context = ssl.SSLContext(ssl.PROTOCOL_TLS)




product_ids = []
f = open("product_ids.txt", "r")
for product_id in f:
    product_ids.append(product_id.rstrip())
print(product_ids)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',}

while True:
    print("while loop")
    for product_id in product_ids:
        print(product_id)
        try:
            response = requests.get("https://secure.louisvuitton.com/ajaxsecure/getStockLevel.jsp?storeLang=fra-fr&pageType=storelocator_section&skuIdList={}&null&_=1583480351074".format(str(product_id)), headers=headers)
            print(response.text.strip())
            json_data = json.loads(response.text)
            if json_data[product_id]["inStock"] == True:
                print("IN STOCK !!")
                # Send an email here
                with smtplib.SMTP(smtp_server, port) as server:
                    server.ehlo()
                    server.sendmail(sender_email, receiver_email, message + product_id)  
                product_ids.remove(product_id)
        except Exception as e:
            print(e.message)
    time.sleep(7)




