x = ["Asia", "Europe", "Australia"]
y= [ "America", "Africa", "Antractica"]

x.append("Canada")
print(x)

x = ["Asia", "Europe", "Australia"]
y1= [ "America", "Africa", "Antractica"]

y1.clear()
print(y1)

x1 = ["Asia", "Europe", "Australia"]
y= [ "America", "Africa", "Antractica"]

x2 = x1.copy()
print(x2)

x3 = ["Asia", "Europe", "Australia"]
y3 = [ "America", "Africa", "Antractica"]
y4 = x3.count("Asia")
print(y4)

x5 = ["Asia", "Europe", "Australia"]
y5 = [ "America", "Africa", "Antractica"]

x5.extend(y5)
print(x5)

x6 = ["Asia", "Europe", "Australia"]
y6 = [ "America", "Africa", "Antractica"]

x6= x6.index("Australia")
print(x6)

x7 = ["Asia", "Europe", "Australia"]
y7 = [ "America", "Africa", "Antractica"]

x7.insert(-4,"Mexico")
print(x7)

x8 = ["Asia", "Europe", "Australia"]
y8 = [ "America", "Africa", "Antractica"]

x8.pop(2)
y8.pop(2)

print(y8)
print(x8)


x9 = ["Asia", "Europe", "Australia"]
y9 = [ "America", "Africa", "Antractica"]

y9.remove("America")
print(y9)

y10 = [ "America", "Africa", "Antractica"]
y10.reverse()
print(y10)

y10.sort()
print(y10)