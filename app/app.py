from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    # fetch the data from the database
    # read them
    # dispaly to table

	return "Hello World!"

if __name__ == '__main__':
	app.run(port=8080)