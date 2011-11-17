import os
import sys

def main():
    listfile = []
    i = 0
    filelist = os.listdir('.')
    for files in filelist:
        if '.list' in files:
            listfile.append(files)
            print files
            i += 1
    print "--{0} list files are in this dir--".format(i)
    if i > 0:
        case1 = raw_input('choose list file you want to open: ')
        linelist = []
        j = 0
        f = open(case1,'r')
        for items in f:
            linelist.append(items.strip())
            j += 1
        if j == 0:
            print "--no items are in the list file--"
        f.close()
    if i == 0:
        case1 = raw_input('creat a list file using this name: ')
        j = 0
        linelist = []
    while True:
        if j == 0:
            print "[A]dd [Q]uit [a]: "
            case2 = raw_input()
            if case2 in 'Aa':
                listin = raw_input('Add items:')
                linelist.append(listin)
                j += 1
            elif case2 in 'Qq':
                exit()
        if j >= 1:
            for item in linelist:
                print item
            print '--{0} items are in the list--'.format(j)
            case3 = raw_input('[A]dd [D]elete [S]ave [Q]uit [a]: ')
            if case3 in 'Aa':
                listin = raw_input('Add item:')
                linelist.append(listin)
                j += 1
            if case3 in 'Dd':
                listin = raw_input('Delete item:')
                linelist.remove(listin)
                j -= 1
                if j == 0:
                    print "--no items are in the list--"
            if case3 in 'Ss':
                f = open(case1,'w')
                for item in linelist:
                    f.write(item + '\n')
                f.close()
            if case3 in 'Qq':
                exit()


main()

