from dotenv import load_dotenv
import os

load_dotenv()

BEDROCK_AWS_ACCESS_KEY = os.getenv('BEDROCK_AWS_ACCESS_KEY')
BEDROCK_AWS_SECRET_KEY = os.getenv('BEDROCK_AWS_SECRET_KEY')
