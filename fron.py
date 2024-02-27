from flask import Flask




app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to Major Project CST A_15"



if __name__=='__main__':
    app.run(debug=True)