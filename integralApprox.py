import math
import random
import matplotlib.pyplot as plt
import csv
import pandas as pd

#write Your Function Below:
def f(x):
    return math.pow(x, 1/3)

def set_initial_data(initial_data):
    
    print("Set integration interval [a,b]:")
    a = float(input("Set a: "))
    b = float(input("Set b: "))

    if b < a:
        print("b must be > a !\n")
        return 1
    
    print("Set M (limit [0, M]): ")
    M = float(input("M: "))  
    
    if M <= 0:
        print("M must be > 0!\n")

        return 1
    
    print("Set number of generated points (n): ")
    n = int(input("n: "))

    if n <= 0:
        print("Number of generated points must be > 0!\n")
        return 1

    print("Set number of repeats of algorithm (k): ")
    k = int(input("k: "))

    initial_data.append(a)
    initial_data.append(b)
    initial_data.append(M)
    initial_data.append(n)
    initial_data.append(k)

def gen_n_points(a, b, M, n, out_data, sum_of_approx):
    
    c = 0
    
    for i in range(n):
       
        #gen. Random Point (x, y)
        x = random.uniform(a, b)
        y = random.uniform(0, M)

        #count points under curve 
        if y <= f(x):               
            c += 1       
    
    
    #append approx to array 
    approx = c/n*(b-a)*M
    out_data.append([n,approx])
    sum_of_approx += approx

    return sum_of_approx

def write_to_CSV(out_data, header):
    with open("data.csv", "w", newline = "") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(out_data)

def display_data_on_diagram(average_arr, initial_data):
    
    print("Generating diagram...")
    
    result = pd.read_csv("data.csv")
    plt.scatter(result["n"], result["Approx"], s = 10)

    # array of x that connects with average_arr
    # and displays average results on diagram (x, average[inx])
    x = []
    j = 50
    
    for i in range(100):  #in range has to be adjusted to max set of gen. num  ex. 5000/50 = 100
        x.append(j)
        j += 50   #cause average is computed for n in {50, 100, 150, ... , 5000}
    plt.scatter(x, average_arr, color = "Red", s = 10)


    plt.title("Approximation of Integral [" + str(initial_data[0]) + "," + str(initial_data[1]) + "] of f(x)")
    plt.xlabel("n")
    plt.ylabel("Approx")

    print("✅ Done!\n")
    plt.show()

def compute_data(initial_data, sum_of_approx, average_arr, out_data):

    print("\nComputing data...")
    
    #repeat approx 50 times per given n and compute average
    for n in range(50, 5001, 50):
        for i in range(initial_data[4]):
            sum_of_approx = gen_n_points(initial_data[0], initial_data[1], initial_data[2], n, out_data, sum_of_approx)
        
        average = sum_of_approx / initial_data[4]
        average_arr.append(average)
        sum_of_approx = 0
    
    print("✅ Done!\n")


#------------------------------------------------------------------------------
#Program Start

#arrays for storing results of approx
header = ["n", "Approx"]
out_data = []

average_arr = []

#used for average
sum_of_approx = 0

initial_data = []

set_initial_data(initial_data)
compute_data(initial_data, sum_of_approx, average_arr, out_data)
write_to_CSV(out_data, header)
display_data_on_diagram(average_arr, initial_data)
