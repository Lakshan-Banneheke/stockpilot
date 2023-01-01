from typing import Dict
from app.utils.db_access import db_action


def test_db_insert_delete_one():
    response01 = db_action("insert_one",[{"name_id":"nimal","age":23,"email":"nimal@skl.com"},"test"],"admin")
    response = db_action("remove_one",[{"name_id":"nimal"},"test"],"admin")
    assert response.deleted_count == 1


def test_db_insert_delete_one_authoritycheck():
    response01 = db_action("insert_one",[{"name_id":"nimal","age":23,"email":"nimal@skl.com"},"test"],"admin")
    response = db_action("remove_one",[{"name_id":"nimal"},"test"],"general")
    assert response == "Error"
    response = db_action("remove_one",[{"name_id":"nimal"},"test"],"admin")


def test_db_insert_authoritycheck():
    response = db_action("insert_one",[{"name_id":"nimal","age":23,"email":"nimal@skl.com"},"test"],"general")
    assert response == "Error"


def test_db_insert_delete_many():
    reponse01 = db_action("insert_many",[[{"name_id":"nimal","age":23,"email":"nimal@skl.com"},{"name_id":"nimal","age":24,"email":"niamal@skl.com"}],"test"],"admin")
    response = db_action("remove_many",[{"name_id":"nimal"},"test"],"admin")
    assert response.deleted_count == 2


def test_db_read_one():
    reponse01 = db_action("insert_one",[{"name_id":"nimal","age":23,"email":"nimal@skl.com"},"test"],"admin")
    response02 = db_action("read_one",[{"name_id":"nimal"},"test"],"admin")
    response03 = db_action("read_one",[{"name_id":"nimal"},"test"],"general")
    assert response02['name_id'] == "nimal"
    assert response03['name_id'] == "nimal"

    db_action("remove_one",[{"name_id":"nimal"},"test"],"admin")


def test_db_update_one():
    response01 = db_action("insert_one",[{"name_id":"nimal","age":23,"email":"nimal@skl.com"},"test"],"admin")
    req_doc = {"name_id":"nimal"}
    new_data = {"$set": {"age": 500}}
    response = db_action("update_one", [req_doc, new_data, "test"], "admin")
    assert response.modified_count == 1
    response = db_action("remove_many",[{"name_id":"nimal"},"test"],"admin")


def test_db_count():
    reponse01 = db_action("insert_many",[[{"name_id":"nimal","age":23,"email":"nimal@skl.com"},{"name_id":"nimal","age":24,"email":"niamal@skl.com"}],"test"],"admin")
    response = db_action("count",[{"name_id":"nimal"},"test"],"admin")
    assert response == 2
    response = db_action("remove_many",[{"name_id":"nimal"},"test"],"admin")


def test_db_last_item():
    reponse01 = db_action("insert_many",[[{"name_id":"nimal","age":23,"email":"nimal@skl.com"},{"name_id":"nimal","age":24,"email":"niamal@skl.com"},{"name_id":"nimali","age":26,"email":"nimali@skl.com"}],"test"],"admin")
    response = db_action("find_last_entry",["test"],"admin")
    assert len(response) == 1
    assert isinstance(response[0],Dict)
    assert response[0]["name_id"] == "nimali"
    response = db_action("remove_many",[{"name_id":"nimal"},"test"],"admin")
    response = db_action("remove_many",[{"name_id":"nimali"},"test"],"admin")
