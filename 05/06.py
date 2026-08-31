text = "My name is {}. I am {} years old. {} is a software developer. {} loves coding."
text_2 = "My name is {0}. I am {1} years old. {0} is a software developer. {0} loves coding."
text_3 = "My name is {name}. I am {age} years old. {name} is a software developer. {name} loves coding."

name = "John"
age = 30

print(text)
print(text.format(name, name, age, "Liza", "Bob"))
print(text_2.format(name, age))
print(text_3.format(age=age, name="Bob"))
