import logging 
logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console = logging.getLogger(__name__)
console.setLevel(logging.ERROR)


# logger.setLevel(level = logging.INFO)
# handler = logging.FileHandler("log.txt")
# handler.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler.setFormatter(formatter)
 
# console = logging.StreamHandler()
# console.setLevel(logging.INFO)
 
# logger.addHandler(handler)
# logger.addHandler(console)
 
# logger.info("Start print log")
# logger.debug("Do something")
# logger.warning("Something maybe fail.")
# logger.info("Finish")