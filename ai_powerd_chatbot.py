from langchain_ollama import OllamaLLM
llm = OllamaLLM(model='llama3',temperature=0)
faqs = """
You are a helpful chatbot for Iron Lady's leadership programs.
Here are the FAQs you must know:

1. Programs: Iron Lady offers leadership programs such as Self-Leadership, Career Acceleration, and Executive Leadership.
2. Duration: Programs range from 6 weeks to 6 months depending on the track.
3. Mode: Iron Lady offers both online and offline programs.
4. Certificate: Yes, certificates are provided upon completion.
5. Mentors: Mentors include industry leaders, certified trainers, and successful women professionals.

Answer only based on the above information. 
If asked something unrelated, politely say you can only answer questions about Iron Lady programs.
"""
def chatbot():
    print("Iron Lady AI Chatbot! (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye")
            break

        prompt = f"{faqs}\nUser: {user_input}\nAssistant:"
        response = llm.invoke(prompt)


        print("Chatbot:", response)

chatbot()