# Initialize the detail_desc variable
detail_desc = ''

# Assume these variables hold some information
name = 'John Doe'
occupation = 'Engineer'
age = 30

# Build the detailed description
if name:
    detail_desc += f"Name: {name}\n"
if occupation:
    detail_desc += f"Occupation: {occupation}\n"
if age:
    detail_desc += f"Age: {age}\n"

# Print the detailed description
print(detail_desc)
