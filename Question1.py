# Write a program which takes array of integers, keep a total score based on the following:
# Add 1 point for every even number in the array
# Add 3 points for every odd number in the array, expect for the number "5"
# Add 5 points every time the number "5" appears in the array
# Note that 0 is considered even.
#
# Example:
# Input [1,2,3,4,5]
# Output: 13
#
# Input: [17, 19, 21]
# Output: 9


import array
Input=array.array('i',[])
n=int(input("Enter How many number you want:"))
for i in range(n):
    Input.append(int(input("Enter a Number:")))

print(Input)
sum=0
sum2=0
for j in Input:
    if j%2==0:
        sum=sum+1


for k in Input:
    if (k % 2 != 0) and (k != 5):
        sum=sum+3


for j in Input:
    if j==5:
        sum=sum+5
print(sum)


