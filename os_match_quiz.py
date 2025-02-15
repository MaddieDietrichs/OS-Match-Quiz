def main():
    print("Welcome to the OS Match Quiz!")
    print("Answer the following questions to find your ideal operating system.\n")

    # Initialize scores
    score = {"Apple": 0, "Windows": 0, "Linux": 0}

    # List of questions and answers
    questions = [
        ("How important is security and privacy to you?",
         [("Very important", "Apple"), 
          ("Somewhat important", "Windows"), 
          ("I don’t mind tweaking settings myself", "Linux")]),

        ("What do you primarily use a computer for?",
         [("Creative work (photo/video editing, music production)", "Apple"), 
          ("Gaming & office work", "Windows"), 
          ("Programming & server hosting", "Linux")]),

        ("Do you prefer a simple, user-friendly system or one you can customize?",
         [("I want something that just works (Apple)", "Apple"),
          ("I like balance: simple but still customizable (Windows)", "Windows"),
          ("I love deep customization (Linux)", "Linux")]),

        ("What is your budget for a computer?",
         [("I don’t mind paying a premium for quality (Apple)", "Apple"),
          ("I want good performance for a reasonable price (Windows)", "Windows"),
          ("I prefer free/open-source options and flexibility (Linux)", "Linux")]),

        ("How often do you troubleshoot or fix computer issues?",
         [("Rarely, I want everything to work smoothly (Apple)", "Apple"),
          ("Sometimes, I can handle minor issues (Windows)", "Windows"),
          ("All the time, I enjoy problem-solving (Linux)", "Linux")]),

        ("Which best describes your work style?",
         [("I focus on design, art, or video editing (Apple)", "Apple"),
          ("I need Microsoft Office and work apps (Windows)", "Windows"),
          ("I use command-line tools, servers, or development tools (Linux)", "Linux")]),

        ("Do you like playing video games on your computer?",
         [("Not really, I mostly use my computer for other things (Apple)", "Apple"),
          ("Yes! I want access to all major games (Windows)", "Windows"),
          ("I play some games, but mostly indie or open-source ones (Linux)", "Linux")]),

        ("What is your opinion on open-source software?",
         [("I don't care, I just need my computer to work (Apple)", "Apple"),
          ("I use some open-source apps but rely on commercial software (Windows)", "Windows"),
          ("I love open-source and prefer free software (Linux)", "Linux")]),

        ("How often do you upgrade or buy new hardware?",
         [("I buy a new device every few years (Apple)", "Apple"),
          ("I upgrade or buy new parts when needed (Windows)", "Windows"),
          ("I tinker with my setup and often change components (Linux)", "Linux")]),

        ("Which ecosystem do you prefer?",
         [("I want everything to integrate seamlessly with my phone and tablet (Apple)", "Apple"),
          ("I use a mix of different brands and apps (Windows)", "Windows"),
          ("I like having full control over my system with no locked ecosystem (Linux)", "Linux")])
    ]

    # Loop through the questions
    for idx, (question, choices) in enumerate(questions, start=1):
        print(f"\n{idx}. {question}")
        for i, (option_text, os_type) in enumerate(choices, start=1):
            print(f"   {i}) {option_text}")

        # Get user input
        while True:
            answer = input("Choose 1, 2, or 3: ").strip()
            if answer in ["1", "2", "3"]:
                selected_os = choices[int(answer) - 1][1]
                score[selected_os] += 1
                break
            else:
                print("Invalid choice! Please enter 1, 2, or 3.")

    # Determine the best OS based on scores
    sorted_scores = sorted(score.items(), key=lambda x: x[1], reverse=True)
    best_os = sorted_scores[0][0]
    second_best_os = sorted_scores[1][0]

    # Detailed explanations for each OS
    explanations = {
        "Apple": "Apple's macOS is known for its security, smooth user experience, and tight integration with iPhones, iPads, and Apple software. It's a great choice for creative professionals, designers, and those who value reliability over customization.",
        "Windows": "Windows is the most widely used operating system, offering strong compatibility for gaming, office work, and business applications. It provides a mix of user-friendliness and customization, making it a good all-around choice.",
        "Linux": "Linux is the most customizable and flexible operating system, great for programmers, developers, and tech enthusiasts who love open-source software. It's ideal for running servers, coding, and having full control over your system."
    }

    # Display detailed results
    print("\n✨ **Your OS Match Results** ✨")
    print(f"\n✅ Your best-matching operating system is: **{best_os}**")
    print(f"   {explanations[best_os]}\n")

    print(f"💡 Your second-best match is: **{second_best_os}**")
    print(f"   {explanations[second_best_os]}\n")

    # Display score summary
    print("🔎 **Your Full OS Compatibility Scores:**")
    for os_name, os_score in sorted_scores:
        print(f"   {os_name}: {os_score} points")

if __name__ == "__main__":
    main()
