// Copyright (c) 2026, Abdelrahman Elsayed and contributors
// For license information, please see license.txt

frappe.ui.form.on("Training Session", {
	refresh(frm) {
		frm.add_web_link(`/training-feedback/new/?session=${frm.doc.name}`, "See on Website");
	},
});
