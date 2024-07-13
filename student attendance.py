classes_held = int(input("enter number of classes held: "))
classes_attended = int(input("enter number of classes attented: "))
attendance_percentage = (classes_attended/ classes_held)* 100
is_allowed = attendance_percentage >= 75

print(f"attendance percentage: {attendance_percentage}%")
print("allowed to sit in exam:", "yes"if is_allowed else "no")

