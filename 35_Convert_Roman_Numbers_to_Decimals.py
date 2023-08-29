tallies = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}

def RomanNumeralToDecimal(romanNumeral):
    decimal_value = 0
    prev_value = 0

    for numeral in reversed(romanNumeral):
        value = tallies[numeral]
        if value < prev_value:
            decimal_value -= value
        else:
            decimal_value += value
        prev_value = value

    return decimal_value

def main():
    roman_input = input("Enter a Roman numeral: ")
    roman_input = roman_input.upper()
    decimal_value = RomanNumeralToDecimal(roman_input)
    print(f"{roman_input} = {decimal_value}")

if __name__ == "__main__":
    main()
