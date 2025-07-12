import google.generativeai as genai
from PIL import Image


class ImageAnalyzer:
    # 画像解析を行うメソッドを定義
    def images_analyze(self, images_file_path: str, keyword: str) -> str:
        """
        画像ファイルの内容を解析し、キーワードを含むかどうかを判定するインターフェース
        サブクラスで各AIサービスごとに実装します
        """
        # 「NotImplementedError ： このメソッドはサブクラスで必ず実装してください」という意図の例外（raise）を発生させる
        raise NotImplementedError


# class クラス名（基底クラス名） ： ImageAnalyzerクラスの継承
class GeminiImageAnalyzer(ImageAnalyzer):
    def __init__(self, api_key: str):
        # Gemini APIキーで初期化
        self.api_key = api_key
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def images_analyze(self, images_file_path: str, keyword: str) -> str:
        """
        指定した画像ファイルをGemini AIで解析し、
        その内容がキーワードを含むかどうかをAIに判定させて返します
        """
        prompt = f"この画像に『{keyword}』というキーワードが含まれているかどうかをチェックしてください。含まれていれば「画像の〇〇箇所にあります」など画像内での該当箇所を説明し、含まれていなければ「含まない」とだけ明記してください。"
        try:
            img = Image.open(images_file_path)
            response = self.model.generate_content([img, prompt])
            return response.text
        except Exception as e:
            return f"[Geminiエラー] {images_file_path}: {e}"
