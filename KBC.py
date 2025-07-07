q=[
"2. What data structure uses LIFO (Last In First Out?",

'3. Which keyword is used to define a function in Python? ' ,

'4. What is the full form of CPU?',

'5. What symbol is used for comments in Python?']
a=["stack","def","cpu",'hesh']
no_ques=len(q)
count=0
for question_index in range(no_ques)  :
    ans = (input(f"{q[question_index]},\nAns:"))

    if ans == a[question_index]:
     count=count+10
     print("for this ques u get:",count)
    else:
        print("the ans is wrong ")
        break
print("You will take money ,",count,"taka")







