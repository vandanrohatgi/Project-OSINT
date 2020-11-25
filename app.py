from flask import Flask, render_template, request
from newscan import new
import time

app=Flask(__name__,static_url_path='',static_folder='web/static',template_folder='web/templates')

@app.route('/')
def index():
    return render_template('history.html')

@app.route('/newscan.html',methods=['GET','POST'])
def newscan():
    return render_template('newscan.html')

@app.route('/history.html')
def history():
    return render_template('history.html')

@app.route('/start',methods=['POST'])
def startScan():
    #if (len(request.form)<3):
    #    return("Please select at least one module")
    params=request.data.decode('utf-8')
    return(new(params))
    
if __name__ == "__main__":
    app.run()