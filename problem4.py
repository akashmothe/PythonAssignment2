from pydoc import ispackage


# def is_palindrome(s):
#     if s == s[::-1]:
#         return "Palindrome"
#     return "Not Palindrome"

# print(is_palindrome("naman"))
# print(is_palindrome("akash"))

is_palindrome = lambda s : "Palindrome" if s == s[::-1] else "Not Palindrome"

print(is_palindrome("naman"))
print(is_palindrome("akash"))
