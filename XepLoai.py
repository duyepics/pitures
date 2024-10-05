import tkinter as tk
from tkinter import messagebox, ttk

class GradeCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Grade Calculator")
        
        self.canvas = tk.Canvas(root)
        self.scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        
        self.course_count_label = tk.Label(self.scrollable_frame, text="Enter number of courses:")
        self.course_count_label.pack()
        
        self.course_count_entry = tk.Entry(self.scrollable_frame)
        self.course_count_entry.pack()
        
        self.submit_count_button = tk.Button(self.scrollable_frame, text="Submit", command=self.submit_course_count)
        self.submit_count_button.pack()
        
        self.course_entries = []
        self.course_labels = []
        self.credit_entries = []
        self.grade_entries = []
        
    def submit_course_count(self):
        try:
            self.course_count = int(self.course_count_entry.get())
            self.course_count_label.pack_forget()
            self.course_count_entry.pack_forget()
            self.submit_count_button.pack_forget()
            
            for i in range(self.course_count):
                course_label = tk.Label(self.scrollable_frame, text=f"Course {i+1} name:")
                course_label.pack()
                self.course_labels.append(course_label)
                
                course_entry = tk.Entry(self.scrollable_frame)
                course_entry.pack()
                self.course_entries.append(course_entry)
                
                credit_label = tk.Label(self.scrollable_frame, text=f"Course {i+1} credits:")
                credit_label.pack()
                self.course_labels.append(credit_label)
                
                credit_entry = tk.Entry(self.scrollable_frame)
                credit_entry.pack()
                self.credit_entries.append(credit_entry)
                
                grade_label = tk.Label(self.scrollable_frame, text=f"Course {i+1} point (out of 10):")
                grade_label.pack()
                self.course_labels.append(grade_label)
                
                grade_entry = tk.Entry(self.scrollable_frame)
                grade_entry.pack()
                self.grade_entries.append(grade_entry)
            
            self.calculate_button = tk.Button(self.scrollable_frame, text="Calculate", command=self.calculate_grades)
            self.calculate_button.pack()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
    
    def calculate_grades(self):
        try:
            total_points_10 = 0
            total_points_4 = 0
            total_credits = 0
            grade_scale = {
                "A+": (9, 10, 4.0),
                "A": (8.5, 9, 3.7),
                "B+": (8, 8.5, 3.3),
                "B": (7, 8, 3.0),
                "C+": (6.5, 7, 2.7),
                "C": (5.5, 6.5, 2.0),
                "D+": (5, 5.5, 1.7),
                "D": (4, 5, 1.0),
                "F": (0, 4, 0.0)
            }
            
            results = []
            
            for i in range(self.course_count):
                course_name = self.course_entries[i].get()
                course_credits = float(self.credit_entries[i].get())
                course_grade = float(self.grade_entries[i].get())
                
                total_points_10 += course_grade * course_credits
                total_credits += course_credits
                
                for grade, (min_score, max_score, grade_point) in grade_scale.items():
                    if min_score <= course_grade <= max_score:
                        total_points_4 += grade_point * course_credits
                        results.append((course_name, course_grade, grade_point, grade))
                        break
            
            gpa_10 = total_points_10 / total_credits
            gpa_4 = total_points_4 / total_credits
            
            result_text = f"Overall GPA (out of 10): {gpa_10:.2f}\n"
            result_text += f"Overall GPA (out of 4): {gpa_4:.2f}\n\n"
            result_text += "Course-wise grades:\n"
            for course_name, course_grade, grade_point, grade in results:
                result_text += f"{course_name}: {course_grade:.2f}/10, {grade_point}/4, {grade}\n"
            
            messagebox.showinfo("Results", result_text)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid grades and credits.")
        
root = tk.Tk()
app = GradeCalculator(root)
root.mainloop()
