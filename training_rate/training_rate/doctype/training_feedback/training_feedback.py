# Copyright (c) 2026, Abdelrahman Elsayed and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class TrainingFeedback(Document):
	def after_insert(self):
		self.send_feedback_notification()

	def send_feedback_notification(self):
		trainer = frappe.get_value(
			"Training Session",
			self.session,
			"trainer"
		)

		if not trainer:
			return

		trainer_email = frappe.get_value(
			"Contact",
			trainer,
			"email_id"
		)

		if not trainer_email:
			return

		subject = f"New Training Feedback Received"

		message = f"""
		<p>Hello,</p>

		<p>You have received a new feedback for the training session:</p>

		<ul>
			<li><strong>Session:</strong> {self.session}</li>
			<li><strong>Rating:</strong> {self.rate} / 1</li>
		</ul>

		<p><strong>Feedback:</strong></p>
		<p>{frappe.utils.escape_html(self.long_text_xhft or "No written feedback")}</p>

		<hr>

		"""

		frappe.sendmail(
			recipients=[trainer_email],
			subject=subject,
			message=message,
		)

