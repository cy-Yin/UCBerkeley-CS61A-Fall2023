test = {
  'name': 'Problem 0',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': '3c1938b66de6e3576c7794432ca0d1f8',
          'choices': [
            r"""
            It represents health protecting the insect, so the insect can only
            be damaged when its health reaches 0
            """,
            r"""
            It represents the strength of an insect against attacks, which
            doesn't change throughout the game
            """,
            r"""
            It represents the amount of health the insect has left, so the
            insect is eliminated when it reaches 0
            """
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': r"""
          What is the significance of an Insect's health attribute? Does this
          value change? If so, how?
          """
        },
        {
          'answer': '94e2e146454b38059092b5bbfd866e20',
          'choices': [
            'damage',
            'health',
            'place',
            'bees'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'Which of the following is a class attribute of the Insect class?'
        },
        {
          'answer': 'f6d580bd3e0db93da86510c934fd4554',
          'choices': [
            'instance, each Ant instance needs its own health value',
            'instance, each Ant starts out with a different amount of health',
            'class, Ants of the same subclass all have the same amount of starting health',
            'class, when one Ant gets damaged, all ants receive the same amount of damage'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'Is the health attribute of the Ant class an instance attribute or class attribute? Why?'
        },
        {
          'answer': '6a4a860840218ef3b1d91d54643165f5',
          'choices': [
            'instance, each Ant does damage to bees at different rates',
            'instance, the damage an Ant depends on where the Ant is',
            'class, all Ants of the same subclass deal the same damage',
            'class, all Ants deal the same damage'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': r"""
          Is the damage attribute of an Ant subclass (such as ThrowerAnt) an
          instance or class attribute? Why?
          """
        },
        {
          'answer': '74e7fc66df4557e00fbf0948791e4841',
          'choices': [
            'Insect',
            'Place',
            'Bee',
            'Ant'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'Which class do both Ant and Bee inherit from?'
        },
        {
          'answer': '2f58d2097027c9718255dd5a02944c22',
          'choices': [
            r"""
            Ants and Bees both have the attributes health, damage, and place
            and the methods reduce_health and action
            """,
            r"""
            Ants and Bees both have the attribute damage and the methods
            reduce_health and action
            """,
            'Ants and Bees both take the same action each turn',
            'Ants and Bees have nothing in common'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What do instances of Ant and instances of Bee have in common? Please choose the most correct answer.'
        },
        {
          'answer': '4eed0239468d72e9a26a9a6f2968e76f',
          'choices': [
            'There can be one Ant and many Bees in a single Place',
            'There can be one Bee and many Ants in a single Place',
            'There is no limit on the number of insects of any type in a single Place',
            'Only one insect can be in a single Place at a time'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': r"""
          How many insects can be in a single Place at any given time in the
          game (before Problem 8)?
          """
        },
        {
          'answer': 'f072f225a70eba63759fe0172bad833c',
          'choices': [
            'The bee moves to the next place, then stings the ant in that place',
            'The bee flies to the nearest Ant and attacks it',
            'The bee stings the ant in its place or moves to the next place if there is no ant in its place',
            'The bee stings the ant in its place and then moves to the next place'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What does a Bee do during one of its turns?'
        },
        {
          'answer': '2470e48297cf873324ff3695472094b1',
          'choices': [
            'When the bees enter the colony',
            'When the colony runs out of food',
            'When any bee reaches the end of the tunnel or when the Queen Ant is killed',
            'When any bee reaches the end of the tunnel and the Queen Ant is killed',
            'When no ants are left on the map'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'When is the game lost?'
        }
      ],
      'scored': True,
      'type': 'concept'
    }
  ]
}
