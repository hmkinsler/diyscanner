points = int(input("How many points [0-100]: "))

if points > 100:
    grade = "impossible!"
elif 100 >= points >= 90:
   grade = "5"
elif 90 > points >= 80:
    grade = "4"
elif 80 > points >= 70:
    grade = "3"
elif 70 > points >= 60:
    grade = "2"
elif 60 > points >= 50:
   grade = "1"
elif 50 > points >= 0:
   grade = "fail"
else:
   grade = "impossible!"

print(f"""Grade: {grade}""")