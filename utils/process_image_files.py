from pathlib import Path
from tqdm import tqdm

from ext_constants import IMAGE_EXTENSIONS


def process_image_files(image_files, keyword, image_analyzer):
    """
    画像ファイルリストに対してAI解析を行い、
    解析結果にキーワードが含まれる場合のみ結果をリストで返す
    """
    results = []

    if image_files:
        print(f"\n[INFO] 画像ファイル解析開始 ({len(image_files)}件)")

        for file_path in tqdm(image_files, desc="画像ファイル解析"):
            ext = Path(file_path).suffix.lower()

            if ext in IMAGE_EXTENSIONS:
                print(f"[DEBUG] 解析中: {Path(file_path).name}")
                analysis = image_analyzer.images_analyze(file_path, keyword)

                if keyword in analysis:
                    results.append(
                        {
                            "type": "image",
                            "file": Path(file_path).name,
                            "path": file_path,
                            "analysis": analysis,
                        }
                    )
            else:
                analysis = f"画像データ（{ext}）ではないので処理スキップします"
                continue

        print(f"[INFO] 画像ファイル解析完了: {len(results)}件ヒット")

    return results
