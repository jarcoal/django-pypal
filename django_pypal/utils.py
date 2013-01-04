#
# Helper functions for Adaptive Payments API
#

def _parse_transactions_from_payments_ipn(post_data):
	"""
	Extracts the nested transaction data from a payments IPN.
	"""

	transactions = []

	for i in range(0, 6):
		prefix = 'transaction(%i).' % i

		data = {
			'transaction_id': post_data.get(prefix + 'id'),
			'status': post_data.get(prefix + 'status'),
			'id_for_sender': post_data.get(prefix + 'id_for_sender'),
			'status_for_sender_txn': post_data.get(prefix + 'status_for_sender_txn'),
			'refund_id': post_data.get(prefix + 'refund_id'),
			'refund_amount': post_data.get(prefix + 'refund_amount'),
			'refund_amount_charged': post_data.get(prefix + 'refund_amount_charged'),
			'receiver': post_data.get(prefix + 'receiver'),
			'invoice_id': post_data.get(prefix + 'invoice_id'),
			'amount': post_data.get(prefix + 'amount'),
			'is_primary_receiver': post_data.get(prefix + 'is_primary_receiver'),
		}

		if not data['transaction_id']:
			break

		transactions.append(data)

	return transactions