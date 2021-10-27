# You are provided with a list of names. Write a program to  rearrange them so that persons with the same surname are adjacent. Each item in the list will contain first name, middle name(optional), and surname, separated by space, the last word will be the surname.
#
# Example:
# "input": ["Pratik Thapa", "Hari Kumar Karki", "Shyam Govind Sharma", "Wilson Karki", "Baladev Thapa"]
# "output": ["Pratik Thapa", "Baladev Thapa", "Hari kumar Karki", "Gopal Karki", "Shyam Govind Sharma"]

list = ["Pratik Thapa", "Hari Kumar Karki", "Shyam Govind Sharma", "Wilson Karki", "Baladev Thapa"]
n=(len(list))
name=[]
for i in range(n):
    name.append(list[i].split())

list=[]
for j in sorted(name, key=lambda x: x[-1]):
    list.append(' '.join(j))
print(list)


