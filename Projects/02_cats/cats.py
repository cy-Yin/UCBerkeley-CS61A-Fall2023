"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def pick(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns True. If there are fewer than K such paragraphs, return
    the empty string.

    Arguments:
        paragraphs: a list of strings
        select: a function that returns True for paragraphs that can be selected
        k: an integer

    >>> ps = ['hi', 'how are you', 'fine']
    >>> s = lambda p: len(p) <= 4
    >>> pick(ps, s, 0)
    'hi'
    >>> pick(ps, s, 1)
    'fine'
    >>> pick(ps, s, 2)
    ''
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    lst = []
    for elem in paragraphs:
        if select(elem) == True:
            lst = lst + [elem]
    if k >= len(lst):
        return ''
    else:
        return lst[k]
    # END PROBLEM 1


def about(subject):
    """Return a select function that returns whether
    a paragraph contains one of the words in SUBJECT.

    Arguments:
        subject: a list of words related to a subject

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> pick(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> pick(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in subject]), 'subjects should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def contain(paragraph):
        modified_paragraph = split(lower(remove_punctuation(paragraph)))
        for elem in modified_paragraph:
            for checker in subject: 
                if checker == elem: 
                    return True
        return False
    return contain
    # END PROBLEM 2


def accuracy(typed, source):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of SOURCE that was typed.

    Arguments:
        typed: a string that may contain typos
        source: a string without errors

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    >>> accuracy('', '')
    100.0
    """
    typed_words = split(typed)
    source_words = split(source)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    if typed_words == [] and source_words == []:
        return 100.0
    elif typed_words == [] and source_words != []:
        return 0.0
    else:
        score = 0
        for index in range(min(len(typed_words), len(source_words))):
            if typed_words[index] == source_words[index]:
                score = score + 1
        accurate_rate = score / len(typed_words) * 100
        return accurate_rate

    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string.

    Arguments:
        typed: an entered string
        elapsed: an amount of time in seconds

    >>> wpm('hello friend hello buddy hello', 15)
    24.0
    >>> wpm('0123456789',60)
    2.0
    """
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    return (len(typed) / 5) / elapsed * 60
    # END PROBLEM 4


############
# Phase 2A #
############


def autocorrect(typed_word, word_list, diff_function, limit):
    """Returns the element of WORD_LIST that has the smallest difference
    from TYPED_WORD. If multiple words are tied for the smallest difference,
    return the one that appears closest to the front of WORD_LIST. If the
    difference is greater than LIMIT, instead return TYPED_WORD.

    Arguments:
        typed_word: a string representing a word that may contain typos
        word_list: a list of strings representing source words
        diff_function: a function quantifying the difference between two words
        limit: a number

    >>> ten_diff = lambda w1, w2, limit: 10 # Always returns 10
    >>> autocorrect("hwllo", ["butter", "hello", "potato"], ten_diff, 20)
    'butter'
    >>> first_diff = lambda w1, w2, limit: (1 if w1[0] != w2[0] else 0) # Checks for matching first char
    >>> autocorrect("tosting", ["testing", "asking", "fasting"], first_diff, 10)
    'testing'
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    if typed_word in word_list:
        return typed_word
    else:
        lst_diff = []
        for check_word in word_list:
            lst_diff = lst_diff + [diff_function(typed_word, check_word, limit)]
        if min(lst_diff, key=abs) > limit: # No correct word
            return typed_word
        else:
            lowest_diff_index = 0
            lowest_diff = lst_diff[0]
            for index in range(len(lst_diff)):
                if lst_diff[index] < lowest_diff:
                    lowest_diff_index = index
                    lowest_diff = lst_diff[index]
            return word_list[lowest_diff_index]
    # END PROBLEM 5


