import sys

with open("sample_input.txt", "r") as f:
    data = f.read().split("\n")

num_emp = int(data[0].split()[-1])

prod_data = []
for ele in data[4:]:
    prod_data.append(tuple(ele.split(": "))) #takes prices and splits it from the goodies

if num_emp==0 or len(prod_data)==0:
    print("Sorry")
    exit(0)

prod_data.sort(key= lambda x: int(x[1]))
if (num_emp > len(prod_data)):
    print("Sorry")
    exit(0)

min_diff = sys.maxsize

i=0

while(i+num_emp-1<len(prod_data)): #compares the prices of the goodies from i to number of employees
	
    diff = int(prod_data[i+num_emp-1][1]) - int(prod_data[i][1]) # if the difference is less then it takes into consideration if not it leaves same
    if (diff < min_diff):
        min_diff = diff #assigns the minimum difference
		
    i+=1



start, end = None, None
for x in range(len(prod_data)):
    for y in range(len(prod_data)):
        if abs(int(prod_data[x][1])-int(prod_data[y][1]))==min_diff:
            start = min(x,y)
            end = max(x,y)
with open("sample_output.txt", "w") as file: #opens the sample_output file and writes the output
    exact = prod_data[start: end + 1]
    file.write('Number of employees: '+str(num_emp)+"\n\n")
    file.write('Here the goodies that are selected for distribution are:\n\n')
    for x,y in exact:
        file.write(x+": "+y+"\n")
    file.write("\nAnd the difference between the chosen goodie with highest price and the lowest price is "+str(min_diff))
