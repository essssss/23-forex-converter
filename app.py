from flask import Flask, request, render_template
from forex_python.converter import CurrencyRates, Decimal

app = Flask(__name__)


@app.route('/')
def show_form():
    return render_template('form.html')


@app.route('/convert')
def show_conversion():

    c = CurrencyRates()
    cur_from = request.args['start']
    cur_to = request.args['end']
    amt = request.args['amt']

    result = c.convert(cur_from, cur_to, Decimal(amt))
    return render_template('result.html', cur_from=cur_from, cur_to=cur_to, amt=amt, result=result)
