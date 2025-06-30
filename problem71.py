'''Create a list of two sports. Ask the
user what their favourite sport is and
add this to the end of the list. Sort the
list and display it.'''
sp=['football','cricket']
n_sp=input("what is yout fav sport?")
sp.append(n_sp)
sp.sort()
print(sp)

'''
Create a list of six school subjects. Ask the user which of these
subjects they don’t like. Delete the subject they have chosen from the
list before you display the list again.

'''
sub=['m','e','b','s','h','p']
x=input("which sub u dont like?")
if x in sub:
    sub.remove(x)
print(sub)
