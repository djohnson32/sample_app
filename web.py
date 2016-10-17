from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	#name - requests.value.get('name', 'nobody')
	##return "Hey world!!"
	return render_template('index.html')

app.run(debug = True)