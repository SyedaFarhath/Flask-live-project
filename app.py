from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# if __name__ == "__main__":
#     app.run(debug=False,port="8001")

# if __name__ == "__main__":
    # app.run(debug=False,host="172.18.210.163")
    
if __name__ == "__main__":
    app.run(debug=False,host="172.18.210.163")
    

    