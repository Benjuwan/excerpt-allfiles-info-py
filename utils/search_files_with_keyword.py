import os
import sys
from pathlib import Path

from utils.process_text_files import process_text_files
from utils.process_image_files import process_image_files
from ext_constants import TEXT_EXTENSIONS, IMAGE_EXTENSIONS


def get_all_files(directory: str) -> list[str]:
    """
    指定ディレクトリ配下の全ファイルパスを再帰的にリストアップ
    """
    p = Path(directory)
    # f がファイルかどうかを判定（ディレクトリを除外）し、指定ディレクトリ配下の全ファイルを検出して、各ファイルパスの文字列リストとして返す
    return [str(f) for f in p.rglob("*") if f.is_file()]


def _get_file_type(file_path: str) -> str:
    """
    ファイルパスから種別を返す（text/image/other）
    """
    ext = Path(file_path).suffix.lower()
    if ext in TEXT_EXTENSIONS:
        return "text"
    elif ext in IMAGE_EXTENSIONS:
        return "image"
    else:
        return "other"


def search_files_with_keyword(
    directory: str, keyword: str, image_analyzer
) -> list[dict]:
    """
    ディレクトリ配下のファイルを走査し、
    テキストはキーワード抽出、画像はAI解析、その他はスキップ。
    戻り値: [{type, file, path, result}] のリスト
    """
    if not os.path.isdir(directory):
        sys.exit(f"[ERROR] 指定ディレクトリが存在しません: {directory}")

    print(f"[INFO] ファイル検索開始: {directory}")

    # 全ファイルを取得
    all_files = get_all_files(directory)
    print(f"[INFO] 検索対象ファイル数: {len(all_files)}件")

    # ファイル種別を分類
    text_files = []
    image_files = []
    other_files = []

    for file_path in all_files:
        file_type = _get_file_type(file_path)
        if file_type == "text":
            text_files.append(file_path)
        elif file_type == "image":
            image_files.append(file_path)
        else:
            other_files.append(file_path)

    print(
        f"[INFO] テキストファイル: {len(text_files)}件, 画像ファイル: {len(image_files)}件, その他: {len(other_files)}件"
    )

    results = []

    # テキストファイルの処理（extendメソッドにより process_text_files関数の処理結果のイテラブルを追加）
    results.extend(process_text_files(text_files, keyword))
    # 画像ファイルの処理
    results.extend(process_image_files(image_files, keyword, image_analyzer))

    print(f"\n[INFO] 検索完了: 合計{len(results)}件の結果")
    return results
