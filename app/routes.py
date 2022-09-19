import os
from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import RequestForm, PayForm
import random

from flask_qrcode import QRcode
from flask import Flask, render_template, request
from lightning import LightningRpc
from lightning.lightning import RpcError

from json2html import *

rpc = LightningRpc(os.environ['RPC_SOCKET'])
connect_str = os.environ['CONNECT_INFO']
QRcode(app)


@app.route('/pay', methods=['GET', 'POST'])
def pay():
    form = PayForm()
    pay_result = None
    if form.validate_on_submit():
        try:
            result = rpc.pay(form.invoice.data)
        except RpcError as e:
            print(e.error["message"], e)
            flash('Error with LN Pay: {}'.format(e.error["message"]))
            return redirect('/index')
        flash('Invoice {}'.format(form.invoice.data))
        pay_result = json2html.convert(json=result)
    return render_template('pay.html', title='Pay Invoice', form=form, pay_result=pay_result)


@app.route('/request', methods=['GET', 'POST'])
def request():
    form = RequestForm()
    invoice = None
    if form.validate_on_submit():
        amount = int(form.amount.data)
        try:
            invoice = rpc.invoice(amount, str(random.random()), str(
                int(random.random()*100)))['bolt11']
        except RpcError as e:
            print(e.error["message"], e)
            flash('Error with LN Request: {}'.format(e.error["message"]))
            return redirect('/index')
    return render_template('request.html', title='Request Invoice', form=form, invoice=invoice)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', connect_str=connect_str)
