import models
from django.views import generic
from utils import _parse_transactions_from_payments_ipn

class AdaptivePaymentsIPNView(generic.CreateView):
	"""
	Receives IPNs emitted by the Payments API
	"""

	model = models.AdaptivePaymentsIPN

	def form_valid(self, form):
		"""
		Saves the IPN and checks for transactions, saving them as well.
		"""

		response = super(AdaptivePaymentsIPNView, self).form_valid(form)

		for transaction_data in _parse_transactions_from_payments_ipn(self.request.POST):
			self.object.transactions.create(**transaction_data)

		return response