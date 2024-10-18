import os
from dotenv import load_dotenv

load_dotenv()

class Credentials:
     if os.environ["STAGE"] == "prod":
         LOGIN = os.getenv("PROD_LOGIN")
         PASSWORD = os.getenv("PROD_PASSWORD")
     elif os.environ["STAGE"] == "qa":
         LOGIN = os.getenv("QA_LOGIN")
         PASSWORD = os.getenv("QA_PASSWORD")