import wolframalpha
import pyttsx3
engine = pyttsx3.init()






client = wolframalpha.Client('RU6X4L-GQ655666HJ')


def newquestion():
    engine.say("Do you have something else you'd like to know?(y for yes and n for no)")

    nsearch = input("Do you have something else you'd like to know?(y for yes and n for no)")

    while nsearch == 'y':
        engine.say("Okay, what would you like to know?")
        engine.runAndWait()
        nreq = input("Okay, what would you like to know?")
        nres = client.query(nreq)
        engine.say((nres.results).text)
        engine.runAndWait()
        print(next(nres.results).text)

        engine.say("would you like more information? (y for yes, n for no)")
        engine.runAndWait()
        ncont = input("would you like more information? (y for yes, n for no)")
        if ncont == "y":
            for pod in res.pods:
                for sub in pod.subpods:
                    engine.say(sub.plaintext)
                    engine.runAndWait()
                    print(sub.plaintext)
        elif ncont == 'n':
            engine.say("Do you have something else you'd like to know?(y for yes and n for no)")
            engine.runAndWait()
            nsearch = input("Do you have something else you'd like to know?(y for yes and n for no)")
    else:
        pass

    return

engine.say("Hi, I'm Eve. What do you need?")
engine.runAndWait()
req = input("Hi, I'm Eve. What do you need?")
res = client.query(req)
count = 0
cont = 'n'
engine.say(res.results)
engine.runAndWait()
print(next(res.results).text)
engine.say("would you like more information? (y for yes, n for no)")
engine.runAndWait()
cont = input("would you like more information? (y for yes, n for no)")

if cont == "y":
    for pod in res.pods:
        for sub in pod.subpods:
            engine.say(sub.plaintext)
            engine.runAndWait()
            print(sub.plaintext)
    newquestion()

else:
    pass
    newquestion()
