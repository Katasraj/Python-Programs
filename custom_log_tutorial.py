import logging
from logging import basicConfig

basicConfig(level=logging.INFO,filename="custom_log.log",filemode='w',
            format="%(asctime)s - %(levelname)s - %(message)s")


logger = logging.getLogger(__name__)
logger.info("Testing the Custom Logger")

