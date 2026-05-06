# Clean up the following variable to give the clean version in lower case. Using inbuilt methods in the str class 
# name = “  JOHn  .“ to “john”
# Slice the below string to get you the resulting sentence:
# sentence_one = “The Dog Breed is German Shepherd” only display “Breed is German”
# sentence_two = “Defeats for the Clinton forces, this was her moment of triumph” only display “Clinton forces”
# Split the below sentence using a semicolon i.e ; And display length of the result. 
# “The lazy dog; ran so fast; it hit the wall.” 
# first_name="  Joh.n"  last_name="   Do,e" Clean up and display Full name i.e John Doe
# Having the string r = '["E","W","C"]' #Manipulate it to display EWC
# Attempt questions in the link below. Whether you get the right answer or not, still read the solution explanation.

name="  JOHn"
name=name.lower()
name=name.strip()
print(name)
sentence_one="The Dog Breed is German Sherpherd"
# sentence_one=sentence_one.index("n")
print(sentence_one[8:24])
sentence_two="Defeats for the Clinton forces, this was her moment of triumph"
i=sentence_two.index("C")
print(i)
j=sentence_two.index("C",16)
print(j)
print(sentence_two[16:30])
sentence_three="The lazy dog;ran so fast;it hit the wall."
sentence_three=sentence_three.split(";")
print(sentence_three)
print(len(sentence_three))
first_name="Joh.n"
last_name="  Do,e"
first_name=first_name.replace(".","")
print(first_name)
last_name=last_name.replace(",","").strip()
print(last_name)
full_name=first_name+" "+last_name
print(full_name)
r='["E","W","C"]'
r=r.replace("[","").replace(",","").replace("]","").replace('"','')
print(r)


