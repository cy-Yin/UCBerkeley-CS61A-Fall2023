test = {
  'name': 'smallest-int-having',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM smallest_int_having LIMIT 10;
          11/23/2023 15:12:57|10
          11/25/2023 21:27:17|11
          11/25/2023 5:20:58|16
          11/23/2023 15:11:11|18
          11/23/2023 15:24:42|22
          11/23/2023 22:55:21|24
          11/23/2023 16:43:39|28
          11/23/2023 18:03:47|29
          11/24/2023 17:48:54|31
          11/23/2023 15:03:50|33
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab13.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
