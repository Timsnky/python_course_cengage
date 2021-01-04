"""
File: doctor.py
Project 5
Conducts an interactive session of nondirective psychotherapy.
Adds a history list of earlier patient sentences, which can
be chosen for replies to shift the conversation to an earlier topic.
"""

import random


class Doctor(object):
    QUALIFIERS = ['Why do you say that ', 'You seem to think that ',
                  'Did I just hear you say that ',
                  'Why do you believe that ']

    REPLACEMENTS = {'i': 'you', 'me': 'you', 'my': 'your',
                    'we': 'you', 'us': 'you', 'am': 'are', 'you': 'I'}

    HEDGES = ['Go on.', 'I would like to hear more about that.',
              'And what do you think about this?', 'Please continue.']

    def __init__(self):
        self.history = []

    def greeting(self):
        return "Hello, how can I help you today?"

    def farewell(self):
        return "Have a nice day!"

    def reply(self, sentence):
        """Implements three different reply strategies."""
        probability = random.randint(1, 5)

        if probability in (1, 2):
            # Just hedge
            answer = random.choice(self.HEDGES)
        elif probability == 3 and len(self.history) > 3:
            # Go back to an earlier topic
            answer = "Earlier you said that " + \
                     self._changePerson(random.choice(self.history))
        else:
            # Transform the current input
            answer = random.choice(self.QUALIFIERS) + self._changePerson(sentence)
        # Always add the current sentence to the history list
        self.history.append(sentence)

        return answer

    def _changePerson(self, sentence):
        """Replaces first person pronouns with second person
        pronouns."""
        words = sentence.split()
        replyWords = []
        for word in words:
            replyWords.append(self.REPLACEMENTS.get(word, word))
        return " ".join(replyWords)


def main():
    """Handles the interaction between patient and doctor."""
    doctor = Doctor()
    print(doctor.greeting())
    while True:
        sentence = input("\n>> ")
        if sentence.upper() == "QUIT":
            print(doctor.farewell())
            break
        print(doctor.reply(sentence))


# The entry point for program execution
if __name__ == "__main__":
    main()
