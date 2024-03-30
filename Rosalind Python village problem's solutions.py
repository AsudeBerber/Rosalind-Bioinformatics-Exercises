#!/usr/bin/env python
# coding: utf-8

# In[1]:


import this


# In[9]:


result = ((809*809) + (856*856))
print(result)


# In[ ]:


#another solution = def hypotenuse(a, b):
                        #return a ** 2 + b ** 2
    
#also with math function import math
                        #math.pow(x,2)+math.pow(y,2)


# In[2]:


#Assign list name 
birthdays = ['person1', 'person2', 'person3', 'person4']
print(birthdays[2])


# In[3]:


#change the name in the list 
birthdays[1] = 'person5'
print(birthdays[1])


# In[4]:


print(birthdays)


# In[6]:


print(birthdays[0:2])


# In[7]:


print(birthdays[2:])


# In[9]:


#Finally, Python equips you with the magic ability to slice strings the same way that you slice lists. A string can be considered as a list of characters, each of which having its own index starting from 0. For example, try running the following code:
a = 'asude'
b = 'berber'
c = b[0:1] + a[2:]
print(c)

#cool:)


# In[16]:


#Rosalind String problem
s = "h4WeAKyYR98yh3lPhysLDSd0TYREgllHPw7ZwkAWJlPTmHJbWVwIQwuBxOIVEuTrionyxeC0YRQh46EHqYg8OENKwOnivalispfQa0OuCdbE8QM8sWk1FJI2yd975Eisn8rHxjJGjGSpCgZSMAgpYjNPai6iThh"
a = 62
b = 68 
c = 90
d = 96

print(s[a:b+1] + " " + s[c:d+1])


# In[22]:


#conditions and loops
#provide python to choose between two actions = if or else
a = 52
if a < 50:
    print('the number is less than 50')
else: 
    print('the number is greater than 50')


# In[24]:


if a + b == 4:
    print('printed when a + b equals four')
print('always printed')
#If we leave out an else, then the program continues on.


# In[ ]:


#If you want to repeat an action several times, you can use a while loop. 
greetings = 1
while greetings <= 3:
    print('Hello! ' * greetings)
greetings = greetings + 1


# In[1]:


names = ['Alice', 'Bob', 'Charley']
for name in names:
    print('Hello, ' + name)


# In[7]:


names = ['RIP', 'Matthew']
for name in names:
    print('2023, ' + name)


# In[2]:


n = 10
for i in range(n):
    print(i)


# In[5]:


n = 10
for i in range(n):
    print(range(5, 12))


# In[6]:


n = 8
for asude in range(n):
    print(range(5, 12))


# In[12]:


#Problem solution of conditions and loops 

a = 4443
b = 9234
s = 0
for i in range(a, b+1):
    if i%2 == 1:
        s += i
print(s)


# In[15]:


a = 4443
b = 9234
print(sum(range(a+1, b+1, 2)))


# In[18]:


####
f = open('./Downloads/rosalind_ini4.txt', 'r')


# In[21]:


g = f.read(n)
print(g)   # returns n bytes of data from the file as a string


# In[22]:


h = f.readline(n)
print(h)


# In[23]:


f = open('output.txt', 'w')


# In[24]:


f.write('anything that I want to write')


# In[25]:


file = open('./Downloads/rosalind_ini5.txt')
lines = file.readlines()
i = 0
for line in lines:
    i += 1
    if i % 2 == 0:
        print(line)


# In[ ]:


f = open('input.txt', 'r')
g = open('output.txt', 'w')
for x in f.readlines()[1::2]:
    g.write(x)
g.close()


with open('rosalind_ini5.txt','r') as f:
    print ''.join(f.readlines()[1::2])

