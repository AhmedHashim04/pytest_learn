from fullname_func import get_full_name
first_name = input("Enter your first name: ")
middle_name = input("Enter your middle name (or leave blank): ")
if middle_name:
    full_name = get_full_name(first_name, middle_name)
else:
    full_name = first_name
last_name = input("Enter your last name: ")
full_name = get_full_name(full_name, last_name)
print(f"Hello, {full_name}!")
