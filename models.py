from openerp import models, fields, api
import datetime
from datetime import date, datetime
import time

#res partner bank class inherited
class tagm_bank_setup(models.Model):
	_inherit = 'res.partner.bank'
	branch = fields.Char('Branch')
	bank_group = fields.Selection([('a', 'A'), ('b', 'B'), ('c', 'C')], 'Bank Group', help='Please Select the bank group')
#account voucher class inherited
class tagm_customer_payment(models.Model):
	_inherit = 'account.voucher'
	custom_bank = fields.Many2one('res.partner.bank',"Bank")
	#overiding parent function
	@api.multi
	def proforma_voucher(self):
		result = super(tagm_customer_payment, self).proforma_voucher()
		self.bank_field_transfer()
		return result

# geting bank name using search by number
	def bank_field_transfer(self):
		if self.custom_bank:
			account_move_recs = self.env['account.move'].search([('name','=',self.number)])
			for rec in account_move_recs.line_id:
				rec.custom_bank = self.custom_bank

#res partner class inherited
class tagm_partner(models.Model):
	_inherit = 'res.partner'
	cc_firm_partner = fields.Boolean(string='Firm Partner')	
#account move class inherited
class tagm_firm_partner(models.Model):
	_inherit = 'account.move'
	firm_partner = fields.Many2one('res.partner',"Firm Partner" , domain="[('cc_firm_partner','=',True)]")
	custom_bank = fields.Many2one('res.partner.bank',"Bank")
#account invoice class inherited
class tagm_invoice_firm_partner(models.Model):
	_inherit = 'account.invoice'
	firm_partner = fields.Many2one('res.partner',"Firm Partner" , domain="[('cc_firm_partner','=',True)]")
#overide invoice validate parent function
	@api.multi
	def invoice_validate(self):
		result = super(tagm_invoice_firm_partner, self).invoice_validate()
		self.firm_partner_transfer()
		return result

#get firm name using number search
	def firm_partner_transfer(self):
		if self.firm_partner:
			account_move_recs = self.env['account.move'].search([('name','=',self.number)])
			account_move_recs.firm_partner = self.firm_partner

#account move line class inherited
class tagm_account_move_line(models.Model):
	_inherit = 'account.move.line'
	custom_bank = fields.Many2one('res.partner.bank',"Bank")

#res company class inherited
class tagm_company(models.Model):
	_inherit='res.company'
	ntn = fields.Char(string='NTN')
	strn = fields.Char(string='STRN ')
	pntn = fields.Char(string='PNTN')
