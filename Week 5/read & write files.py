# import os

# to check all files in working directory
# cwd = os.getcwd()
# files = os.listdir(cwd)
# print("Files in %r: %s" % (cwd, files))

# use 'r' to read only
# use 'r+' to read and write
# use 'w' to write only
# use 'w+' to write and read
# use 'a' to append only
# use 'a+' to append and read

# to opening file:
# File_object = open(r"File_Name","Access_Mode")

# Open function to open the file "MyFile1.txt"
# (same directory) in append mode and
# file1 = open("MyFile1.txt", "a")

# store its reference in the variable file1
# and "MyFile2.txt.txt" in D:\Text in file2
# file2 = open(r"D:\Text\MyFile2.txt", "w+")

# to close file:
# Opening and Closing a file "MyFile.txt"
# for object name file1.
# file1 = open("MyFile.txt", "a")
# file1.close()

# to write files in 2 ways:
# write():
# File_object.write(str1)
# writelines():
# File_object.writelines(L) for L = [str1, str2, str3]

# to read files in 3 ways:
# read():
# File_object.read([n])

# readline()
# File_object.readline([n])

# readlines()
# File_object.readlines()

# note: ‘\n’ is treated as a special character of two bytes

# Program to show various ways to read and
# write data in a file.
file1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

# \n is placed to indicate EOL (End of Line)
file1.write("Hello \n")
file1.writelines(L)
file1.close()  # close file to change file access modes

file1 = open("myfile.txt", "r+")

print("Output of Read function is ")
print(file1.read())
print()

# seek(n) takes the file handle to the nth
# byte from the beginning.
file1.seek(0)

print("Output of Readline function is ")
print(file1.readline())
print()

file1.seek(0)

# To show difference between read and readline
print("Output of Read(9) function is ")
print(file1.read(9))
print()
file1.seek(0)
print("Output of Readline(9) function is ")
print(file1.readline(9))
file1.seek(0)
# readlines function
print("Output of Readlines function is ")
print(file1.readlines())
print()
file1.close()

# Python program to illustrate
# Append vs write mode
file1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
file1.writelines(L)
file1.close()
# Append-adds at last
file1 = open("myfile.txt", "a")  # append mode
file1.write("Today \n")
file1.close()
file1 = open("myfile.txt", "r")
print("Output of Readlines after appending")
print(file1.readlines())
print()
file1.close()
# Write-Overwrites
file1 = open("myfile.txt", "w")  # write mode
file1.write("Tomorrow \n")
file1.close()
file1 = open("myfile.txt", "r")
print("Output of Readlines after writing")
print(file1.readlines())
print()
file1.close()

# to write a CSV file:
# saving dataframe:
# df.to_csv('data.csv')
# to expand code block:
# Data.csv

# to read a CSV file:
# df = pd.read_csv('data.csv', index_col=0)
# df

# Using pandas to Write and Read Excel Files:
# need to install:
# • xlwt to write to .xls files
# • openpyxl or XlsxWriter to write to .xlsx files
# • xlrd to read Excel files
# can do with: pip install xlwt openpyxl xlsxwriter xlrd

# to write an Excel file:
# df.to_excel('data.xlsx')

# to read an Excel file:
# df = pd.read_excel('data.xlsx', index_col=0)
# df

# JSON Files:

# creating data frame:
# df = pd.DataFrame(data=data).T
# df.to_json('data-columns.json')

# to get different file structure:
# df.to_json('data-index.json', orient='index')
