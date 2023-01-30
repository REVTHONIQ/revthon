from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID =29112329
    API_HASH = "c99a62ee1c3c5afc3490cfaf7bd52d22"
    # the name to display in your alive message
    ALIVE_NAME = "timo"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://sulwofpj:yxoskMUv6cyBEaMuavtQsNia2HeOcG6K@mouse.db.elephantsql.com/sulwofpj"
    # After cloning the repo and installing requirements do python3 telesetup.py an fill that value with this
    STRING_SESSION = "1ApWapzMBuxC7W_gA5EwROFY-gV8sR8fgfk59VZwnRQHgQvmoHisHlFBx9XXQvMVeWCdLXLIZuQXZ_aQ4scf99cIhJHncujNoAAvLn9Jlm9-LBi-qOIXXnjahLlXTPsO_K9WtHFGkHu1QlOcBYRTL9Iocy4z1qz12LihJrNr4YrEx-J5EE6RQXe0OHWspDURwvIVrnkRuve-xb7Y8qysZ1-KDQRxzqhf0BVlOmC9KZIFPnN6vBu4gJ7rN3P8naJFqBa2UdNzH0M69o7s01kZYSVZpgtnWwpR4JC0kDpgIygfQOcPWfNyA7XMIoETHb3IHDaHChTWcoAwm7_EsHcRkd6Whb3PQWfo="
    # create a new bot in @botfather and fill the following vales with bottoken and username respectively
    TG_BOT_TOKEN = "1745605169:AAEsNvIS3zqP9sAlbnNmkq6wcUuy5YHbbr8"
    TG_BOT_USERNAME = "@L_LIZABOT"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -100
    # command handler
    COMMAND_HAND_LER = "."
    # sudo enter the id of sudo users userid's in that array
    SUDO_USERS = []
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
