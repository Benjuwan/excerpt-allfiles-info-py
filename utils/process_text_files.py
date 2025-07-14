from pathlib import Path
from tqdm import tqdm

from utils.text_extractors import extract_text_matches


def process_text_files(text_files, keyword):
    """
    テキストファイルリストに対してキーワード検索を行い、
    ヒットした結果をリストで返す
    """
    results = []

    if text_files:
        print(f"\n[INFO] テキストファイル検索開始 ({len(text_files)}件)")
        for file_path in tqdm(text_files, desc="テキストファイル検索"):
            matches = extract_text_matches(file_path, keyword)
            if matches:
                results.append(
                    {
                        "type": "text",
                        "file": Path(file_path).name,
                        "path": file_path,
                        "matches": matches,
                    }
                )
        print(f"[INFO] テキストファイル検索完了: {len(results)}件ヒット")

    return results
