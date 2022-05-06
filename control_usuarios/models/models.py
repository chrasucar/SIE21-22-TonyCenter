# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class control_usuarios(models.Model):
#     _name = 'control_usuarios.control_usuarios'
#     _description = 'control_usuarios.control_usuarios'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import models, fields, api
from dateutil.relativedelta import *
from datetime import date

class gimnasio(models.Model):

    _name = 'control_usuarios.gimnasio'
    _description = 'Informaciones que contiene el gimnasio'
    _order = 'numero_clientes'

    numero_clientes = fields.Integer(string = 'Número De Clientes')
    numero_aparatos = fields.Integer(string = 'Número De Aparatos', required = True)
    numero_entrenadores = fields.Integer(string = 'Número De Entrenadores', required = True)

    #Relaciones entre tablas

    clientes_id = fields.Many2many('control_usuarios.clientes')

    def name_get(self):
        resultados = []
        for gimnasio in self:
            descripcion = f'{len(gimnasio.clientes_id)} Información del gimnasio y clientes'
            resultados.append((gimnasio.id, descripcion))
        return resultados


class clientes(models.Model):

    _name = 'control_usuarios.clientes'
    _description = 'Información de cada cliente'
    _order = 'nombre_id'

    nombre_id = fields.Many2one('res.partner')
    edad = fields.Integer('Edad', compute = '_get_edad')
    peso = fields.Integer(string = 'Peso')
    altura = fields.Float(string = 'Altura')
    dni = fields.Text(string = 'DNI')
    direccion = fields.Text(string = 'Dirección')
    ciudad = fields.Text(string = 'Ciudad')
    codigoPostal = fields.Text(string = 'Código Postal')
    pais = fields.Text(string = 'País')
    fechaRegistro = fields.Date(string = 'Fecha de Registro', required = True)
    lesionado = fields.Boolean(string = 'Lesionado', required = True, default = False)
    email = fields.Text(string = 'Correo Electrónico')
    telefono = fields.Integer(string = 'Teléfono')
    image = fields.Binary(string = 'Foto:')

    @api.depends('fechaRegistro')
    def _get_edad(self):
        for clientes in self:
            hoy = date.today()
            clientes.edad = relativedelta(hoy, clientes.fechaRegistro).years

    #Relaciones entre tablas

    gimnasio_id = fields.Many2one('control_usuarios.gimnasio', string = 'Gimnasio')

    gestion_ids = fields.Many2many('control_usuarios.control', string = 'Gestiones')

    def name_get(self):
        resultados = []
        for clientes in self:
            descripcion = f'{len(clientes.gestion_ids)} Información'
            resultados.append((clientes.id, descripcion))
        return resultados


class control(models.Model):

    _name = 'control_usuarios.control'
    _description = 'Gestión de cada cliente por su entrenador personal'
    _order = 'fechaGestion'

    nombreEntrenador_id = fields.Many2one('hr.employee', string = 'Nombre Entrenador')
    telefonoEntrenador = fields.Integer(string = 'Teléfono Entrenador')
    dietaSeleccionada = fields.Selection(string = 'Tipo Dieta', selection = 
    [('M', 'Mediterránea'), ('V', 'Vegetariana')], default = 'M', required = True)
    estado = fields.Selection(string = 'Estado', selection = 
    [('D', 'Delgado'), ('N', 'Peso Normal'), ('O', 'Obeso')], default = 'N', required = True)
    ingesta = fields.Integer(string = 'Ingesta Calórica')
    fechaGestion = fields.Date(string = 'Comienzo de Gestión')
    aparato = fields.Selection(string = 'Tipo Aparato', selection = 
    [('E', 'Aeróbico'), ('M', 'Musculación'), ('A', 'Ambos')], default = 'M', required = True)

    #Relaciones entre tablas

    clientes_ids = fields.Many2many('control_usuarios.clientes')

    def name_get(self):
        resultados = []
        for control in self:
            descripcion = f'{len(control.clientes_ids)} Entrenamiento - {control.aparato}'
            resultados.append((control.id, descripcion))
        return resultados




