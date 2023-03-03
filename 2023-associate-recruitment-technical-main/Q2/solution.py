n = int(input())  # read the total number of records

allValid = True
errorCodes = []

for i in range(n):
    record = input().split()  # read the record and split it into id, isValid, and errorMessage
    
    if record[1] == 'false':  # check if the item is valid
        allValid = False
        errorCodes.append(record[2])  # add the error message to the list

if allValid:
    print("Yes")
else:
    print("No")
    print(' '.join(errorCodes))  # print all error messages separated by space character
