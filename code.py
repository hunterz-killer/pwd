import itertools

rqpwd = "abc123"

charts = "abcdefghijklmnopqrstuvxyz1234567890"
digits = 6

for pwd in itertools.product(charts, repeat=digits):
    c_pwd = "".join(pwd)
    print(c_pwd)
    if c_pwd != rqpwd:
        print(c_pwd)
    else:
        break

print("The Pwd is ", c_pwd)
