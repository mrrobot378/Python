a = 5 #var is integer
a = "Hello" #now var is str
a = b = "Both" #assign same value to both vars
a = b = float(5) #change type of vars
print (a, b) #to print both vars in same time

text = "amazing"
print(text[0]) #to print specif part of str (based on index)
print(text[0:5]) #to print a collection of characters based on index
for x in "amazing": #to print str with a loop for
    print(x)

text_2 = "the cow is beautiful"
if ("cow" in text_2): #to verify if a word is in text
    print ("The word cow is present in text!")    