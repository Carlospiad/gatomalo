#!flask/bin/python
from flask import render_template
from flask import Flask, jsonify,request,abort
from sqlalchemy.sql import exists
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import datetime
from models.models import *
from modules import db_worker
import os
import logging
from modules import printer

db_url = os.environ['gatomalo_development']
engine = create_engine(db_url, convert_unicode=True, echo=True)
Base.metadata.create_all(engine)
session_maker = sessionmaker(bind=engine)
#logger = logging.getLogger('flask')
facturas = []

app = Flask(__name__)

def parse_cliente_from_post(post):
    empresa = post.form['factura[cliente][empresa]']
    direccion = post.form['factura[cliente][direccion]']
    telefono = post.form['factura[cliente][telefono]']
    ruc = post.form['factura[cliente][ruc]']
    return { 'empresa':empresa,'direccion':direccion,'telefono':telefono,'ruc':ruc }

def parse_productos_from_post(post):
    nombre = post.form['factura[productos][nombre]']
    cantidad = post.form['factura[productos][cantidad]']
    tasa = post.form['factura[productos][tasa]']
    precio = post.form['factura[productos][precio]']
    return { 'nombre':nombre,'cantidad':cantidad,'tasa':tasa,'precio':precio }

@app.route('/facturas', methods = ['POST'])
def create_factura():
    session = session_maker()
    print(request.json)
#    return str(request.form['factura[cliente][empresa]'])
    if request.json and 'factura' in request.json:
        productos = request.json['factura']['productos']
        cliente =  request.json['factura']['cliente']
    elif request.form:
        cliente = parse_cliente_from_post(request)
        productos = parse_productos_from_post(request)
    else:
        abort(400)
    try:
        factura,productos,cliente = db_worker.create_factura(session,cliente,productos)
    except Exception as e:
            raise(e)
            session.rollback()
    printer.write_string_to_printer(str(factura))
    return str(factura)

@app.route('/nota', methods = ['POST'])
def create_nota():
    session = session_maker()
#   return str(request.form['factura[cliente][empresa]'])
    if request.json and 'nota' in request.json:
        factura_id = request.json['nota']['factura_id']
        legacy_id = request.json['nota']['legacy_id']
    else:
        abort(400)
    try:
        nota = db_worker.create_nota(session,factura_id,legacy_id)
    except Exception as e:
            raise(e)
            session.rollback()
    printer.write_string_to_printer(str(nota))
    return str(nota)
#
@app.route('/facturas', methods = ['GET'])
def get_facturas():
    session = session_maker()
    facturas = db_worker.all_facturas(session)
    return jsonify({f.id:f.to_json() for f in facturas})

if __name__ == "__main__":
    app.run(debug=True)
