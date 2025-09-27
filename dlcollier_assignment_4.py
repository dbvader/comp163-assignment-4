# step 1 setup
student_name = "Dwaun Collier"
current_gpa = 3.7
study_hours = 12
social_points = 40
stress_level = 100

print(f"\n[BOOTING...] WELCOME {student_name} ... INITIALIZING STUDENT PROFILE...")
print(f"CURRENT GPA: {current_gpa}")
print(f"STUDY HOURS: {study_hours}")
print(f"SOCIAL POINTS: {social_points}")
print(f"STRESS LEVEL: {stress_level}\n")

# step 2 - course load
print("SELECT COURSE LOAD:")
print("A) LIGHT (12 credits)")
print("B) STANDARD (15 credits)")
print("C) HEAVY (18 credits)")

choice = input("INPUT CHOICE: ")

if choice == "A":
    study_hours = study_hours - 2
    stress_level = stress_level - 10
elif choice == "B":
    study_hours = study_hours + 2
    stress_level = stress_level - 5
elif choice == "C":
    if current_gpa >= 3.5:
        study_hours = study_hours + 5
        stress_level = stress_level + 10
    else:
        study_hours = study_hours + 3
        stress_level = stress_level + 20
        current_gpa = current_gpa - 0.3
else:
    print("INVALID SELECTION. PARAMETERS UNCHANGED.")
