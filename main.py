import wolframalpha
import speech_recognition as sr
import pyjokes
import pyttsx3
import Functions


def newquestion():

    nsearch = input("Do you have something else you'd like to know?(y for yes and n for no)")

    if nsearch == 'y':
        nreq = input("Okay, what would you like to know?")
        nres = client.query(nreq)

        if nreq == "stop":    #if user acciodentally hits y they can still stop it
            quit()

        print(next(nres.results).text)

        ncont = input("would you like more information? (y for yes, n for no)")
        if ncont == "y":
            for pod in nres.pods:
                for sub in pod.subpods:
                    print(sub.plaintext)
            newquestion()

        if ncont == 'n':
            newquestion()








sr.__version__

r = sr.Recognizer()


client = wolframalpha.Client('RU6X4L-GQ655666HJ')




print("At any point you can say stop and I will stop.")
req = input("Hi, I'm Eve. What do you need?")


if req == "stop":
    quit()
if "joke" in req:
    x = 1
    while x > 0:
        print(pyjokes.get_joke())
        x -= 1

if "joke" not in req:
    res = client.query(req)
    count = 0                                               #stores the question and gets the first result and prints it
    cont = 'n'
    print(next(res.results).text)

    cont = input("would you like more information? (y for yes, n for no)")      #

    if cont == "y":
        for pod in res.pods:
            for sub in pod.subpods:     #if user wants more info this will print all of the related pods to the question
                print(sub.plaintext)    # until there are no new pods
        newquestion()
        cont = "n"

    else:
        pass
newquestion()           #bug that doesnt end up asking u if u ahve abnother question it just automatically
                #has u ask another one so ur stuck in a loop, if u answer yes to more info
                #it will automatically ask what else would u want to know
