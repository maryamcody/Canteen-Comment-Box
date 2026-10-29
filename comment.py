#
LEXICON = {
    "delicious": 3, "great": 3, "tasty": 2, "kind": 2, "fresh": 2, "good": 2,
    "cold": -1, "slow": -1, "bad": -2, "rude": -2, "burnt": -2, "awful": -3,
}
NEGATIONS = {"not", "never", "no"}
PUNCTUATION = ".,!?:;\"'()"

TEST_COMMENTS = [
    ("The pasta was delicious and the staff were kind", "HAPPY"),
    ("The queue was slow and the juice was awful", "UNHAPPY"),
    ("Not good, the rice was cold", "UNHAPPY"),
    ("Not bad at all, I will come again", "HAPPY"),
    ("Lunch is at 1 pm on Fridays", "OK"),
    ("Great, they ran out of food again", "UNHAPPY"),
]

def clean_words(comment):
    return [word.lower().strip(PUNCTUATION) for word in comment.split()]

def is_negation(word):
     return word in NEGATIONS or word.endswith("n't")

def analyse(comment):
    analysed = []
    flip = False
    for word in clean_words(comment):
        if is_negation(word):
            flip = True
            continue
        points = LEXICON.get(word, 0)
        if points and flip:
            points = -points
            flip = False
        analysed.append((word, points))
    return analysed

def comment_score(comment):
    return sum(points for _, points in analyse(comment))

def mood(comment):
    return comment_score(comment)

print("\nPART 2: Score")
print(comment_score("Not good, the rice was cold"))





def classify(comment):
    score = mood(comment)
    if score >= 1:
        return "HAPPY"
    if score <= -1:
        return "UNHAPPY"
    return "NEUTRAL"
    return "OK"


print("\nPART 4: Test all comments")
mistakes = 0

def run_tests():
    correct = 0
    for review, expected in TEST_COMMENTS:
        result = classify(review)
        mark = "OK" if result == expected else "XX"
        correct += result == expected
        print(f"{mark}  {result:<8}  score={mood(review):>3}  {review}")
    print(f"\nAccuracy: {correct}/{len(TEST_COMMENTS)}")


    run_tests()
    print("\nType a review to check it, or 'quit' to stop.")
    while True:
        review = input("\n> ")
        if review.strip().lower() == "quit":
            break
        scored = [(w, p) for w, p in analyse(review) if p != 0]
        print(f"{classify(review)} | score: {mood(review)} | words: {scored}")

if __name__ == "__main__":
    run_tests()
    print("\nType a review to check it, or 'quit' to stop.")
    while True:
        review = input("\n> ")
        if review.strip().lower() == "quit":
            break
        scored = [(w, p) for w, p in analyse(review) if p != 0]
        print(f"{classify(review)} | score: {mood(review)} | words: {scored}")

