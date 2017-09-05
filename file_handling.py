#### File Handling ####

"""
Open a file which returns a file handle.
Use the handle to perform read or write action.
Close the file handle.
"""

## Open File ##

# syntax
#
# variable_name = open(file_name,  access_mode)

# f = open("file.txt")


## Closing the file

# f = open("file.txt", 'r')
# # perform file operations
# f.close()
#
#
# try:
#     f = open("file.txt", 'r')
#     # perform file operations
# finally:
#     f.close()

# best way is with, it automatically closes

# with open("file.txt", 'r') as f:
#     # perform file operation
#     pass


### Reading

# f = open("file.txt", 'r')
# print f.read(4)    # read the first 4 data
#
# print f.read(4)    # read the next 4 data
# #
# print f.read()     # read in the rest till end of file
# #
# print f.read()
#
# print f.read()  # further reading returns empty sting
#
# print f.tell()
# #
# print f.seek(6)
#
# print f.tell()
#
# print f.read()
#
# for line in f:
#     print line

# print f.readline()
# print f.readline()
# print f.readline()
# print f.readline()
#
# print f.readlines()


#### Writing to file
#
# f = open('file.txt', 'w')
# f.write('and I\'m looking for more')
# f.close()
#
# with open('file.txt', 'w') as f:
#     # first line
#     f.write('my first file\n')
#     # second line
#     f.write('This file\n')
#     # third line
#     f.write('contains three lines\n')
#
# with open('file.txt', 'r') as f:
#     content = f.readlines()
#
# print content
#
# for line in content:
#     print(line)


### Appending
# #
# f = open('file1.txt', 'a')
# f.write('and I\'m looking for more\n')
# f.close()


## Read and write to same file

# fh = open('colours.txt', 'w+')
# fh.write('The colour brown')
#
# # Go to the 12th byte in the file, counting starts with 0
# fh.seek(11)
# print fh.read(5)
# print fh.tell()
# fh.seek(11)
# fh.write('green')
# fh.seek(0)
# content = fh.read()
# print(content)


#### FIle Open Modes ###

# """
# <r>	It opens a file in read-only mode while the file offset stays at the root.
# <rb> It opens a file in (binary + read-only) modes. And the offset remains at the root level.
# <r+> It opens the file in both (read + write) modes while the file offset is again at the root level.
# <rb+> It opens the file in (read + write + binary) modes. The file offset is again at the root level.
# <w>	It allows write level access to a file. If the file already exists, then it ll get overwritten.
# <wb> Use it to open a file for writing in binary format. Same behavior as for write-only mode.
# <w+> It opens a file in both (read + write) modes. Same behavior as for write-only mode.
# <wb+> It opens a file in (read + write + binary) modes. Same behavior as for write-only mode.
# <a>	It opens the file in append mode. The offset goes to the end of the file.
# <ab> It opens a file in (append + binary) modes. Same behavior as for append mode.
# <a+> It opens a file in (append + read) modes. Same behavior as for append mode.
# <ab+> It opens a file in (append + read + binary) modes. Same behavior as for append mode.
# """



# # # Open a file in write and binary mode.
# f = open("file.txt", "wb")
# f.close()
# # Display file name.
# print "File name: ", f.name
# # Display state of the file.
# print "File state: ", f.closed
# # Print the opening mode.
# print "Opening mode: ", f.mode

