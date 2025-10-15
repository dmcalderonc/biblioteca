# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Biblioteca(models.Model):
    _name = 'biblioteca.libro'
    _description = 'biblioteca.biblioteca'
    _rec_name= 'firstname'

    firstname = fields.Char(string='Titulo')
    author = fields.Many2one('biblioteca.author', string='Author del libro')
    isbn = fields.Char(string='ISBN')
    genero = fields.Many2one('biblioteca.genero', string='Género')
    fecha = fields.Char(string='Año de publicación')
    description = fields.Text(string='Resumen del libro')
    editorial = fields.Many2one('biblioteca.editorial', string='Editorial')
    ejemplares = fields.Integer(string='Número de ejemplares')
    estado= fields.Char(string='Estado')
    costo = fields.Float(compute="_value_pc", store=True, string='Costo')
    ubicacion = fields.Many2one('biblioteca.ubicacion', string="Ubicación física")

    @api.depends('costo')
    def _value_pc(self):
        for record in self:
           record.costo = float(record.ejemplares) / 100

class BibliotecaAutor(models.Model):
    _name= 'biblioteca.author'
    _description = 'biblioteca.author'
    _rec_name= 'firstname'
    firstname = fields.Char(string='Nombre')
    lastname = fields.Char(string='Apellido')
    nacimiento =fields.Date(string='Fecha de nacimiento')
    alias= fields.Char(string='Pseudonimo')
    libros_autores= fields.Many2many('biblioteca.libro',
                                    relation="Libro_author_rel",
                                    column1= "author_id", colum_2="libro_id", string='Libros autores')
    
    @api.depends('firstname','lastname')
    def _compute_display_name(self):
        for record in self:
            record.display_name= f"{record.firstname}{" "}{record.lastname}"

class BibliotecaUsuario(models.Model):
    _name= 'biblioteca.usuario'
    _description= 'biblioteca.usuario'
    _rec_name='firstname'
    firstname= fields.Char(string='Nombre')
    lastname = fields.Char(string='Apellido')
    cedula = fields.Integer(string='Cédula')
    telefono= fields.Integer(string='Telefono')
    direccion= fields.Char(string='Dirección')
    correo= fields.Char(string='Correo electronico')
    tipo_usuario= fields.Selection(selection=[('alumno', 'Alumno'),
                                              ('profesor', 'Profesor'),
                                              ('personal', 'Personal'),
                                              ('externo', 'Usuario externo')],string='Tipo de usuario')
    historial_prestamo= fields.Many2one('biblioteca.prestamo', string='Historial de prestamo')

    @api.depends('firstname','lastname')
    def _compute_display_name(self):
        for record in self:
            record.display_name= f"{record.firstname}{" "}{record.lastname}"
            
    @api.onchange('cedula')
    def onchange_cedula(self):
        if self.cedula:
            if int(self.cedula) >'0' and int(self.cedula)<100:
                raise ValueError("el numero es correcto")
                return{'warning':{'title':"alerta",
                                  'message':"el numero es correcto"}}
                print("Hola mundo")
            else:
                raise ValueError("El numero impreso es 0")  
        

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

class BibliotecaGeneros(models.Model):
    _name= 'biblioteca.genero'
    _description= 'biblioteca.genero'
    _rec_name='genero'
    genero= fields.Char(string='Género')
    descripcion=fields.Char(string='Descripción')
    @api.depends('genero')
    def _compute_display_name(self):
        for record in self:
            record.display_name= f"{record.genero}"

class BibliotecaPrestamos(models.Model):
    _name= 'biblioteca.prestamo'
    _description= 'biblioteca.prestamo'
    _rec_name= 'libro'
    name=fields.Char()
    usuario= fields.Many2one('biblioteca.usuario', string='Usuario')
    libro=fields.One2many('biblioteca.libro', 'firstname' , string='Titulo del libro')
    fecha_prestamo= fields.Date(string='Fecha de prestamo')
    fecha_devolucion= fields.Date(string='Fecha de devolución')
    estado= fields.Selection(selection=[('b', 'Borrador'),
                                        ('p', 'Prestamo'),
                                        ('m', 'Multa'),
                                        ('d', 'Devuelto'),],string='Estado', default='b')
    multa_bool= fields.Boolean(default=False)
    multa=fields.Float()
    
    def generar_prestamo(self):
        print("generando Prestamo")
        self.write({'estado': 'p'})
    
    
    @api.depends('libro','estado')
    def _compute_display_name(self):
        for record in self:
            record.display_name= f"{record.libro}{" "}{record.estado}"

class BibliotecaMultas(models.Model):
    _name= 'biblioteca.multa'
    _description= 'biblioteca.multa'
    codigo=fields.Char(string='Código de multa')
    usuario= fields.Many2one('biblioteca.usuario', string='Usuario')
    monto= fields.Float(string='Monto a pagar')
    motivo= fields.Selection(selection=[('retraso', 'Retraso'),
                                        ('daño', 'Daño'),
                                        ('perdida','Perdida')],string='Causa de la multa')
    pago= fields.Selection(selection=[('pendiente', 'Pendiente'),
                                        ('saldada', 'Saldada')],string='Pago  de la multa')
    
class BibliotecaUbicacion(models.Model):
    _name= 'biblioteca.ubicacion'
    _description= 'biblioteca.ubicacion'
    _rec_name= 'ubicacion'
    libro= fields.Many2one('biblioteca.libro', string='Titulo del libro')
    ubicacion= fields.Char(string='Ubicación')

