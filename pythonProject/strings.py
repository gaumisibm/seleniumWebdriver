nam= "Gaurav Mishra"
#Print only gaurav
print(nam[0:6])
st= "Listen If you really want to do somethings in your life you have to push yourself a bit more"
#using split() function you can really do this
res=st.split() #Let say if you have to split on the basis of dot(.) char then syntax goes st.split(".")
print(res)
print(str(res))
str1=""
for a in res:
    str1=str1+a+" "

print(str1)

#finding if a string is present inside another
str2="Gaurav"
str3="Gau"
str4="Gar"

print(str3 in str2) # true
print(str4 in str2) #false


#Removing whitespaces for the string
str5="Look "
str.strip(" ")
print(str5)
