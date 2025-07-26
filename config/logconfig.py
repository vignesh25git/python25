import logging

# Basic logging config
logging.basicConfig(
    level=logging.DEBUG,  # capture all levels
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',   # save to file
    filemode='w'          # overwrite file each time
)
