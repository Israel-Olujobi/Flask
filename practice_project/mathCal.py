from flask import Flask, render_template, request
from Maths.mathematics import summation, multiplication, subtraction

app = Flask('Mathematics Problem Solver')

@app.route('/sum')
def my_sum():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = summation(num1, num2)

# As per instructions

    if result.is_integer():                # is_integer checks if number is a whole number, output is True/False
        result = int(result)               # Convert number to an integer
    return str(result)                     # Finally, return integer into a string



@app.route('/sub')
def my_sub():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = subtraction(num1, num2)

    if result.is_integer():
        result = int(result)
    return str(result)


@app.route('/mul')
def my_mul():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = multiplication(num1, num2)

    if result.is_integer():
        result = int(result)
    return str(result)

# for endpoint, implement a method that renders the index.html

@app.route('/')
def render_index_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080)



# To run code:

# cd practice_project
# flask --app mathCal --debug run
# Click http link