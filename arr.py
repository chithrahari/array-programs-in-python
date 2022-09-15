arr=[1,2,3,4,5,7,6,9,10]
missing_elements=[item for item in range(arr[0],arr[-1]+1) if item not in arr]
print(missing_elements)
