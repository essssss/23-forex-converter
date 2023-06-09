from flask import Flask, request, render_template, flash, redirect
from forex_python.converter import CurrencyRates, CurrencyCodes
from calculations import conversion_function, invalidate_cur_code, append_symbol

app = Flask(__name__)

app.config['SECRET_KEY'] = 'supersecret'


@app.route('/')
def show_form():
    return render_template('form.html')


@app.route('/convert')
def show_conversion():

    cur_from = request.args['start']
    cur_to = request.args['end']
    amt = float(request.args['amt'])

    if invalidate_cur_code(cur_from):
        flash(f"{cur_from} is not a valid Currency Code!")
        return redirect("/")
    elif invalidate_cur_code(cur_to):
        flash(f"{cur_to} is not a valid Currency Code!")
        return redirect("/")
    else:
        result = conversion_function(cur_from, cur_to, amt)
        result_with_symbol = append_symbol(cur_to, result)
        return render_template('result.html', cur_from=cur_from, cur_to=cur_to, amt=amt, result=result_with_symbol)
