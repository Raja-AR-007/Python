#               File Handling

# 'MyData' is file name
# 'r' is read
'''
f = open("MyData", 'r')

# for i in f:
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
'''

# Writing Data to the file which we mentioned in argument
# open() will create file automatically where there is no file that we are gonna open

# 'abc' is file name
# 'w' is write
'''
f1 = open('abc', 'w')

# If i'm deleted this line it also delete in file
f1.write('Hello Raja \n') 
f1.write('How are you')
'''

# 'a' is append
'''
f1 = open("abc", 'a')

# If i'm deleted this line it not delete in file
f1.write('Have good day \n')
f1.write('Wear Mask when you go out from House')
'''

# printing whole data from a file 'MyData'
'''
f = open("MyData", 'r')

for data in f:
    print(data)
'''

# copying one file's all data to another file
'''
f = open("MyData", 'r')
f1 = open('abc', 'w')

for data in f:
    f1.write(data)
'''

# reading image
# 'rb' is read binary
'''
f2 = open('marvel_spider.jpg', 'rb')

for i in f2:
    print(i)
'''

# copying one file's image to another file

f1 = open('marvel_spider.jpg', 'rb')
f2 = open('MyPic.JPG', 'wb')

for i in f1:
    f2.write(i)
