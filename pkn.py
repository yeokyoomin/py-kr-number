#py-kr-number

#PKN

#how to use "pkn"?

#import pkn
#number = 10000
#result = pkn.convert(number, "won")
#print(result)
#output = 1만0000won

#Do not modify this code unless you know how it works.
#You can modify the code as needed.

#If you need to edit this file, please check this out and do it!

#==========Edit method==========#
#count == ??:
#You can make it by raising that part by 4.
def convert(num, end):
    n_int = int(num)
    n_str = str(n_int)
    list_1 = []
    list_2 = []
    count = 0
    for i in range(len(n_str)):
        list_2.append(n_str[i])
    list_2.reverse()
    r_str = ''.join(list_2)
    if n_str[0] == "0":
        raise Exception("The first number of entered values ​​is zero.")
    for i in range(len(r_str)):
        if count == 4:
            list_1.append("만")
            list_1.append(r_str[i])
            count += 1
        elif count == 8:
            list_1.append("억")
            list_1.append(r_str[i])
            count += 1
        elif count == 12:
            list_1.append("조")
            list_1.append(r_str[i])
            count += 1
        elif count == 16:
            list_1.append("경")
            list_1.append(r_str[i])
            count += 1
        elif count == 20:
            list_1.append("해")
            list_1.append(r_str[i])
            count += 1
        else:
            list_1.append(r_str[i])
            count += 1
    list_1.reverse()
    list_1.append("원")
    return ''.join(list_1)
def help_pkn():
    print("====<help>====")
    print("> convert(numberm, won)")
    print("> help()")
