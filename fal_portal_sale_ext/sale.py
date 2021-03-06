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
    
    @api.multi
    def action_set_checkout(self):
        self.is_checkout = True
        
    partner_id = fields.Many2one(default=_default_partner_id)
    is_checkout = fields.Boolean('Is Checkout?')
    
#end of SaleOrder()

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"
    
    name_display = fields.Text(string='Description', related="name", readonly="1")
    price_unit_display = fields.Float('Unit Price', related="price_unit", readonly="1")
    tax_id_display = fields.Many2many('account.tax', string='Taxes', related="tax_id", readonly="1")    
    
#end of SaleOrderLine()

class ResPartner(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"
    
    region_manager_id = fields.Many2one('res.partner', string="Region Manager", required=1)
    
#end of ResPartner

class ResUsers(models.Model):
    _name = "res.users"
    _inherit = "res.users"

    partner_price_list_id = fields.Many2one('product.pricelist', related="partner_id.property_product_pricelist", string="PriceList", required=1)
    partner_sale_person_id = fields.Many2one('res.users', related="partner_id.user_id", string="Sale Person", required=1)
    partner_country_id = fields.Many2one('res.country', related="partner_id.country_id", string="Country", required=1)
    partner_region_manager_id = fields.Many2one('res.partner', related="partner_id.region_manager_id", string="Region Manager", required=1)
    
#end of ResUsers()