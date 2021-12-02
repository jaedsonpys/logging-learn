import logging

logging.basicConfig(
    level=logging.DEBUG, # nivel
    filemode='w',
    filename='app.log',
    format='[%(asctime)s] %(name)s: %(levelname)s - %(message)s'
)

logging.debug('Isso é um debug')
logging.error('Isso é um erro')
logging.critical('Isso é um erro crítico!')
logging.info('Isso é uma informação')
logging.warning('Isso é um alerta')