from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('form.html')


@app.route('/', methods=['GET', 'POST'])
def submisssion():
    if request.method == 'POST':
        form_data=request.form
        return render_template('data.html',form_data=form_data)

   
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5009)
