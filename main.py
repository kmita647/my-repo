import functions_framework

@functions_framework.http
def main(request):
    """HTTPリクエストを受け取り、シンプルなメッセージを返す関数です。"""
    return "Hello from GitHub Actions CI/CD!", 200