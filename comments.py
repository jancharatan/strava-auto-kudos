from random import choice, choices

emojis = ["💯", "🔥", "🥵", "💣", "✨", "🪄", "😮‍💨", "🫨", "🤯", "😤", "😴"]

comments = [
    "The only place success comes before work is in the dictionary. — Vince Lombardi",
    "When you are asked if you can do a job, tell 'em, 'Certainly I can' Then get busy and find out how to do it. — Theodore Roosevelt",
    "Every day I get up and look through the Forbes list of the richest people in America. If I’m not there, I go to work. — Robert Orben",
    "Whatever you do, always give 100% — unless you’re donating blood. — Bill Murray",
    "Be like a postage stamp; stick to one thing until you get there. — Josh Billings",
    "Hustle until your haters ask if you’re hiring. — Steve Maraboli"
    "The difference between try and triumph is just a little umph! — Marvin Phillips"
    "Just keep swimming. — Finding Nemo (2002)",
    "Trying is the first step toward failure. — Homer Simpson"
    "Never put off till tomorrow what you can do the day after tomorrow. — Mark Twain"
]

def fetch_random_comment() -> str:
    return f"{choice(comments)} {"".join(choices(emojis, 3))}"
