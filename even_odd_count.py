a=int(input("How may numbers?"))
even_count=0
odd_count=0
for i in range(1,a+1):

   num=int(input(f"Enter number {i} : "))

   if num%2==0:


      even_count=even_count+1


   else:
    odd_count=odd_count+1

print("The total odd", odd_count)
print("The total even",even_count)
print("end")

