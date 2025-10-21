# task_1.py

file_name = 'sample.txt'

try:
    with open(file_name, 'r') as file:
        print(f"-Contents of {file_name} --")
        for line in file:
            
            print(line, end='')
        print("\n---------------------------------")

except FileNotFoundError:
    print(f"\nError:  file '{file_name}' nt found.")


# task_2.py

output_filename = 'output.txt'


user_data = input("Please enter something to write to the file: ")


with open(output_filename, 'w') as file:
       file.write(user_data + '\n')

with open(output_filename, 'a') as file:
    file.write("This is the second line.\n")
    file.write("This is the third line.\n")

print(f"\n--- Final content of {output_filename} ---")

# Read the file back and print it all.
with open(output_filename, 'r') as file:
    print(file.read())
  
