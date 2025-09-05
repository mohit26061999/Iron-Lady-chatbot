def chatbot():
    faqs = {
        "programs": "Iron Lady offers leadership programs such as Self-Leadership, Career Acceleration, and Executive Leadership.",
        "duration": "Programs range from 6 weeks to 6 months depending on the track.",
        "mode": "Iron Lady offers both online and offline programs.",
        "certificate": "Yes, certificates are provided upon completion.",
        "mentors": "Mentors include industry leaders, certified trainers, and successful women professionals."
    }
    print('Welcome to chatbot! Type exit to quit')
    while True:
        user_input = input('you: ').lower()
        if user_input== 'exit':
            print('Goodbye!')
            break
        elif "program" in user_input:
            print("Chatbot:", faqs["programs"])
        elif "duration" in user_input:
            print("Chatbot:", faqs["duration"])
        elif "online" in user_input or "offline" in user_input or "mode" in user_input:
            print("Chatbot:", faqs["mode"])
        elif "certificate" in user_input:
            print("Chatbot:", faqs["certificate"])
        elif "mentor" in user_input or "coach" in user_input:
            print("Chatbot:", faqs["mentors"])
        else:
            print("Chatbot: Sorry, I don’t know that. Try asking about programs, duration, mode, certificate, or mentors.")

chatbot()