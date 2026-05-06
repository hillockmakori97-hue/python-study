my_dict={
    "name":"Hillock Makori",
    "Gender":"Male",
    "age":"17",
    "city":"Nairobi"
}
print(my_dict)
print(type(my_dict))
#in accessing values in a dictionsry we use keys 
print(my_dict["age"])
print(my_dict["city"])
#Updating nd adding
my_dict["Residency"]="Rongai"
my_dict["Residency"]="Total"
print(my_dict)
#Dictionary Methods
my_dict.pop("age")
my_dict["postal code"]=153165
print(my_dict)
# my dict.pop item 
my_dict.popitem()
print(my_dict)
