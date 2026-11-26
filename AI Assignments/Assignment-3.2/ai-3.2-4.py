import tkinter as tk
from tkinter import messagebox, ttk


SUBJECTS = ("Mathematics", "Science", "English", "Computer Science", "Social Studies")
MAX_MARKS_PER_SUBJECT = 100


class GradingApp:
	def __init__(self, root):
		self.root = root
		self.root.title("Student Grade Calculator")
		self.root.geometry("560x650")
		self.root.minsize(500, 580)
		self.root.configure(bg="#f4f7fb")

		self.name_var = tk.StringVar()
		self.mark_vars = [tk.StringVar() for _ in SUBJECTS]
		self.total_var = tk.StringVar(value="-- / 500")
		self.percentage_var = tk.StringVar(value="--%")
		self.grade_var = tk.StringVar(value="--")
		self.status_var = tk.StringVar(value="Enter marks for all five subjects to see the result.")

		self._configure_styles()
		self._build_ui()

	def _configure_styles(self):
		style = ttk.Style()
		style.theme_use("clam")
		style.configure("TFrame", background="#f4f7fb")
		style.configure("Card.TFrame", background="#ffffff")
		style.configure("Title.TLabel", background="#f4f7fb", foreground="#17324d", font=("Segoe UI", 24, "bold"))
		style.configure("Subtitle.TLabel", background="#f4f7fb", foreground="#637487", font=("Segoe UI", 10))
		style.configure("CardTitle.TLabel", background="#ffffff", foreground="#17324d", font=("Segoe UI", 13, "bold"))
		style.configure("Field.TLabel", background="#ffffff", foreground="#425466", font=("Segoe UI", 10))
		style.configure("ResultLabel.TLabel", background="#ffffff", foreground="#718096", font=("Segoe UI", 9))
		style.configure("ResultValue.TLabel", background="#ffffff", foreground="#17324d", font=("Segoe UI", 18, "bold"))
		style.configure("Primary.TButton", background="#1976d2", foreground="#ffffff", font=("Segoe UI", 10, "bold"), padding=(18, 10))
		style.map("Primary.TButton", background=[("active", "#125da8")])
		style.configure("Secondary.TButton", background="#e8eef5", foreground="#425466", font=("Segoe UI", 10), padding=(18, 10))
		style.map("Secondary.TButton", background=[("active", "#d7e2ee")])

	def _build_ui(self):
		main = ttk.Frame(self.root, padding=(36, 28))
		main.pack(fill="both", expand=True)

		ttk.Label(main, text="Student Grade Calculator", style="Title.TLabel").pack(anchor="w")
		ttk.Label(main, text="Enter the marks below to calculate the final result.", style="Subtitle.TLabel").pack(anchor="w", pady=(4, 22))

		input_card = ttk.Frame(main, style="Card.TFrame", padding=24)
		input_card.pack(fill="x")
		ttk.Label(input_card, text="Student details", style="CardTitle.TLabel").grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 18))
		ttk.Label(input_card, text="Student name", style="Field.TLabel").grid(row=1, column=0, sticky="w", pady=6)
		name_entry = ttk.Entry(input_card, textvariable=self.name_var, width=30, font=("Segoe UI", 10))
		name_entry.grid(row=1, column=1, sticky="ew", pady=6)

		for row, (subject, mark_var) in enumerate(zip(SUBJECTS, self.mark_vars), start=2):
			ttk.Label(input_card, text=f"{subject} mark", style="Field.TLabel").grid(row=row, column=0, sticky="w", pady=6)
			entry = ttk.Entry(input_card, textvariable=mark_var, width=12, font=("Segoe UI", 10))
			entry.grid(row=row, column=1, sticky="e", pady=6)
			entry.bind("<Return>", lambda _event: self.calculate())

		input_card.columnconfigure(1, weight=1)
		name_entry.focus_set()

		button_row = ttk.Frame(main)
		button_row.pack(fill="x", pady=18)
		ttk.Button(button_row, text="Calculate result", style="Primary.TButton", command=self.calculate).pack(side="left")
		ttk.Button(button_row, text="Reset", style="Secondary.TButton", command=self.reset).pack(side="right")

		result_card = ttk.Frame(main, style="Card.TFrame", padding=24)
		result_card.pack(fill="x")
		ttk.Label(result_card, text="Result summary", style="CardTitle.TLabel").grid(row=0, column=0, columnspan=3, sticky="w", pady=(0, 20))
		for column, (label, variable) in enumerate((("TOTAL MARKS", self.total_var), ("PERCENTAGE", self.percentage_var), ("GRADE", self.grade_var))):
			ttk.Label(result_card, text=label, style="ResultLabel.TLabel").grid(row=1, column=column, sticky="w")
			ttk.Label(result_card, textvariable=variable, style="ResultValue.TLabel").grid(row=2, column=column, sticky="w", pady=(4, 0))
		result_card.columnconfigure(0, weight=1)
		result_card.columnconfigure(1, weight=1)
		result_card.columnconfigure(2, weight=1)

		ttk.Label(main, textvariable=self.status_var, style="Subtitle.TLabel", wraplength=480).pack(anchor="w", pady=(18, 0))

	def calculate(self):
		marks = []
		for subject, mark_var in zip(SUBJECTS, self.mark_vars):
			try:
				mark = float(mark_var.get().strip())
			except ValueError:
				messagebox.showerror("Invalid mark", f"Enter a number for {subject}.")
				return
			if not 0 <= mark <= MAX_MARKS_PER_SUBJECT:
				messagebox.showerror("Invalid mark", f"{subject} must be between 0 and 100.")
				return
			marks.append(mark)

		total = sum(marks)
		percentage = total / len(SUBJECTS)
		self.total_var.set(f"{total:g} / {len(SUBJECTS) * MAX_MARKS_PER_SUBJECT}")
		self.percentage_var.set(f"{percentage:.1f}%")
		self.grade_var.set(self._get_grade(percentage))
		student_name = self.name_var.get().strip() or "Student"
		self.status_var.set(f"Result calculated for {student_name}.")

	def reset(self):
		self.name_var.set("")
		for mark_var in self.mark_vars:
			mark_var.set("")
		self.total_var.set("-- / 500")
		self.percentage_var.set("--%")
		self.grade_var.set("--")
		self.status_var.set("Enter marks for all five subjects to see the result.")

	@staticmethod
	def _get_grade(percentage):
		if percentage >= 90:
			return "A+"
		if percentage >= 80:
			return "A"
		if percentage >= 70:
			return "B"
		if percentage >= 60:
			return "C"
		if percentage >= 50:
			return "D"
		return "F"


if __name__ == "__main__":
	root = tk.Tk()
	GradingApp(root)
	root.mainloop()
