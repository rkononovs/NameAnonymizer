import nltk

def preprocess(text):
    ne_person = []
    ne_person_list = []
    ne_name = ''

    ne_tree = nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(text))) # Chunk, tokenize and label text

    for subtree in ne_tree.subtrees(filter=lambda t: t.label() == 'PERSON'): # Filter every instance of the named entity with tag PERSON
        for leaf in subtree.leaves():
            ne_person.append(leaf[0]) # Append part of full name with title
        for part in ne_person:
            ne_name += part + ' ' # Add part of persons name to complete it
        if ne_name[:-1] not in ne_person_list:
            ne_person_list.append(ne_name[:-1]) # Append full name to person list
        ne_name = ''
        ne_person = []
        for ne_full_name in ne_person_list: # Replace all full name occurances with a tag 'person' // Change to unique ID
            text = text.replace(ne_full_name, 'PERSON')

    print(text) # Print processed text
    print(ne_person_list) # Print names for DEBUG PURPOSES

text = """
MACON, Ga. — President Trump held a rally in Georgia on Friday, 18 days before the November general election. It wasn’t a good sign for him.

That Mr. Trump is still campaigning in what should be a safely Republican state — and in others that should be solidly in his column like Iowa and Ohio — is evidence to many Democrats that Joseph R. Biden Jr.’s polling lead in the presidential race is solid and durable. Mr. Trump spent Monday in Arizona, too, a state that was once reliably Republican but where his unpopularity has helped make Mr. Biden competitive.

For some Democrats, Mr. Trump’s attention to red states is also a sign of something else — something few in the party want to discuss out loud, given their scars from Mr. Trump’s surprise victory in 2016. It’s an indication that Mr. Biden could pull off a landslide in November, achieving an ambitious and rare electoral blowout that some Democrats think is necessary to quell any doubts — or disputes by Mr. Trump — that Mr. Biden won the election.

On one level, such a scenario is entirely plausible based on the weeks and the breadth of public polls that show Mr. Biden with leads or edges in key states. But this possibility runs headlong into the political difficulties of pulling off such a win, and perhaps even more, the psychological hurdles for Democrats to entertain the idea. Many think that Mr. Trump, having pulled off a stunning win before, could do it again, even if there are differences from 2016 that hurt his chances.
""" # Sample text

preprocess(text)