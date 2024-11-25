import pytest 

@pytest.fixture
def make_customer_record():
    created_records = []

    def _make_customer_record(name):
        record = name
        created_records.append(record)
        return record

    yield _make_customer_record

    created_records = []


def test_customer_records(make_customer_record):
    customer_1 = make_customer_record("Lisa")
    customer_2 = make_customer_record("Mike")
    customer_3 = make_customer_record("Meredith")

    assert customer_1 == "Lisa"