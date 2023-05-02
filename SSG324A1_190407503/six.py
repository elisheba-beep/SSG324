percentage = int(input("What is your percentage?:"))
if percentage > 90:
    print("grade: A")
elif percentage > 80 and percentage <= 90:
    print("grade: B")
elif percentage >= 60 and percentage <= 80:
    print("grade: C")
elif percentage < 60:
    print("grade: D")