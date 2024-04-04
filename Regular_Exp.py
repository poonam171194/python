
import re

text = """
Hello this is your email address list like poonam17@gmail.com, pragnesh97@yahoo.com, pooja12@linkdin.in
"""

List_of_emails = re.findall('([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+',text)
print(List_of_emails)