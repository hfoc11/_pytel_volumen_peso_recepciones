from odoo import api, fields, models, _


class StockMove(models.Model):
    _inherit = 'stock.move'

    peso_stock_move = fields.Float(string='Peso', compute='_compute_volumen_stock_move')
    volumen_stock_move = fields.Float(string="Volumen", compute='_compute_volumen_stock_move')

    @api.one
    @api.depends('product_uom_qty', 'product_id','quantity_done')
    def _compute_volumen_stock_move(self):
        self.peso_stock_move = (self.product_id.weight or 0) * (self.quantity_done or 0)
        self.volumen_stock_move = (self.product_id.volume or 0) * (self.quantity_done or 0)


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    peso_stock_move = fields.Float(string='Peso', compute='_compute_volumen_stock_move_line')
    volumen_stock_move = fields.Float(string="Volumen", compute='_compute_volumen_stock_move_line')

    @api.one
    @api.depends('product_id','qty_done')
    def _compute_volumen_stock_move_line(self):
        self.peso_stock_move = (self.product_id.weight or 0) * (self.qty_done or 0)
        self.volumen_stock_move = (self.product_id.volume or 0) * (self.qty_done or 0)


class StockPicking(models.Model):
    _inherit = 'stock.picking'
    
    total_volumen = fields.Float(string='Volumen Total', compute='_compute_peso_volumen_stock_picking')
    total_peso = fields.Float(string='Volumen Total', compute='_compute_peso_volumen_stock_picking')
    
    @api.depends('move_lines')
    def _compute_peso_volumen_stock_picking(self):
        
        for line in self.move_lines:            
            self.total_volumen += ((line.product_id.volume or 0) * (line.quantity_done or 0))
            self.total_peso += ((line.product_id.weight or 0) * (line.quantity_done or 0))

    
    # se añade total peso, este se encuentra de forma nativa como weight en stock.picking, pero es calculado al validar.
      
