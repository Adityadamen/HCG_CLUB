from flask import Flask,render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict3',methods=['POST'])
def predict3():

   return render_template('index.html')


if __name__ == '__main__':
    app.run()
