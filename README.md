# NumPy Data Explorer

This project was developed as part of an internship at **Syntecxhub**.  
It demonstrates basic **data exploration and analysis using Python, NumPy, and Matplotlib**.

## Project Overview

This project reads employee productivity data from a text file and performs analysis on it using NumPy.

Each line in `company.txt` represents one company or branch, and each number in that line represents the monthly productivity of an employee.

The program:

- reads data from `company.txt`
- converts it into NumPy arrays
- displays the productivity data of the first company
- calculates salary based on products made
- shows a graph of employee productivity
- finds the most productive company
- finds the least productive company
- calculates average productivity for each company
- calculates overall average productivity for all employees

## Features

- Load numerical data using NumPy
- Perform basic array operations
- Statistical analysis using:
  - mean
  - sum
  - min
  - max
- Data exploration using NumPy functions
- Employee salary calculation
- Productivity graph using Matplotlib

## Technologies Used

- Python
- NumPy
- Matplotlib

## Project Files

### `main.py`
This is the main file of the project.

It:
- reads the data from `company.txt`
- stores the data in NumPy arrays
- calls analysis functions
- creates an object of the `IntArray` class
- prints productivity results

### `operationclass.py`
This file contains the `IntArray` class.

It is responsible for:
- storing integer array data
- displaying the array
- calculating salary
- plotting productivity graph
- returning total, average, maximum, and minimum values

### `company.txt`
This file contains the raw productivity data.

Example:
```txt
52,43,56,47,58,41,50,44,59,45
43,50,38,54,46,36,52,42,51,37,49,40
```

## How the Code Works

### 1. File Handling
The program opens `company.txt`, reads each line, splits values using commas, converts them into integers, and stores them in NumPy arrays.

### 2. Productivity Analysis
Using NumPy functions like `sum()` and `mean()`, the program calculates:
- total productivity of each company
- best company
- worst company
- average productivity per company
- overall average productivity

### 3. Salary Calculation
The first company’s employee productivity is used to calculate salary.  
The default salary rate is **7 per product**.

### 4. Data Visualization
The project uses Matplotlib to create a line graph of employee productivity for the first company.

## Sample Functionalities

- `display()` → shows employee productivity array
- `salary()` → calculates salaries
- `show_data()` → plots productivity graph
- `total_products()` → total products by a company
- `average_products()` → average products
- `max_products()` → maximum products
- `min_products()` → minimum products

## Learning Outcome

This project helps in understanding:

- Python basics
- file handling
- object-oriented programming
- NumPy arrays
- statistical analysis
- basic data visualization using Matplotlib

## Conclusion

This is a simple but useful mini project for learning how to work with numerical datasets in Python.  
It shows how NumPy can be used for fast calculations and how Matplotlib can be used for visualization.
""operationclass.py explanation
1
import numpy as np

Ye NumPy library import kar raha hai.
NumPy arrays, sum, mean, max, min jaise numerical operations ke liye use hota hai.

2
import matplotlib.pyplot as plt

Ye graph banane ke liye use hota hai.
plt ke through plot, title, label, grid, show sab karte hain.

3
class IntArray:

Yahan ek class ban rahi hai jiska naam IntArray hai.

Class ka kaam:

employee productivity data ko object ke andar rakhna

us data par operations karna

display, salary, graph, total, average wagaira nikalna

Constructor
4
def __init__(self, int_array):

Ye constructor hai.
Jab bhi tum IntArray(data_frame[0]) likhoge tab ye automatically call hoga.

self matlab current object.
int_array matlab jo data tum object me bhej rahe ho.

5
int_array = np.array(int_array)

Input ko NumPy array me convert kar diya.

Reason:

ho sakta hai input list ho

ho sakta hai already NumPy array ho

Dono cases me standard format chahiye, isliye NumPy array bana diya.

6
if not isinstance(int_array, np.ndarray):

Ye check karta hai ki input NumPy array hai ya nahi.

isinstance() type check karne ke liye hota hai.

7
raise ValueError("Input must be a NumPy array")

Agar input valid nahi hua to error throw karega.

ValueError ka matlab value expected format me nahi hai.

8
try:

Ye risky code ko test karne ke liye hota hai.

Yahan hum integer conversion try kar rahe hain.

9
int_array = int_array.astype(int)

Ye array ki sari values ko integer me convert karta hai.

Example:

['1', '2', '3'] -> [1, 2, 3]

