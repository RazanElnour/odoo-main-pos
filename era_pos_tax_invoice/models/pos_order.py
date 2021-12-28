
from odoo import models, fields, api

class POSConfigInherit(models.Model):
    _inherit = 'pos.config'

    #image = fields.Binary(string='Image')
    allow_qr_code = fields.Boolean(string="Add QR Code in Receipt")
   

    pos_logo = fields.Binary(string='POS Logo')
    show_barcode = fields.Boolean(string="Show Barcode")
     

class pos_order_inherit(models.Model):
	_inherit = "pos.order"

	barcode_number = fields.Char(string="Barcode Number")

	@api.model
	def _order_fields(self, ui_order):
		res = super(pos_order_inherit, self)._order_fields(ui_order)
#		res['barcode_number'] = ui_order['barcode']
		return res	
    


