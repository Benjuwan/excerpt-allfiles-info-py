# excerpt-allpages-info-py

指定したディレクトリ内のファイルを検索し、テキストファイルからキーワードを抽出、画像ファイルをAI解析して結果をExcelに出力するシステムです。<br>`search_result.xlsx`という検索結果のExcelファイルが出力されます。

> [!NOTE]
> Cursor の Agent Mode（Auto）を通じたAI駆動開発の機能となります

## ユースケース

- **文書管理**: 大量の文書（PDF、Excel、Word、PowerPoint等）から特定のキーワードを含むファイルを検索
    - `.txt`, `.md`, `.json`, `.csv`, `.pdf`, `.xlsx`, `.docx`, `.pptx`
- **画像整理**: 画像ファイルの内容を自動解析して分類
    - `.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`
- **データ抽出**: 複数のファイル形式から情報を統一的に抽出
- **レポート作成**: 検索結果をExcelで整理してレポート作成（`search_result.xlsx`）

## 使い方
### 仮想環境を構築（初回のみ）
ターミナル／コマンドプロンプトを開いてルート（ファイルの最上階層）にいる状態で以下フローを実行
```bash
mkdir venv # venv ディレクトリ（仮想環境ディレクトリ）を作成
cd venv    # 作成した仮想環境ディレクトリ（`venv`）へ移動

# 新しい仮想環境を作成してアクティベート
# WindowsOS の場合: python -m venv env
python3 -m venv env # env{は仮想環境名}

# WindowsOS の場合: env\Scripts\activate
source env/bin/activate

# 仮想環境をアクティベートした状態で、パス指定して`requirements.txt`から各種ライブラリをインストール
# `../requirements.txt`なのは`requirements.txt`がルート直下にあるため
pip install -r ../requirements.txt
```

> [!NOTE]
> インポートしたライブラリを`requirements.txt`に保存する場合は以下コマンドを実行
```bash
# 一階層前にある requirements.txt にライブラリ情報を保存
python -m pip freeze > requirements.txt
```

### 仮想環境を立ち上げる（初回以降）
```bash
# 1. 仮想環境を格納しているディレクトリへ移動（存在しない場合は上記を参照に新規作成）
cd venv

# 2. 仮想環境をアクティベート
# WindowsOS の場合: env\Scripts\activate
source env/bin/activate
```

### ルートへ移動して実行
必ず仮想環境をアクティベートした状態で以下フローを実行
```bash
# ※必要に応じて以下コマンドを実行
# 仮想環境をアクティベートした直後だと`venv`ディレクトリへいるためルートに移動する
cd ../

# WindowsOS の場合:
# python main.py

python3 main.py
```

## 注意事項

- 大量のファイルを処理する場合は時間がかかる場合があります
- 画像解析にはGemini APIの利用料金が発生します
- 機密情報を含むファイルの処理には十分注意してください