def feline_fixes(typed, source, limit):
    """A diff function for autocorrect that determines how many letters
    in TYPED need to be substituted to create SOURCE, then adds the difference in
    their lengths and returns the result.

    Arguments:
        typed: a starting word
        source: a string representing a desired goal word
        limit: a number representing an upper bound on the number of chars that must change

    >>> big_limit = 10
    >>> feline_fixes("nice", "rice", big_limit)    # Substitute: n -> r
    1
    >>> feline_fixes("range", "rungs", big_limit)  # Substitute: a -> u, e -> s
    2
    >>> feline_fixes("pill", "pillage", big_limit) # Don't substitute anything, length difference of 3.
    3
    >>> feline_fixes("roses", "arose", big_limit)  # Substitute: r -> a, o -> r, s -> o, e -> s, s -> e
    5
    >>> feline_fixes("rose", "hello", big_limit)   # Substitute: r->h, o->e, s->l, e->l, length difference of 1.
    5
    """
    # BEGIN PROBLEM 6
    '''
    The code below has passed all the tests except suite 1 case 6, which is described as follows.

    > from cats import feline_fixes, autocorrect
    > import tests.construct_check as test
    > # Check that the recursion stops when the limit is reached
    > import trace, io
    > from contextlib import redirect_stdout
    > with io.StringIO() as buf, redirect_stdout(buf):
    .     trace.Trace(trace=True).runfunc(feline_fixes, "someaweqwertyuio", "awesomeasdfghjkl", 3)
    .     output = buf.getvalue()
    > len([line for line in output.split('\n') if 'funcname' in line]) < 12
    False

    Why is that? 
    > for line in output.split('\n'):
    .     print(line)
    .
    --- modulename: cats, funcname: feline_fixes
    cats.py(201):     if typed == "" or source == "": # "someaweqwertyuio", "awesomeasdfghjkl"
    cats.py(204):         typed_check, new_typed = typed[0], (typed[1:] if len(typed) >= 1 else "")
    cats.py(205):         source_check, new_source = source[0], (source[1:] if len(source) >= 1 else "")
    cats.py(206):         if typed_check == source_check:
    cats.py(209):             return 1 + feline_fixes(new_typed, new_source, limit)
    --- modulename: cats, funcname: feline_fixes
    cats.py(201):     if typed == "" or source == "": # "omeaweqwertyuio", "wesomeasdfghjkl"
    cats.py(204):         typed_check, new_typed = typed[0], (typed[1:] if len(typed) >= 1 else "")
    cats.py(205):         source_check, new_source = source[0], (source[1:] if len(source) >= 1 else "")
    cats.py(206):         if typed_check == source_check:
    cats.py(209):             return 1 + feline_fixes(new_typed, new_source, limit)
    --- modulename: cats, funcname: feline_fixes
    cats.py(201):     if typed == "" or source == "": # "meaweqwertyuio", "esomeasdfghjkl"
    cats.py(204):         typed_check, new_typed = typed[0], (typed[1:] if len(typed) >= 1 else "")
    cats.py(205):         source_check, new_source = source[0], (source[1:] if len(source) >= 1 else "")
    cats.py(206):         if typed_check == source_check:
    cats.py(209):             return 1 + feline_fixes(new_typed, new_source, limit)
    --- modulename: cats, funcname: feline_fixes
    cats.py(201):     if typed == "" or source == "": # "eaweqwertyuio", "someasdfghjkl"
    cats.py(204):         typed_check, new_typed = typed[0], (typed[1:] if len(typed) >= 1 else "")
    cats.py(205):         source_check, new_source = source[0], (source[1:] if len(source) >= 1 else "")
    cats.py(206):         if typed_check == source_check:
    cats.py(209):             return 1 + feline_fixes(new_typed, new_source, limit)
    --- modulename: cats, funcname: feline_fixes
    cats.py(201):     if typed == "" or source == "": # "aweqwertyuio", "omeasdfghjkl"
    cats.py(204):         typed_check, new_typed = typed[0], (typed[1:] if len(typed) >= 1 else "")
    cats.py(205):         source_check, new_source = source[0], (source[1:] if len(source) >= 1 else "")
    cats.py(206):         if typed_check == source_check:
    cats.py(209):             return 1 + feline_fixes(new_typed, new_source, limit)
    --- modulename: cats, funcname: feline_fixes
    cats.py(201):     if typed == "" or source == "": # "weqwertyuio", "measdfghjkl"
    cats.py(204):         typed_check, new_typed = typed[0], (typed[1:] if len(typed) >= 1 else "")
    cats.py(205):         source_check, new_source = source[0], (source[1:] if len(source) >= 1 else "")
    cats.py(206):         if typed_check == source_check:
    cats.py(209):             return 1 + feline_fixes(new_typed, new_source, limit)
    --- modulename: cats, funcname: feline_fixes
    cats.py(201):     if typed == "" or source == "": # "eqwertyuio", "easdfghjkl"
    cats.py(204):         typed_check, new_typed = typed[0], (typed[1:] if len(typed) >= 1 else "")
    cats.py(205):         source_check, new_source = source[0], (source[1:] if len(source) >= 1 else "")
    cats.py(206):         if typed_check == source_check:
    cats.py(207):             return feline_fixes(new_typed, new_source, limit)
    --- modulename: cats, funcname: feline_fixes
    cats.py(201):     if typed == "" or source == "": # "qwertyuio", "asdfghjkl"
    cats.py(204):         typed_check, new_typed = typed[0], (typed[1:] if len(typed) >= 1 else "")
    cats.py(205):         source_check, new_source = source[0], (source[1:] if len(source) >= 1 else "")
    cats.py(206):         if typed_check == source_check:
    cats.py(209):             return 1 + feline_fixes(new_typed, new_source, limit)
    --- modulename: cats, funcname: feline_fixes
    cats.py(201):     if typed == "" or source == "": # "wertyuio", "sdfghjkl"
    cats.py(204):         typed_check, new_typed = typed[0], (typed[1:] if len(typed) >= 1 else "")
    cats.py(205):         source_check, new_source = source[0], (source[1:] if len(source) >= 1 else "")
    cats.py(206):         if typed_check == source_check:
    cats.py(209):             return 1 + feline_fixes(new_typed, new_source, limit)
    --- modulename: cats, funcname: feline_fixes
    cats.py(201):     if typed == "" or source == "": # "ertyuio", "dfghjkl"
    cats.py(204):         typed_check, new_typed = typed[0], (typed[1:] if len(typed) >= 1 else "")
    cats.py(205):         source_check, new_source = source[0], (source[1:] if len(source) >= 1 else "")
    cats.py(206):         if typed_check == source_check:
    cats.py(209):             return 1 + feline_fixes(new_typed, new_source, limit)
    --- modulename: cats, funcname: feline_fixes
    cats.py(201):     if typed == "" or source == "": # "rtyuio", "fghjkl"
    cats.py(204):         typed_check, new_typed = typed[0], (typed[1:] if len(typed) >= 1 else "")
    cats.py(205):         source_check, new_source = source[0], (source[1:] if len(source) >= 1 else "")
    cats.py(206):         if typed_check == source_check:
    cats.py(209):             return 1 + feline_fixes(new_typed, new_source, limit)
    --- modulename: cats, funcname: feline_fixes
    cats.py(201):     if typed == "" or source == "": # "tyuio", "ghjkl"
    cats.py(204):         typed_check, new_typed = typed[0], (typed[1:] if len(typed) >= 1 else "")
    cats.py(205):         source_check, new_source = source[0], (source[1:] if len(source) >= 1 else "")
    cats.py(206):         if typed_check == source_check:
    cats.py(209):             return 1 + feline_fixes(new_typed, new_source, limit)
    --- modulename: cats, funcname: feline_fixes
    cats.py(201):     if typed == "" or source == "": # "yuio", "hjkl"
    cats.py(204):         typed_check, new_typed = typed[0], (typed[1:] if len(typed) >= 1 else "")
    cats.py(205):         source_check, new_source = source[0], (source[1:] if len(source) >= 1 else "")
    cats.py(206):         if typed_check == source_check:
    cats.py(209):             return 1 + feline_fixes(new_typed, new_source, limit)
    --- modulename: cats, funcname: feline_fixes
    cats.py(201):     if typed == "" or source == "": # "uio", "jkl"
    cats.py(204):         typed_check, new_typed = typed[0], (typed[1:] if len(typed) >= 1 else "")
    cats.py(205):         source_check, new_source = source[0], (source[1:] if len(source) >= 1 else "")
    cats.py(206):         if typed_check == source_check:
    cats.py(209):             return 1 + feline_fixes(new_typed, new_source, limit)
    --- modulename: cats, funcname: feline_fixes
    cats.py(201):     if typed == "" or source == "": # "uio", "jkl"
    cats.py(204):         typed_check, new_typed = typed[0], (typed[1:] if len(typed) >= 1 else "")
    cats.py(205):         source_check, new_source = source[0], (source[1:] if len(source) >= 1 else "")
    cats.py(206):         if typed_check == source_check:
    cats.py(209):             return 1 + feline_fixes(new_typed, new_source, limit)
    --- modulename: cats, funcname: feline_fixes
    cats.py(201):     if typed == "" or source == "": # "o", "l"
    cats.py(204):         typed_check, new_typed = typed[0], (typed[1:] if len(typed) >= 1 else "")
    cats.py(205):         source_check, new_source = source[0], (source[1:] if len(source) >= 1 else "")
    cats.py(206):         if typed_check == source_check:
    cats.py(209):             return 1 + feline_fixes(new_typed, new_source, limit)
    --- modulename: cats, funcname: feline_fixes
    cats.py(201):     if typed == "" or source == "": # "", ""
    cats.py(202):         return max(len(typed), len(source))
    15

    The function has computed the whole diff between two words. However, if the diff has been larger than limit, 
    we do not need to know whether the diff is (limit + 1) or (limit + 100). We just return (limit + 1) to give 
    the message that the diff is too large to autocorrect, rather than computing the whole recursion, which will 
    minimize the extra computation.

    Original Code:
    ```
    if typed == "" or source == "":
        return max(len(typed), len(source))
    else:
        typed_check, new_typed = typed[0], (typed[1:] if len(typed) >= 1 else "")
        source_check, new_source = source[0], (source[1:] if len(source) >= 1 else "")
        if typed_check == source_check:
            return feline_fixes(new_typed, new_source, limit)
        else:
            return 1 + feline_fixes(new_typed, new_source, limit)
    ```
    '''
    if typed == "" or source == "":
        return max(len(typed), len(source))
    elif limit == 0:
        if typed == source:
            return 0
        else:
            return 1
    else:
        typed_check, new_typed = typed[0], (typed[1:] if len(typed) >= 1 else "")
        source_check, new_source = source[0], (source[1:] if len(source) >= 1 else "")
        if typed_check == source_check:
            return feline_fixes(new_typed, new_source, limit)
        else:
            return 1 + feline_fixes(new_typed, new_source, limit - 1)
    # END PROBLEM 6


