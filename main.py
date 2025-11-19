from PhMeter import PhMeter

print("Program running: pH meter with classification function")

device = PhMeter()

while True:
    print("\n1 - Take measurements.\n"
          "2 - Exit.")
    user_input = int(input("Choose the option: "))

    if user_input == 1:
        device.analyze_ph()
        device.print_results()
    elif user_input == 2:
        print("The program closed.")
        break
    else:
        print("There is no such option, try again.")
        print("-" * 50)

