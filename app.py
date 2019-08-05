from flask import Flask, redirect, url_for, request, render_template, session
import os


from test_login import test_login
from AutoLink import auto_connector, auto_applyer


port = int(os.environ.get("PORT", 5000))

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

try:
	session.pop('i')
	session.pop('j')
	session.pop('auto_connect_called')
	session.pop('auto_apply_called')
except:
	pass
	
	
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login/', methods=["GET", "POST"])
def login():

	if request.method == "POST":
	
		if test_login(request.form["mail"],request.form["password"]) == True :
		
			session['mail'] = request.form["mail"]
			session['password']= request.form["password"]
			return render_template('home.html')
		else:
			return render_template('try_again.html')
			
	return render_template('login.html')
	
@app.route('/home/')
def home():
	if session['mail'] != None:
		return render_template('home.html')
	return redirect(url_for('login'))	

@app.route('/auto_apply/', methods=["GET", "POST"])
def apply():
	if session['mail'] != None:
		if request.method == "POST":
			session['job'] = request.form['job']
			session['location'] = request.form['location']
			return redirect(url_for('process', fun='auto_apply'))
			
		return render_template('auto_apply.html')
	return redirect(url_for('login'))	

@app.route('/auto_connect/', methods=["GET", "POST"])
def connect():
	if session['mail'] != None:
		if request.method == "POST":
			session['job'] = request.form['job']
			
			return redirect(url_for('process', fun='auto_connect'))
		return render_template('auto_connect.html')
	return redirect(url_for('login'))	

@app.route("/process/<fun>", methods=['GET', 'POST'])
def process(fun, *args):
	
	if fun == 'auto_connect' or fun == 'auto_apply':
		if request.method == 'GET':
			return render_template('wait.html', fun=fun)
			
		if request.method == 'POST':

			if fun == 'auto_connect':
				
				session['i'] = auto_connector(session['mail'], session['password'], session['job'])
				session['auto_connector_called'] = auto_connector.has_been_called
				try:
					if session['i'] > 0 :
				
						return redirect(url_for('success/auto_connect'))
				except:
					return redirect(url_for('error'))
					
			elif fun == 'auto_apply':
				session['j'] = auto_applyer(session['mail'], session['password'], session['job'], session['location'])
				session['auto_applyer_called'] = auto_applyer.has_been_called
				try:
					if session['j'] > 0 :
				
						return redirect(url_for('success/auto_apply'))
				except:
					return redirect(url_for('error'))
			else:
				return redirect(url_for('error'))
	return redirect(url_for('error'))		
        

@app.route('/success/<fun>')
def success(fun):
	if session['mail'] != None:
		print(fun)
		print(auto_connector.has_been_called)
		if fun == 'auto_apply' or fun == 'auto_connect':
			try:
			
				if session['auto_applyer_called'] and session['j'] > 0 :
					return render_template('success.html', fun=fun, j=session['j'])
			except:
				try:
					if session['auto_connector_called'] and session['i'] > 0:
						return render_template('success.html', fun=fun, i=session['i'])
				except:
					try:
						session.pop('i')
						
					except:
						try:
							session.pop('j')
						except:
							pass	
					return redirect(url_for('error'))
		return redirect(url_for('error'))	
	return redirect(url_for('login'))				

@app.route('/error/')
def error():
	if session['mail'] != None:
		return render_template('error.html', code = 'UNKNOWN')
	return redirect(url_for('login'))
	
@app.errorhandler(404)
def page_not_found(e):
	if session['mail'] != None:
   		return render_template('error.html', code="404"), 404	
	return redirect(url_for('login'))
	
	
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=port, debug=True)
