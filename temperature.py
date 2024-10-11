#Temperature Calculation
cel=float(input("Enter Celsius: "))
fah=(cel*9/5)+32
print("Celsius: ",cel, "Farenheit" ,fah)
f=float(input("Enter Farenheit: "))
c=(f-32)*5/9
k=c+273.15
print("Fahenhiet: ",f,"Celsius: ",c,"Kelvin: ",k)
kel=float(input("Enter Kelvin: "))
cc=kel-273.15
ff=(cc*9/5)+32
print("Fahrenheit: ",ff,"Celsius: ",cc,"kelvin: ",kel)
