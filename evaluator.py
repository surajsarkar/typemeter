class Evaluator:

    def judge(self, demo_story, user_typed_story):

        demo_story = demo_story.replace( '\n', ' ' )[:len( user_typed_story.replace( '\n', ' ' ) ) + 1]
        user_typed_story = user_typed_story.replace( '\n', ' ' )
        words_len = [len( word ) for word in demo_story.split( " " ) if word not in ('a', 'an', 'the', ' ')]
        avg_word_len = sum( words_len ) / len( words_len )

        mistakes = []
        letter_number = 0
        for real_letter in demo_story :
            if letter_number <= len( user_typed_story ) - 1 :
                typed_letter = user_typed_story[letter_number]

                if typed_letter != real_letter :
                    mistakes.append( real_letter )
            else:
                break
            letter_number += 1

        correct_typed_letters = len( user_typed_story ) - len( mistakes )
        # speed

        no_of_words = (correct_typed_letters / avg_word_len)
        wpm = ( no_of_words*2)

        ret_tup = (correct_typed_letters, mistakes, wpm)
        return ret_tup

