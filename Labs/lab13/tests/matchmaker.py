test = {
  'name': 'matchmaker',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM matchmaker LIMIT 10;
          dog|Dancing Queen|green|blue
          dog|Dancing Queen|green|blue
          dog|Dancing Queen|green|pink
          dog|Dancing Queen|green|green
          dog|Bohemian Rhapsody|lavender|orange
          dog|Bohemian Rhapsody|lavender|blue
          dog|Bohemian Rhapsody|lavender|orange
          dog|Bohemian Rhapsody|lavender|black
          dog|Shake It Off|black|blue
          dog|Shake It Off|black|blue
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
