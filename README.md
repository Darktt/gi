# gi — Git Ignore Generator

從 [Toptal gitignore API](https://www.toptal.com/developers/gitignore/api/) 自動產生 `.gitignore` 檔案的命令列工具。

## 使用方式

```bash
gi python,java,macos
```

執行後會在當前目錄產生 `gitignore` 檔案。

關鍵字可至 https://www.toptal.com/developers/gitignore 查詢支援的語言與環境。

## 安裝

將 `dist/gi/gi` 複製至 PATH 路徑下：

```bash
cp dist/gi/gi /usr/local/bin/gi
```

## 開發

```bash
# 建立並啟動虛擬環境
python3.13 -m venv venv
source venv/bin/activate

# 安裝依賴
pip install requests pyinstaller

# 直接執行
python gi.py python,macos

# 重新打包為可執行檔
pyinstaller gi.spec
```
