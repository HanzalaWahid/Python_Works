# import pyttsx3
#
# if __name__ == '__main__':
#     print("Welcome to my Robo Speaker 11.3 created by Hanzala")
#     x = input("Enter What You Want To Speak: ")
#     command = f"say {x}"
#     pyttsx3.system(command)
import pyttsx3


def speak_text(text):

    # Function to speak the provided text.

    engine = pyttsx3.init()
    engine.setProperty("rate", 100)
    engine.setProperty("volume", 1.0)
    engine.say(text)
    engine.runAndWait()


if __name__ == '__main__':
    print("Welcome to my Robo Speaker 11.3 created by Hanzala")
    while True:
        user_input = input("Enter What You Want To Speak: ")
        if user_input.lower() == "stop":
            break
        speak_text(user_input)

