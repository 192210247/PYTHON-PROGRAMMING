import re

def is_valid_number(s: str) -> bool:
    integer_pattern = r'^[+-]?\d+$'
    decimal_pattern = r'^[+-]?\d+(\.\d*|\.\d+|\d+\.)\d*$'
    exponential_pattern = r'^[+-]?\d+(\.\d*)?[eE][+-]?\d+$'

    full_pattern = f'^({integer_pattern}|{decimal_pattern}|{exponential_pattern})$'

    return bool(re.match(full_pattern, s))

test_cases = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789",
              "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]

for case in test_cases:
    print(f"{case}: {is_valid_number(case)}")
