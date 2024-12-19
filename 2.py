lst=[]
def sliding_window(elements,window_size):
    if len(elements)<=window_size:
        return elements
    for i in range(len(elements)):
        print(elements[i:i+window_size])
n=int(input("enter no of elements"))
print("enter th elements")
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
print(lst)
m=int(input("enter the window size"))
print("enetr the slidind protocol output")
sliding_window(lst,m)