
# import logging
#
# logging.basicConfig(level = logging.DEBUG,
#                     filename = "animal.log",
#                     format = "%(asctime)s - %(levelname)s - %(message)s"
#                     )
#
# logging.debug("Debug Message")
# logging.info("Info Message")
# logging.warning("Warning Message")
# logging.error("Error Message")
# logging.critical("Critical Message")

# try:
#     1/0
# except ZeroDivisionError as error:
#     logging.exception(error)
#


import logging
logging.basicConfig(level = logging.DEBUG,
                    filename = "animal.log",
                    format = "%(asctime)s - %(levelname)s - %(message)s"
                    )

class Pet:
    def __init__(self,type,age):
        self.type = type
        self.age = age

        logging.info(f"Created a new Pet OBject: {type} {age}")

pet_1 = Pet("Cat",8)
pet_2 = Pet("Dog",3)

















