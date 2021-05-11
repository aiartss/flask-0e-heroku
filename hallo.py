from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    app.run(ssl_context=('cert.pem','key.pem')) 
    return render_template('index.html')
