# German Frequency Lemmatizer

## Requirements

- the `analyze.txt` that will contain the German text you wish to
lemmatize and rank

## Logic

1. SpaCy loads its statistical model for German language processing. 
2. Path saves the German text from `./analyze.txt`
3. NLTK saves its German stopwords list (list = array in JS) into a var
4. define the func `preprocess`
  1. text argument is put in all lowercase
  2. `rid` is a list to rid the final frequency list of those (doesn't seem to work rn)
  3. the tokens list is set to empty
  4. we fill the tokens list with elements that each hold one word
  5. we change the tokens list to rid any elements that are in the German stopwords, a punctuation mark, or in the rid list
  6. a new string var is created to hold each element in `tokens` separated by 1 space
5.`preprocess` does the above to the string variable (from step 2) and the results are stored in `formatted_text`
6. the SpaCy's German model processes `formatted_text` and saves the results to doc 
7. make a new var list to hold each lemma from said results, i.e. `doc`
8. convert this new lemma list into a string var 
9. new string var is used by NLTK to do two things: tokenize each word and then rank them 