print("This is a demonstration of string concatenation")
name = input("Input a Genshin character's name.")
country = input("What's this character's country of origin?")
activity = input("What is an activity you would do with them?")
object = input("What is something you can give them?")

madlib = f"{name} is a survivor of {country}. Besides that singular fact, I know little about him\
, and would never want to {activity} together with {name}. He seems to want {object} from me, though. \
In the past, he sent me on many trips to {country} hoping to coerce me to give him {object}."

print(madlib)