[1.0, 2.0] -> [1, 2]

10
except (ValueError, TypeError):

Agar conversion fail ho jaye to ye block chalega.

Example:

'abc' ko int me convert nahi kar sakte

ya invalid object ho

11
raise ValueError("Input must contain only integer values")

Custom clear error message de raha hai.

12
self.int_array = int_array

Final cleaned integer NumPy array object ke andar store kar diya.

Ab object ke saare methods isse use karenge.

display()
13
def display(self):

Ye method array display karne ke liye hai.

14
print("Employee productivity data:")

Heading print kar raha hai.

15
print(self.int_array)

Actual productivity array print ho jayega.

Example:

[52 43 56 47 58 41 50 44 59 45]
salary()
16
def salary(self, rate_per_product=7):

Ye method salary calculate karta hai.

rate_per_product=7 matlab default rate 7 hai.
Agar tum kuch aur dena chaho to दे सकते ho:

first_branch.salary(10)
17
salaries = self.int_array * rate_per_product

Har employee ke products ko per-product rate se multiply karta hai.

Example:

productivity = 52

rate = 7

salary = 364

NumPy vectorized multiplication kar raha hai.

18
print(f"People made {self.int_array} products")

Products print karega.

19
print(f"Rate per product: {rate_per_product}")

Rate print karega.

20
print(f"Salaries: {salaries}")

Final salary array print karega.

21
return salaries

Ye important hai. Sirf print nahi, salary array return bhi karta hai.
Baad me kahin aur use kar sakte ho.

show_data()
22
def show_data(self):

Graph banane wala method.

23
x = np.arange(1, len(self.int_array) + 1)

X-axis ke liye employee numbers ban rahe hain.

Agar 10 employees hain to:

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Pehle code me 0 se start ho raha tha. Ab 1 se start kar diya, zyada natural hai.

24
plt.plot(x, self.int_array, marker='o')

Line graph ban raha hai.

x-axis = employee number

y-axis = products per month

marker='o' se har point circle mark me dikh raha hai

25
plt.title('Productivity of Employees')

Graph ka title.

26
plt.xlabel('Employee Number')

X-axis label.

27
plt.ylabel('Products per Month')

Y-axis label.

28
plt.xticks(x)

X-axis ke ticks wahi numbers honge jo employees ke hain.

29
plt.grid(True)

Graph par grid lines on kar deta hai.

30
plt.show()

Graph window display karega.

Extra utility methods
31
def total_products(self):
    return np.sum(self.int_array)

Total products nikalta hai.

32
def average_products(self):
    return np.mean(self.int_array)

Average products per employee.

33
def max_products(self):
    return np.max(self.int_array)

Sabse zyada products ek employee ne kitne banaye.

34
def min_products(self):
    return np.min(self.int_array)

Sabse kam products ek employee ne kitne banaye.

main.py explanation
1
import numpy as np

NumPy import kiya.

2
from operationclass import IntArray

operationclass.py wali class import ki.

Matlab ab IntArray use kar sakte ho.

3
file_path = 'company.txt'

Data file ka path store kiya.

Program isi file se data uthayega.

productivity_of_company()
4
def productivity_of_company(order, data_frame):

Ye function kisi specific company ka total production nikalega.

order = company index

data_frame = all companies data

5
return np.sum(data_frame[order])

Selected company ke row ka sum return karta hai.

Example:
Company 1 row ka sum = total products of company 1.

max_productivity()
6
def max_productivity(data_frame):

Ye function sabse zyada productive company nikalta hai.

7
best_company = 1

Default best company first company maan li.

8
num_of_products = productivity_of_company(0, data_frame)

First company ke total products ko initial max maan liya.

Ye pehle wale 0 se better hai kyunki agar sab negative ya special case hota to bhi logic stable rehta.

9
for i in range(len(data_frame)):

Har company ke liye loop.

10
result = productivity_of_company(i, data_frame)

Current company ka total production nikala.

11
if result > num_of_products:

Agar current company ka production ab tak ke best se zyada hai to update karo.

12
num_of_products = result

New max set ho gaya.

13
best_company = i + 1

Company number human-friendly 1-based format me store kiya.

14
print(f"The best company is company {best_company} with {num_of_products} products made")

Final best company print ho jayegi.

min_productivity()
15
def min_productivity(data_frame):

Least productive company nikalne ka function.

