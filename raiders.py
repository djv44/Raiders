from flask import Flask, render_template #imports Flask and template
app = Flask(__name__) #imports Flask app with name we specify


@app.route('/')
def home(): #defining the home function
	return render_template('index.html') #when if works will return this

#def home(): #defining the home function
#def hello_world():
	#return "Raiders Website" #when if works will return this

#this is where we will build other pages later on

@app.route('/main')
def main():#defines main
	return render_template('main.html') #calls main template

@app.route('/my-topic')
def page(): #defines page
	return render_template('topic.html')


if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0', port=8080)	
#if the name ==main, run the app, host = 0.0.0.0 through port 8080