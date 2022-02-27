
import xlrd
import random
grouppool=[]
total=[]
sgrecord=[]

def import_xl(path):
    data=xlrd.open_workbook(path)
    table=data.sheets()[0]
    data_list=[]
    data_list.extend(table.col_values(0))
    return data_list
def addname(name):
    return name
def parter(name):
    #way1找到所有组合的方式
    # name_two=copy.deepcopy(name)
    # for i in name:
    #     name_two.remove(i)
    #     for j in name_two:
    #        if i is not j:
    #            group=[i,j]
    #            grouppool.append(group)
    #
    # print(grouppool)
    for i in range(0,len(name)):
        for j in range(i+1,len(name)):
            grouppool.append([name[i],name[j]])
    return(grouppool)
def daluan(x,len):
    a = random.sample(x, len)
    return a

def selet_group(grouppool,desknumber):
    k = 0
    sg = [[]]
    for group in grouppool:
        if k <= desknumber*2:
            a=yanzheng(group,sg)
            if a==1:
               sg.append(group)
               k=k+1
    sg.remove([])
    total.append(sg)
    return sg

def yanzheng(group,sg):
    a=1
    for j in sg:
        if group[0] in j or group[1] in j:
            a=0
    return a

def main():
    path="C:/Users/Admin/PycharmProjects/guandan/guandan2/data.xls"
    a=import_xl(path)

    name=addname(a)
    name = daluan(name,len(name))
    grouppool=parter(name)
    desknumber=int(len(name)/4)
    count = 0
    while len(grouppool)>0:
        sg=selet_group(grouppool,desknumber)
        for i in sg:
            grouppool.remove(i)

        count=count+1
    return total
    # print("count=",count)
if __name__ == '__main__':
    total=main()
    print(total)