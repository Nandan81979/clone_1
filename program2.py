def is_eligible(age):
  if age >= 18:
    return True
  else:
    return False

age = int(input("Enter your age: "))

if is_eligible(age):
  print("Eligible to vote.")
else:
  print("Not eligible to vote.")
