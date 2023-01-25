from flask import render_template
from app import app
from models.objects import orders

@app.route('/orders')
@app.route('/')
def index():
    return render_template('index.html', title='Shop', orders=orders)

@app.route('/orders/<int:index>')
def single_order(index):
    # return f"Testing {index}"
    return render_template('single_order.html', title='Orders', orders=orders[index])