16
worst_company = 1

Default first company.

17
num_of_products = productivity_of_company(0, data_frame)

Minimum compare karne ke liye first company ka sum starting point banaya.

18
for i in range(len(data_frame)):

Sab companies loop me.

19
result = productivity_of_company(i, data_frame)

Current company ka total.

20
if result < num_of_products:

Agar current company aur kam productive hai, to minimum update karo.

21
num_of_products = result

New minimum save.

22
worst_company = i + 1

Company number update.

23
print(f"The worst company is company {worst_company} with {num_of_products} products made")

Final worst company print.

Pehle code me yahan bug tha: “best company” likha tha. Ab fix kar diya.

mean_products()
24
def mean_products(data_frame):

Har company ka average aur overall average nikalta hai.

25
for i in range(len(data_frame)):

Sab companies ke liye loop.

26
average = np.mean(data_frame[i])

Current company ka average productivity nikalta hai.

27
print(f"On average, one employee from company {i + 1} produced {average:.2f} products")

Average 2 decimal tak print kar raha hai.

.2f ka matlab 2 decimal places.

28
total_sum = 0

Overall total production collect karne ke liye variable.

Pehle sum naam use ho raha tha, jo built-in function ko shadow karta tha. Ab correct variable name use hua.

29
num_elements = 0

Total employees count karne ke liye.

30
for row in data_frame:

Har company row par loop.

31
for element in row:

Har employee production value par loop.

32
total_sum += element

Total production me add kiya.

33
num_elements += 1

Employee count increment kiya.

34
total_mean = total_sum / num_elements

Overall average nikal diya.

35
print(f"Mean productivity of the entire monopoly is {total_mean:.2f} per employee")

Final overall mean print.

file_handling()
36
def file_handling():

File read karke structured data banane ka function.

37
lines = []

Temporary empty list.

38
with open(file_path, 'r') as file:

company.txt file read mode me kholi.

with ka fayda:

kaam khatam hote hi file automatically close ho jati hai

39
for line in file:

File ki har line ko read karo.

40
values = line.strip().split(',')

Line ko clean aur split kiya.

Example:

"52,43,56"

ban gaya:

['52', '43', '56']

strip() newline hata deta hai.

41
int_values = [int(val) for val in values]

List comprehension use karke strings ko integers me convert kiya.

Example:

['52', '43', '56'] -> [52, 43, 56]
42
lines.append(np.array(int_values, dtype=int))

Current row ko NumPy integer array bana ke lines list me add kar diya.

Important:
Har row integer array hai.
Ye pehle wale code se better hai.

43
data_frame = np.array(lines, dtype=object)

Ab sari rows ko ek outer NumPy array me wrap kiya.

dtype=object kyu?
Kyuki har company me employees ki count alag hai.
Unequal-length rows ko normal 2D int array me directly nahi rakh sakte.

44
return data_frame

Final processed data return.

main()
45
def main():

Program ka main controller function.

46
data_frame = file_handling()

File read karke all company data le aaya.

47
print("Complete company data:")

Heading print.

48
print(data_frame)

Poora data print.

49
print()

Blank line for clean output formatting.

50
first_branch = IntArray(data_frame[0])

First company ka data IntArray object ke andar bheja.

Ab is object par methods call kar sakte ho.

51
first_branch.display()

First company ke employee productivity values print.

52
print()

Spacing.

53
first_branch.salary()

First company ke employees ki salary calculate aur print.

54
print()

Spacing.

55
first_branch.show_data()

First company ka graph show karta hai.

56
print(f"Total products of first company: {first_branch.total_products()}")

First company total products print.

57
print(f"Average products of first company: {first_branch.average_products():.2f}")

Average products print with 2 decimals.

58
print(f"Maximum products by one employee in first company: {first_branch.max_products()}")

Sabse zyada productive employee ka count.

59
print(f"Minimum products by one employee in first company: {first_branch.min_products()}")

Sabse kam productive employee ka count.

60
print()

Spacing.

61
max_productivity(data_frame)

Best company nikal ke print karega.

62
min_productivity(data_frame)

Worst company nikal ke print karega.

63
mean_products(data_frame)

Har company aur overall mean productivity print karega.

Entry point
64
if __name__ == "__main__":

Ye check karta hai ki file direct run hui hai ya import hui hai.

Agar direct run hui hai tab hi neeche wala main() chalega.

65
main()

Program start.

""