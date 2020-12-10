from flask import Flask, render_template, request,redirect,g,session,url_for
from newscan import new
from history import retrieve
from db import initialize

initialize()
app=Flask(__name__,static_url_path='',static_folder='web/static',template_folder='web/templates')
app.secret_key="somethingcomplex"


class User:
    def __init__(self, uuid, username, password):
        self.id = uuid
        self.username = username
        self.password = password

users = []
users.append(User(uuid=1, username='test', password='test'))
#users.append(User(uuid=2, username='Becca', password='secret'))
#users.append(User(uuid=3, username='Carlos', password='somethingsimple'))

@app.before_request
def before_request():
    g.user=None
    if 'user_id' in session:
        user=[x for x in users if x.id == session['user_id']][0]
        g.user=user

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form.get('username')
        password = request.form.get('password')
        
        user=None
        for x in users:
            if x.username==username:
                user=x
                break

        #user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('history'))
        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id',None)
    return redirect(url_for('login'))

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/newscan')
def newscan():
    if not g.user:
        return redirect(url_for('login'))
    return render_template('newscan.html')

@app.route('/history')
def history():
    if not g.user:
        return redirect(url_for('login'))
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