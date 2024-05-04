data = ("01110011", "01110100", "01100001", "01111001", "00100000", "01100001", "01110111", "01100001", "01111001", "00100000", "01100110", "01110010", "01101111", "01101101", "00100000", "01110100", "00100000", "01100111","01101001", "01110010", "01101100")
# Loop through each element in the data list and print it
horizontal_string = ""
for each in data:
  decimal_value =int(each,2)
  character =chr(decimal_value)
  horizontal_string += character
  print(horizontal_string)
