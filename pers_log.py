# log com manipuladores

import logging

# __name__ mostrará o nome do arquivo
logger = logging.getLogger(__name__)

# criando handlers

f_handler = logging.FileHandler('file.log', mode='w') # ou logging.FileHandler para arquivos
f_handler.setLevel(logging.DEBUG)

# criando formatter
f_formatter = logging.Formatter('[%(asctime)s] %(name)s: %(levelname)s - %(message)s')
f_handler.setFormatter(f_formatter)

# adicionando handler ao logger

logger.addHandler(f_handler)
logger.critical('The server is offline')
logger.critical('The server is offline')
logger.critical('The server is offline')
logger.critical('The server is offline')
logger.critical('The server is offline')
logger.critical('The server is offline')