# a function that calculates and returns number of lower case characters in a string
def NbCMin(s):
    count = 0
    for c in s:
        if c.islower():
            count += 1
    return count


# a function that calculates and returns number of uppercase case characters in a string
def NbCMaj(s):
    count = 0
    for c in s:
        if c.isupper():
            count += 1
    return count


# a function that calculates and returns number of non-alphabetic characters in a string
def NbCNonAlpha(s):
    count = 0
    for c in s:
        if not c.isalpha():
            count += 1
    return count


# a function that calculates and returns the length of the longest sequence of uppercase alphabetic characters in a
# string
def longMaj(s):
    count = 0
    maxCount = 0
    for c in s:
        if c.isupper():
            count += 1
        else:
            if count > maxCount:
                maxCount = count
            count = 0
    if count > maxCount:
        maxCount = count
    return maxCount


# a function that calculates and returns the length of the longest sequence of lower case alphabetic characters in a
# string
def longMin(s):
    count = 0
    maxCount = 0
    for c in s:
        if c.islower():
            count += 1
        else:
            if count > maxCount:
                maxCount = count
            count = 0
    if count > maxCount:
        maxCount = count
    return maxCount


# a function that calculates and show  the score of a password and shows if the password is strong or not
# the score is calculated as follows:
# - adding all the bonuses as follows:
#   - 1 the total number of characters in the password * 4
#   - 2 (the total number of characters - the number of upper case characters) in the password * 2
#   - 3 (the total number of characters - the number of lower case characters) in the password * 3
#   - 4 the number of non-alphabetic characters in the password * 5
# - minus the penalties as follows:
#   - 1 the length of the longest sequence of lower case alphabetic characters in the password * 2
#   - 2 the length of the longest sequence of uppercase alphabetic characters in the password * 3
# the password is considered as strong as follows:
# - if the score is less than 20, the password is considered too weak
# - if the score is between 20 and 40, the password is considered weak
# - if the score is between 40 and 80, the password is considered strong
# - if the score is more than 80, the password is considered very strong

def score(s):
    sc = len(s) * 4 + (len(s) - NbCMaj(s)) * 2 + (len(s) - NbCMin(s)) * 3 + NbCNonAlpha(s) * 5 \
         - longMin(s) * 2 - longMaj(s) * 3

    if sc < 20:
        print('\033[91m' + 'Too weak' + '\033[0m')
    elif sc < 40:
        print('\033[91m' + 'Weak' + '\033[0m')
    elif sc < 80:
        print('\033[93m' + 'Strong' + '\033[0m')
    else:
        print('\033[92m' + 'Very strong' + '\033[0m')


if __name__ == '__main__':
    password = input('Password: ')
    score(password)
