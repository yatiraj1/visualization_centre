from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

""" 
@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name) """

@app.route('/<int:name>')
def linear_equation_with_fixed_coefficients(name):
    return "lm {}!".format(name*20 + 5)


@app.route('/<int:name>/<int:multiplier>/<int:adder>')
def linear_equation_with_variable_coefficients(name, multiplier, adder):
    return "lm {}!".format(name*multiplier + adder)


if __name__ == '__main__':
    app.run()
