password = 'testpassword123'
password_l = []
last_password = input("Enter lass password you remembered: ")
check_password = []
c = 0
t = 0
cv = 0
l = 0

for i in range(len(last_password)):
    check_password.append(last_password[i])

for j in range(len(password)):
    password_l.append(password[j])

if len(password) > len(last_password):
    c = len(password) - len(last_password)
else:
    c = len(last_password) - len(password)
    l = 1

if c > 4:
    print("\n\tIncorrect")
else:
    t = 1

if l == 0 and t == 1:
    for k in range(len(password_l)):
        
        if k == len(check_password):
            break

        if password_l[k] == check_password[k]:
            cv += 1
elif l == 1 and t == 1:
    for k in range(len(check_password)):

        if k == len(password_l):
            break

        if check_password[k] == password_l[k]:
            cv += 1


percentage_accuracy = (cv / len(password_l)) * 100

if t==1:
    if percentage_accuracy < 70:
        print("\n\tSorry, we couldn't retrieve your password")
        print(cv)
        print(percentage_accuracy)
    else:
        print(f"\n\tSuccessfully retrieved your password: {password}")