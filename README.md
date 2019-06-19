# Your Next Book

## Dataset
Many stories were obtained from Project Gutenberg, a free and easily obtainable data source with multiple story formats such as txt and pdf. All of the books in this project were in the format of txt. All of the stories were chosen because they were listed as being the "Top 100 EBooks last 30 days." As such, if the website is scraped again, the books listed would be different from the books at the time of scraping for this project. (If interested, the scraper is contained in the "get books.ipynb" through the "get_data/" path). All the books were then cleaned to contain only the basic characters that every novel would have such as the alpahbet, numbers, question marks, periods, etc and finally combined into one corpus for easier access. (This process can be found in the "combine books.ipynb" through the "get_data/" path).

Although this method of obtaining data is very easy, it should be noted that the topics and genres discussed within the obtained books will vary. As such, producing pieces of text will result in the combination of words that normally wouldn't be seen in the same story such as "Frankenstein" and "Prince". Project Gutenberg is also filled with many texts that have no copyright issue, which means that these pieces of texts are much older and will result in the creation of older english syntax rather than what is familiar in modern times.

The final corpus is located in "books_combined.txt" and contains 96 books, totaling to 74 million characters.

## Method
This project tackles the problem of creating unique pieces of texts by predicting the next character given a sequence of characters. As this is a sequence problem, it is fitting to use Recurrent Nueral Networks(RNN). Long short-term memory(LSTM), an alternate version of RNNs, was chosen for its method of alleviating the vanishing gradient problem.

There are many ways to create sequences through text. One way is to convert each character in the sequence into a unique integer value e.g. a -> 1, b -> 2. This is the method used to create the sequence, but with an additional one hot encoding variation. <br>
("Gone so Soon?" Table)
The above image represents one datapoint/sequence ("gone so soon?"). The columns represent the unique characters within the corpus however, it should be noted that this image is just a visual representation and there are more unique characters within the actual corpus. Each row represents a corresponding character within the sequence. As you can see, unique characters that are present within the sequence are given a 1, representing that it exist. <br>

## Dealing with Large Data
There are around 74 million characters within the corpus, which means there are a corresponding 74 million sequences that could have been made. However, the computer this project was run on did not have enough space to hold all of that information therefore, alternate methods were explored to go around this problem. Here we note the advantages and disadvantages of the alternate methods:

1. Lessen Corpus Size
    - Having a large corpus allows the model to generalise on the every novel at once.
    - Using a batch of the corpus means taking the weights which the network has learned from the previous batch and sending it into the new batch. It was found that the model would be able to create texts which resembles the portion of the corpus it was trained on but completely change its writing style once it was trained on a different section of the corpus with little to no reference to the previous corpus batch.
 
2. Lessen Sequence Length
    - The larger the sequence, the more unique the sequence becomes and the easier it is to know what the next character is.
    - Lessening the sequence size leads to generalising which would result in the appearnce of more stop words such as "the" or "is."
    - "staunch and true friend; and it was with a feeling o" vs. "feeling o"

3. Lessen Amount of Sequences created with each Corpus Batch
    - The more sequences, the better. It allows the model to learn sentence syntax better simply because of having more training examples.
    - Less sequences leads to less rentention of grammatical syntax. Words which appear less frequently in the corpus such as "calculus" move never be learned by the model. It would know 'c' would come after a certain sequence and 's' would come after a different unique sequence. But never be able to learn to predict 'c','a','l','c','u','l','u','s' given a sequence simply because it has never been trained on it.


