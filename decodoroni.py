# Accept user input for the list of hex values
hex_input = input("Enter the list of raw hex values separated by spaces: ")
hex_list = [int(hex_value, 16) for hex_value in hex_input.split()]

# Generate limabean variable and print its value
limabean = ''.join([chr(hex_value) for hex_value in hex_list])
print(limabean)

