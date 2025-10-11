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
        