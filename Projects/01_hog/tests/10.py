test = {
  'name': 'Question 10',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> boar_strategy(40, 51, threshold=7, num_rolls=2)
          962aea5f59fc55bd65ccacf4603c8f22
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> boar_strategy(40, 51, threshold=15, num_rolls=7)
          962aea5f59fc55bd65ccacf4603c8f22
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> boar_strategy(40, 51, threshold=16, num_rolls=7)
          c42887e7b9ffe8fc26bb57b61329f916
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> boar_strategy(44, 53, threshold=3, num_rolls=2)
          962aea5f59fc55bd65ccacf4603c8f22
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> boar_strategy(44, 53, threshold=4, num_rolls=2)
          46caef5ffd6d72c8757279cbcf01b12f
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> boar_strategy(40, 31, threshold=9, num_rolls=5)
          962aea5f59fc55bd65ccacf4603c8f22
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> boar_strategy(40, 31, threshold=10, num_rolls=5)
          26f5762c932a578994ea1c8fc7fa6c02
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> boar_strategy(40, 52, threshold=15, num_rolls=2)
          962aea5f59fc55bd65ccacf4603c8f22
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> boar_strategy(40, 52, threshold=16, num_rolls=2)
          46caef5ffd6d72c8757279cbcf01b12f
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
          ...     if boar_brawl(90, s) >= 10:
          ...         assert boar_strategy(90, s, threshold=10, num_rolls=3) == 0
          ...     else:
          ...         assert boar_strategy(90, s, threshold=10, num_rolls=3) == 3
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
