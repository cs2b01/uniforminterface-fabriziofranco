from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import connector

class Usuario(connector.Manager.Base):
    __tablename__ = 'USUARIO'
    id = Column(Integer, Sequence('usuario_id_seq'), primary_key=True)
    Nombre = Column(String(100))
    Codigo = Column(String(20))
    Correo = Column(String(100))
