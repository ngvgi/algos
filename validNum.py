""" 

A valid number can be split up into these components (in order):

A decimal number or an integer.
(Optional) An 'e' or 'E', followed by an integer.
A decimal number can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One of the following formats:
At least one digit, followed by a dot '.'.
At least one digit, followed by a dot '.', followed by at least one digit.
A dot '.', followed by at least one digit.
An integer can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
At least one digit.
For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.

"""


import re
class Solution:    
    def isNumber(self, s: str) -> bool:
        decimal_check = "(\+|-)?(\d+\.{1}|\d+\.{1}\d+|\.{1}\d+)"
        integer_check = "(\+|-)?\d+((e|E)?(\+|-)?\d+)?"
        # "(\+|-)?\d+((e|E)?(\+|-)?\d+)?"
        # is_decimal = re.match(decimal_check, s)
        # is_integer = re.match(integer_check, s)
        validityCheck = "(((\+|-)?(\d+\.{1}|\d+\.{1}\d+|\.{1}\d+)(e|E)?((\+|-)?\d+)?)|(\+|-)?(\d)+((e|E)?((\+|-)?\d)+)?)"

        vals = ["abc", "1a", "1e", "e3", "99e2.5", "6", "-+3", "95a54e53","-9.34"]

        for val in vals:
            if re.match(validityCheck, val):
                print('{}  => Valid'.format(val))
            else:
                print('{}  => Invalid'.format(val))

        
        
        return 'Complete Parse'


print(Solution().isNumber('p+8'))