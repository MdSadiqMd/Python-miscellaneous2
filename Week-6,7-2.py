s=input()
sub1,sub2=map(str(input()).split(" "))
if sub1 in s and sub2 in s:
    result=s[s.index(sub1)+len(sub1)+1:s.index(sub2)]
    print(result)
else:

    print("substrings are not present in the main string")
