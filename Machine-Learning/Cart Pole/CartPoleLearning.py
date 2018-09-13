'''
Goal of this project is to give an idea of how constructing a neural network works.

Project idea is from OpenAi gym
https://gym.openai.com/envs/CartPole-v1/
CartPole Description
A pole is attached by an un-actuated joint to a cart, which moves along a
frictionless track. The system is controlled by applying a force of +1 or
-1 to the cart. The pendulum starts upright, and the goal is to prevent it
from falling over. A reward of +1 is provided for every timestep that the
pole remains upright. The episode ends when the pole is more than 15 degrees
from vertical, or the cart moves more than 2.4 units from the center.
'''

import gym #Environment game
import random #Agent which moves randomly for starting data
import numpy as np
import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
from statistics import mean, median
from collections import Counter


LR = 1e-3 # Learning rate
env = gym.make("CartPole-v0").env #This takes from OpenAi gym creating the game
env.reset()
goal_steps = 500 #Every frame with the pole still balanced is +1 point
score_requirment = 50 # Chooses the games with the score greater than this
initial_games = 10000


def some_random_games_first():
    for episode in range(5):
        env.reset()
        for t in range(goal_steps):
            env.render() # Shows you the learning process
            action = env.action_space.sample() #Takes random action in your env
            # Observation is data from game like movements
            # Reward balances vs not
            observation, reward, done, info = env.step(action)
            if done:
                break


def intial_population():
    training_data = [] # Actual data to train Observaiton and move made
    scores = [] # Overall scores
    accepted_scores = [] # Scores above 50
    for _ in range(initial_games):
        score = 0
        game_memory = []
        prev_observation = []
        for _ in range(goal_steps):
            action = random.randrange(0,2)
            observation, reward, done, info = env.step(action)
            if len(prev_observation) > 0:
                game_memory.append([prev_observation, action])
            prev_observation = observation
            score += reward
            if done:
                break
        if score >= score_requirment:
            accepted_scores.append(score)
            for data in game_memory:
                if data[1] == 1:
                    output = [0, 1]
                elif data[1] == 0:
                    output = [1, 0]
                training_data.append([data[0], output])
        env.reset()
        scores.append(score)
    training_data_save = np.array(training_data)
    np.save("saved.npy", training_data_save)
    print("Average accepted scores: ", mean(accepted_scores))
    print("Median accepted score: ", median(accepted_scores))
    print(Counter(accepted_scores))
    return training_data


def neural_network_model(input_size):
    network = input_data(shape = [None, input_size, 1], name = "input")
    
    network = fully_connected(network, 128, activation="relu")
    network = dropout(network, 0.8)
    
    network = fully_connected(network, 256, activation="relu")
    network = dropout(network, 0.8)
    
    network = fully_connected(network, 512, activation="relu")
    network = dropout(network, 0.8)
    
    network = fully_connected(network, 256, activation="relu")
    network = dropout(network, 0.8)
    
    network = fully_connected(network, 128, activation="relu")
    network = dropout(network, 0.8)

    network = fully_connected(network, 2, activation = "softmax")
    network = regression(network, optimizer = "adam", learning_rate=LR, loss = "categorical_crossentropy", name = "targets")
    model = tflearn.DNN(network, tensorboard_dir = "log")

    return model


def train_model(training_data, model=False):
    x = np.array([i[0] for i in training_data]).reshape(-1, len(training_data[0][0]), 1)
    y = [i[1] for i in training_data]
    if not model:
        model = neural_network_model(input_size = len(x[0]))
    model.fit({"input":x}, {"targets":y}, n_epoch = 3, snapshot_step = 500, show_metric = True, run_id = "openaistuff")
    return model


training_data = intial_population()
model = train_model(training_data)

scores = []
choices = []

for each_game in range(100):
    score = 0
    game_memory = []
    prev_obs = []
    env.reset()
    for _ in range(goal_steps):
        #env.render()
        if len(prev_obs) == 0:
            action = random.randrange(0,2)
        else:
            action = np.argmax(model.predict(prev_obs.reshape(-1, len(prev_obs), 1))[0])
        choices.append(action)
        new_observation, reward, done, info = env.step(action)
        prev_obs = new_observation
        game_memory.append([new_observation, action])
        score += reward
        if done:
            break
    scores.append(score)


print("Average Score: ", sum(scores)/len(scores))
print("Choice 1: {}, Choice 0: {}".format(choices.count(1)/len(choices), choices.count(0)/len(choices)))
