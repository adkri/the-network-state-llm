import pyfiglet
from termcolor import colored
from llm_chat.find_best_response import find_best_response


def run_chat_interface():
    # Print ASCII art title
    title = pyfiglet.figlet_format('The Network State LLM Chat', font='slant')
    print(title)

    # Start chat loop
    while True:
        user_input = input(colored('User: ', 'yellow'))
        if user_input.lower() == 'exit':
            print(colored('AI: Goodbye!', 'green'))
            break
        response = find_best_response(user_input)
        print(colored(f'AI: {response}', 'green'))


if __name__ == "__main__":
    run_chat_interface()

