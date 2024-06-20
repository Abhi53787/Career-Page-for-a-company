from flask import Flask, render_template,jsonify 
# From module called flask we are just importing thr Flask class 
app= Flask(__name__)
JOBS =[
  {
  'id':1,
  'title': 'Data Analyst',
  'location': 'Bengaluru, India',
  'Salary': 'Negotiable '
    
  
},
  {'id': 2,
  'title' : 'SDE I',
  'location': 'Chennai , India',
  'salary':'Negotiable'},
   {'id': 3,
    'title' : 'SDE II',
    'location': 'Chennai , India',
    'salary':'Negotiable'},
   {'id': 4,
    'title' : 'QA Analyst ',
    'location': 'Hyderabad , India',
    'salary':'Negotiable'}

]
@app.route("/") # / represents  like home page
def hello_world():
  return render_template('home.html',jobs=JOBS,
                        company_name='Aeroaegis')
#Creating api route
@app.route("/api /jobs")
def list_jobs():
  return jsonify(JOBS)
  
if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)