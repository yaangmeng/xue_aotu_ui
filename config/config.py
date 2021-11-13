import os

DRIVER_PATH = "D:\\Software\\chromedriver.exe"
BROWSER_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
TEST_CASE = os.path.join( os.path.dirname(__file__),"../test_case")

GY_UI_URL = '192.168.6.80:2002'

GY_DB_MALL = {
    'host': '192.168.6.80',
    'port': 3306,
    'db': 'uni_user_test',
    'user': 'root',
    'passwd': 'Tsl@2019',
    'charset': 'utf8'                       
}											
