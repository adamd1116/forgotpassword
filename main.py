password = 'testpassword123'
password_l = []
last_password = input("Enter lass password you remembered: ")
check_password = []
c = 0
t = 0

for i in range(len(last_password)):
    check_password.append(last_password[i])

for j in range(len(password)):
    password_l.append(password[j])

if len(password) > len(last_password):
    c = len(password) - len(last_password)
else:
    c = len(last_password) - len(password)

if c <= 4:
    print("\n\tIncorrect")
else:
    t = 1

