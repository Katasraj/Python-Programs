import logging

values = ['hi',10,5,6,0,9,8,2,'hello']

for value in values:
    try:
        print(value/2)
    except Exception as e:
        logging.exception((e))
    except ZeroDivisionError as e:
        logging.exception(e)
    except ValueError as e:
        logging.exception(e)
    finally:
        pass
