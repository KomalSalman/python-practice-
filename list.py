fruits=["mango","peach","pineapple","pear"]
number=[1,2,5,10,6,8]
mix=["cup",9,"bag","horse"]

#print(fruits)
#print(number.index(1))
#print(type(number))

first=number[3] #its a positive index
#print(first)

last=number[-3] #its a negitive index
#print(last)

middle=fruits[2:5] #its a multiple access  and 5 in the last is called exclusive
#print(middle)

pin=mix[::3] #it can jump on 1st to any num you wrote
#print(pin)

fruits.append("cherry") #in append it appear on end 
#print(fruits)
       
mix.insert(0,"dog")  #in insert it can appear on specific location
#print(mix)

max=mix+number #it can cancatenate means it add two brack
print(max)

newlist=sorted(number) #it sort the num in line
print(newlist)



