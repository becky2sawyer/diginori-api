from diginori_api.database.crud import select


def test_predict_lotto_number():
    r = select(sql="SELECT * from test", db="../../../sqllite.db")
    assert len(r) > 0
