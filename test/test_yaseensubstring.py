# Execute subset of test suite
# 1.select the tests to run based on substring matching of test name
# syntax:
# pytest  -k <substring> -v

# 2.select tests groups to run based on the markers applied
# steps:
# 1.import pytest
# 2.mark group name for each test method
# [@pytest.mark<groupname>]
# syntax:
# pytest -m <groupname> -v
#
#
#
# import pytest
#
# @pytest.mark.E2E
# @pytest.mark.smoke
# def test_reg_facebook():
#     print("facebook registeartion")
#
# @pytest.mark.E2E
# @pytest.mark.reg
# def test_reg_twitter():
#     print("twitter registeration")
#
# @pytest.mark.E2E
# @pytest.mark.sanity
# def test_reg_gmail():
#     print("gmail registeration")