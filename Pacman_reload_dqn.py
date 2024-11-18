import pickle 
import matplotlib.pyplot as plt 
import torch

def save_execution(target_net_dict, policy_net_dict, memory, BATCH_SIZE, GAMMA, EPS_START, EPS_END, EPS_DECAY, TAU, LR, steps_done, total_rewards, REPLAY_MEMORY_CAPACITY):
    print("Beginning to save execution")
    print("-------------------------------------------------------------")
    #Save the target_net
    torch.save(target_net_dict, 'previous_run/target_net.pth') 
    print("Target_net saved to target_neth.pth")
    #Save the policy net
    torch.save(policy_net_dict, 'previous_run/policy_net.pth')  
    print("Policy_net saved to policy_net.pth")
    #Save the replay memory
    with open("previous_run/replay_memory.pkl", "wb") as f:
        pickle.dump(memory.memory, f)
    print("Replay memory saved to replay_memory.pkl")

    hyperparameters = {
        'BATCH_SIZE': BATCH_SIZE,
        'GAMMA': GAMMA,
        'EPS_START': EPS_START,
        'EPS_END': EPS_END,
        'EPS_DECAY': EPS_DECAY,
        'TAU': TAU,
        'LR': LR,
        'steps_done': steps_done,
        'REPLAY_MEMORY_CAPACITY': REPLAY_MEMORY_CAPACITY
    }
    # Save all the hyperparameters 
    with open('previous_run/hyperparameters.pkl', 'wb') as f:
        pickle.dump(hyperparameters, f)
    print("Hyperparameters saved to hyperparameters.pkl")

    plt.figure()
    plt.plot(range(1, len(total_rewards)+1), total_rewards, label="Total Reward vs Episode #")
    plt.xlabel('Episode')
    plt.ylabel('Total Reward')
    plt.legend()
    plt.savefig('previous_run/Rewards_Plot.png', dpi=300, bbox_inches='tight')
    print("Figure plotted to Rewards_Plot.png ")
    print("Finished saving execution to previous_run/")
    print("-------------------------------------------------------------")

def load_execution(policy_net, target_net=None, memory=None):
    print("Loading previous execution")
    # This loads the saved weights ------------------------------------------------------------------------
    policy_net.load_state_dict(torch.load('previous_run/policy_net.pth', weights_only=True))

    if target_net:
        target_net.load_state_dict(torch.load('previous_run/target_net.pth', weights_only=True))

    # To load the old hyperparameters  ------------------------------------------------------------------------
    with open('previous_run/hyperparameters.pkl', 'rb') as f:
        loaded_hyperparameters = pickle.load(f)

    BATCH_SIZE = loaded_hyperparameters['BATCH_SIZE']
    GAMMA = loaded_hyperparameters['GAMMA']
    EPS_START = loaded_hyperparameters['EPS_START']
    EPS_END = loaded_hyperparameters['EPS_END']
    EPS_DECAY = loaded_hyperparameters['EPS_DECAY']
    TAU = loaded_hyperparameters['TAU']
    LR = loaded_hyperparameters['LR']
    steps_done = loaded_hyperparameters['steps_done']
    REPLAY_MEMORY_CAPACITY = loaded_hyperparameters['REPLAY_MEMORY_CAPACITY']

    # To load the ReplayMemory ------------------------------------------------------------------------
    if memory:
        memory = ReplayMemory(REPLAY_MEMORY_CAPACITY)
        with open("previous_run/replay_memory.pkl", "rb") as f:
            memory.memory = pickle.load(f)

    print("Finished loading previous execution")
    return [BATCH_SIZE, GAMMA, EPS_START, EPS_END, EPS_DECAY, TAU, LR, steps_done, REPLAY_MEMORY_CAPACITY]
