from flask import Flask, render_template, request,redirect
#from flask_login import LoginManager
from newscan import new
from history import retrieve

app=Flask(__name__,static_url_path='',static_folder='web/static',template_folder='web/templates')
#login=LoginManager(app)

@app.route('/')
def index():
    return redirect("/history.html",code=302)

@app.route('/newscan.html',methods=['GET','POST'])
def newscan():
    return render_template('newscan.html')

@app.route('/history.html')
def history():
    rows=retrieve()
    return render_template('history.html',rows=rows)

@app.route('/start',methods=['POST'])
def startScan():
    #if (len(request.form)<3):
    #    return("Please select at least one module")
    params=request.data.decode('utf-8')
    return(new(params))

@app.route('/getInfo',methods=['GET'])
def getInfo():
    try:
        uuid=request.args['id']
    except:
        return("please supply an id")
    data=request.args.get('data')
    if data==None:
        resultList=retrieve(uuid,data)
        head=resultList[0]
        result=resultList[1]
        return render_template('results.html',result=result,head=head)
    else:
        return(retrieve(uuid,data))

@app.route('/test')
def test():
    rows={'name':'lol','surname':'loli'}
    return render_template("test.html",rows=rows)

if __name__ == "__main__":
    app.run()