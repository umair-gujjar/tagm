# -*- coding: utf-8 -*-
from openerp import http

# class Tagm(http.Controller):
#     @http.route('/tagm/tagm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tagm/tagm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tagm.listing', {
#             'root': '/tagm/tagm',
#             'objects': http.request.env['tagm.tagm'].search([]),
#         })

#     @http.route('/tagm/tagm/objects/<model("tagm.tagm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tagm.object', {
#             'object': obj
#         })