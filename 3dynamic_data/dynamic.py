from flask import Flask

app = Flask(__name__)

@app.route('/allow/<int:Number>')
def allow(Number):
    if Number<25:
        return f'you have been allowd to enter'
    else:
        return f'you are not allowed'
@app.route('/disallow')
def disallow():
    return 'you have not been allowd to enter'

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5005)