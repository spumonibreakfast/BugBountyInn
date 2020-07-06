# File: FUZZ_endinserter.py
# Non-Destructive. It will write changes to another location not what is loaded in memory.

def main():

    path_read = str(input("What file do you wish me to read and where do I find it? "))
    path_write = str(input("Where do you want me to leave my work? (Type * for the same location) "))
    separator = path_read.find('/')
    if separator != -1:
        separator = '/'
    else:
        separator = '\\'
    infile = open(path_read, 'r')
    temp_path = path_read.split(separator)
    filename = 'FUZZready_' + temp_path.pop()
    if path_write == '*' or path_write == '**':
        temp_path.append(filename)
        path_write = separator.join(temp_path)
    else:
        path_write = path_write + filename
    outfile = open(path_write, 'w')
    for line in infile.readlines():
        if not(line.endswith('/FUZZ')):
            newstring = line.split('.')
            # delete the \n at the end
            newstring.pop()
            newstring.append('com/FUZZ')
            finalstring = ""
            for item in newstring:
                #put . in between
                finalstring = finalstring + item
                if not(finalstring[-1] == 'Z'):
                    finalstring = finalstring + '.'
            print(finalstring, file=outfile)
        else:
            print(line, file=outfile, end='')
    print("\n~)\DONE/(~ The file I created starts with 'FUZZready_' because that is what I do! ~)\DONE/(~")
    infile.close()
    outfile.close()


main()
