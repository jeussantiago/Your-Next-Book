import os
import numpy as np

# from tensorflow.keras.models import model_from_json
import random
from IPython.display import clear_output
import time


#returns a character to int and vice versa dictionary
def get_char_int_conversion():
    #basic characters in all books
    unique_chars = [' ', '!', '&', "'", '(', ')', ',', '-', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '?', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    #turn characters into integers and integers into characters - chars should be sorted to keep consistency
    char_to_int = {}
    int_to_char = {}
    for i, char in enumerate(sorted(set(unique_chars))):
        char_to_int[char] = i
        int_to_char[i] = char
        
    return char_to_int, int_to_char

#returns a list of all the path weights and the architecture
def get_weights_and_arch():
    round_path = "../Modelling/models/"
    model_paths = []
    for root, dirs, files in os.walk(round_path):
        #file names in files path
        for file in files:
            if file.endswith('hdf5'):
                model_paths.append(root+"/"+file)
            elif file.endswith('model_8_architecture.json'):
                architecture_path = root+"/"+file
    #sort paths
    model_paths.sort()
    # load json architecture
    json_file = open(architecture_path, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    #return model paths
    return model_paths, loaded_model_json


#creates new sentences
def create_passage(model, sentence, char_to_int, int_to_char):

    sentence_length = len(sentence)
    
    print('original sentence: ', sentence.split("  ")[-1])
    print('\n')
    #predict the next 500 characters 
    gen_sentence = sentence
    print(gen_sentence.split("  ")[-1], end="", flush=True)
    # print(gen_sentence.split("  ")[-1])
    for i in range(500):
        #turn single sentence into model format
        x_pred = np.zeros((1, sentence_length, len(char_to_int)))
        #fill tensor with correspoinding values
        for k, c in enumerate(sentence):
            x_ind = char_to_int[c]
            x_pred[0, k, x_ind] = 1

        #predict next character - returns predicted probabilities
        prob_c = model.predict(x_pred, verbose=0)[0]
        #turn to float64 - mulitnomial gives error otherwise
        prob_c = np.asarray(prob_c).astype('float64')
        #sample from the probability - try out difference softmax temperature values - 0.5 produced best results
        log_prob = np.log(prob_c) / 0.5
        exp_prob = np.exp(log_prob)
        pred_prob = exp_prob/np.sum(exp_prob)
        #sample from new probability distribution
        p = np.random.multinomial(1, pred_prob, 1) 
        #get the probability position
        prob_ind = np.argmax(p)

        #turn prediction into a character
        next_c = int_to_char[prob_ind]
        #add character to generated sentence
        gen_sentence += next_c
        #get new sentence by sliding to index of sentence
        sentence = sentence[1:]+next_c
        print(next_c, end="", flush=True)

  
    return gen_sentence.split("  ")[-1]
    # return gen_sentence


#gets input from user and modifies it
def input_sentence():
    #take input from user
    while True:
        sentence = input("Type in some text: ")
        sent_len = len(sentence)
        #check if the user inputed anything
        if sent_len > 0:
            break
        else:
            print("You didn't enter anything in.")
            time.sleep(1.8)
            clear_output()
    #check if the length is less than the length of the sentences the model was trained on
    if sent_len < 50:
        while sent_len < 50:
            sentence = ' ' + sentence
            sent_len = len(sentence)
    #sentence has more characters than what was trained on
    else:
        #grab the last 50 characters
        sentence = sentence[-50:]
    
    #lowercase everything
    sentence = sentence.lower()

    return sentence

