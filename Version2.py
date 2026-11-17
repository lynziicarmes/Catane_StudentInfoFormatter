first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
section = input("Enter section: ")
subject = input("Enter favorite subject: ")

first_name = first_name.strip().title()
last_name = last_name.strip().title()
section = section.strip().upper()
subject = subject.strip().title()

full_name = first_name + " " + last_name

print("\nFormatted Output:")
print("Name:", full_name)
print("Name Code:", full_name.upper())
print("Section:", section)
print("Favorite Subject:", subject)
print("Character Count:", len(full_name))