############
# Phase 2B #
############


def minimum_mewtations(typed, source, limit):
    """A diff function that computes the edit distance from TYPED to SOURCE.
    This function takes in a string TYPED, a string SOURCE, and a number LIMIT.
    Arguments:
        typed: a starting word
        source: a string representing a desired goal word
        limit: a number representing an upper bound on the number of edits
    >>> big_limit = 10
    >>> minimum_mewtations("cats", "scat", big_limit)       # cats -> scats -> scat
    2
    >>> minimum_mewtations("purng", "purring", big_limit)   # purng -> purrng -> purring
    2
    >>> minimum_mewtations("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus -> kittens
    3
    """
    # Recursive cases should go below here
    if typed == "" or source == "":
        return max(len(typed), len(source))
    elif limit == 0:
        if typed == source:
            return 0
        else:
            return 1
    else:
        typed_check, new_typed = typed[0], (typed[1:] if len(typed) >= 1 else "")
        source_check, new_source = source[0], (source[1:] if len(source) >= 1 else "")
        if typed_check == source_check:
            return minimum_mewtations(new_typed, new_source, limit)
        else:
            add = 1 + minimum_mewtations(source[0] + typed, source, limit - 1) # Fill in these lines
            remove = 1 + minimum_mewtations(typed[1:], source, limit - 1)
            substitute = 1 + minimum_mewtations(typed[1:], source[1:], limit - 1)
            # BEGIN
            "*** YOUR CODE HERE ***"
            return min(add, remove, substitute)
            # END
    


