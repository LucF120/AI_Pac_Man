# This pacman scored a positive reward in one episode

BATCH_SIZE = 128
GAMMA = 0.99
EPS_START = 1
EPS_END = 0.01
EPS_DECAY = 3000000    
TAU = 0.005
LR = 1e-4
num_episodes = 100




Episode 0 training loss: 4.265888140420429.          Total Reward: -78.0
Episode 1 training loss: 69.61400052532554.          Total Reward: -77.0
Episode 2 training loss: 83.9546702876687.          Total Reward: -80.0
Episode 3 training loss: 82.69491489836946.          Total Reward: -85.0
Episode 4 training loss: 100.11041699256748.          Total Reward: -87.0
Episode 5 training loss: 113.08185399882495.          Total Reward: -82.0
Episode 6 training loss: 90.19336864165962.          Total Reward: -88.0
Episode 7 training loss: 86.4648544229567.          Total Reward: -94.0
Episode 8 training loss: 94.59523701667786.          Total Reward: -91.0
Episode 9 training loss: 155.0269207507372.          Total Reward: -91.0
Episode 10 training loss: 198.64855264872313.          Total Reward: -78.0
Episode 11 training loss: 242.4938474074006.          Total Reward: -85.0
Episode 12 training loss: 230.03352692723274.          Total Reward: -81.0
Episode 13 training loss: 221.598384141922.          Total Reward: -93.0
Episode 14 training loss: 406.1155662089586.          Total Reward: -72.0
Episode 15 training loss: 355.15965884923935.          Total Reward: -78.0
Episode 16 training loss: 556.395284473896.          Total Reward: -72.0
Episode 17 training loss: 492.1128120422363.          Total Reward: -83.0
Episode 18 training loss: 512.7481089234352.          Total Reward: -87.0
Episode 19 training loss: 649.733641564846.          Total Reward: -84.0
Episode 20 training loss: 601.6159720420837.          Total Reward: -93.0
Episode 21 training loss: 765.4591118097305.          Total Reward: -88.0
Episode 22 training loss: 819.4428855776787.          Total Reward: -89.0
Episode 23 training loss: 1088.8145016431808.          Total Reward: -85.0
Episode 24 training loss: 1561.259225010872.          Total Reward: -84.0
Episode 25 training loss: 1113.5630412101746.          Total Reward: -88.0
Episode 26 training loss: 1644.125144958496.          Total Reward: -82.0
Episode 27 training loss: 2176.542875289917.          Total Reward: -81.0
Episode 28 training loss: 2445.392962694168.          Total Reward: -79.0
Episode 29 training loss: 2045.0837173461914.          Total Reward: -90.0
Episode 30 training loss: 4823.188863039017.          Total Reward: -43.0
Episode 31 training loss: 3448.2417125701904.          Total Reward: -82.0
Episode 32 training loss: 3375.3784255981445.          Total Reward: -86.0
Episode 33 training loss: 3617.3915100097656.          Total Reward: -88.0
Episode 34 training loss: 3691.4470930099487.          Total Reward: -85.0
Episode 35 training loss: 4855.007560253143.          Total Reward: -86.0
Episode 36 training loss: 4184.2471833229065.          Total Reward: -91.0
Episode 37 training loss: 5482.856785297394.          Total Reward: -83.0
Episode 38 training loss: 5926.141688346863.          Total Reward: -89.0
Episode 39 training loss: 5087.86434841156.          Total Reward: -93.0
Episode 40 training loss: 5989.952949047089.          Total Reward: -87.0
Episode 41 training loss: 5612.736078262329.          Total Reward: -91.0
Episode 42 training loss: 7862.069585800171.          Total Reward: -82.0
Episode 43 training loss: 16476.222317695618.          Total Reward: 1.0
Episode 44 training loss: 7551.9808559417725.          Total Reward: -86.0
Episode 45 training loss: 8570.313364982605.          Total Reward: -81.0
Episode 46 training loss: 7094.052508354187.          Total Reward: -94.0
Episode 47 training loss: 9330.225501060486.          Total Reward: -89.0
Episode 48 training loss: 12963.630133628845.          Total Reward: -78.0
Episode 49 training loss: 11606.855725288391.          Total Reward: -85.0
Episode 50 training loss: 11671.278443336487.          Total Reward: -85.0
Episode 51 training loss: 14501.988716125488.          Total Reward: -75.0
Episode 52 training loss: 11406.368168830872.          Total Reward: -86.0
Episode 53 training loss: 10378.8794631958.          Total Reward: -88.0
Episode 54 training loss: 17249.969829559326.          Total Reward: -78.0
Episode 55 training loss: 16307.047602653503.          Total Reward: -82.0
Episode 56 training loss: 14768.942029953003.          Total Reward: -80.0
Episode 57 training loss: 17461.700145721436.          Total Reward: -89.0
Episode 58 training loss: 19627.86363220215.          Total Reward: -85.0
Episode 59 training loss: 22563.32038116455.          Total Reward: -84.0
Episode 60 training loss: 17989.466625213623.          Total Reward: -89.0
Episode 61 training loss: 18909.36095046997.          Total Reward: -88.0
Episode 62 training loss: 19506.603889465332.          Total Reward: -83.0
Episode 63 training loss: 25016.422632217407.          Total Reward: -83.0
Episode 64 training loss: 33699.0178604126.          Total Reward: -50.0
Episode 65 training loss: 29945.52974319458.          Total Reward: -81.0
Episode 66 training loss: 42367.9807510376.          Total Reward: -73.0
Episode 67 training loss: 28402.343547821045.          Total Reward: -87.0
Episode 68 training loss: 32793.17611312866.          Total Reward: -83.0
Episode 69 training loss: 34330.452587127686.          Total Reward: -83.0
Episode 70 training loss: 29201.611892700195.          Total Reward: -83.0
Episode 71 training loss: 54207.60974121094.          Total Reward: -73.0
Episode 72 training loss: 39611.301094055176.          Total Reward: -77.0
Episode 73 training loss: 37058.50296783447.          Total Reward: -91.0
Episode 74 training loss: 59761.13620758057.          Total Reward: -70.0
Episode 75 training loss: 49975.20796203613.          Total Reward: -85.0
Episode 76 training loss: 60293.751861572266.          Total Reward: -84.0
Episode 77 training loss: 67441.065284729.          Total Reward: -79.0
Episode 78 training loss: 54699.78926849365.          Total Reward: -87.0
Episode 79 training loss: 54464.15148925781.          Total Reward: -77.0
Episode 80 training loss: 70864.56735229492.          Total Reward: -77.0
Episode 81 training loss: 61575.82430267334.          Total Reward: -87.0
Episode 82 training loss: 58290.83016204834.          Total Reward: -88.0
Episode 83 training loss: 84724.10202026367.          Total Reward: -78.0
Episode 84 training loss: 67846.23097991943.          Total Reward: -91.0
Episode 85 training loss: 73032.02593231201.          Total Reward: -89.0
Episode 86 training loss: 75966.48949813843.          Total Reward: -88.0
Episode 87 training loss: 90377.95167541504.          Total Reward: -81.0
Episode 88 training loss: 85046.08882904053.          Total Reward: -84.0
Episode 89 training loss: 66248.60803222656.          Total Reward: -91.0
Episode 90 training loss: 115170.25580596924.          Total Reward: -82.0
Episode 91 training loss: 92069.4803390503.          Total Reward: -79.0
Episode 92 training loss: 125639.10348510742.          Total Reward: -55.0
Episode 93 training loss: 95793.2236328125.          Total Reward: -90.0
Episode 94 training loss: 112660.36126708984.          Total Reward: -89.0
Episode 95 training loss: 90179.71394348145.          Total Reward: -91.0
Episode 96 training loss: 130839.78662109375.          Total Reward: -78.0
Episode 97 training loss: 111109.31561279297.          Total Reward: -84.0
Episode 98 training loss: 134997.8635559082.          Total Reward: -78.0
Episode 99 training loss: 124009.57885742188.          Total Reward: -85.0