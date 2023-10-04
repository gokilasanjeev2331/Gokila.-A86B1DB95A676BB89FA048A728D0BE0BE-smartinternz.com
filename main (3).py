#1. 1 Implement a recursive factorial to calculate the factorial of given number 

def fact_rect(n):
  if ￼n==0 or ￼n==1:
    return 1
  else:
     return n*fact_rect(n-1)

number =2
res = fact_rec(number)

print("The Factorial of {} is{} ", format(number ))
  