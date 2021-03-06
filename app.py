from flask import Flask, render_template, request
import requests
import time, threading

app = Flask(__name__)

product_ids = []
def thread_func():
    while True:
        for product_id in product_ids:
            response = requests.get("https://secure.louisvuitton.com/ajaxsecure/getStockLevel.jsp?storeLang=fra-fr&pageType=storelocator_section&skuIdList={}&null&_=1583480351074".format(str(product_id)), headers=headers)
            #app.logger.error("ERRORRRRRRRRRRRRRRRRRRRRRRR")
            #app.logger.warning("WARNINGGGGGGGGGGGGGGGGGGGGGGGG")
            #app.logger.info("INFOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
            print(response)
        time.sleep(7)

main_thread = threading.Thread(target=thread_func)
main_thread.start()
main_thread.join()

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',}

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/test')
def test():
    return 'Hello from Flask!'

@app.route('/lv-tracking', methods=['GET','POST'])
def lv_tracking_get():
    if request.method == 'GET':
        return render_template('lv-tracking.html')
    else:
        product_id = request.form["myId"]
        product_ids.append(product_id)
        return render_template('lv-tracking.html')




