def get_spam_keywords():
    return [
        "free",
        "winner",
        "congratulations",
        "you've won",
        "prize",
        "cash bonus",
        "guaranteed",
        "risk-free",
        "act now",
        "limited time",
        "urgent",
        "click here",
        "claim now",
        "no obligation",
        "special offer",
        "exclusive offer",
        "make money",
        "work from home",
        "earn money",
        "double your money",
        "credit card",
        "verify your account",
        "confirm your information",
        "account suspended",
        "wire transfer",
        "gift card",
        "cryptocurrency",
        "lottery",
        "refund",
        "free trial"
    ]


def calculate_spam_score(email, keywords):
    email_lower = email.lower()
    score = 0
    matches = []

    for keyword in keywords:
        if keyword in email_lower:
            score += 1
            matches.append(keyword)

    return score, matches


def get_spam_likelihood(score):
    if score == 0:
        return "Very unlikely to be spam"
    elif score <= 3:
        return "Unlikely to be spam"
    elif score <= 6:
        return "Possibly spam"
    elif score <= 10:
        return "Likely spam"
    else:
        return "Very likely to be spam"


def main():
    print("===================================")
    print("       SPAM EMAIL DETECTOR")
    print("===================================")

    email = input("\nEnter the email message to scan:\n")

    keywords = get_spam_keywords()

    score, matches = calculate_spam_score(email, keywords)

    likelihood = get_spam_likelihood(score)

    print("\n===================================")
    print("           SCAN RESULTS")
    print("===================================")

    print("Spam Score:", score)
    print("Likelihood:", likelihood)

    if matches:
        print("\nWords/phrases that triggered the spam score:")

        for keyword in matches:
            print("-", keyword)
    else:
        print("\nNo spam keywords or phrases were found.")

    print("\n===================================")


main()

