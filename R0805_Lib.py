import csv

def generate_symbol(data):
    symbol_template = '''
  (symbol "R0805F_{0}" (pin_numbers hide) (pin_names (offset 0.254) hide) (in_bom yes) (on_board yes)
    (property "Reference" "R" (at 0.762 0.508 0)
      (effects (font (size 1.27 1.27)) (justify left))
    )
    (property "Value" "{0}" (at 0.762 -1.016 0)
      (effects (font (size 1.27 1.27)) (justify left))
    )
    (property "Footprint" "Resistor_SMD:R_0805_2012Metric" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Datasheet" "~" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "MFG #1" "{2}" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "P/N #1" "{3}" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "MFG #2" "{4}" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "P/N #2" "{5}" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "MFG #3" "{6}" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "P/N #3" "{7}" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Tolerance" "1%" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "ki_keywords" "Res, {0}, 1%, 125mW, R0805" (at 0 0 0) 
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "ki_description" "{1}" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "ki_fp_filters" "R_*" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (symbol "R0805F_{0}_1_1"
      (polyline
        (pts
          (xy 0 0)
          (xy 1.016 -0.381)
          (xy 0 -0.762)
          (xy -1.016 -1.143)
          (xy 0 -1.524)
        )
        (stroke (width 0) (type default))
        (fill (type none))
      )
      (polyline
        (pts
          (xy 0 1.524)
          (xy 1.016 1.143)
          (xy 0 0.762)
          (xy -1.016 0.381)
          (xy 0 0)
        )
        (stroke (width 0) (type default))
        (fill (type none))
      )
      (pin passive line (at 0 2.54 270) (length 1.016)
        (name "~" (effects (font (size 1.27 1.27))))
        (number "1" (effects (font (size 1.27 1.27))))
      )
      (pin passive line (at 0 -2.54 90) (length 1.016)
        (name "~" (effects (font (size 1.27 1.27))))
        (number "2" (effects (font (size 1.27 1.27))))
      )
    )
  )
    '''
    return symbol_template.format(*data)

def read_csv_and_generate_symbols(filename):
    symbols = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)  # Skip the header
        next(reader, None)  # Skip the second line
        for row in reader:
            symbols.append(generate_symbol(row))
    return symbols

def write_symbols_to_file(filename, symbols):
    with open(filename, 'w') as f:
        f.write('(kicad_symbol_lib (version 20220914) (generator kicad_symbol_editor)\n')
        for symbol in symbols:
            f.write(symbol)
        f.write(')')

def main():
    csv_file = 'R0805_Lib.csv'  # replace with your csv filename
    output_file = 'R0805F.kicad_sym' #Change
    symbols = read_csv_and_generate_symbols(csv_file)
    write_symbols_to_file(output_file, symbols)

if __name__ == "__main__":
    main()

