def main():
    print("Welcome to the OS Match Quiz!")
    print("Answer the following questions to find your ideal operating system.\n")

    score = {"Apple": 0, "Windows": 0, "Linux": 0}

    # Question 1
    print("1. How important is security and privacy to you?")
    print("   a) Very important (Apple)")
    print("   b) Somewhat important (Windows)")
    print("   c) I don’t mind tweaking settings myself (Linux)")
    q1 = input("Choose a, b, or c: ").strip().lower()
    if q1 == "a":
        score["Apple"] += 1
    elif q1 == "b":
        score["Windows"] += 1
    elif q1 == "c":
        score["Linux"] += 1

    # Question 2
    print("\n2. What do you primarily use a computer for?")
    print("   a) Creative work (Apple)")
    print("   b) Gaming & office work (Windows)")
    print("   c) Programming & server hosting (Linux)")
    q2 = input("Choose a, b, or c: ").strip().lower()
    if q2 == "a":
        score["Apple"] += 1
    elif q2 == "b":
        score["Windows"] += 1
    elif q2 == "c":
        score["Linux"] += 1

    # Determine the best OS based on scores
    best_os = max(score, key=score.get)
    print(f"\nYour ideal operating system is: {best_os}")

if __name__ == "__main__":
    main()
