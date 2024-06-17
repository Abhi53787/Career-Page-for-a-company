from flask import Flask 
# From module called flask we are just importing thr Flask class 
app= Flask(__name__)
@app.route("/") # / represents  like home page
def hello_world():
  return "Hello World!"
  print(__name__)
if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)