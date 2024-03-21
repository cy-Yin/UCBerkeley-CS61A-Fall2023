test = {
  'name': 'switch-factors',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (switch-factors 1)
          one
          scm> (switch-factors 2)
          prime
          scm> (switch-factors 3)
          prime
          scm> (switch-factors 4)
          composite
          scm> (switch-factors 7)
          prime
          scm> (switch-factors 11)
          prime
          scm> (switch-factors 135)
          composite
          scm> (switch-factors 21)
          composite
          scm> (switch-factors 53)
          prime
          scm> (switch-factors 62)
          composite
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".")
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
