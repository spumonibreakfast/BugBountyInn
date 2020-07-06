# File: GeneralExterminator.py
# Non-Destructive. It will write changes to another location not what is loaded in memory.

def main():

    path_read = str(input("What file do you wish to rectify and where do I find it? "))
    omitPattern = str(input("What do you want me to remove? "))
    path_write = str(input("Where do you want me to leave my work? (Type * for the same location) "))
    separator = path_read.find('/')
    if separator != -1:
        separator = '/'
    else:
        separator = '\\'
    infile = open(path_read, 'r')
    temp_omitPattern = omitPattern
    length_pattern = len(temp_omitPattern)
    temp_path = path_read.split(separator)
    if (temp_omitPattern[0] == '/'):
        if (length_pattern > 1):
            temp_omitPattern = 'fwdslash' + temp_omitPattern[1:]
        else:
            temp_omitPattern = "fwdslash"
    filename = 'no' + temp_omitPattern + '_' + temp_path.pop()
    if path_write == '*' or path_write == '**':
        temp_path.append(filename)
        path_write = (separator).join(temp_path)
    else:
        path_write = path_write + filename
    outfile = open(path_write, 'w')
    for line in infile.readlines():
        newstring = line.split(omitPattern)
        newstring = ''.join(newstring)
        print(newstring, file=outfile, end='')
        #if line.startswith(omitPattern):
            #print(line.lstrip(omitPattern), file=outfile, end='')
        #elif line.endswith(omitPattern):
            #print("line ends with " + omitPattern)
            #print(line.rstrip(omitPattern), file=outfile, end='')
        #else:
            #print(line, file=outfile, end='')
    print("\n~)\DONE/(~ The file I created starts with 'no" + temp_omitPattern + "_' because that is what I do! ~)\DONE/(~")
    infile.close()
    outfile.close()


main()
