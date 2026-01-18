// Copyright (c) 2026, Abdelrahman Elsayed and contributors
// For license information, please see license.txt

frappe.ui.form.on("Training Session", {
	refresh(frm) {
		frm.add_web_link(`/training-feedback/new/?session=${frm.doc.name}`, "See on Website");
	},
	async setup(frm) {
		const filterTrainer = await frappe.db.get_single_value(
			"Training Rate Config",
			"filter_trainer_by_current_user",
		);
		if (cint(filterTrainer) === 1) {
			frm.set_query("trainer", () => ({
				filters: {
					user: frappe.session.user,
				},
			}));
		}
	},
});
