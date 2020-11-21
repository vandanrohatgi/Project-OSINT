from flask import Flask, render_template

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

if __name__ == "__main__":
    app.run()