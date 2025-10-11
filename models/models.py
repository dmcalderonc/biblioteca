# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Biblioteca(models.Model):
    _name = 'biblioteca.libro'
    _description = 'biblioteca.biblioteca'

    firstname = fields.Char(string='Nombre Libro')
    author = fields.Many2one('biblioteca.author', string='Author del libro')
    value = fields.Integer(string='Número de ejemplares')
    value2 = fields.Float(compute="_value_pc", store=True, string='Costo')
    description = fields.Text(string='Resumen del libro')
    
    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

class BibliotecaAutor(models.Model):
    _name= 'biblioteca.author'
    _description = 'biblioteca.author'
    _rec_name= 'firstname'
    firstname = fields.Char()
    lastname = fields.Char()
    
    @api.depends('firstname','lastname')
    def _compute_display_name(self):
        for record in self:
            record.display_name= f"{record.firstname}{" "}{record.lastname}"
        