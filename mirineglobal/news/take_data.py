from flask import Flask,render_template,request
import pandas as pd

app = Flask(__name__)

@app.route('/search')
def index():
    return render_template('web.html')
@app.route('/search', methods=['POST'])
def search():
    dt = pd.read_csv("28-new2.csv",encoding= 'UTF-8')
    dt.to_html("csv.html", encoding= 'UTF-8')
    return render_template('csv.html')
if __name__ == '__main__':
    app.run()


