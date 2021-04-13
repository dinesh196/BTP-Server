from flask import Flask
from flask import request, escape

app = Flask(__name__)


@app.route("/")
def index():
    data = request.args.get("data", "")
    if data:
        result = check_func(data)
    else:
        result = ""
    return """ 
    <form action="" method="get">
        <input type="text" name="data" >
        <input type="submit" value="Give Value" >
    </form>"""
    +"Data value: "
    +result


@app.route("/<int:data>")
def check_func(data):
    try:
        return data
    except expression as identifier:
        return "invalid input"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
