from  add_codingCase import addApi
def generate_case1():
    list1=input().split()
    str2=input()
    for str in list1:
        print(str,str2)
        title=str+" "+str2
        add_api=addApi(title)

if __name__ == '__main__':
    generate_case1()