# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Biblioteca(models.Model):
    _name = 'biblioteca.libro'
    _description = 'biblioteca.biblioteca'

    firstname = fields.Char(string='Titulo')
    author = fields.Many2one('biblioteca.author', string='Author del libro')
    isbn = fields.Char(string='ISBN')
    genero = fields.Char(string='Género')
    fecha = fields.Char(string='Año de publicación')
    description = fields.Text(string='Resumen del libro')
    editorial = fields.Many2one('biblioteca.editorial', string='Editorial')
    value = fields.Integer(string='Número de ejemplares')
    estado= fields.Char(string='Estado')
    value2 = fields.Float(compute="_value_pc", store=True, string='Costo')
    ubicacion = fields.Char(string="Ubicación del libro")

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

class BibliotecaAutor(models.Model):
    _name= 'biblioteca.author'
    _description = 'biblioteca.author'
    _rec_name= 'firstname'
    firstname = fields.Char(string='Nombre')
    lastname = fields.Char(string='Apellido')
    
    @api.depends('firstname','lastname')
    def _compute_display_name(self):
        for record in self:
            record.display_name= f"{record.firstname}{" "}{record.lastname}"

class BibliotecaUsuario(models.Model):
    _name= 'biblioteca.usuario'
    _description= 'biblioteca.usuario'

    firstname= fields.Char(string='Nombre')
    lastname = fields.Char(string='Apellido')
    cedula = fields.Integer(string='Cédula')
    telefono= fields.Integer(string='Telefono')
    direccion= fields.Char(string='Dirección')
    correo= fields.Char(string='Correo electronico')
    tipo_usuario= fields.Char(string='Tipo de usuario')
    historial_prestamo= fields.Char(string='Historial de prestamo')

class BibliotecaEditorial(models.Model):
    _name= 'biblioteca.editorial'
    _description= 'biblioteca.editorial'
    _rec_name='editorial'
    editorial= fields.Char(string='Editorial')
    @api.depends('editorial')
    def _compute_display_name(self):
        for record in self:
            record.display_name= f"{record.editorial}"

class BibliotecaPersonal(models.Model):
    _name= 'biblioteca.personal'
    _description= 'biblioteca.personal'

    firstname = fields.Char(string='Nombre')
    lastname = fields.Char(string='Apellido')
    cargo= fields.Char(string='Cargo')
    usuario= fields.Char(string='Usuario')
    clave= fields.Char(string='Clave')

