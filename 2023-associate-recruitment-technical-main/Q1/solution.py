# Reading input from user
n = int(input())
t_shirts = input().split()
m = int(input())
requests = input().split()

# Creating a dictionary to store the count of each T-shirt size in the shop
t_shirts_count = {}
for size in t_shirts:
    if size in t_shirts_count:
        t_shirts_count[size] += 1
    else:
        t_shirts_count[size] = 1

# Checking if all requests can be fulfilled
for request in requests:
    if request in t_shirts_count and t_shirts_count[request] > 0:
        t_shirts_count[request] -= 1
    else:
        for size in ['L', 'XL', 'XXL', 'XXXL', 'XXXXL', 'XXXXXL']:
            larger_size = '1000' + 'X' * (len(size) - 1) + size
            if larger_size in t_shirts_count and t_shirts_count[larger_size] > 0:
                t_shirts_count[larger_size] -= 1
                break
        else:
            print("No")
            break
else:
    print("Yes")
