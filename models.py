from openerp import models, fields, api
import datetime
from datetime import date, datetime
import time


class tagm_bank_setup(models.Model):
	_inherit = 'res.partner.bank'
	branch = fields.Char('Branch')
	bank_group = fields.Selection([('a', 'A'), ('b', 'B'), ('c', 'C')], 'Bank Group', help='Please Select the bank group')

class tagm_customer_payment(models.Model):
	_inherit = 'account.voucher'
	custom_bank = fields.Many2one('res.partner.bank',"Bank")

#class tagm_journal_entry_line(models.Model):
	#_inherit = 'account.move.line'
	#custom_bank = fields.Many2one('res.partner.bank',"Bank") 

	
class tagm_partner(models.Model):
	_inherit = 'res.partner'
	cc_firm_partner = fields.Boolean(string='Firm Partner')	

class tagm_firm_partner(models.Model):
	_inherit = 'account.move'
	firm_partner = fields.Many2one('res.partner',"Firm Partner" , domain="[('cc_firm_partner','=',True)]")

class tagm_invoice_firm_partner(models.Model):
	_inherit = 'account.invoice'
	firm_partner = fields.Many2one('res.partner',"Firm Partner" , domain="[('cc_firm_partner','=',True)]")	





	


