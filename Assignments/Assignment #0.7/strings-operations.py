x1= "dushanbe city"
y1 = x1.capitalize()
print(y1)

x2= "DUSHANBE CITY"
y2 = x2.casefold()
print(y2)

x3 = "dushanbe city"
y3 = x3.center(20)
print(y3)

x4 = "dushanbe city"
y4 = x4.count("city")
print(y4)

x5 = "dushanbe city"
y5 = x5.encode()
print(y5)

x6 = "Hello, welcome to Dushanbe."
y6 = x6.endswith(".")
print(y6)

x7 = "H\te\tl\tl\to"
y7 =  x7.expandtabs(2)
print(y7)

x8 = "Hello"
y8 = x8.isalpha()
print(y8)

x9 = "Hello, welcome to Dushanbe."
y9 = x9.find("welcome")
print(y9)

x10 = "This is for {price:.2f} somoni only"
print(x10.format(price = 50))

x11 = "Hello, welcome to Dushanbe."
y11 = x11.upper()
print(y11)

x12 = "Hello, Welcome To dushanbe."
y12 = x12.swapcase()
print(y12)


x13 = "Hello, Welcome To Dushanbe."
y13 = x13.split()
print(y13)


x14 = "Hello, Welcome To Dushanbe."
y14 = x14.replace("Dushanbe", "Kabul")
print(y14)

x15 = "Kabul"
y15 = x15.strip()
print("I like", y15, "city.")


x16 = "Thank you for the arrival\nWelcome to the Dushanbe"
y16 = x16.splitlines()
print(y16)

x17 = ("John", "Peter", "Vicky")
y17 = "# ".join(x17)
print(y17)


x18 = "Hello John!"
y18 = str.maketrans("John", "Khan")
print(x18.translate(y18))

x19 = "Thank you for the arrival\nWelcome to the Dushanbe"

y19 = x19.title()

print(y19)