import os

from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = os.environ["BOT_TOKEN"]
ADMINS = os.environ["ADMINS"]
