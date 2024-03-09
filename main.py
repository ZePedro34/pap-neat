from __future__ import print_function
import os
import neat
from Simulation import runPreySimulation, runSimulation
from controller.NeatPredatorController import NeatPredatorController
from controller.NeatPreyController import NeatPreyController
import visualize
import pickle


def eval_genomes(genomes, config):
    for genome_id, genome in genomes:
        neural_net = neat.nn.FeedForwardNetwork.create(genome, config)
        preyController = NeatPreyController(neural_net)
        genome.fitness = runPreySimulation(800, preyController)


def run(config_file):
    # Load configuration.
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    #stats = neat.StatisticsReporter()
    #p.add_reporter(stats)
    #p.add_reporter(neat.Checkpointer(5000))

    # Run for up to 300 generations.
    winner = p.run(eval_genomes, 10)
    print('\nBest genome:\n{!s}'.format(winner))

    # Save best genome neural network
    winner_net = neat.nn.FeedForwardNetwork.create(winner, config)
    with open(f'winner_neural_net.pickle', 'wb') as file:
        pickle.dump(winner_net, file) 

    # Show visualizer (diagrams, charts, ...)
    #node_names = {-1:'E', -2: 'F1', -3: 'F2', -4: 'F3', -5: 'F4', -6: 'F4', -7: 'F5', -8: 'F6', 0:'FW', 1:'RL', 2:'RR'}
    #visualize.draw_net(config, winner, True, node_names=node_names)
    #visualize.plot_stats(stats, ylog=False, view=True)
    #visualize.plot_species(stats, view=True)


def runFromCheckpoint():
    pass
    #p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-4')
    #p.run(eval_genomes, 10)

def runFromFile():
    with open(f'winner_neural_net.pickle', 'rb') as file:
        winner_net = pickle.load(file)
    preyController = NeatPreyController(winner_net)
    predatorController = NeatPredatorController(winner_net)
    runSimulation(preyController, predatorController)



if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'neat-preypred-config')
    
    #run(config_path)
    runFromFile()