"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text.
        def __init__(self) serves a constructor
        """
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items(): 
            text = text.replace("{" + key + "}", val)
            """
            The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list. 
            The replace() method replaces a specified phrase with another specified phrase
            when generating, the answer will be passed in as a dictionairy with the key as the prompt and the val as the answer. We relace they key val pair in the templae with just the value
            """

        return text


# Here's a story to get you started


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

# """Down here we define our first use of the class
# 1. our word parameter is a list of word types
# 2. our second parameter is a string which serves as our template
# """