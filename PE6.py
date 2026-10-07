import re


# --------------------------------------------------
# Function: validate_phone
# Purpose: Validates a phone number using a regular expression.
# --------------------------------------------------

def validate_phone(phone):
    # Accepts formats such as:
    # 123-456-7890
    # (123) 456-7890
    # 1234567890
    # 123.456.7890

    pattern = r"^(?:\(\d{3}\)\s?|\d{3}[-.\s]?)\d{3}[-.\s]?\d{4}$"

    return bool(re.match(pattern, phone))


# --------------------------------------------------
# Function: validate_ssn
# Purpose: Validates a Social Security number.
# --------------------------------------------------

def validate_ssn(ssn):
    # Accepts the standard format:
    # 123-45-6789
    #
    # Also accepts the same number without dashes:
    # 123456789

    pattern = r"^\d{3}-?\d{2}-?\d{4}$"

    return bool(re.match(pattern, ssn))


# --------------------------------------------------
# Function: validate_zip
# Purpose: Validates a United States ZIP code.
# --------------------------------------------------

def validate_zip(zip_code):
    # Accepts standard five-digit ZIP codes:
    # 34231
    #
    # Also accepts ZIP+4:
    # 34231-1234

    pattern = r"^\d{5}(?:-\d{4})?$"

    return bool(re.match(pattern, zip_code))


# --------------------------------------------------
# Function: run_tests
# Purpose: Tests the validation functions with
#          multiple valid and invalid examples.
# --------------------------------------------------

def run_tests():
    print("\n--- Testing Phone Numbers ---")

    # Valid phone number examples
    valid_phones = [
        "123-456-7890",
        "(123) 456-7890",
        "1234567890",
        "123.456.7890"
    ]

    # Invalid phone number examples
    invalid_phones = [
        "123-456-789",
        "123-45-67890",
        "abc-def-ghij",
        "12345678901"
    ]

    # Test valid phone numbers
    for phone in valid_phones:
        print(f"{phone}: {validate_phone(phone)}")

    # Test invalid phone numbers
    for phone in invalid_phones:
        print(f"{phone}: {validate_phone(phone)}")


    print("\n--- Testing Social Security Numbers ---")

    # Valid SSN examples
    valid_ssns = [
        "123-45-6789",
        "123456789"
    ]

    # Invalid SSN examples
    invalid_ssns = [
        "123-456-789",
        "12-345-6789",
        "123-45-67890",
        "abcdefghijk"
    ]

    # Test valid SSNs
    for ssn in valid_ssns:
        print(f"{ssn}: {validate_ssn(ssn)}")

    # Test invalid SSNs
    for ssn in invalid_ssns:
        print(f"{ssn}: {validate_ssn(ssn)}")


    print("\n--- Testing ZIP Codes ---")

    # Valid ZIP code examples
    valid_zips = [
        "34231",
        "34231-1234",
        "90210",
        "10001"
    ]

    # Invalid ZIP code examples
    invalid_zips = [
        "3423",
        "342311",
        "34231-123",
        "abcde"
    ]

    # Test valid ZIP codes
    for zip_code in valid_zips:
        print(f"{zip_code}: {validate_zip(zip_code)}")


    # Test invalid ZIP codes
    for zip_code in invalid_zips:
        print(f"{zip_code}: {validate_zip(zip_code)}")


# --------------------------------------------------
# Function: main
# Purpose: Gets phone number, SSN, and ZIP code
#          from the user and displays whether
#          each value is valid.
# --------------------------------------------------

def main():
    # Get information from the user
    print("========================================")
    print("     Personal Information Validator")
    print("========================================")

    phone = input("Enter your phone number: ")
    ssn = input("Enter your Social Security number: ")
    zip_code = input("Enter your ZIP code: ")


    # Validate and display the phone number result
    if validate_phone(phone):
        print("Phone number: Valid")
    else:
        print("Phone number: Invalid")


    # Validate and display the SSN result
    if validate_ssn(ssn):
        print("Social Security number: Valid")
    else:
        print("Social Security number: Invalid")


    # Validate and display the ZIP code result
    if validate_zip(zip_code):
        print("ZIP code: Valid")
    else:
        print("ZIP code: Invalid")


# --------------------------------------------------
# Program starting point
# --------------------------------------------------

if __name__ == "__main__":
    # Run the automated tests first.
    run_tests()

    # Run the main program.
    main()