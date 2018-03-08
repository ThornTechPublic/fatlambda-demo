import logging

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s')

logging.info("Fat Lambda started")

# Do some work
