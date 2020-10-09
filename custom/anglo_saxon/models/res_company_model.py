# -*- coding: utf-8 -*-

from odoo import fields, models

""" 
    Extend res.company to add "active" field to allow company archive
"""
class ResCompany(models.Model): 
    _name = 'res.company' 
    _inherit = 'res.company' 

    active = fields.Boolean(string="Active", required=True, default=True)
    