def final_diff(typed, source, limit):
    """A diff function that takes in a string TYPED, a string SOURCE, and a number LIMIT.
    If you implement this function, it will be used."""
    assert False
    '''The diff function as follows does not have a good autocorrect effect. Sad!!!'''
    if typed == "" or source == "":
        return max(len(typed), len(source))
    elif limit == 0:
        if typed == source:
            return 0
        else:
            return 1
    else:
        typed_check, new_typed = typed[0], (typed[1:] if len(typed) >= 1 else "")
        source_check, new_source = source[0], (source[1:] if len(source) >= 1 else "")
        if typed_check == source_check:
            return final_diff(new_typed, new_source, limit)
        else:
            add = 1 + final_diff(source[0] + typed, source, limit - 1) # Fill in these lines
            remove = 1 + final_diff(typed[1:], source, limit - 1)
            substitute = 1 + final_diff(typed[1:], source[1:], limit - 1)
            if len(typed) >= 2:
                exchange = 1 + final_diff(typed[0] + typed[1] + typed[2:], source, limit - 1)
                return min(add, remove, substitute, exchange)
            else:
                return min(add, remove, substitute)

FINAL_DIFF_LIMIT = 4 # REPLACE THIS WITH YOUR LIMIT


###########
# Phase 3 #
###########


