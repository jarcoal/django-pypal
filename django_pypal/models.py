from django.db import models
from resources import AdaptivePaymentsResource


class AdaptivePaymentsIPN(models.Model):
	"""
	IPN messages sent by the Payments API
	https://www.x.com/developers/paypal/documentation-tools/adaptive-payments/integration-guide/APIntro
	"""

	transaction_type = models.CharField(max_length=100, blank=True)
	status = models.CharField(max_length=25, blank=True)
	sender_email = models.EmailField(blank=True)
	action_type = models.CharField(max_length=25, blank=True)
	payment_request_date = models.DateTimeField(null=True)
	reverse_all_parallel_payments_on_error = models.NullBooleanField(null=True)
	
	return_url = models.URLField(blank=True)
	cancel_url = models.URLField(blank=True)
	ipn_notification_url = models.URLField(blank=True)

	pay_key = models.CharField(max_length=50, blank=True)
	memo = models.TextField(max_length=4000, blank=True)
	fees_payer = models.CharField(max_length=25, blank=True)
	tracking_id = models.CharField(max_length=50, blank=True)
	preapproval_key = models.CharField(max_length=50, blank=True)

	reason_code = models.CharField(max_length=50, blank=True)

	def __unicode__(self):
		return self.pay_key

class AdaptivePaymentsIPNTransaction(models.Model):
	"""
	single transaction inside of an adaptive payment
	"""

	ipn = models.ForeignKey(AdaptivePaymentsIPN, related_name='transactions')

	transaction_id = models.CharField(max_length=100, blank=True)
	status = models.CharField(max_length=25, blank=True)
	id_for_sender = models.CharField(max_length=100, blank=True)
	status_for_sender_txn = models.CharField(max_length=25, blank=True)
	refund_id = models.CharField(max_length=25, blank=True)
	refund_amount = models.DecimalField(null=True, decimal_places=2, max_digits=9)
	refund_account_charged = models.EmailField(blank=True)
	receiver = models.EmailField(blank=True)
	invoice_id = models.CharField(max_length=50, blank=True)
	amount = models.DecimalField(null=True, decimal_places=2, max_digits=9)
	is_primary_receiver = models.NullBooleanField(null=True)

	def refund(self, amount=None):
		"""
		Refunds all or part of this transaction.
		"""

		if amount is None:
			amount = self.amount

		if self.refund_amount == self.amount:
			raise Exception('transaction is already refunded')

		if self.refund_amount and self.refund_amount + amount > self.amount:
			raise Exception('cannot refund more than initial amount')

		resource = AdaptivePaymentsResource()
		resource.refund(payKey=self.ipn.pay_key, receiverList=[{ 'email': self.receiver, 'amount': amount }])

	def __unicode__(self):
		return self.transaction_id