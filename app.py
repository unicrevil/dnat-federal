from flask import Flask, render_template, jsonify
import requests
app=Flask(__name__)
@app.route('/')
def index(): return render_template('index.html')
@app.route('/api/geo/<ip>')
def geo(ip):
    try:
        r=requests.get(f'http://ip-api.com/json/{ip}', timeout=5).json()
        return jsonify(r)
    except: return jsonify({"city":"Caxias","lat":-29.1681,"lon":-51.1792})
if __name__=='__main__': app.run(host='0.0.0.0',port=5000,debug=True)
