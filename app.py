from flask import Flask

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return "This is a just a practise session for docker"

if __name__=="__main__":
    app.run(debug=True)

    