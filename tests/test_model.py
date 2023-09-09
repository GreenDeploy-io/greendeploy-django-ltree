import pytest
from django.core.exceptions import ImproperlyConfigured
from taxonomy.models import Taxonomy

TEST_DATA = [
    {'name': 'Bacteria'},
    {'name': 'Plantae'},
    {
        'name': 'Animalia',
        'sub': [
            {
                'name': 'Chordata',
                'sub': [
                    {
                        'name': 'Mammalia',
                        'sub': [
                            {
                                'name': 'Carnivora',
                                'sub': [
                                    {
                                        'name': 'Canidae',
                                        'sub': [
                                            {
                                                'name': 'Canis',
                                                'sub': [{'name': 'Canis lupus'}, {'name': 'Canis rufus'}]
                                            },
                                            {
                                                'name': 'Urocyon',
                                                'sub': [{'name': 'Urocyon cinereoargenteus'}]
                                            }
                                        ]
                                    },
                                    {
                                        'name': 'Feliformia',
                                        'sub': [
                                            {
                                                'name': 'Felidae',
                                                'sub': [
                                                    {
                                                        'name': 'Felinae',
                                                        'sub': [
                                                            {
                                                                'name': 'Lynx',
                                                                'sub': [{'name': 'Lynx lynx'}, {'name': 'Lynx rufus'}]
                                                            },
                                                            {
                                                                'name': 'Puma',
                                                                'sub': [{'name': 'Puma concolor'}]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                'name': 'Pilosa',
                                'sub': [
                                    {
                                        'name': 'Folivora',
                                        'sub': [
                                            {
                                                'name': 'Bradypodidae',
                                                'sub': [
                                                    {
                                                        'name': 'Bradypus',
                                                        'sub': [{'name': 'Bradypus tridactylus'}]
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        'name': 'Reptilia',
                        'sub': [
                            {
                                'name': 'Squamata',
                                'sub': [
                                    {
                                        'name': 'Iguania',
                                        'sub': [
                                            {
                                                'name': 'Agamidae',
                                                'sub': [
                                                    {
                                                        'name': 'Pogona',
                                                        'sub': [
                                                            {'name': 'Pogona barbata'},
                                                            {'name': 'Pogona minor'},
                                                            {'name': 'Pogona vitticeps'}
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }
]


def create_objects(objects, parent):
    for obj in objects:
        created = Taxonomy.objects.create_child(parent, name=obj['name'])
        if 'sub' in obj:
            create_objects(obj['sub'], created)


def create_test_data():
    create_objects(TEST_DATA, parent=None)


def test_create(db):
    create_test_data()
    assert Taxonomy.objects.count() != 0


def test_roots(db):
    create_test_data()
    roots = Taxonomy.objects.roots().values_list('name', flat=True)
    assert set(roots) == {'Bacteria', 'Plantae', 'Animalia'}


@pytest.mark.parametrize(
    'name, expected', [
        ('Animalia', ['Chordata']),
        ('Mammalia', ['Carnivora', 'Pilosa']),
        ('Reptilia', ['Squamata']),
        ('Pogona', ['Pogona barbata', 'Pogona minor', 'Pogona vitticeps'])
    ]
)
def test_children(db, name, expected):
    create_test_data()
    children = Taxonomy.objects.get(name=name).children().values_list('name', flat=True)
    assert set(children) == set(expected)


def test_label(db):
    create_test_data()
    for item in Taxonomy.objects.all():
        label = item.label()
        assert label.isalnum()
        assert str(item.path).endswith(label)


@pytest.mark.parametrize(
    'name, expected', [
        ('Canis lupus', ['Animalia', 'Chordata', 'Mammalia', 'Carnivora', 'Canidae', 'Canis', 'Canis lupus']),
        ('Bacteria', ['Bacteria']),
        ('Chordata', ['Animalia', 'Chordata'])
    ]
)
def test_ancestors(db, name, expected):
    create_test_data()
    ancestors = Taxonomy.objects.get(name=name).ancestors().values_list('name', flat=True)
    assert list(ancestors) == expected


def test_get_ancestors_paths(db):
    create_test_data()

    # Build a lookup dictionary to map names to actual paths
    name_to_path = {obj.name: obj.path for obj in Taxonomy.objects.all()}

    test_cases = [
        ('Canis lupus', [
            name_to_path['Animalia'],
            name_to_path['Chordata'],
            name_to_path['Mammalia'],
            name_to_path['Carnivora'],
            name_to_path['Canidae'],
            name_to_path['Canis'],
        ]),
        ('Bacteria', []),
        ('Chordata', [
            name_to_path['Animalia'],
        ]),
    ]

    # sourcery skip: no-loop-in-tests
    for name, expected_paths in test_cases:
        tax = Taxonomy.objects.get(name=name)
        ancestors_paths = tax.get_ancestors_paths()
        ancestors_paths_str = [[str(part) for part in path] for path in ancestors_paths]
        assert ancestors_paths_str == expected_paths



@pytest.mark.parametrize(
    'name, expected', [
        ('Canidae', ['Canidae', 'Canis', 'Canis lupus', 'Canis rufus', 'Urocyon', 'Urocyon cinereoargenteus']),
        ('Bradypus tridactylus', ['Bradypus tridactylus']),
        ('Pogona', ['Pogona', 'Pogona barbata', 'Pogona minor', 'Pogona vitticeps'])
    ]
)
def test_descendants(db, name, expected):
    create_test_data()
    descendants = Taxonomy.objects.get(name=name).descendants().values_list('name', flat=True)
    assert set(descendants) == set(expected)


@pytest.mark.parametrize(
    'name, expected', [
        ('Feliformia', 'Carnivora'),
        ('Plantae', None),
        ('Pogona minor', 'Pogona')
    ]
)
def test_parent(db, name, expected):
    create_test_data()
    parent = Taxonomy.objects.get(name=name).parent()
    assert getattr(parent, 'name', None) == expected


@pytest.mark.parametrize(
    'name, expected', [
        ('Carnivora', ['Pilosa']),
        ('Pogona vitticeps', ['Pogona minor', 'Pogona barbata'])
    ]
)
def test_siblings(db, name, expected):
    create_test_data()
    siblings = Taxonomy.objects.get(name=name).siblings().values_list('name', flat=True)
    assert set(siblings) == set(expected)


def test_slicing(db):
    create_test_data()
    qs = Taxonomy.objects.all()
    assert qs[:3].count() == 3


def test_add_child(db):
    create_test_data()

    parent = Taxonomy.objects.get(name="Animalia")

    # Test Case 1: Adding a child properly
    try:
        child = parent.add_child(name="Mammalia")
        assert child.name == "Mammalia"
        assert str(child.path) == "Animalia.Mammalia"  # Assuming PathValue's string representation works like this
    except Exception as e:
        pytest.fail(f"Exception {e} was raised unexpectedly.")

    # Test Case 2: Adding a child without providing the label_field in kwargs
    with pytest.raises(ImproperlyConfigured):
        parent.add_child()

    # Test Case 3: Adding a child with label_field set to None
    with pytest.raises(ImproperlyConfigured):
        parent.add_child(name=None)