# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_name = (name1 + name2)
combined_name = combined_name.lower()
t= combined_name.count("t")
r= combined_name.count("r")
u= combined_name.count("u")
e= combined_name.count("e")
true = t + r + u + e 

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")
love = l + o + v + e 
true_love = str(true) +str(love)

if int(true_love )< 10 or int(true_love)>90:
    print(f"Your score is {true_love}, you go together like coke and mentos.")   
elif(int(true_love)>40 and int(true_love)<50):
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}")


