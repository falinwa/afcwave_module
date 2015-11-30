# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
import openerp.addons.decimal_precision as dp

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

#end of SaleOrderLine()

class ProductTemplate(models.Model):
    _inherit = "product.template"
    
    fal_quantity_perbox = fields.Float(string='Quantity per Box')
    
    

