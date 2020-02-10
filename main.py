sfrom flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
  return "Hi!"

@app.route('/home', aktiva_lapa = 'home')
def home():
  return"<h1><a href='/about'>my home</a></h1>"

@app.route('/about', aktiva_lapa = 'about')
def about():
  return render_template('about.html')

@app.route('/contact', aktiva_lapa = 'contact')
def contact():
  return render_template('contact.html',Phone=29647470)

@app.route('/params')
def params():
  args= request.args
  for key, value in args.items():
    print(f"{key}:{value}")
  return args

@app.route('/params_table')
def params_table():
  args= request.args

  return render_template('params_table.html', args = args)

if __name__ =='__main__':
  app.run(host="0.0.0.0",port=5232, threaded = True , debug = True) 

