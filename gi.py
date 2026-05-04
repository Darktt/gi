import sys
import requests

# 從命令和取得關鍵字
# https://www.toptal.com/developers/gitignore/api/


def main():
    if len(sys.argv) < 2:
        print("請輸入關鍵字，例如：python gi.py python,java")
        return
    keywords = sys.argv[1]
    url = f"https://www.toptal.com/developers/gitignore/api/{keywords}"
    response = requests.get(url)
    if response.status_code == 200:
        with open('gitignore', 'w', encoding='utf-8') as f:
            f.write(response.text)
        print("gitignore 已下載完成")
    else:
        print("下載失敗，請檢查關鍵字是否正確")


if __name__ == "__main__":
    main()
