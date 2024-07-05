import re
def is_valid_regex(s):
    try:
        re.compile(s)
        return True
    except re.error:
        return False

T = int(input().strip())
for _ in range(T):
    s = input().strip()
    if is_valid_regex(s):
        print("True")
    else:
        print("False")