def report_progress(typed, source, user_id, upload):
    """Upload a report of your id and progress so far to the multiplayer server.
    Returns the progress so far.

    Arguments:
        typed: a list of the words typed so far
        source: a list of the words in the typing source
        user_id: a number representing the id of the current user
        upload: a function used to upload progress to the multiplayer server

    >>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
    >>> # The above function displays progress in the format ID: __, Progress: __
    >>> print_progress({'id': 1, 'progress': 0.6})
    ID: 1 Progress: 0.6
    >>> typed = ['how', 'are', 'you']
    >>> source = ['how', 'are', 'you', 'doing', 'today']
    >>> report_progress(typed, source, 2, print_progress)
    ID: 2 Progress: 0.6
    0.6
    >>> report_progress(['how', 'aree'], source, 3, print_progress)
    ID: 3 Progress: 0.2
    0.2
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    total_num = len(source)
    report = {'id': user_id, 'progress': 0.0}
    index = 0
    while index < min(len(typed), len(source)) and typed[index] == source[index]:
        index = index + 1
    report['progress'] = index / total_num
    upload(report)
    
    return report['progress']
    # END PROBLEM 8


def time_per_word(words, timestamps_per_player):
    """Given timing data, return a match data abstraction, which contains a
    list of words and the amount of time each player took to type each word.

    Arguments:
        words: a list of words, in the order they are typed.
        timestamps_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.

    >>> p = [[75, 81, 84, 90, 92], [19, 29, 35, 36, 38]]
    >>> match = time_per_word(['collar', 'plush', 'blush', 'repute'], p)
    >>> get_all_words(match)
    ['collar', 'plush', 'blush', 'repute']
    >>> get_all_times(match)
    [[6, 3, 6, 2], [10, 6, 1, 2]]
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    times = []
    for per_timestamp in timestamps_per_player:
        per_interval = [(per_timestamp[i] - per_timestamp[i - 1]) for i in range(1, len(per_timestamp))]
        times += [per_interval]

    return match(words, times)
    # END PROBLEM 9


def fastest_words(match):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        match: a match data abstraction as returned by time_per_word.

    >>> p0 = [5, 1, 3]
    >>> p1 = [4, 1, 6]
    >>> fastest_words(match(['Just', 'have', 'fun'], [p0, p1]))
    [['have', 'fun'], ['Just']]
    >>> p0  # input lists should not be mutated
    [5, 1, 3]
    >>> p1
    [4, 1, 6]
    """
    player_indices = range(len(get_all_times(match)))  # contains an *index* for each player
    word_indices = range(len(get_all_words(match)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    lst_fastest_word = [[] for _ in player_indices]
    for word_indice in word_indices:
        index = 0
        fastest_player_time = time(match, 0, word_indice)
        for player_indice in player_indices:
            if time(match, player_indice, word_indice) < fastest_player_time:
                index = player_indice
                fastest_player_time = time(match, player_indice, word_indice)
        lst_fastest_word[index] += [get_word(match, word_indice)]
    
    return lst_fastest_word
    # END PROBLEM 10


def match(words, times):
    """A data abstraction containing all words typed and their times.

    Arguments:
        words: A list of strings, each string representing a word typed.
        times: A list of lists for how long it took for each player to type
            each word.
            times[i][j] = time it took for player i to type words[j].

    Example input:
        words: ['Hello', 'world']
        times: [[5, 1], [4, 2]]
    """
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return {"words": words, "times": times}


def get_word(match, word_index):
    """A utility function that gets the word with index word_index"""
    assert 0 <= word_index < len(get_all_words(match)), "word_index out of range of words"
    return get_all_words(match)[word_index]


def time(match, player_num, word_index):
    """A utility function for the time it took player_num to type the word at word_index"""
    assert word_index < len(get_all_words(match)), "word_index out of range of words"
    assert player_num < len(get_all_times(match)), "player_num out of range of players"
    return get_all_times(match)[player_num][word_index]

def get_all_words(match):
    """A selector function for all the words in the match"""
    return match["words"]

def get_all_times(match):
    """A selector function for all typing times for all players"""
    return match["times"]


def match_string(match):
    """A helper function that takes in a match data abstraction and returns a string representation of it"""
    return f"match({get_all_words(match)}, {get_all_times(match)})"

enable_multiplayer = True  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        source = pick(paragraphs, select, i)
        if not source:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(source)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, source))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)