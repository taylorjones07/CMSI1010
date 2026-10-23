
import random

# list of stories for the game
templates = [
    {
        "text": "The :color :animal jumped over the :adjective :object.",
        "author": "Taylor Jones"
    },
    {
        "text": "Yesterday I saw a :animal eating :food at the :place.",
        "author": "Taylor Jones"
    },
    {
        "text": "My :adjective teacher turned into a :animal during :class.",
        "author": "Taylor Jones"
    },
    {
        "text": "The princess wore a :color dress and married a :adjective :animal.",
        "author": "Taylor Jones"
    },
    {
        "text": "I went to :place and found a :adjective :object in my bag.",
        "author": "Taylor Jones"
    },
    {
        "text": "My best friend brought a :animal to :place and started :verbing.",
        "author": "Taylor Jones"
    },
    {
        "text": "The :adjective superhero saved the city using a :object.",
        "author": "Taylor Jones"
    },
    {
        "text": "For breakfast I ate :number :food and drank :liquid.",
        "author": "Taylor Jones"
    },
    {
        "text": "The :animal became famous after winning a :adjective contest.",
        "author": "Taylor Jones"
    },
    {
        "text": "At midnight, a :color ghost appeared in my :room.",
        "author": "Taylor Jones"
    }
]

# mean yes
yes_answers = {"yes", "y", "yeah", "yep", "sure", "si", "sí", "oui", "ok", "okay"}

# start the game
playing = True

while playing:
    # pick a random story
    story = random.choice(templates)

    # get the story text
    words = story["text"].split()
    new_words = []

    # go through each word
    for word in words:
        if word.startswith(":"):
            # take off the colon and punctuation
            word_type = word[1:].strip(".,!?")

            # ask the player for a word
            answer = input("Enter a " + word_type + ": ")

            # make sure the answer is not too long or empty
            while len(answer) < 1 or len(answer) > 30:
                print("Please enter 1 to 30 characters.")
                answer = input("Enter a " + word_type + ": ")

            # keep punctuation at the end
            punctuation = word[len(word.rstrip(".,!?")):]

            # add the answer to the story
            new_words.append(answer + punctuation)
        else:
            new_words.append(word)

    # put the story together
    finished_story = " ".join(new_words)

    # show the completed story
    print()
    print(finished_story)
    print()
    print("Written by:", story["author"])
    print()
    print()

    # ask if they want to play again
    again = input("Do you want to play again? ").lower().strip()

    if again not in yes_answers:
        playing = False
        print("Thanks for playing!")
