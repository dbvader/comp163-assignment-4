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

# step 3 - study strategy
study_options = ["Programming", "Math", "English", "History"]
print(f"\nAVAILABLE STUDY MODULES: {study_options}")

subj = input("INPUT MODULE: ")

if subj in study_options:
    # ai helped me figure out this with logic in,and,or
    if subj == "Programming" and stress_level > 80:
        current_gpa = current_gpa - 0.1
    elif subj == "Math" or subj == "English":
        current_gpa = current_gpa + 0.1
        social_points = social_points - 5
    elif subj == "History" and (study_hours > 10 and stress_level < 70):
        social_points = social_points + 10
elif subj not in study_options:
    print("ERROR: INVALID MODULE SELECTED. GPA -0.1")
    current_gpa = current_gpa - 0.1

# step 4 - semester wrap up
print("\n>>> FINAL SEMESTER ASSESSMENT <<<")

if type(current_gpa) is not float:
    print("ERROR: GPA NOT FLOAT TYPE. SYSTEM MALFUNCTION.")
else:
    print("SYSTEM CHECK: GPA STORED AS FLOAT... OK.")

if current_gpa >= 3.5:
    if stress_level < 70:
        ending = "YOU HAVE MADE THE DEAN'S LIST. STATUS: ELITE STUDENT MODE."
    else:
        ending = "YOU HAVE MAINTAINED GPA > 3.5 BUT SYSTEM REPORTS: BURNOUT DETECTED."
elif current_gpa >= 2.0:
    if social_points > 50:
        ending = "YOU HAVE SURVIVED THE SEMESTER WITH BALANCE. GPA: AVERAGE. SOCIAL LIFE: ONLINE."
    else:
        ending = "YOU HAVE PASSED. HOWEVER, SOCIAL INTERACTIONS: MINIMAL. RESULT: MEDIOCRE PATHWAY."
else:
    ending = "YOU HAVE ACHIEVED ACADEMIC PROBATION. SYSTEM FLAG: CRITICAL FAILURE."

print("\n--- FINAL STUDENT STATS ---")
print(f"GPA: {current_gpa}")
print(f"HOURS: {study_hours}")
print(f"SOCIAL: {social_points}")
print(f"STRESS: {stress_level}")
print(f"OUTCOME: {ending}")
