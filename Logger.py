import logging

#create a logger
logger = logging.getLogger('mylogger')
#set logger level
logger.setLevel(logging.ERROR)
#or set one of the following level
#logger.setLevel(logging.WARNING)
#logger.setLevel(logging.INFO)
#logger.setLevel(logging.DEBUG)

handler = logging.FileHandler('mylog.log')
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

#write a error message
logger.error('This is an ERROR message')
