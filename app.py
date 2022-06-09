from flask import Flask,redirect,render_template,url_for
from sqlalchemy import true


app = Flask(__name__)


@app.route('/')
def home():
        return render_template('index.html')
        
@app.route('/login')
def login():
        return render_template('login.html', sese=login)


@app.route('/register')
def register():
        return render_template('register.html')
    
@app.route('/cours')
def cours():
        return render_template('courses.html')

@app.route('/about')
def about():
        return render_template('about.html')
  
@app.route('/contact')
def contact():
        return render_template('contact.html')
  
if __name__ =='__main__':
    app.run(debug=true)
