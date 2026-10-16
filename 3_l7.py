employees = { 'E01': { 'name': 'Ali', 'age': 28 ,'salary': 3000 }, 
              'E02': { 'name': 'Sara', 'age': 32, 'salary': 4500}, 
              'E03':{ 'name': 'Reza', 'age': 25, 'salary': 2800 } }
def find_highest_salary(employees) :
    salaries = 0
    highest_name = ''
    for key , value in employees.items():
        salary = value['salary']
        name = value['name']
        if salary > salaries :
            salaries = salary
            highest_name = name
    return highest_name


find_highest_salary(employees) #Sara




#b
def find_lowest_salary(employees) :
    salaries = 4500
    lowest_name = ''
    for key , value in employees.items():
        salary = value['salary']
        name = value['name']
        if salary < salaries :
            salaries = salary
            lowest_name = name
    return lowest_name


find_lowest_salary(employees) #Reza




#c
def find_300_salary(employees) :
    salaries = 3000
    employees_name = []
    for key , value in employees.items():
        salary = value['salary']
        name = value['name']
        if salary >= salaries :
            salaries = salary
            employees_name.append(name)
    return employees_name

find_300_salary(employees) #['Ali', 'Sara']




#e
def find_salary(employees , number) :
    employees_name = []
    for key , value in employees.items():
        salary = value['salary']
        name = value['name']
        if salary >= number :
            number = salary
            employees_name.append(name)
    return employees_name

find_salary(employees , 3500 ) #['Sara']





#f
def average_salaries(employees):
    total = 0
    for key, value in employees.items():
        total += value['salary']

    return total / len(employees)
    
average_salaries(employees) #3433.3333333333335
    
    
    

#g
sales = ( ('Ali', 'Laptop', 1200),
        ('Sara', 'Phone', 800),
        ('Ali', 'Phone', 800),
        ('Reza', 'Laptop', 1200),
        ('Sara', 'Laptop', 1200),
        ('Ali', 'Mouse', 50) )

def total_purchase(sales):
    people = {}
    for name, product , price in sales:
        if name in people:
            people[name] += price
        else:
            people[name] = price
    return people


total_purchase(sales) #{'Ali': 2050, 'Sara': 2000, 'Reza': 1200}



#h
def count_products(sales):

    products = {}
    for name , product , price in sales : 
        if product in products :
            products[product] += 1
        else :
            products[product] = 1
    return products


count_products(sales) #{'Laptop': 3, 'Phone': 2, 'Mouse': 1}




#i
def total_revenue(sales):
    total = 0
    for name , product , price in sales :
        total += price
    return total


total_revenue(sales) #5250





























