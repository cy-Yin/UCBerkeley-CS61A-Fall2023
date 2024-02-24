test = {
  'name': 'Question 11',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> sus_strategy(31, 21, threshold=10, num_rolls=2)
          46caef5ffd6d72c8757279cbcf01b12f
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> sus_strategy(30, 41, threshold=10, num_rolls=2)
          962aea5f59fc55bd65ccacf4603c8f22
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> sus_strategy(53, 60, threshold=14, num_rolls=2)
          962aea5f59fc55bd65ccacf4603c8f22
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> sus_strategy(53, 60, threshold=15, num_rolls=2)
          46caef5ffd6d72c8757279cbcf01b12f
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> sus_strategy(23, 54, threshold=4, num_rolls=2)
          962aea5f59fc55bd65ccacf4603c8f22
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> sus_strategy(14, 21, threshold=8, num_rolls=2)
          46caef5ffd6d72c8757279cbcf01b12f
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> sus_strategy(14, 21, threshold=12, num_rolls=5)
          26f5762c932a578994ea1c8fc7fa6c02
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> s = 0
          >>> while s < 100:
          ...     if sus_update(0, 20, s) - 20 >= 10:
          ...         assert sus_strategy(20, s, threshold=10, num_rolls=3) == 0
          ...     else:
          ...         assert sus_strategy(20, s, threshold=10, num_rolls=3) == 3
          ...     s += 1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
