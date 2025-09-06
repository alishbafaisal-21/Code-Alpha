import re
import os

#create data.text file automatically
if not os.path.exists("data.txt"):
    with open("data.txt", "w") as f:
        f.write("Welcome to CodeAlpha Internship Program.\n")
        f.write("For queries, email us at head.codealpha@gmail.com.\n")
        f.write("You may also reach out to hr@codealpha.org. \n")
    print("Sample data.txt file created with test emails.")


with open("data.txt", "r") as f:
    text = f.read()


emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)

with open("emails.txt", "w") as f:
    for email in emails:
        f.write(email + "\n")

print("Emails extracted and saved to emails.txt")
print("Extracted Emails:", emails)
