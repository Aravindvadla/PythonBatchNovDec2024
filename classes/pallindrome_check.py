# Input a sentence from the user
sentence = input("Enter a sentence to check if it is a palindrome: ")

# Remove all spaces and check for palindrome using string slicing
processed_sentence = sentence.replace(" ", "").lower()
is_palindrome = processed_sentence == processed_sentence[::-1]

# Print the result
if is_palindrome:
    print("The given sentence is a palindrome.")
else:
    print("The given sentence is not a palindrome.")
