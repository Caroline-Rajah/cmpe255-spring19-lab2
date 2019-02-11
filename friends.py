def mean_num_friends(x):
    sum=0
    count=0
    for num in x:
        sum+=num
        count+=1
    return sum/count

def median_num_friends(x):
    x.sort()
    length= len(x)
    return x[length//2]

num_friends=[100, 49, 41, 40, 25, 10, 5, 4, 7, 20, 60]
print("mean={}".format(mean_num_friends(num_friends)))

print("median={}".format(median_num_friends(num_friends)))