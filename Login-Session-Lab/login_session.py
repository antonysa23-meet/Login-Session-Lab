from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fwmdvsuiuieasfhewioenf3uil'

@app.route('/', methods = ['GET', 'POST']) # What methods are needed?
def home():

	if request.method == 'POST':
		try:
			if 'qoute' not in login_session:
				login_session['qoute'] = [request.form['qoute']]
			else:
				print(login_session['qoute'])
				x = login_session['qoute']
				x.append(request.form['qoute'])
				login_session['qoute'] = x
				print(login_session['qoute'])


			if 'age' not in login_session:
				login_session['age'] = [request.form['age']]
			else:
				print(login_session['age'])
				x = login_session['age']
				x.append(request.form['age'])
				login_session['age'] = x
				print(login_session['age'])


			if 'name' not in login_session:
				login_session['name'] = [request.form['name']]
			else:
				print(login_session['name'])
				x = login_session['name']
				x.append(request.form['name'])
				login_session['name'] = x
				print(login_session['name'])
			return redirect(url_for('thanks'))
		except:
				return render_template('error.html')
	else:
		return render_template('home.html')


@app.route('/error')
def error():

	return render_template('error.html')


@app.route('/display')
def display():

	return render_template('display.html', qoute = login_session['qoute'], name = login_session['name'], age = login_session['age']) # What variables are needed?


@app.route('/thanks')
def thanks():

	return render_template('thanks.html')


if __name__ == '__main__':
	app.run(debug=True)