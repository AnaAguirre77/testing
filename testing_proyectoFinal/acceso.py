# acceso.py
from datetime import datetime

class Acceso:
    def __init__(self, id, fechaIngreso, fechaSalida, usuarioLogueado):
        self.__id = id
        self.__fechaIngreso = fechaIngreso
        self.__fechaSalida = fechaSalida
        self.__usuarioLogueado = usuarioLogueado

    # get y set para id
    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    # get y set para fechaIngreso
    def get_fechaIngreso(self):
        return self.__fechaIngreso

    def set_fechaIngreso(self, fechaIngreso):
        self.__fechaIngreso = fechaIngreso

    # get y set para fechaSalida
    def get_fechaSalida(self):
        return self.__fechaSalida

    def set_fechaSalida(self, fechaSalida):
        self.__fechaSalida = fechaSalida

    # get y set para usuarioLogueado
    def get_usuarioLogueado(self):
        return self.__usuarioLogueado

    def set_usuarioLogueado(self, usuarioLogueado):
        self.__usuarioLogueado = usuarioLogueado