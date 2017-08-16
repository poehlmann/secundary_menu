# -*- coding: utf-8 -*-
from odoo import http

# class ThanosSecundaryMenu(http.Controller):
#     @http.route('/thanos_secundary_menu/thanos_secundary_menu/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/thanos_secundary_menu/thanos_secundary_menu/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('thanos_secundary_menu.listing', {
#             'root': '/thanos_secundary_menu/thanos_secundary_menu',
#             'objects': http.request.env['thanos_secundary_menu.thanos_secundary_menu'].search([]),
#         })

#     @http.route('/thanos_secundary_menu/thanos_secundary_menu/objects/<model("thanos_secundary_menu.thanos_secundary_menu"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('thanos_secundary_menu.object', {
#             'object': obj
#         })