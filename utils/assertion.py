"""
在这里添加各种自定义的断言，断言失败抛出AssertionError就OK。
这个断言传入响应，以及期望的响应码列表，如果响应码不在列表中，则断言失败。
"""


def assertHTTPCode(response, code_list=None):
    res_code = response.status_code
    if not code_list:
        code_list = [200]
    if res_code not in code_list:
        raise AssertionError('响应code不在列表中！')  # 抛出AssertionError，unittest会自动判别为用例Failure，不是Error