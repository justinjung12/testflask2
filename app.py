from flask import Flask, request, redirect,jsonify,render_template
from datetime import datetime
from flask_cors import CORS
import json
import random
alerts = []
currentalerts = ''

app = Flask(__name__)
CORS(app)
def current_date_yyyymmdd():
    # 현재 날짜를 가져옴
    current_date = datetime.now()
    # 'yyyymmdd' 형태로 포맷팅하여 문자열로 변환
    formatted_date = current_date.strftime('%Y%m%d')
    return str(formatted_date)

def reseat():
    name_list = ["강규리","곽예신","김은별","김은서","남시연","박지우","성유빈","양정현","오승희","오하은","윤지민","이루미","정소윤","조규림","홍채연","홍희주","경윤서","김도윤","김동아","김준민","박도영","박정민","변규민","신현웅","심규민","김종혁","윤찬우","이화륜","정우진","임동혁","조단휘","표창민","하랑"]
    global result
    result = []
    seat_result_list = []
    for i in range(0,random.randint(0,10)):
        random.shuffle(name_list)
    for i in range(16):
        partner1 = name_list[random.randint(0,len(name_list)-1)]
        name_list.remove(partner1)
        
        partner2 = name_list[random.randint(0,len(name_list)-1)]
        name_list.remove(partner2)

        seat_result_list.append([partner1,partner2])
    result =  jsonify(seat_result_list)
    return seat_result_list


@app.route('/')
def main():
    print(currentalerts)
    return render_template('schoolapp.html',alert= alerts, currentalert = currentalerts)
@app.route('/writealert',methods=['GET', 'POST'])
def writealert():
    global currentalerts
    if request.method == 'GET':
        return render_template('writealert.html')
    if request.method == 'POST':
        result = {}
        if request.form['pw'] == '123':
            result['text'] = request.form['text']
            result['date'] = current_date_yyyymmdd()
            alerts.append(result)
            currentalerts = result['text']
            return render_template('writealert.html')
@app.route('/seats/',methods=['GET', 'POST'])
def seat():
    if request.form['use'] == 'reseat':
        reseat_result = reseat()
        return reseat_result
    elif request.form['use'] == 'show':
        reseat()
        return result

app.run()