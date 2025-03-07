from classes.classmetinbot import MetinBot
from util.logger import get_logger

MainLogger= get_logger("MainLogger")


if __name__ == "__main__":
    MainLogger.info("Bot iniciado")
    bot = MetinBot()
    bot.iniciar()