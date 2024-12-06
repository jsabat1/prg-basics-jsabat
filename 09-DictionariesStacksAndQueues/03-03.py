##MIGHT BE ON THE TEST
##COMPLETE THE CODE AT HOME


import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct
parentheses = ['(',')','[',']','{','}']
q=queue.LifoQueue()
def brackets_ok(expression):
   for i in expression:
        if i in parentheses:
             q.put(i)
    if q.qsize()%2!=0:
        return False
   
   return #True if brackets in expression are ok of False otherwise

if brackets_ok(expression1):
   print(...)
else

if brackets_ok(expression2):
