from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session, jsonify
from stockx import file1

app = Flask(__name__)

@app.route('/')
def index():
  return redirect('/home/')

@app.route('/home/')
def homeHome():
  return render_template('index.html')

@app.route('/test1/', methods=['GET', 'POST'])
def stocksHome():
  sneakersApi = file1.main('BB1234')
  kwargs = {
   'title':'Stock page',
   'heading':'Stock page',
   'apiCall': sneakersApi
  }
  return render_template('test1.html', **kwargs)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80, debug=True)

