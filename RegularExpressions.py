#RegularExpressions
#tool for matching patterns in text

#e.g. r"^(From|To|Cc).*?python-list@python.org"
#^ matches text at beginning of a line
#(From|To|CC) means line has to start with one of words separated by pipe | (OR operator)
# .*? means ungreedily match any number of characters except the newline \n character
#ungreedy means to match as few repetitions as possible
#. means any non-newline character
#* means to repeat 0 or more times
#? makes it ungreedy 

#matches:
#From: python-list@python.org To: !asp]<,. python-list@python.org

#re syntax found in python docs

#example of proper email-matching regex

# Example: 
import re
pattern = re.compile(r"\[(on|off)\]") # Slight optimization
print(re.search(pattern, "Mono: Playback 65 [75%] [-16.50dB] [on]"))
# Returns a Match object!
print(re.search(pattern, "Nada...:-("))
# Doesn't return anything.
# End Example

# Exercise: make a regular expression that will match an email
def test_email(your_pattern):
    pattern = re.compile(your_pattern)
    emails = ["john@example.com", "python-list@python.org", "wha.t.`1an?ug{}ly@email.com"]
    for email in emails:
        if not re.match(pattern, email):
            print("You failed to match %s" % (email))
        elif not your_pattern:
            print("Forgot to enter a pattern!")
        else:
            print("Pass")
pattern = r".*?@.*?..*?" # Your pattern here!
test_email(pattern)

#alternatively
print("alternatively")
def test_email(your_pattern):
    pattern = re.compile(your_pattern)
    emails = ["john@example.com", "python-list@python.org", "wha.t.`1an?ug{}ly@email.com"]
    for email in emails:
        if not re.match(pattern, email):
            print("You failed to match %s" % (email))
        elif not your_pattern:
            print("Forgot to enter a pattern!")
        else:
            print("Pass")
pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?" # Your pattern here!
test_email(pattern)