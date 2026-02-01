import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import tkinter as tk
from tkinter import messagebox

# -----------------------------
# Step 1: Sample Data
# -----------------------------
data = {
    "Student Name": ["Amit", "Sneha", "Rahul", "Pooja", "Karan"],
    "Marks": [78, 85, 67, 90, 74]
}

df = pd.DataFrame(data)

# -----------------------------
# Function to Generate PDF
# -----------------------------
def generate_report():
    average_marks = df["Marks"].mean()
    highest_marks = df["Marks"].max()
    lowest_marks = df["Marks"].min()

    pdf = SimpleDocTemplate("student_report.pdf", pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    # Title
    elements.append(Paragraph("<b>Automated Student Performance Report</b>", styles["Title"]))

    # Summary
    elements.append(Paragraph("This report is automatically generated using Python.", styles["Normal"]))
    elements.append(Paragraph(f"<b>Average Marks:</b> {average_marks:.2f}", styles["Normal"]))
    elements.append(Paragraph(f"<b>Highest Marks:</b> {highest_marks}", styles["Normal"]))
    elements.append(Paragraph(f"<b>Lowest Marks:</b> {lowest_marks}", styles["Normal"]))

    # Table
    table_data = [df.columns.tolist()] + df.values.tolist()
    table = Table(table_data)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightblue),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("ALIGN", (1, 1), (-1, -1), "CENTER"),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
    ]))

    elements.append(Paragraph("<br/><b>Student Marks Table</b>", styles["Heading2"]))
    elements.append(table)

    pdf.build(elements)
    messagebox.showinfo("Success", "PDF report generated successfully!")

# -----------------------------
# GUI Setup
# -----------------------------
root = tk.Tk()
root.title("Automated Report Generator")
root.geometry("400x250")
root.resizable(False, False)

# Heading
heading = tk.Label(root, text="Student Report Generator", font=("Helvetica", 16, "bold"))
heading.pack(pady=10)

# Description
desc = tk.Label(root, text="Click the button below to generate PDF report.", font=("Helvetica", 11))
desc.pack(pady=10)

# Generate Button
generate_btn = tk.Button(root, text="Generate Report", font=("Helvetica", 12, "bold"), bg="green", fg="white", command=generate_report)
generate_btn.pack(pady=20, ipadx=10, ipady=5)

# Quit Button
quit_btn = tk.Button(root, text="Quit", font=("Helvetica", 10), bg="red", fg="white", command=root.destroy)
quit_btn.pack(pady=10, ipadx=10, ipady=5)

# Run GUI
root.mainloop()
