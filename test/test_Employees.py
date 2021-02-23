# **********************************************
# pytest fixtures
# to provide  a fixed  baseline upon which tests can repeatedly executed

# @pytest.fixture()
# -->Execute specific method before every test method

# @pytest.yield_fixtue()
# -->Execute specific method before and after every test method

# parallel -Execution:
# 1. pip install pytest-xdist
# 2.pytest -n <threadcount>


# XML Report:(Techinical report  only Technical team knows)
# pytest -v -s  --junitxml="name.xml"


# HTML-Report:
# pip install pytest -html
# pytest  -v -s --html=reportname.html

 # @pytest.fixture()
# -->Execute specific method before every test method

# import pytest
#
# @pytest.fixture()
# def setup():
#     print("before exceution of every test method")
#
# def test_reg_facebook(setup):
#     print("facebook registeration")
#
# def test_reg_twitter(setup):
#     print("twitter registeration")
#
# def test_reg_gmail(setup):
#     print("gmail registeration")
#
 # @pytest.yield_fixtue()
# -->Execute specific method before and after every test method
# import pytest
#
# @pytest.yield_fixture()
# def setup():
#     print("before Executing  of every methods ")
#     yield
#     print("after Execution of every methods")
#
# def test_reg_facebook(setup):
#     print("facebook registeration")
#
# def test_reg_twitter(setup):
#     print("twitter registeration")
#
# def test_reg_gmail(setup):
#     print("gamil registration")



