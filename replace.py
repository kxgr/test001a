def write_file(name):
    fo = open('test001.txt', 'w')
    fo.write(name)
    fo.close()


def read_file():
    fo = open('test03.txt', 'r')
    text = fo.read()
    cleantext = text.replace('  ', '')
    cleantext1 = cleantext.replace(' ','')
    cleantext2= cleantext1.replace(':', '')
    #cleantext3 = cleantext2.replace(' ', '')
    cleantext4 = cleantext2.replace('"', '')
    append_file(cleantext4)
    fo.close()



def append_file(name):
    fo = open('test04.txt', 'a')
    fo.write(name)
    fo.write("\n")
    fo.close()



def main():
    #name = input("pes kati: ")
    #write_file(name)
    #append_file(name)
    read_file()

if __name__ == '__main__':
    main()
