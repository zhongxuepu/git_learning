import os
import logging

# try:
scene = "000000000"
x = os.listdir("./111")
logging.basicConfig(filename='./ok.log', format='%(asctime)s %(levelname)s: %(message)s', encoding='utf-8', level=logging.DEBUG)
logging.info("%s right!", scene)
# except:
#     logging.basicConfig(filename='./example.log', format='%(asctime)s %(levelname)s: %(message)s', encoding='utf-8', level=logging.DEBUG)
#     logging.error('%s calc errorxxxxx', scene)