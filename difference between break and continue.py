print("Loop with 'break':")
for i in range(1, 11):
    if i % 3 == 0:
        break
    print(i)
print("Loop with 'continue':")
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i)
