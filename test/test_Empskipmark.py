# to skipping the test
# 1.skip
# 2.skip with reason
#3.skip based on condition and reason

#1.@pytest.mark.skip
# 2.@pytest.mark.skip("reason")
# 3.@pytest.mark.skipIf(condition,reason)

# import pytest
#
# def test_login():
#     print("login")
#
# @pytest.mark.skip
# def test_payment():
#     print("payment")
# @pytest.mark.skip("As of now i dont want to book")
# def test_booking():
#     print("booking")
# @pytest.mark.skipif(1==2,reason="condition getting false thats why skipping")
# def test_search():
#     print("search")
# @pytest.mark.skipif(1==1,reason="condition true thats  why skipping")
# def test_online():
#     print("online")
