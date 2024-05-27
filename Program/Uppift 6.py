def is_palindrome(word):
    word = word.lower()
    if word == word[::-1]:
        print("True")
    else:
        print("False")

while True:
    is_palindrome(input(""))
