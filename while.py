#n#=5
#while n>3:
   # print(n-1)# does this determine how many times your code will run,do we need brackets for our 
    #our expression.
   # print(n-3) #it runs endlessly
   # print(n-8)
name = ''
while name != 'your name':
    #print('Please type your name.')
    name = input("Enter your name")
    print(name)
print('Thank you!')  # it is not printing.
def two_oldest_ages(ages):
    ages.sort()
    p=[]
    p=[ages[-2],max(ages)]
    
    return p
y=two_oldest_ages([6,78])
print(y)


