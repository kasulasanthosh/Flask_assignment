from flask import Flask,request,jsonify,render_template
app=Flask(__name__)

@app.route("/")
def hello(): 
    message = "Hello, World"
    return render_template('index.html',message=message) 
@app.route("/image") 
def serve_image(): 
    message = "Image Route"
    return render_template('image.html', message=message)


if __name__=="__main__":
    app.run(host="0.0.0.0",port=8008)