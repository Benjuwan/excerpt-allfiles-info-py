import os
import time
from dotenv import load_dotenv
from analyzers.gemini import GeminiImageAnalyzer
from utils.generate_xlsx import generate_search_result_xlsx
from utils.search_files_with_keyword import search_files_with_keyword


def main():
    # .envからAPIキー取得
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("[ERROR] .envにGEMINI_API_KEYが設定されていません")
        return

    # ユーザー入力
    directory = input("検索対象ディレクトリを入力してください（例: ./file）: ").strip()
    keyword = input("検索キーワードを入力してください: ").strip()
    if not directory or not keyword:
        print("[ERROR] ディレクトリ・キーワードは必須です")
        return

    print(f"\n{'=' * 50}")
    print(f"検索設定")
    print(f"ディレクトリ: {directory}")
    print(f"キーワード: {keyword}")
    print(f"{'=' * 50}\n")

    analyzer = GeminiImageAnalyzer(api_key=api_key)
    print(f"[INFO] Gemini AI初期化完了")

    start_time = time.time()
    results = search_files_with_keyword(directory, keyword, analyzer)
    end_time = time.time()

    print(f"\n{'=' * 50}")
    print(f"検索結果サマリー")
    print(f"処理時間: {end_time - start_time:.2f}秒")
    print(f"ヒット件数: {len(results)}件")
    print(f"{'=' * 50}\n")

    print("[INFO] Excelファイル出力開始...")
    generate_search_result_xlsx(results)
    print("[INFO] 処理完了")


if __name__ == "__main__":
    main()
