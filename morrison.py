# question 1. String Manipulation
def capitalize_words(sentence):
    words = sentence.split()
    capitalized = [word.capitalize() for word in words]
    return ' '.join(capitalized)
example = "hello world from python"
print(capitalize_words(example))


# question 2: List Methods
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = numbers
double_numbers = [n * 2 for n in numbers]
even_numbers = [n * 2 for n in numbers if n % 2 == 0]
total  = sum(numbers)
print(double_numbers)
print(even_numbers)
print(sum(numbers))


# question 3: Dictionary Unpacking Equivalent
def extract_user_info(user):
    username = user["profile"]["username"]
    email = user["profile"]["email"]
    theme = user["settings"]["theme"]

    print(f"Username: {username}")
    print(f"Email: {email}")
    print(f"Theme: {theme}")


user = {
    "id": 1,
    "profile": {
        "username": "Morris",
        "email": "Morris@gmail.com",
    },
    "settings": {
        "theme": "dark",
        "notifications": True
    }
}
extract_user_info(user)


# question 4: list of dictionaries
def get_affordable_products(products, budget):
    affordable_products = []
    for product in products:
        if product["price"] <= budget:
            affordable_products.append(product)
    return affordable_products

products = [
    {"name": "phone", "price": 800},
    {"name": "Tablet", "price": 600},
    {"name": "laptop", "price": 1200},
    ]

budget = 1200
affordable_products = get_affordable_products(products, budget)
print(affordable_products)


#Question 5: args and set union
def merge_lists(lists):
    merged_list = []
    for sublist in lists:
        for item in sublist:
            if item not in merged_list:
                merged_list.append(item)
    return merged_list

list_set = ([0,1],[2,2],[3,4],[4,5],[5,6],[7,8])
print(merge_lists(list_set))


#question 6: sorting and finding
def second_largest(lst):
    if len(lst) < 2:
        raise ValueError("List must contain at least two numbers")

    largest = second = float('-inf')
    for num in lst:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    if second == float('-inf'):
        raise ValueError("List must contain at least two distinct numbers")

    return second

print(second_largest([10, 20, 4, 45, 99]))




#Question 7:
def apply_operation(lst, operation):
    if operation == "square":
        return [x ** 2 for x in lst]
    elif operation == "double":
        return [x * 2 for x in lst]
    elif operation == "negate":
        return [-x for x in lst]
    else:
        raise ValueError("Invalid operation. Choose 'square', 'double', or 'negate'.")

print(apply_operation([1, 2, 3], "square"))
print(apply_operation([1, 2, 3], "double"))
print(apply_operation([1, 2, 3], "negate"))








