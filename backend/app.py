from datetime import timedelta
from flask import Flask, jsonify, render_template, request,redirect,g,session,url_for
from newscan import new
from history import retrieve
import json
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity,unset_jwt_cookies, jwt_required, JWTManager



app=Flask(__name__,static_url_path='',static_folder='web/static',template_folder='web/templates')
#app=Flask(__name__)
#app.secret_key="somethingcomplex"
app.config["JWT_SECRET_KEY"]="change_this_later"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
jwt=JWTManager(app)
app.env="development"
app.debug=True


with open("keys.json") as creds:
    credentials=json.load(creds)['credentials']

users=credentials.keys()

@app.before_request
def before_request():
    g.user=None
    if 'user' in session:
        g.user=session['user']


'''#@app.route('/login', methods=['GET', 'POST'])
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        session.pop('user', None)

        username = request.form.get('username')
        password = request.form.get('password')
        
        user=None
        for x in users:
            if x==username:
                user=x
                break

        if user and credentials[user] == password:
            session['user'] = user
            #return redirect(url_for('history'))
            return redirect('/history',code=302)
        #return redirect(url_for('login'))
        return redirect('/login',code=302)
    #return render_template('login.html')
'''

@app.route('/login',methods=['POST'])
def login():
    username=request.json.get('username',None)
    password=request.json.get('password',None)
    for user in users:
        if user==username:
            if credentials[user]==password:
                access_token = create_access_token(identity=username)
                response = {"access_token":access_token}
                return response,200
        return 'unauthorized',401
'''
@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect(url_for('login'))
'''

@app.route('/logout',methods=['POST'])
@jwt_required()
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response,200

@app.route('/')
def index():
    #return redirect(url_for('login'))
    return jsonify({"msg":"API works!"})

'''@app.route('/newscan')
@jwt_required()
def newscan():
    if not g.user:
        return redirect(url_for('login'))
    return render_template('newscan.html')'''


'''@app.route('/history')
@jwt_required()
def history():
    #if not g.user:
    #    return redirect(url_for('login'))
    rows=retrieve()
    #print(type(rows))
    #print(rows)
    return jsonify(rows)
    #return render_template('history.html',rows=rows)
'''

@app.route('/start',methods=['POST'])
@jwt_required
def startScan():
    #if (len(request.form)<3):
    #    return("Please select at least one module")
    #params=request.data.decode('utf-8')
    params=request.json
    return(new(params))

@app.route('/getScanInfo',methods=['GET'],endpoint='info')
@jwt_required
def info():
    id=request.args.get('id',None)
    data=request.args.get('data',None)
    past_scan=retrieve(uuid=id,data=data)
    return jsonify(past_scan)
    '''try:
        uuid=request.args['id']
    except:
        return("please supply an id")'''
    '''if data==None:
        resultList=retrieve(uuid,data)
        head=resultList[0]
        result=resultList[1]
        return render_template('results.html',result=result,head=head)
    else:
        return(retrieve(uuid,data))'''


if __name__ == "__main__":
    app.run()