def say(word="shout"):

    def shout(word="Hello"):
        return word.upper() + "!"

    def whisper(word="Bye"):
        return word.lower() + "..."

    if word == "shout":
        return shout
    else:
        return whisper


func = say("---")
print(func("maksim"))
print(say()("Anastasia"))
