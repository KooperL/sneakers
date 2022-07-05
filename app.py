from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session, jsonify
import scripts.stockx.file1 
import scripts.stockx.file2 

app = Flask(__name__)

@app.route('/')
def index():
  return redirect('/home')


@app.route('/home')
def homeHome():
  sneakersApi = scripts.stockx.file2.main()
  return render_template('index.html', productsArray=sneakersApi)


@app.route('/test', methods=['GET'])
def stocksHome():
  product_id = request.args.get('pid')
  print(product_id)
  sneakersApi = scripts.stockx.file1.main(product_id)
  kwargs = {
   'title': f'{sneakersApi["name"]} preview',
   'heading': sneakersApi['name'],
   'pid': product_id,
   'apiCall': sneakersApi
  }
  return render_template('testFile.html', **kwargs)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80, debug=True)

