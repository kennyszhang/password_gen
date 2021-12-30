#password gen by kenny zhang
import pyperclip, random, string, time

def main():
    password = []
    
    for x in range(random.randint(5,6)):
        temp = random.choice(string.digits.replace('0''1', ''))
        password.append(temp)
    for x in range(random.randint(5,6)):
        temp = random.choice("@&$!#?%")
        password.append(temp)
    temp = 16 - len(password)
    for x in range(temp):
        temp = random.choice(string.ascii_letters.replace('I''l''o''O',''))
        password.append(temp)

    random.shuffle(password)
    password = "".join(password)
    print(password)
    pyperclip.copy(str(password))
    print("\npassword copied to clipboard")
    time.sleep(5)
    
main()




