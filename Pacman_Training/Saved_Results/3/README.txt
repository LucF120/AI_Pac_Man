# For this run, I tried limiting pacman to only 1 life

BATCH_SIZE = 128
GAMMA = 0.99
EPS_START = 1
EPS_END = 0.05
EPS_DECAY = 300000    
TAU = 0.005
LR = 1e-4
num_episodes = 100  


Episode 0 training loss: 48.017269291507546.          Total Reward: 6.0
Episode 1 training loss: 7.076593084726483.          Total Reward: 1.0
Episode 2 training loss: 8.479890490882099.          Total Reward: 7.0
Episode 3 training loss: 10.68365529505536.          Total Reward: 9.0
Episode 4 training loss: 14.752660534344614.          Total Reward: 12.0
Episode 5 training loss: 17.99949494469911.          Total Reward: 0.0
Episode 6 training loss: 21.62525077071041.          Total Reward: 1.0
Episode 7 training loss: 25.345503230579197.          Total Reward: 5.0
Episode 8 training loss: 30.36596279591322.          Total Reward: 8.0
Episode 9 training loss: 46.03052737843245.          Total Reward: 9.0
Episode 10 training loss: 43.75778440386057.          Total Reward: 4.0
Episode 11 training loss: 48.411907037720084.          Total Reward: 4.0
Episode 12 training loss: 47.15943847037852.          Total Reward: -3.0
Episode 13 training loss: 59.289119539782405.          Total Reward: 7.0
Episode 14 training loss: 68.81247668899596.          Total Reward: 13.0
Episode 15 training loss: 68.33044662326574.          Total Reward: 5.0
Episode 16 training loss: 127.20941985026002.          Total Reward: 7.0
Episode 17 training loss: 84.1141132041812.          Total Reward: 7.0
Episode 18 training loss: 96.17010166682303.          Total Reward: 12.0
Episode 19 training loss: 101.0512135066092.          Total Reward: 2.0
Episode 20 training loss: 99.29971895366907.          Total Reward: -3.0
Episode 21 training loss: 94.05653197690845.          Total Reward: 1.0
Episode 22 training loss: 125.86123008653522.          Total Reward: 3.0
Episode 23 training loss: 144.9817772321403.          Total Reward: 7.0
Episode 24 training loss: 149.34303674846888.          Total Reward: 16.0
Episode 25 training loss: 173.90571822226048.          Total Reward: -1.0
Episode 26 training loss: 130.64056626707315.          Total Reward: 1.0
Episode 27 training loss: 156.50066586583853.          Total Reward: 0.0
Episode 28 training loss: 222.1954341456294.          Total Reward: 11.0
Episode 29 training loss: 216.30955333262682.          Total Reward: 6.0
Episode 30 training loss: 202.2137698456645.          Total Reward: 0.0
Episode 31 training loss: 333.38365994393826.          Total Reward: 10.0
Episode 32 training loss: 237.7448395267129.          Total Reward: 5.0
Episode 33 training loss: 205.5177903547883.          Total Reward: -3.0
Episode 34 training loss: 217.98909457027912.          Total Reward: 0.0
Episode 35 training loss: 293.67384096980095.          Total Reward: 5.0
Episode 36 training loss: 309.62358701229095.          Total Reward: 4.0
Episode 37 training loss: 413.14008286595345.          Total Reward: 10.0
Episode 38 training loss: 337.4375279545784.          Total Reward: 2.0
Episode 39 training loss: 412.77794839441776.          Total Reward: 9.0
Episode 40 training loss: 409.4682144522667.          Total Reward: 3.0
Episode 41 training loss: 470.5320113301277.          Total Reward: 4.0
Episode 42 training loss: 463.4019497036934.          Total Reward: 7.0
Episode 43 training loss: 443.99731731414795.          Total Reward: 1.0
Episode 44 training loss: 818.2943937778473.          Total Reward: 10.0
Episode 45 training loss: 698.1446897089481.          Total Reward: 9.0
Episode 46 training loss: 564.3319638371468.          Total Reward: 2.0
Episode 47 training loss: 685.0231868624687.          Total Reward: 5.0
Episode 48 training loss: 720.1908877491951.          Total Reward: 9.0
Episode 49 training loss: 863.2988401651382.          Total Reward: 18.0
Episode 50 training loss: 1142.3366503119469.          Total Reward: 8.0
Episode 51 training loss: 1010.0101419091225.          Total Reward: 4.0
Episode 52 training loss: 1026.0301581025124.          Total Reward: 7.0
Episode 53 training loss: 1041.161226451397.          Total Reward: 3.0
Episode 54 training loss: 1401.5776727199554.          Total Reward: 15.0
Episode 55 training loss: 1626.0726557970047.          Total Reward: 5.0
Episode 56 training loss: 1184.8054711818695.          Total Reward: 4.0
Episode 57 training loss: 1500.5404249429703.          Total Reward: 5.0
Episode 58 training loss: 1276.8407599925995.          Total Reward: 3.0
Episode 59 training loss: 2532.2612484693527.          Total Reward: 19.0
Episode 60 training loss: 1705.8171964883804.          Total Reward: 1.0
Episode 61 training loss: 2183.683298587799.          Total Reward: 2.0
Episode 62 training loss: 1704.896847128868.          Total Reward: 1.0
Episode 63 training loss: 1978.3973681926727.          Total Reward: 1.0
Episode 64 training loss: 2288.4585342407227.          Total Reward: 5.0
Episode 65 training loss: 2545.11015856266.          Total Reward: 5.0
Episode 66 training loss: 2372.7529945373535.          Total Reward: 3.0
Episode 67 training loss: 2238.1053812503815.          Total Reward: 3.0
Episode 68 training loss: 2477.6993622779846.          Total Reward: 2.0
Episode 69 training loss: 5374.874907255173.          Total Reward: 47.0
Episode 70 training loss: 2415.7703926563263.          Total Reward: -2.0
Episode 71 training loss: 4045.5423378944397.          Total Reward: 9.0
Episode 72 training loss: 3555.0703432559967.          Total Reward: 5.0
Episode 73 training loss: 3203.6852424144745.          Total Reward: 6.0
Episode 74 training loss: 4664.43087720871.          Total Reward: 8.0
Episode 75 training loss: 3147.8813829421997.          Total Reward: -1.0
Episode 76 training loss: 3609.1306385993958.          Total Reward: 1.0
Episode 77 training loss: 3859.133912563324.          Total Reward: 3.0
Episode 78 training loss: 5892.000668525696.          Total Reward: 5.0
Episode 79 training loss: 4005.758871078491.          Total Reward: -2.0
Episode 80 training loss: 6208.142524719238.          Total Reward: 11.0
Episode 81 training loss: 7326.380584716797.          Total Reward: 14.0
Episode 82 training loss: 5821.877962589264.          Total Reward: 0.0
Episode 83 training loss: 8306.856366157532.          Total Reward: 16.0
Episode 84 training loss: 7526.7683572769165.          Total Reward: 5.0
Episode 85 training loss: 8558.046510696411.          Total Reward: 13.0
Episode 86 training loss: 12521.376080513.          Total Reward: 17.0
Episode 87 training loss: 9225.395599365234.          Total Reward: -3.0
Episode 88 training loss: 10236.64111995697.          Total Reward: 1.0
Episode 89 training loss: 8982.193661689758.          Total Reward: -2.0
Episode 90 training loss: 11806.397058486938.          Total Reward: -2.0
Episode 91 training loss: 9767.671091079712.          Total Reward: -2.0
Episode 92 training loss: 12441.001356124878.          Total Reward: 0.0
Episode 93 training loss: 17419.90965270996.          Total Reward: 8.0
Episode 94 training loss: 18960.983156204224.          Total Reward: 5.0
Episode 95 training loss: 18716.18228340149.          Total Reward: 7.0
Episode 96 training loss: 23106.558839797974.          Total Reward: 8.0
Episode 97 training loss: 25030.024229049683.          Total Reward: 11.0
Episode 98 training loss: 23486.338417053223.          Total Reward: 9.0
Episode 99 training loss: 30739.46007347107.          Total Reward: 11.0