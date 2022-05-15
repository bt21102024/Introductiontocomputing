side_a = int(input("Enter the length of 1st side:" , ))
side_b = int(input("Enter the length of 2nd side:" , ))
side_c = int(input("Enter length of 3rd side:" , ))
if side_a < side_b + side_c and side_b < side_a + side_c and side_c < side_b + side_a:
    print("yes")
else:
    print("no")
         