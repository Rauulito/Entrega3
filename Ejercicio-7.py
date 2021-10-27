print("Año dado:")
year = int(input())

def is_leap(year):
    leap = False
# Write your logic here
    if(year % 4 == 0): #Condicion para que sea bisiesto
        leap= True
    return leap
print(is_leap(year))