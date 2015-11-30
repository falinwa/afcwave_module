# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
import openerp.addons.decimal_precision as dp

class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    @api.model
    def _default_partner_id(self):
        for group in self.env.user.groups_id:
            if group.is_portal:                
                return self.env.user.partner_id.id
    
    partner_id = fields.Many2one(default=_default_partner_id)
    
#end of SaleOrder()

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"
    
    name_display = fields.Text(string='Description', related="name", readonly="1")
    price_unit_display = fields.Float('Unit Price', related="price_unit", readonly="1")
    tax_id_display = fields.Many2many('account.tax', string='Taxes', related="tax_id", readonly="1")
    
#end of SaleOrderLine()