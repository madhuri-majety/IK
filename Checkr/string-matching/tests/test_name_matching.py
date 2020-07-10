from string_matching import name_matching as nm
import pytest

@pytest.fixture()
def known_aliases():
     known_aliases = ['Alphonse Gabriel Capone', 'Alphonse F Capone']

     return known_aliases

def test_exact_match():
    known_aliases = ['Alphonse Gabriel Capone', 'Al Capone']

    assert nm.name_match(known_aliases, 'Alphonse Gabriel Capone') == True, "Should be True"
    assert nm.name_match(known_aliases, 'Alphonse Capone') == True, "Should be True"
    assert nm.name_match(known_aliases, 'Alphonse Francis Capone') == False, "Should be False"

def test_middle_name_missing_on_alias():
    known_aliases = ['Alphonse Capone']

    assert nm.name_match(known_aliases, 'Alphonse Gabriel Capone') == True, "Should be True"
    assert nm.name_match(known_aliases, 'Alphonse Francis Capone') == True, "Should be True"
    assert nm.name_match(known_aliases, 'Alexander Capone') == False, "Should be False"

def test_middle_name_missing_on_record():
    known_aliases = ['Alphonse Gabriel Capone']

    assert nm.name_match(known_aliases, 'Alphonse Capone') == True, "Should be True"
    assert nm.name_match(known_aliases, 'Alphonse Francis Capone') == False, "Should be False"
    assert nm.name_match(known_aliases, 'Alexander Capone') == False, "Should be False"

def test_more_middle_name():
    known_aliases = ['Alphonse Gabriel Capone', 'Alphonse Francis Capone']

    assert nm.name_match(known_aliases, 'Alphonse Gabriel Capone') == True, "Should be True"
    assert nm.name_match(known_aliases, 'Alphonse Francis Capone') == True, "Should be True"
    assert nm.name_match(known_aliases, 'Alphonse Edward Capone') == False, "Should be False"

@pytest.mark.parametrize("record_name, status", [('Alphonse G Capone', True), ('Alphonse Francis Capone', True), ('Alphonse E Capone', False), ('Alphonse Edward Capone', False), ('Alphonse Gregory Capone', False)])
def test_middle_name_matches_initial(known_aliases, record_name, status):
    assert nm.name_match(known_aliases, record_name) == status, "Should be " + str(status)




