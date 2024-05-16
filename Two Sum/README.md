Use Hashmap to check for difference value. The hash map will add index of last occurence of a num. Do not use the same element twice. 
Start with an empty hash map. 
Calculate the difference between the target and the value at index 0. Example 9-2 = 7
Is the value(7) already in the map? No. 
Add the k, v into the map. Then move to the next index. 
Perform the subtraction again. 9-7 = 2
Is the value(2) in the hash map? Yes. 
Then return the indices. 

array nums = nums = [2,7,11,15]
target = 9