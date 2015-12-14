# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
import openerp.addons.decimal_precision as dp

class SaleOrder(models.Model):
    _inherit = "sale.order"    

    @api.onchange('fal_payment_term')
    def _onchange_fal_payment_term(self):
        if self.fal_payment_term == 'adv':
            pricelist = self.env['product.pricelist'].search([('name','ilike','net 30')])
            self.pricelist_id = pricelist and pricelist[0]
        if self.fal_payment_term == 'net30':
            pricelist = self.env['product.pricelist'].search([('name','ilike','distributor')])
            self.pricelist_id = pricelist and pricelist[0]

    @api.one
    @api.depends('fal_payment_term')
    def _compute_is_fal_payment_term_invisible(self):
        if self.pricelist_id.name ilike 'distributor':            
            self.is_fal_payment_term_invisible = False
        else:
            self.is_fal_payment_term_invisible = True
            
    is_fal_payment_term_invisible = fields.Boolean('Is Fal Payment Term Invisible', compute='_compute_is_fal_payment_term_invisible')    
    fal_payment_term = fields.Selection([('adv','TT in Advance'),('net30','Net 30')], 'Term of Payment')
    
    
    
#end of SaleOrder()

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"
    
    @api.onchange('fal_box_quantity')
    def onchange_fal_box_quantity(self):
        vals = {
            'product_uom_qty' : self.product_id.fal_quantity_perbox * self.fal_box_quantity,
        }
        self.update(vals)
    
    fal_box_quantity = fields.Integer(string='Box Quantity')
    product_uom_qty_display = fields.Float(string='Quantity', digits=dp.get_precision('Product Unit of Measure'), related="product_uom_qty", readonly=1)
    fal_quantity_available = fields.Float('Available Quantity', related="product_id.qty_available")
    

#end of SaleOrderLine()

class ProductTemplate(models.Model):
    _inherit = "product.template"
    
    fal_quantity_perbox = fields.Float(string='Quantity per Box')
    fal_empty_price = fields.Float(string="Empty Price")
    
    

