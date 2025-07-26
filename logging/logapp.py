from config import logconfig
# Basic logging config
import logging

logging.basicConfig(
    level=logging.DEBUG,  # capture all levels
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',   # save to file
    filemode='a'          # overwrite file each time
)

def divide(a, b):
    logging.info(f"Dividing {a} by {b}")
    try:
        result = a / b
        logging.debug(f"Result: {result}")
        return result
    except ZeroDivisionError:
        logging.error("Tried to divide by zero!")
        return None

# Test
divide(10, 2)
divide(10, 0)
