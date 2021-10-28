import itertools
import time

start_time = time.time()
rqpwd = "abc123"  # replace it 

charts = "abcdefghijklmnopqrstuvxyz1234567890"
digits = 6

for pwd in itertools.product(charts, repeat=digits):
    c_pwd = "".join(pwd)
    if c_pwd == rqpwd:
        end_time = time.time()
        runtime = round(end_time - start_time, 2)
        print("The Pwd is", c_pwd, "found in", runtime, "Seconds")
        break
