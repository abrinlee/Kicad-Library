import pandas as pd

def replace_symbol(line, row):
    # List of symbols
    symbols = ['C_Small', 'C_Small_0_1', 'C_Small_1_1']
    for symbol in symbols:
        new_symbol = row['Symbol'] + symbol.split('C_Small')[-1]
        if symbol in line:
            line = line.replace(symbol, new_symbol)
            break
    return line

def replace_properties(line, row):
    # List of properties
    properties = ['Value', 'Dielectric', 'Voltage', 'Tolerance', 
                  'MFG #1', 'P/N #1', 'MFG #2', 'P/N #2', 'MFG #3', 'P/N #3', 'Description', 
                  'ki_keywords', 'ki_description']

    for prop in properties:
        if f'(property "{prop}"' in line:
            if prop == 'Value':
                line = line.replace('C_Value', row['Value'])
            elif prop in ['Dielectric', 'Voltage', 'Tolerance', 
                          'MFG #1', 'P/N #1', 'MFG #2', 'P/N #2', 'MFG #3', 'P/N #3']:
                line = line.replace('""', f'"{row[prop]}"')
            elif prop == 'Description':
                line = line.replace('Unpolarized capacitor, small symbol', 
                                    f'MLCC, {row["Value"]}, {row["Voltage"]}, {row["Dielectric"]}, {row["Tolerance"]}, C0402')
            elif prop == 'ki_keywords':
                line = line.replace('capacitor cap', 
                                    f'C0402 {row["Value"]} {row["Voltage"]} {row["Dielectric"]} {row["Tolerance"]}')
            elif prop == 'ki_description':
                line = line.replace('Unpolarized capacitor, small symbol', 
                                    f'MLCC, {row["Value"]}, {row["Voltage"]}, {row["Dielectric"]}, {row["Tolerance"]}, C0402')
            break
    return line

def write_to_output_file(row, lines):
    # Open output file in append mode
    with open('C0402.kicad_sym', 'a') as f:
        for line in lines:
            line = replace_symbol(line, row)
            line = replace_properties(line, row)
            # Write the line to the output file
            f.write(line)

# Read the csv file into a pandas DataFrame
df = pd.read_csv('C0402.CSV')

# Open template file and read its content
with open('template0402.kicad_sym', 'r') as f:
    lines = f.readlines()

# Create output file and write the initial line
with open('C0402.kicad_sym', 'w') as f:
    f.write('(kicad_symbol_lib (version 20220914) (generator kicad_symbol_editor)\n')

# Iterate over each row in the DataFrame
for _, row in df.iterrows():
    write_to_output_file(row, lines)

# Append closing bracket to the output file
with open('C0402.kicad_sym', 'a') as f:
    f.write(')\n')
