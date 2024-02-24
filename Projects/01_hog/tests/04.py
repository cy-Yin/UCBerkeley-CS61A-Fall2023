test = {
  'name': 'Question 4',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> num_factors(1)
          43d176e102c8d95338faf8791aa509b3
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> num_factors(2)
          46caef5ffd6d72c8757279cbcf01b12f
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> num_factors(3)
          46caef5ffd6d72c8757279cbcf01b12f
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> num_factors(9)
          16e2cf37e8254529473d9e0a36b75fcb
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> num_factors(28)
          327b19ffebddf93982e1ad2a4a6486f4
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> num_factors(64)
          c42887e7b9ffe8fc26bb57b61329f916
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> num_factors(72)
          12
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> num_factors(97)
          46caef5ffd6d72c8757279cbcf01b12f
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> num_factors(99)
          6
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sus_points(1)
          43d176e102c8d95338faf8791aa509b3
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> sus_points(21)
          d4e635123d3bf027954fb7a6e4ca8cdb
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> sus_points(25)
          29
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sus_points(62)
          2c3cbe4a2ba154412b20007fbd3a9b63
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> sus_points(64)
          5c6853796ff2cb8acdd00712bc721759
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> sus_points(67)
          67
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sus_points(75)
          75
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sus_points(86)
          89
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sus_points(100)
          100
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> simple_update(2, 5, 7, make_test_dice(2, 4))
          ebb85ed86e75db9ccb48b9592f867cc1
          # locked
          >>> sus_update(2, 5, 7, make_test_dice(2, 4)) # is 11 a sus number?
          ebb85ed86e75db9ccb48b9592f867cc1
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> simple_update(0, 15, 37) # what happens when you roll 0 dice?
          6790f7070fa643e868f99363486b6275
          # locked
          >>> sus_update(0, 15, 37) # is 21 a sus number?
          d4e635123d3bf027954fb7a6e4ca8cdb
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> simple_update(2, 2, 3, make_test_dice(4))
          70e71b420a966665c548a3bb2cb30d7d
          # locked
          >>> sus_update(2, 2, 3, make_test_dice(4)) # is 10 a sus number?
          ebb85ed86e75db9ccb48b9592f867cc1
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> sus_update(3, 11, 12, make_test_dice(4, 5, 6))
          29
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sus_update(2, 29, 17, make_test_dice(1, 3))
          30
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sus_update(0, 41, 42)
          50
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sus_update(0, 40, 22)
          47
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sus_update(2, 56, 56, make_test_dice(4))
          64
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> import types
          >>> def imports():
          ...     for name, val in globals().items():
          ...         if isinstance(val, types.ModuleType):
          ...             yield val.__name__
          >>> list(imports()) # do NOT import any new modules!
          ['tests.construct_check', 'types']
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      >>> import tests.construct_check as test
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
