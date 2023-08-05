from flask import Flask

app = Flask(__name__)
print()


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def emphasis(function):
    def wrapper():
        return f"<em>{function()}"
    return wrapper
@app.route("/")
def hello_world():
    return '<h1 style="text-aline: center">Hello, World</h1>' \
           '<p>this is a paragraph</p>' \
           '<img src="https://giphy.com/gifs/funny-cat-mlvseq9yvZhba" width=200>'



@app.route("/bye")
@make_bold
@emphasis
def bye():
    return "Bye"


# to extract variables <name>
@app.route("/username/<name>/<int:number>")
def username(name, number):
    return f"Hello there {name} you are{number} years old"


# if __name__ == "__main__":
#     app.run(debug=True)
