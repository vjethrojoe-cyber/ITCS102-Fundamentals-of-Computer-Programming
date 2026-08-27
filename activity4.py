#activity4.py
#escape sequence --> to modify the behavior of linear formatted string
# \n - new line 
# \t - tab space
# \r - carriage return / deprecated (obsolete)
# \b - back space
# \\ - insert slash
# \" - insert double quotation

phrase1 = "Item List:\n- Python\n- Java\n- C++"
phrase2 = "Name:\tJethro Joe Vedra\nID:\t2026-12345"
phrase3 = "To open Python, navigate to your folder: C:\\Users\\hp\\exercises"
phrase4 = "The coach has strictly instructed, \"Do not be late in practices!\""
phrase5 = "This text has an extraa\b character removed."
phrase6 = "Wipe this out\rThis sentence completely replaces the text behind it."


print("=== Individual Escape Sequence Examples ===")
print(phrase1)
print("\n" + phrase2)
print("\n" + phrase3)
print("\n" + phrase4)
print("\n" + phrase5)
print("\n" + phrase6)

print("\n=== Mixed Classroom Exercise Phrase ===")
