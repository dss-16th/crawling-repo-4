from flask import *
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://public_ip:port_num')
db = client.keyword

    
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/vaccine")
def kword1():
    results_vac = db.kword_vaccine.find().sort("date", -1)
    results_list=list(results_vac)
    datas_vac = []
    result_vac = {}
    for data_vac in results_list:
        datas_vac.append({
             'date': data_vac['date'],     
             'title': data_vac['title'],
             'link': data_vac['link'],
         })    
        print(datas_vac)
    
    result_vac['datas_vac'] = datas_vac
    
    return jsonify(result_vac)

@app.route("/soc_distance")
def kword2():
    results_soc = db.kword_soc_distance.find().sort("date", -1)
    results_list=list(results_soc)
    datas_soc = []
    result_soc = {}
    for data_soc in results_list:
        datas_soc.append({
             'date': data_soc['date'],      
             'title': data_soc['title'],
             'link': data_soc['link'],
         })    
        print(datas_soc)
    
    result_soc['datas_soc'] = datas_soc
    
    return jsonify(result_soc)

@app.route("/infection")
def kword3():
    results_inf = db.kword_infection.find().sort("date", -1)
    results_list=list(results_inf)
    datas_inf = []
    result_inf = {}
    for data_inf in results_list:
        datas_inf.append({
             'date': data_inf['date'],      
             'title': data_inf['title'],
             'link': data_inf['link'],
         })    
        print(datas_inf)
    
    result_inf['datas_inf'] = datas_inf
    
    return jsonify(result_inf)

@app.route("/support")
def kword4():
    results_sup = db.kword_support.find().sort("date", -1)
    results_list=list(results_sup)
    datas_sup = []
    result_sup = {}
    for data_sup in results_list:
        datas_sup.append({
             'date': data_sup['date'],      
             'title': data_sup['title'],
             'link': data_sup['link'],
         })    
        print(datas_sup)
    
    result_sup['datas_sup'] = datas_sup
    
    return jsonify(result_sup)

app.run(debug=True)
