from django_ltree.fields import PathValue
from django_ltree.paths import PathGenerator


def test_path_generator_iterable(db):
    path_gen = PathGenerator()
    assert iter(path_gen) is path_gen

def test_path_generator_next(db):
    path_gen = PathGenerator(label_size=1, prefix=["prefix"])
    expected_alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # sourcery skip: no-loop-in-tests
    for expected_label in expected_alphabet:
        assert path_gen.__next__() == PathValue(["prefix", expected_label])

def test_path_generator_skip(db):
    skip = [PathValue(["prefix", "0"]), PathValue(["prefix", "1"])]
    path_gen = PathGenerator(label_size=1, prefix=["prefix"], skip=skip)

    # Consume two items
    next(path_gen)
    next(path_gen)

    # The third one should be 2
    assert path_gen.__next__() == PathValue(["prefix", "2"])

def test_path_generator_next_alias(db):
    path_gen = PathGenerator(label_size=1)
    assert path_gen.next() == path_gen.__next__()

