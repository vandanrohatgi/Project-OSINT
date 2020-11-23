from flask import Flask, render_template, request
from newscan import start

app=Flask(__name__,static_url_path='',static_folder='web/static',template_folder='web/templates')

@app.route('/')
def index():
    return render_template('history.html')

@app.route('/newscan.html')
def newscan():
    return render_template('newscan.html')

@app.route('/history.html')
def history():
    return render_template('history.html')

@app.route('/start',methods=['POST'])
def startScan():
    return (start(request.form))

if __name__ == "__main__":
    app.run()