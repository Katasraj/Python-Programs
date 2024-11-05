import logging
from logging import basicConfig

basicConfig(level=logging.INFO,filename="basic_log.log",filemode='w',
            format="%(asctime)s - %(levelname)s - %(message)s")

x = 2

logging.info(f"The value of x is {x}")

try:
    1/0
except ZeroDivisionError as e:
    logging.exception("ZeroDivisionError")


# logging.debug("debug")
# logging.info("info")
# logging.critical("critical")
# logging.warning("warning")
# logging.error("error")



