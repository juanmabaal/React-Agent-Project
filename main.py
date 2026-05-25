from dotenv import load_dotenv
import os

load_dotenv()

def main():
    print("Hello from langgraph-project!")


if __name__ == "__main__":
    main()
    print(os.getenv('DEEPSEEK_API_KEY'))