from config import Config
from core import execute_task

def main():
    print(f'Starting {Config.APP_NAME}...')
    result = execute_task()
    print('Execution Result:', result)

if __name__ == '__main__':
    main()
