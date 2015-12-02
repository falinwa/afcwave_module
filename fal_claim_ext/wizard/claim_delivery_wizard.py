from openerp.osv import fields, orm
from openerp.tools.translate import _

class  claim_delivery_wizard(orm.TransientModel):
    _name = 'claim.delivery.wizard'


    def _default_serial_id(self, cr, uid, context=None):
       stock_move_id = context.get('active_id')
       stock_move_obj = self.pool.get('stock.move')
       stock_move = stock_move_obj.browse(cr, uid, stock_move_id)
      
       #serial_id = self.pool.get('stock.move').context.get('prodlot_id')
       

       return stock_move.prodlot_id.id 


    

# def _default_serial_id(self):
#     return self.env['stock.move'].context.get('prodlot_id')

#     serial_id = fields.many2one('stock.production.lot', string=_("Serial Number"), default =_default_serial_id)


    # def save(self, cr, uid, id, context=None):



        
    #     claim_values = {
    #     'serial_id' : self.('serial_id'),
    #     'name' : self.env('name'),
    #     'description' : self.env('description'),     
    # }
    #     claim_obj = self.pool.get('crm.claim')
    #     claim_id = claim_obj.create(cr, uid, claim_values, context=context)



    #     return claim_id 
        
    
    _columns = {
        'serial_id' : fields.many2one('stock.production.lot', string=_("Serial Number")),
        'name' : fields.char('Last Serial Number', size=256),
        'description' : fields.char('Create New Serial Number'),
    }

    _defaults = {
        'serial_id': _default_serial_id,
    }



#end of claim_delivery_wizard()