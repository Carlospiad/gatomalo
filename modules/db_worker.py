from sqlalchemy.sql import exists
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import datetime
from models.models import *
import os
import logging

db_url = os.environ['panadata_development']
engine = create_engine(db_url, convert_unicode=True)
Base.metadata.create_all(engine)
session_maker = sessionmaker(bind=engine)
logger = logging.getLogger('db_worker')

def find_or_create_cliente_from_dict(session,cliente):
    instance = session.query(Cliente).filter(Cliente.empresa == cliente['empresa']).first()
    if not instance:
        instance = Cliente.from_dict(cliente)
        session.add(instance)
        session.commit()
    return instance

def create_factura(session,cliente,productos):
    if isinstance(cliente,dict):
        cliente = find_or_create_cliente_from_dict(session,cliente)
    if isinstance(cliente,Cliente):
        factura = Factura(cliente)
        session.add(factura)
        session.commit()
        session.refresh(factura)
        productos = factura.create_productos_from_dict(productos)
        session.add_all(productos)
        session.commit()
    return factura,productos,cliente
