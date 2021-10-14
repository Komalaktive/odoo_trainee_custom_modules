
from odoo import http


class Controller(http.Controller):
    @http.route('/trainee_practical/trainee_practical/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/trainee_practical/trainee_practical/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('trainee_practical.listing', {
            'root': '/trainee_practical/trainee_practical',
            'objects': http.request.env['trainee_practical.trainee_practical'].search([]),
        })

    @http.route('/trainee_practical/trainee_practical/objects/<model("trainee_practical.trainee_practical"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('trainee_practical.object', {
            'object': obj
        })
