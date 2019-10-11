from flask import Flask, request, render_template, jsonify

app = Flask(__name__, static_folder="static")

var_on_server = [1,2,3,4,5,6]

@app.route('/')
def index():
    """Return the main page."""
    print('index print statement here')
    return render_template('index.html', var_from_server=var_on_server)


@app.route('/increment_on_server', methods=['GET', 'POST'])
def increment_on_server():
    """Receieve number from browser, add one and return it."""

    print('increment_on_server print statement here')

    data = request.json
    try:
        new_number = 1 + int(data['package_to_server'])
        return str(new_number)
    except ValueError:
        return 'Please Input A Valid Number'
