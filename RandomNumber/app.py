from flask import Flask,request,render_template
import random
app=Flask(__name__)

@app.route('/')
def base():
  return render_template('index.html')
@app.route('/random',methods=['POST'])
def rans():
  a=int(request.form['a'])
  b=int(request.form['b'])
  num=random.randint(a,b)
  return render_template('index.html',result=num)

if __name__ =="__main__":
  app.run(debug=True)