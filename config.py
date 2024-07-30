from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

BEDROCK_AWS_ACCESS_KEY = os.getenv('BEDROCK_AWS_ACCESS_KEY')
BEDROCK_AWS_SECRET_KEY = os.getenv('BEDROCK_AWS_SECRET_KEY')

NEO4J_URI = os.getenv('NEO4J_URI')
NEO4J_USER = os.getenv('NEO4J_USER')
NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD')






