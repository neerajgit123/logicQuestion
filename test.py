# n=int(input())
# l=[]
# for i in range(n):
#     e=int(input('enter'))
#     l.append(e)
# m=max(l)
# print(l)
# b=len(l)
# e=[]
# for i in range(0,b):
#     if l[i]==m:
#         continue
#     else :
#         e.append(l[i])
# print(e)
# print(max(e))

    
# l=[]
# for i in range(3):
#     l1=[]
#     name=input()
#     mark=float(input())
#     l1.append(name)
#     l1.append(mark)
#     l.append(l1)
# print(l)

# for i in range(len(l)):
#     print(i)
#     print(l[i][1:2])


# l=[['jkdf', 3.6], ['df', 2.3], ['df', 8.9]]
# print('djfkd')
# print('jkfdjg',l[0][1:2])

# for i in range(len(l)):
#     for j in range(i):
        

# def count_substring(string, sub_string):
#     count = 0
#     for i in range(len(string)):
#         if string[i:].startswith(sub_string):
#             count += 1
#     return count

# s=input()
# a=b=c=d=e=None
# for i in s:
#     if i.isalnum():
#         a=True
#     if i.isalpha():
#         b=True
#     if i.isdigit():
#         c=True
#     if i.islower():
#         d=True
#     if i.isupper():
#         e=True
        
# print(a,b,c,d,e,sep='\n')
        
    
# def checkStr(string, fn):
#         for c in string:
#                 if fn(c):
#                         return True
#         return False

# if __name__ == '__main__':
#         s = input()
#         for fn in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
#                 print(checkStr(s, fn))

# n = int(input())
# ints = input().split()
# t = tuple(int(i) for i in ints)
# print(t)
# print(hash(t))


# Students = dict()
# for i in range(int(input())):
#     m=0
#     line = list(input().split())
#     name= line[0]
#     k=len(line[1:])
#     for i in range(0,len(line[1:])):
#         m+=float(i)
#         marks=m/len(line[1:])
        
#     Students[name] = marks
# print('%.2f' % Students[input()])



# Students = dict()
# for i in range(int(input())):
#     m=0
#     line = list(input().split())
#     name= line[0]
#     k=len(line[1:])
#     for i in range(1,4):
#         m+=float(line[i])
#     mar=m/k  
#     print(mar)
#     Students[name] = mar
# print('%.2f' % Students[input()])





# def solve(s):
#     k=''
#     s1=s.split(' ')
#     l=list(map(lambda i:i.capitalize(),s1))
#     for i in l:
#         k+=i+' '
       
# #     return k
# import textwrap
# '\n'.join(textwrap.wrap(string,maxwidth))




# l=[1,2]
# l1=[3,4]
# for i in l:
#     for j in l1:
#         print(tuple((i,j)))

# import textwrap
# a='asdf 2'.split()
# k=[]
# for i in a[0]:
#     for j in a[0]:
#         if i==j:
#             continue
#         else:
#             k1=i+j
            
#             k.append(k1)
            
           

# k.sort()
# s=''
# for i in k:
#     s+=i
#     print(s)
#     s=''
        

# from itertools import permutations
# print( sorted(list(permutations(['1','2','3']))))


from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print(i)