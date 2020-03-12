import requests, json, time
import sendgrid
import os
from sendgrid.helpers.mail import Mail

product_ids = []
f = open("product_ids.txt", "r")
for product_id in f:
    product_ids.append(product_id.rstrip())
print(product_ids)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',}

while True:
    for product_id in product_ids:
        print(product_id)
        response = requests.get("https://secure.louisvuitton.com/ajaxsecure/getStockLevel.jsp?storeLang=fra-fr&pageType=storelocator_section&skuIdList={}&null&_=1583480351074".format(str(product_id)), headers=headers)
        print(response.text)
        json_data = json.loads(response.text)
        if json_data[product_id]["inStock"] == True:
            message = Mail(
                from_email='lv-tracking',
                to_emails='congmb@gmail.com',
                subject='Alarm!!!!! Louis Vuitton has a new product',
                html_content='<strong>{} is now available \n Search for it on Google and purchase it now!</strong>'.format(product_id))
            try:
                sg = sendgrid.SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
                response = sg.send(message)
                print(response.status_code)
                print(response.body)
                print(response.headers)
            except Exception as e:
                print(e.message)
            product_ids.remove(product_id)
    time.sleep(7)




