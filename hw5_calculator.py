def main():
    import random
    amount = 5000
    people = int(input("How many people splitting the bill. "))
    names = input("Their names with comma.  ").split(",", people)
    tips = int(input('DO u wanna tip us  '))
    pay = amount // people
    random.shuffle(names)
    a_1 = round((amount * (1 / (2**len(names)-1))), 2)
    #Unfortunately do not understand why do I need the names because they have to pay the same shit but will try to use it
    def default():
        for i in names:
            print(i + " have to pay  " + str(pay))

    #I will create random list and person after will pay two times more
    def optional():
        print(names[0]+ " is lucky have to pay  "+ str(a_1))
        for i in names:
            if names.index(i) == 0:
                continue
            else:
                a_n = a_1 * (2**(names.index(i)))
                print(i + " UNLUCK  " + str(a_n))

    optional()
    if (tips >= amount*0.2):
        print("YOU are GENEROUSITY")




main()



