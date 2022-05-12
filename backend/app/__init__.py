from datetime import timedelta
from flask import Flask, jsonify, render_template, request,redirect,g,session,url_for
from app.newscan import new
from app.history import retrieve
import json
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity,unset_jwt_cookies, jwt_required, JWTManager
from flask_cors import CORS,cross_origin
import uuid
from app.db import database

def flask_app():
#app=Flask(__name__,static_url_path='',static_folder='web/static',template_folder='web/templates')
    app=Flask(__name__)
    #app.secret_key="somethingcomplex"
    CORS(app=app,supports_credentials=True)
    app.config["JWT_SECRET_KEY"]=str(uuid.uuid1())
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
    db=database()
    jwt=JWTManager(app)
    app.env="development"
    app.debug=True

    credentials=[x['credentials'] for x in db.get_creds() if x.get('credentials',None)!=None][0]
    '''with open("app/keys.json") as creds:
        credentials=json.load(creds)['credentials']
'''
    users=credentials.keys()

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

    @app.route('/logout',methods=['GET'])
    @jwt_required()
    def logout():
        response = jsonify({"msg": "logout successful"})
        unset_jwt_cookies(response)
        return response,200

    @app.route('/')
    def index():
        #return redirect(url_for('login'))
        return jsonify({"msg":"API works!"})

    @app.route('/start',methods=['POST'])
    @jwt_required()
    def startScan():
        """
        {
            "name":<name of scan>,
            "target":<target domain>,
            "modules":['portScanModule','sslModule','emailModule','subDomainModule','allPortScanModule','PublicIPsModule','gitHubModule']
        }
        """
        params=request.json
        new(params,db)
        return jsonify({"msg":"Scan Complete!"})

    @app.route('/getScanInfo',methods=['GET'],endpoint='info')
    @jwt_required()
    def info():
        """
        {
            "id":<Scan ID> (Optional),
            "data":<module name> (Optional)
        }
        """
        id=request.args.get('id',None)
        data=request.args.get('data',None)
        past_scan=retrieve(uuid=id,data=data)
        return jsonify(past_scan)
    return app


#if __name__ == "__main__":
#    app.run(host="0.0.0.0")