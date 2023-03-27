
import tda.auth
##chrome_driver_binary =  "/usr/local/bin/chromedriver"
##driver = webdriver.Chrome(chrome_driver_binary, options=Options())
from selenium import webdriver
driver = webdriver.Chrome()
##from selenium.webdriver.chrome.options import Options
token_path='/home/az2/Downloads/35'
api_key='CLIFWQTIZ6EBH0BD3BVY4TASYUXMINAN'
redirect_uri='https://127.0.0.1'
TOKEN_ENDPOINT = 'https://api.tdameritrade.com/v1/oauth2/token'

def client_from_token_file(token_path, api_key, asyncio=False, enforce_enums=True):
    '''
    Returns a session from an existing token file. The session will perform
    an auth refresh as needed. It will also update the token on disk whenever
    appropriate.
    :param token_path: Path to an existing token. Updated tokens will be written
                       to this path. If you do not yet have a token, use
                       :func:`~tda.auth.client_from_login_flow` or
                       :func:`~tda.auth.easy_client` to create one.
    :param api_key: Your TD Ameritrade application's API key, also known as the
                    client ID.
    :param asyncio: If set to ``True``, this will enable async support allowing
                    the client to be used in an async environment. Defaults to
                    ``False``
    :param enforce_enums: Set it to ``False`` to disable the enum checks on ALL
                          the client methods. Only do it if you know you really
                          need it. For most users, it is advised to use enums
                          to avoid errors.
    '''

    load = __token_loader(token_path)

    return client_from_access_functions(
        api_key, load, __update_token(token_path), asyncio=asyncio,
        enforce_enums=enforce_enums)







tda.auth.easy_client('CLIFWQTIZ6EBH0BD3BVY4TASYUXMINAN','/home/az2/Downloads/35','https://127.0.0.1')
b=tda.auth.client_from_login_flow(driver, 'CLIFWQTIZ6EBH0BD3BVY4TASYUXMINAN', \
                                  'https://127.0.0.1', token_path, redirect_wait_time_seconds=0.1, \
                                  max_waits=3000, asyncio=False, token_write_func=None, enforce_enums=True)



