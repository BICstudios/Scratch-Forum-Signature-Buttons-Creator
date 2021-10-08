print("This tool was created by BIC. If you encounter some bugs or glitch, please report it to me in my Scratch profile https://scratch.mit.edu/users/BIC_Studios")
print()

while True:
  amount = input("Button amount: ")
  print()
  if amount.isnumeric() and int(amount) != 0: # Only runs the code if the answer is a positive integer
        img = [] # Reset both arrays
        link = []
        for i in range(0, int(amount), 1): # Asks user for image(s) and link(s)
          img.append(input("Image " + str(i+1) + ": "))
          link.append(input("Link " + str(i+1) + ": "))
          print()
        print("Copy the BBCode below and paste it into your signature.")
        print()
        button = str()
        for i in range(0, int(amount), 1): # Combines the image(s) and link(s) into BBCode
          button = button + "[url=" + link[i] + "]" + "[img]" + img[i] + "[/img]" + "[/url]"
        print("[center]" + button + "[/center]") # Adds center tag
        print()
  else:
    print("The answer must be a positive integer")
    print()
  print()
