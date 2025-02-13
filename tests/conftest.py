import pytest
from SingletonMeta import SeleniumDriver
from other_entity.logger import Logger


@pytest.fixture(scope='session', autouse=True)
def browser():
    SeleniumDriver().get_driver()
    yield SeleniumDriver().get_driver()
    SeleniumDriver().get_driver().quit()


@pytest.fixture(scope='function', autouse=True)
def logger(request):
    test_name = request.node.name
    Logger().setup(test_name)
    yield Logger().get_logger()
