#For this run, I normalized the inputs by dividing by 255.0\

BATCH_SIZE = 128
GAMMA = 0.99
EPS_START = 1
EPS_END = 0.05
EPS_DECAY = 300000    
TAU = 0.005
LR = 1e-4
num_episodes = 100

Episode 0 training loss: 2.176415321562672.          Total Reward: -88.0
Episode 1 training loss: 68.22454378777184.          Total Reward: -88.0
Episode 2 training loss: 76.54661304992624.          Total Reward: -88.0
Episode 3 training loss: 80.42451235838234.          Total Reward: -89.0
Episode 4 training loss: 119.09664109256119.          Total Reward: -88.0
Episode 5 training loss: 79.25134874507785.          Total Reward: -90.0
Episode 6 training loss: 93.66839941497892.          Total Reward: -91.0
Episode 7 training loss: 103.6828837543726.          Total Reward: -86.0
Episode 8 training loss: 116.88085597753525.          Total Reward: -88.0
Episode 9 training loss: 107.30384599044919.          Total Reward: -91.0
Episode 10 training loss: 158.57747292518616.          Total Reward: -80.0
Episode 11 training loss: 188.48398815095425.          Total Reward: -83.0
Episode 12 training loss: 165.09791761636734.          Total Reward: -80.0
Episode 13 training loss: 136.28333489224315.          Total Reward: -92.0
Episode 14 training loss: 179.14351592957973.          Total Reward: -83.0
Episode 15 training loss: 216.79422419518232.          Total Reward: -86.0
Episode 16 training loss: 159.90709379315376.          Total Reward: -92.0
Episode 17 training loss: 214.78895961493254.          Total Reward: -87.0
Episode 18 training loss: 185.48646973073483.          Total Reward: -92.0
Episode 19 training loss: 210.39175705611706.          Total Reward: -91.0
Episode 20 training loss: 277.86448960006237.          Total Reward: -81.0
Episode 21 training loss: 252.6185928285122.          Total Reward: -84.0
Episode 22 training loss: 306.64835450053215.          Total Reward: -86.0
Episode 23 training loss: 348.9232355207205.          Total Reward: -79.0
Episode 24 training loss: 467.36825700104237.          Total Reward: -85.0
Episode 25 training loss: 277.64464950561523.          Total Reward: -91.0
Episode 26 training loss: 472.0968009829521.          Total Reward: -73.0
Episode 27 training loss: 537.5862221419811.          Total Reward: -87.0
Episode 28 training loss: 375.267492800951.          Total Reward: -90.0
Episode 29 training loss: 415.1913043856621.          Total Reward: -90.0
Episode 30 training loss: 552.6044293344021.          Total Reward: -85.0
Episode 31 training loss: 655.7759625315666.          Total Reward: -88.0
Episode 32 training loss: 583.016411781311.          Total Reward: -83.0
Episode 33 training loss: 647.7382362484932.          Total Reward: -86.0
Episode 34 training loss: 667.9039560556412.          Total Reward: -83.0
Episode 35 training loss: 674.1251267194748.          Total Reward: -87.0
Episode 36 training loss: 789.488803088665.          Total Reward: -80.0
Episode 37 training loss: 887.188990175724.          Total Reward: -87.0
Episode 38 training loss: 854.5840367078781.          Total Reward: -85.0
Episode 39 training loss: 1173.5840241909027.          Total Reward: -82.0
Episode 40 training loss: 968.5316544771194.          Total Reward: -82.0
Episode 41 training loss: 970.9670035243034.          Total Reward: -86.0
Episode 42 training loss: 938.8000153303146.          Total Reward: -85.0
Episode 43 training loss: 1228.2356305122375.          Total Reward: -84.0
Episode 44 training loss: 1114.7601310014725.          Total Reward: -81.0
Episode 45 training loss: 1126.9627106189728.          Total Reward: -85.0
Episode 46 training loss: 856.7238371372223.          Total Reward: -92.0
Episode 47 training loss: 1079.2502082586288.          Total Reward: -91.0
Episode 48 training loss: 1170.8706045150757.          Total Reward: -87.0
Episode 49 training loss: 1135.3122688531876.          Total Reward: -82.0
Episode 50 training loss: 2067.037011384964.          Total Reward: -82.0
Episode 51 training loss: 1601.797699213028.          Total Reward: -89.0
Episode 52 training loss: 1600.9424793720245.          Total Reward: -82.0
Episode 53 training loss: 1253.6710540056229.          Total Reward: -94.0
Episode 54 training loss: 1330.503668308258.          Total Reward: -84.0
Episode 55 training loss: 2027.2757263183594.          Total Reward: -72.0
Episode 56 training loss: 1493.5371783971786.          Total Reward: -87.0
Episode 57 training loss: 1419.5477249622345.          Total Reward: -91.0
Episode 58 training loss: 1424.1869773864746.          Total Reward: -91.0
Episode 59 training loss: 2462.97895359993.          Total Reward: -78.0
Episode 60 training loss: 1959.0830742120743.          Total Reward: -82.0
Episode 61 training loss: 2069.195919394493.          Total Reward: -78.0
Episode 62 training loss: 2201.0812408924103.          Total Reward: -85.0
Episode 63 training loss: 2009.7057577371597.          Total Reward: -91.0
Episode 64 training loss: 3245.5517570972443.          Total Reward: -86.0
Episode 65 training loss: 2449.3004117012024.          Total Reward: -82.0
Episode 66 training loss: 2114.0762066841125.          Total Reward: -86.0
Episode 67 training loss: 2863.902253627777.          Total Reward: -85.0
Episode 68 training loss: 3276.051916360855.          Total Reward: -75.0
Episode 69 training loss: 2498.8717534542084.          Total Reward: -80.0
Episode 70 training loss: 2322.863620519638.          Total Reward: -89.0
Episode 71 training loss: 2788.8287813663483.          Total Reward: -88.0
Episode 72 training loss: 3028.4543948173523.          Total Reward: -74.0
Episode 73 training loss: 2825.828594684601.          Total Reward: -83.0
Episode 74 training loss: 4700.373844861984.          Total Reward: -78.0
Episode 75 training loss: 3390.5511569976807.          Total Reward: -84.0
Episode 76 training loss: 4009.107012271881.          Total Reward: -81.0
Episode 77 training loss: 5997.88614654541.          Total Reward: -86.0
Episode 78 training loss: 3671.3793210983276.          Total Reward: -85.0
Episode 79 training loss: 3719.954319000244.          Total Reward: -88.0
Episode 80 training loss: 4329.936456680298.          Total Reward: -85.0
Episode 81 training loss: 3699.0540647506714.          Total Reward: -85.0
Episode 82 training loss: 4461.195041656494.          Total Reward: -86.0
Episode 83 training loss: 7870.614924907684.          Total Reward: -77.0
Episode 84 training loss: 4477.00778055191.          Total Reward: -85.0
Episode 85 training loss: 4013.7899832725525.          Total Reward: -92.0
Episode 86 training loss: 6052.720845222473.          Total Reward: -80.0
Episode 87 training loss: 5260.7464599609375.          Total Reward: -86.0
Episode 88 training loss: 4845.791329860687.          Total Reward: -83.0
Episode 89 training loss: 6121.076213359833.          Total Reward: -86.0
Episode 90 training loss: 5220.332784175873.          Total Reward: -91.0
Episode 91 training loss: 6659.103207588196.          Total Reward: -85.0
Episode 92 training loss: 8931.46407365799.          Total Reward: -74.0
Episode 93 training loss: 6589.432014942169.          Total Reward: -86.0
Episode 94 training loss: 11057.80040550232.          Total Reward: -85.0
Episode 95 training loss: 6817.126842498779.          Total Reward: -89.0
Episode 96 training loss: 9712.291670799255.          Total Reward: -80.0
Episode 97 training loss: 8747.79125213623.          Total Reward: -83.0
Episode 98 training loss: 9622.377119064331.          Total Reward: -72.0
Episode 99 training loss: 10907.055158615112.          Total Reward: -85.0