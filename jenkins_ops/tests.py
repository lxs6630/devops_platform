import os
dir_list=[]
def visit(arg, dirname, names):
    for filespath in names:
        s=(os.path.join(dirname,filespath))
        dir_list.append(s)
os.path.walk('/root/2', visit, ())
for i in dir_list:
    try:
        os.removedirs(i)
        print(i)
    except:
        pass
# for i in dir_list:
#     if os.path.isdir(i):


#         if not os.listdir(i):
#             os.rmdir(i)
