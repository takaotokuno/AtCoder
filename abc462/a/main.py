import re
s=input().strip()
print(re.sub(r"[a-zA-Z]","",s))