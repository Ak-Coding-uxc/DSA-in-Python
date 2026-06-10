# BUBBLE SORT

# Sorting 
arranging elements(names  , numbers) in incresing or decreasing order.
also called sort in short.

BUBBLE SORT
- compare consocative 2 elements. 
- increasing order a =< b( if repeated elements allowed)
- used iteration( round of loop.)..

for ex:- subah se raat tak joh kiya wo ek iteration hain.
iteration is repeation.

first time called first iteration and so on
loop is used for iteration.

# MAIN LOGIC
compare 2 consecutive elements ( smaller in start.)
and swap them.<br>
for ex:- 51 , 23 , 40 , 3 ( compare 51 and 23)  
=> 23, 51, 40, 3

# Swap in python
a = 64 , b = 32  
code => a , b = b ,a  
now a = 32 and b = 64  

another method is using temp variable  
temp = a  
a = b   
b = temp  
for ex:- a = 64 , b= 32 , temp  
temp = 64 , a = 32 , b = 64  

i = 0  
i++  


### IDHER BAS ITNA HO RAHA H KI JOH BADA ELEMENT H ex:- 64 then send 64 in backward , means usko backward push karte jao



# Performing  
5(total element)  ,  n = 6
i bas n-1 tak hi jayega uske aage nhi jayega  
have 2 loop ( internal and external loop)  
first time loop => i = 0 and n -1 tak hi jayega  ( 6 - 1  = 5)
second time => i = 0 and n - 2 tak  

check current element if i = 0 then compare i = 0 is bigger than i = 1 or not if yes then swap them.

code is hardcoded joh logic ban gya so ban gya ab change nhi ho sakta if you don't want to change the logic.



