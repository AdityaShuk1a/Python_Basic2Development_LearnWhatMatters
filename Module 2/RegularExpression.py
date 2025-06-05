import re

'''
re.search
re.findall
re.sub

'''

'''
\d
\w
+
.
*
{}
'''

text = "Aditya - 9324893423, Rahul - 8787878787, Rohit - 232323" #Indian number ka format

pattern = r'\d{10}'

match = re.findall(pattern, text)
print(match)

text2 = " Sam -  (999)-3434-2323, Samuel -  (990)-3124-2333" #American Number ka format

pattern2  = r'\(\d{3}\)\-\d{4}\-\d{4}'

match2 = re.findall(pattern2, text2)
print(match2)

text3 = "mujhe dhundhna hai ki mera paisa kidhar ha"

pattern3 = r'PAISA'

match3 = re.search(pattern3, text3, flags = re.IGNORECASE )

print(match3)


text4 = "aditya shukla email is - aditya123@gmail.com"
text5 = "aditya shukla email is - aditya123@gmail.in"

pattern4 = r'\w+\@\w+\.\w{2,3}' #\w [a-zA-z0-9]

match4 = re.search(pattern4, text5)
print(match4)

text6 = "a&b afb a.b ajb agdb"

pattern6 = r'a\.b'

match6 = re.findall(pattern6, text6)

print(match6)

text7 = "I love riya"

pattern7 = r'riya'

substitute  = re.sub(pattern7, "priya", text7 )

print(substitute)


text8 = "hi      my    name is    aditya"

substitute2 = re.sub(r'\s+', " ", text8)

print(substitute2)

text9 = "cyclone is destroying every city. dyclone Dyclone Syclone is destroying every city."
pattern9 = r'[a-zA-Z]yclone'

match9 = re.findall(pattern9, text9)

print(match9)