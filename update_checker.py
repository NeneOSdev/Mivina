import requests

LATEST_VERSION_URL = 'https://raw.githubusercontent.com/NeneOSdev/Mivina/main/version.txt'
def get_latest_version():
    response = requests.get(LATEST_VERSION_URL)
    # ^^ тут мы считываем файл из LATEST_VERSION_URL и сохраняем ответ в response
    return response.text.strip() # возвращаем текст из ответа

# функция проверки обновлений
def check_updates(current_version):
    latest_version = get_latest_version()
    if latest_version != current_version:
        print(f'Your version is outdated! {latest_version} is available.')