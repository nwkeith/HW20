# HW 20 CE 232
# Nathan Keith
# Task 1
class Stack():
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return self.items == []
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def get_stack(self):
        return self.items

def divtwo(dec_num):
    s=Stack()
    binStr=""
    while dec_num!=0:
        remainder=dec_num%2
        dec_num=dec_num//2
        s.push(remainder)
    while(not s.is_empty()):
        binStr+=str(s.pop())
    return binStr
print(divtwo(125))

def reverse(forward):
    s=Stack()
    finalString=""
    for index in range(len(forward)):
        s.push(forward[index])
    while(not s.is_empty()):
        finalString+=s.pop()
    return finalString
print(reverse("Sparky"))
# I didn't look at the examples for these, but maybe I just have a photographic memory

def paren_check(parString):
    if parString=="":
        return False
    s=Stack();
    for x in range(len(parString)//2):
        if parString[x] in ['[','(','{']:
            s.push(parString[x])
        else:
            return False
    if s.is_empty():
        return False
    index2=len(parString)//2
    while index2<len(parString):
        if s.is_empty(): # Added for "())"
            return False # If the size of the right portion exceeds the size of the left portion then it is not symmetrical.
        left=s.pop()
        if parString[index2]=="]" and left=='[':
            index2+=1
        elif parString[index2]=="}" and left=='{':
            index2+=1
        elif parString[index2]==")" and left=='(':
            index2+=1
        else:
            return False
    return True
print(paren_check("{{{}}}"))
print(paren_check("{[()]}"))    
print(paren_check("{[()])"))
print(paren_check(""))
print(paren_check("((")) # Mine seems to work here. Lucky me.
print(paren_check("())")) # Should be fixed now
print(paren_check("))"))
print(paren_check("((()"))

