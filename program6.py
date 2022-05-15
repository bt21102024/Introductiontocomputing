a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
num = a^b
Count_flipped_bit = 0
while (num != 0):
    num = num & (num - 1)
    Count_flipped_bit += 1
print("No. of bits needed to convert a to b:", Count_flipped_bit)