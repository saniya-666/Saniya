def build_index(text):
    index = {}
    words = text.split()

    for position, word in
    enumerate(words):
    word = word.lower().strip(".,!?")
    if word not in index:
        