import logging

# Create a logger specific to your module
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a handler (e.g. console output)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Create and attach a formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Attach handler to your logger
logger.addHandler(console_handler)

# Prevent logs from propagating to the root logger
logger.propagate = False
