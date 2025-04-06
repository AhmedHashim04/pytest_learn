from fullname_func import get_full_name

def test_get_full_name():
    full_name = get_full_name('john', 'doe')
    assert full_name == 'John Doe', f"Expected 'John Doe', but got {full_name}"