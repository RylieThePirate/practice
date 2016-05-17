print "What is your name?"
name = raw_input()
print "Hello " + name + "!"
print "How old are you?"
age = int(raw_input())
print "Wow! In 5 years, you'll be " + str(age + 5) + "!"
print name + " what is your weight?"
weight = int(raw_input())
print "Thanks! Now what is your height?"
height = int(raw_input())
BMI = (weight * 703.0)/height**2
print "Aw shit! Your BMI is " + str(BMI) + "!"

# underweight (BMI less than 18.5)
if BMI < 18.5:
    print "Go eat a damn sandwich!"
# normal weight (BMI between 18.5 & 24.9)
elif BMI >= 18.5 and BMI <= 24.9:
    print "Gooood. Gooooood."
# overweight (BMI between 25.0 & 29.9)
elif BMI >= 25.0 and BMI <= 29.9:
    print "Dang."
# obese (BMI 30.0 and above)
else:
    print "Daaaaaaang."
