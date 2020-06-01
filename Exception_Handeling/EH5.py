#when finaly not execute
import os as OPS
try:
    OPS._exit(0)
except:
    print("exception Occured") 
finally:
    print("code handeld")        