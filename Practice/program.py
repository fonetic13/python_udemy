def sentence_builder(input):
    upitni = ("Who", "What", "When", "Where", "Why")
    cap = input.capitalize()
    if cap.startswith(upitni):
        cap = f"{cap}?"
    else:
        cap = f"{cap}."
    return cap

holder = []
while True:
    say_some = input("Say something: ")
    if say_some == "\end":
        break
    else:
        holder.append(sentence_builder(say_some))
print("-".join(holder))
