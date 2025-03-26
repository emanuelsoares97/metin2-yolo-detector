from classes.classmetinbot import MetinBot
from util.logger import get_logger

logger= get_logger(__name__)


if __name__ == "__main__":
    logger.info("Bot iniciado")
    bot = MetinBot()
    bot.iniciar()