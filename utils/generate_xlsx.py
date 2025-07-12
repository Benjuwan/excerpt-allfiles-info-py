import openpyxl
from openpyxl.styles import Alignment


def generate_search_result_xlsx(
    results: list[dict], output_path: str = "search_result.xlsx"
):
    """
    検索結果リストをエクセル出力
    テキスト: ファイル名, パス, 行番号, 行内容
    画像: ファイル名, パス, 解析テキスト
    """
    wb = openpyxl.Workbook()
    ws = wb.active

    if ws is None:
        return

    ws.title = "検索結果"

    # ヘッダー
    ws.append(["種別", "ファイル名", "パス", "行番号", "内容/解析結果"])

    for item in results:
        if item["type"] == "text":
            for match in item["matches"]:
                ws.append(
                    [
                        "text",
                        item["file"],
                        item["path"],
                        match["line_number"],
                        match["line"],
                    ]
                )
        elif item["type"] == "image":
            ws.append(["image", item["file"], item["path"], "", item["analysis"]])

    # 列幅調整
    ws.column_dimensions["A"].width = 8
    ws.column_dimensions["B"].width = 30
    ws.column_dimensions["C"].width = 60
    ws.column_dimensions["D"].width = 10
    ws.column_dimensions["E"].width = 60

    # 折り返し
    for row in ws.iter_rows(min_row=2, min_col=5, max_col=5):
        for cell in row:
            cell.alignment = Alignment(wrap_text=True)

    wb.save(output_path)
    print(f"エクセル出力完了: {output_path}")
