# -*- coding: utf-8 -*-
# from odoo import http


# class ControlUsuarios(http.Controller):
#     @http.route('/control_usuarios/control_usuarios', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/control_usuarios/control_usuarios/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('control_usuarios.listing', {
#             'root': '/control_usuarios/control_usuarios',
#             'objects': http.request.env['control_usuarios.control_usuarios'].search([]),
#         })

#     @http.route('/control_usuarios/control_usuarios/objects/<model("control_usuarios.control_usuarios"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('control_usuarios.object', {
#             'object': obj
#         })
