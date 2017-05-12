from flask import Flask #imports Flask
app = Flask(__name__) #imports Flask app with name we specify

@app.route('/')
def home(): #defining the home function
	return "Raiders Website" #when if works will return this
#this is where we will build other pages later on
if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0', port=8080)	
#if the name ==main, run the app, host = 0.0.0.0 through port 8080