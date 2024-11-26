# Positive results after 1300 episodes
# Changed reward from -1 to -10 for pacman dying


BATCH_SIZE = 64
GAMMA = 0.99
EPS_START = 1
EPS_END = 0.01
EPS_DECAY = 40000    
TAU = 0.005
LR = 1e-5
REPLAY_MEMORY_CAPACITY = 10000

num_episodes = 10000
# This decides how many episodes until running save_execution() 
save_rate = 100



Episode 0 training loss: 29.77444025730074.          Total Reward: -23.0
Steps done: 407        Epsilon: 0.9899778242856405
Episode 1 training loss: 41.43115158910223.          Total Reward: -28.0
Steps done: 760        Epsilon: 0.9813675686203779
Episode 2 training loss: 57.405461766029475.          Total Reward: -23.0
Steps done: 1295        Epsilon: 0.9684620255985202
Episode 3 training loss: 41.301102782948874.          Total Reward: -28.0
Steps done: 1714        Epsilon: 0.958474536677057
Episode 4 training loss: 40.721277906006435.          Total Reward: -28.0
Steps done: 2131        Epsilon: 0.9486380513978357
Episode 5 training loss: 56.79582680770545.          Total Reward: -17.0
Steps done: 2732        Epsilon: 0.9346404350979313
Episode 6 training loss: 31.262308721314184.          Total Reward: -31.0
Steps done: 3051        Epsilon: 0.9272957534731578
Episode 7 training loss: 48.20120815135306.          Total Reward: -27.0
Steps done: 3500        Epsilon: 0.9170566829343689
Episode 8 training loss: 45.00559310161043.          Total Reward: -26.0
Steps done: 3935        Epsilon: 0.9072458844142384
Episode 9 training loss: 43.39446017006412.          Total Reward: -22.0
Steps done: 4354        Epsilon: 0.897896287778086
Episode 10 training loss: 40.67592725530267.          Total Reward: -24.0
Steps done: 4739        Epsilon: 0.8893912820074792
Episode 11 training loss: 49.84323200734798.          Total Reward: -23.0
Steps done: 5194        Epsilon: 0.8794448835631243
Episode 12 training loss: 43.36736846936401.          Total Reward: -24.0
Steps done: 5595        Epsilon: 0.8707722428506711
Episode 13 training loss: 31.643983603804372.          Total Reward: -31.0
Steps done: 5948        Epsilon: 0.8632093481638363
Episode 14 training loss: 38.154352278332226.          Total Reward: -30.0
Steps done: 6305        Epsilon: 0.8556283353237326
Episode 15 training loss: 40.14875507541001.          Total Reward: -23.0
Steps done: 6650        Epsilon: 0.848366154107853
Episode 16 training loss: 56.58343473402783.          Total Reward: -22.0
Steps done: 7143        Epsilon: 0.8380967067265338
Episode 17 training loss: 40.97847389103845.          Total Reward: -28.0
Steps done: 7492        Epsilon: 0.830902991179867
Episode 18 training loss: 53.113581663230434.          Total Reward: -26.0
Steps done: 7923        Epsilon: 0.8221052444290174
Episode 19 training loss: 49.214162182062864.          Total Reward: -20.0
Steps done: 8338        Epsilon: 0.8137232095113566
Episode 20 training loss: 51.54276719596237.          Total Reward: -22.0
Steps done: 8775        Epsilon: 0.8049903236959592
Episode 21 training loss: 40.65686843544245.          Total Reward: -30.0
Steps done: 9098        Epsilon: 0.798596626128094
Episode 22 training loss: 49.77045151917264.          Total Reward: -30.0
Steps done: 9503        Epsilon: 0.790652370947805
Episode 23 training loss: 57.79274898348376.          Total Reward: -19.0
Steps done: 9962        Epsilon: 0.781745585406885
Episode 24 training loss: 69.58915617596358.          Total Reward: -16.0
Steps done: 10569        Epsilon: 0.7701227573976742
Episode 25 training loss: 54.653766681905836.          Total Reward: -28.0
Steps done: 11016        Epsilon: 0.7616756715820137
Episode 26 training loss: 49.58372910064645.          Total Reward: -25.0
Steps done: 11401        Epsilon: 0.7544754996560469
Episode 27 training loss: 51.4466352253221.          Total Reward: -27.0
Steps done: 11832        Epsilon: 0.7464968383786987
Episode 28 training loss: 59.45286687463522.          Total Reward: -26.0
Steps done: 12273        Epsilon: 0.7384215575174419
Episode 29 training loss: 58.177947795484215.          Total Reward: -29.0
Steps done: 12706        Epsilon: 0.7305789190217971
Episode 30 training loss: 55.16768268821761.          Total Reward: -21.0
Steps done: 13129        Epsilon: 0.7229989466961022
Episode 31 training loss: 50.675391643773764.          Total Reward: -31.0
Steps done: 13500        Epsilon: 0.7164164549594374
Episode 32 training loss: 60.3949901368469.          Total Reward: -25.0
Steps done: 13977        Epsilon: 0.7080424678675189
Episode 33 training loss: 44.53979154024273.          Total Reward: -31.0
Steps done: 14324        Epsilon: 0.7020131394823311
Episode 34 training loss: 77.31458176951855.          Total Reward: -22.0
Steps done: 14889        Epsilon: 0.6923071637149488
Episode 35 training loss: 54.38955502398312.          Total Reward: -17.0
Steps done: 15312        Epsilon: 0.6851297827479848
Episode 36 training loss: 55.42001914791763.          Total Reward: -18.0
Steps done: 15749        Epsilon: 0.677794133816188
Episode 37 training loss: 79.46944386791438.          Total Reward: 0.0
Steps done: 16344        Epsilon: 0.6679342110556973
Episode 38 training loss: 90.44842359377071.          Total Reward: -21.0
Steps done: 17007        Epsilon: 0.6571188315734382
Episode 39 training loss: 64.52165678981692.          Total Reward: -22.0
Steps done: 17508        Epsilon: 0.649064215538369
Episode 40 training loss: 85.75123397214338.          Total Reward: -22.0
Steps done: 18205        Epsilon: 0.6380249802395663
Episode 41 training loss: 78.45417629508302.          Total Reward: -18.0
Steps done: 18862        Epsilon: 0.6277939225114517
Episode 42 training loss: 49.87070492049679.          Total Reward: -32.0
Steps done: 19277        Epsilon: 0.6214174457358947
Episode 43 training loss: 62.73543762229383.          Total Reward: -24.0
Steps done: 19824        Epsilon: 0.613113221708226
Episode 44 training loss: 45.36431459756568.          Total Reward: -31.0
Steps done: 20229        Epsilon: 0.607037510530788
Episode 45 training loss: 48.37868175469339.          Total Reward: -27.0
Steps done: 20616        Epsilon: 0.6012890257523245
Episode 46 training loss: 54.49228953709826.          Total Reward: -28.0
Steps done: 21071        Epsilon: 0.5946012220792184
Episode 47 training loss: 67.5474938582629.          Total Reward: -14.0
Steps done: 21622        Epsilon: 0.5866035506701033
Episode 48 training loss: 66.25539926905185.          Total Reward: -21.0
Steps done: 22183        Epsilon: 0.5785731308230843
Episode 49 training loss: 47.550727132707834.          Total Reward: -24.0
Steps done: 22588        Epsilon: 0.5728453735765289
Episode 50 training loss: 50.7986826505512.          Total Reward: -22.0
Steps done: 23001        Epsilon: 0.5670638933474685
Episode 51 training loss: 69.56285844370723.          Total Reward: -20.0
Steps done: 23562        Epsilon: 0.5593056044156778
Episode 52 training loss: 79.35103224217892.          Total Reward: -12.0
Steps done: 24183        Epsilon: 0.5508434920194116
Episode 53 training loss: 58.620751367881894.          Total Reward: -19.0
Steps done: 24692        Epsilon: 0.544004861648078
Episode 54 training loss: 60.919632910285145.          Total Reward: -19.0
Steps done: 25241        Epsilon: 0.5367257123515053
Episode 55 training loss: 58.13642448512837.          Total Reward: -20.0
Steps done: 25742        Epsilon: 0.5301696160647165
Episode 56 training loss: 33.16122300410643.          Total Reward: -31.0
Steps done: 26055        Epsilon: 0.5261151725173773
Episode 57 training loss: 50.40370529610664.          Total Reward: -23.0
Steps done: 26466        Epsilon: 0.5208392406371978
Episode 58 training loss: 53.91224154783413.          Total Reward: -27.0
Steps done: 26883        Epsilon: 0.5155414045053174
Episode 59 training loss: 48.11091786483303.          Total Reward: -26.0
Steps done: 27298        Epsilon: 0.5103235269777979
Episode 60 training loss: 57.43490696884692.          Total Reward: -21.0
Steps done: 27749        Epsilon: 0.5047140619953974
Episode 61 training loss: 57.12556616868824.          Total Reward: -23.0
Steps done: 28216        Epsilon: 0.4989718606463567
Episode 62 training loss: 75.07457118993625.          Total Reward: -17.0
Steps done: 28827        Epsilon: 0.49155957095999636
Episode 63 training loss: 115.10232697287574.          Total Reward: -6.0
Steps done: 29788        Epsilon: 0.48012797417912356
Episode 64 training loss: 45.484369890298694.          Total Reward: -26.0
Steps done: 30169        Epsilon: 0.47567126400205284
Episode 65 training loss: 53.13405614718795.          Total Reward: -19.0
Steps done: 30592        Epsilon: 0.47077273699712924
Episode 66 training loss: 67.89426314318553.          Total Reward: -23.0
Steps done: 31147        Epsilon: 0.4644236638240878
Episode 67 training loss: 47.16042139660567.          Total Reward: -24.0
Steps done: 31540        Epsilon: 0.459980812572997
Episode 68 training loss: 61.80575567018241.          Total Reward: -26.0
Steps done: 32009        Epsilon: 0.45473559770835087
Episode 69 training loss: 57.73618627153337.          Total Reward: -22.0
Steps done: 32486        Epsilon: 0.44946362233407916
Episode 70 training loss: 61.594097709748894.          Total Reward: -25.0
Steps done: 32969        Epsilon: 0.4441890086633053
Episode 71 training loss: 67.12657990213484.          Total Reward: -18.0
Steps done: 33516        Epsilon: 0.4382918874355133
Episode 72 training loss: 51.35770131088793.          Total Reward: -28.0
Steps done: 33903        Epsilon: 0.4341681441995587
Episode 73 training loss: 90.52418907312676.          Total Reward: -9.0
Steps done: 34628        Epsilon: 0.4265493504773061
Episode 74 training loss: 72.73306851414964.          Total Reward: -13.0
Steps done: 35237        Epsilon: 0.4202554207340606
Episode 75 training loss: 56.996798979118466.          Total Reward: -19.0
Steps done: 35690        Epsilon: 0.4156354878418423
Episode 76 training loss: 53.60568574257195.          Total Reward: -27.0
Steps done: 36109        Epsilon: 0.41140863290886476
Episode 77 training loss: 54.14332735328935.          Total Reward: -20.0
Steps done: 36546        Epsilon: 0.4070471117843982
Episode 78 training loss: 51.46489787148312.          Total Reward: -28.0
Steps done: 36969        Epsilon: 0.4028704615384981
Episode 79 training loss: 47.406610168516636.          Total Reward: -27.0
Steps done: 37352        Epsilon: 0.3991266788316273
Episode 80 training loss: 69.85948491608724.          Total Reward: -14.0
Steps done: 37899        Epsilon: 0.39384159065055435
Episode 81 training loss: 39.62712355097756.          Total Reward: -19.0
Steps done: 38266        Epsilon: 0.3903359507714925
Episode 82 training loss: 88.6076315836981.          Total Reward: -16.0
Steps done: 39003        Epsilon: 0.383392424545492
Episode 83 training loss: 41.295911700464785.          Total Reward: -18.0
Steps done: 39364        Epsilon: 0.38003771879388215
Episode 84 training loss: 77.3244748567231.          Total Reward: -10.0
Steps done: 40005        Epsilon: 0.37415512452408195
Episode 85 training loss: 63.65863767778501.          Total Reward: -17.0
Steps done: 40494        Epsilon: 0.3697304291830336
Episode 86 training loss: 56.73918620729819.          Total Reward: -17.0
Steps done: 40959        Epsilon: 0.3655727761243981
Episode 87 training loss: 66.63735133735463.          Total Reward: -23.0
Steps done: 41460        Epsilon: 0.3611470013756677
Episode 88 training loss: 72.98647104669362.          Total Reward: -3.0
Steps done: 42045        Epsilon: 0.3560488476003149
Episode 89 training loss: 72.55329686263576.          Total Reward: -7.0
Steps done: 42578        Epsilon: 0.35146833216462064
Episode 90 training loss: 55.20375915477052.          Total Reward: -15.0
Steps done: 43013        Epsilon: 0.34777498303782245
Episode 91 training loss: 67.67401346983388.          Total Reward: -18.0
Steps done: 43536        Epsilon: 0.34338732197655775
Episode 92 training loss: 55.314857930876315.          Total Reward: -20.0
Steps done: 44005        Epsilon: 0.33950118263893364
Episode 93 training loss: 49.99267828464508.          Total Reward: -15.0
Steps done: 44418        Epsilon: 0.33611658597648997
Episode 94 training loss: 50.29130571661517.          Total Reward: -24.0
Steps done: 44827        Epsilon: 0.3327990337748074
Episode 95 training loss: 58.74292193632573.          Total Reward: -23.0
Steps done: 45266        Epsilon: 0.329275684126061
Episode 96 training loss: 75.3125909017399.          Total Reward: -11.0
Steps done: 45853        Epsilon: 0.3246245248137754
Episode 97 training loss: 52.482604160904884.          Total Reward: -27.0
Steps done: 46284        Epsilon: 0.3212526441888314
Episode 98 training loss: 55.08970777131617.          Total Reward: -20.0
Steps done: 46699        Epsilon: 0.3180400919368886
Episode 99 training loss: 51.50811177305877.          Total Reward: -29.0
Steps done: 47096        Epsilon: 0.3149979157960945
Beginning to save execution
-------------------------------------------------------------
Target_net saved to target_neth.pth
Policy_net saved to policy_net.pth
Replay memory saved to replay_memory.pkl
Hyperparameters saved to hyperparameters.pkl
Figure plotted to Rewards_Plot.png
Finished saving execution to previous_run/
-------------------------------------------------------------
Episode 100 training loss: 54.71557462750934.          Total Reward: -25.0
Steps done: 47495        Epsilon: 0.31197068500052605
Episode 101 training loss: 38.88295317906886.          Total Reward: -29.0
Steps done: 47816        Epsilon: 0.30955706784542225
Episode 102 training loss: 91.92836189642549.          Total Reward: -12.0
Steps done: 48545        Epsilon: 0.3041470884642244
Episode 103 training loss: 56.678738814778626.          Total Reward: -24.0
Steps done: 48944        Epsilon: 0.30122755662971507
Episode 104 training loss: 40.4910330013372.          Total Reward: -23.0
Steps done: 49293        Epsilon: 0.29869764896950163
Episode 105 training loss: 42.61138379573822.          Total Reward: -22.0
Steps done: 49636        Epsilon: 0.2962326504152779
Episode 106 training loss: 67.18325616372749.          Total Reward: -27.0
Steps done: 50103        Epsilon: 0.29291031608597917
Episode 107 training loss: 61.64042035443708.          Total Reward: -23.0
Steps done: 50550        Epsilon: 0.28976639269353205
Episode 108 training loss: 49.16159948660061.          Total Reward: -29.0
Steps done: 50887        Epsilon: 0.28741926200649204
Episode 109 training loss: 54.475602311082184.          Total Reward: -33.0
Steps done: 51260        Epsilon: 0.2848443515667586
Episode 110 training loss: 49.41195893660188.          Total Reward: -31.0
Steps done: 51633        Epsilon: 0.2822933405625752
Episode 111 training loss: 66.3109359596856.          Total Reward: -16.0
Steps done: 52128        Epsilon: 0.2789444743201682
Episode 112 training loss: 49.302645936608315.          Total Reward: -23.0
Steps done: 52489        Epsilon: 0.27652817041158256
Episode 113 training loss: 54.24300019349903.          Total Reward: -26.0
Steps done: 52894        Epsilon: 0.27384318834555327
Episode 114 training loss: 122.55731460126117.          Total Reward: 0.0
Steps done: 53811        Epsilon: 0.2678633885981581
Episode 115 training loss: 45.270214036572725.          Total Reward: -24.0
Steps done: 54174        Epsilon: 0.2655338645494298
Episode 116 training loss: 91.55823886301368.          Total Reward: -11.0
Steps done: 54835        Epsilon: 0.26134586607804483
Episode 117 training loss: 64.22048692312092.          Total Reward: -22.0
Steps done: 55286        Epsilon: 0.25852785781296783
Episode 118 training loss: 81.55443644616753.          Total Reward: -3.0
Steps done: 55877        Epsilon: 0.2548828524992069
Episode 119 training loss: 75.05493743997067.          Total Reward: -21.0
Steps done: 56410        Epsilon: 0.25164143241187564
Episode 120 training loss: 95.02191788051277.          Total Reward: -17.0
Steps done: 57181        Epsilon: 0.24702839477330182
Episode 121 training loss: 42.16556178452447.          Total Reward: -26.0
Steps done: 57520        Epsilon: 0.24502806748735442
Episode 122 training loss: 57.235813927371055.          Total Reward: -24.0
Steps done: 57943        Epsilon: 0.24255574113934786
Episode 123 training loss: 55.82151415664703.          Total Reward: -23.0
Steps done: 58362        Epsilon: 0.2401324339803589
Episode 124 training loss: 53.95497632259503.          Total Reward: -29.0
Steps done: 58805        Epsilon: 0.2375977788343206
Episode 125 training loss: 64.03380562365055.          Total Reward: -17.0
Steps done: 59282        Epsilon: 0.23489979402843525
Episode 126 training loss: 82.37524776253849.          Total Reward: -8.0
Steps done: 59923        Epsilon: 0.2313244983965652
Episode 127 training loss: 61.851817198097706.          Total Reward: -11.0
Steps done: 60414        Epsilon: 0.2286243462662876
Episode 128 training loss: 64.20781293138862.          Total Reward: 8.0
Steps done: 60961        Epsilon: 0.22565500745863754
Episode 129 training loss: 47.65998818259686.          Total Reward: -29.0
Steps done: 61360        Epsilon: 0.2235145420784289
Episode 130 training loss: 54.00204309541732.          Total Reward: -20.0
Steps done: 61805        Epsilon: 0.22115235681638748
Episode 131 training loss: 53.91745981993154.          Total Reward: -28.0
Steps done: 62260        Epsilon: 0.21876410767595253
Episode 132 training loss: 51.80113738402724.          Total Reward: -22.0
Steps done: 62687        Epsilon: 0.21654740353531454
Episode 133 training loss: 57.845209932886064.          Total Reward: -21.0
Steps done: 63176        Epsilon: 0.21403773314327293
Episode 134 training loss: 58.92709307745099.          Total Reward: -15.0
Steps done: 63643        Epsilon: 0.2116694443952538
Episode 135 training loss: 51.970129635185.          Total Reward: -28.0
Steps done: 64036        Epsilon: 0.20969774394330484
Episode 136 training loss: 50.8391115530394.          Total Reward: -25.0
Steps done: 64459        Epsilon: 0.20759706720598253
Episode 137 training loss: 74.22085616923869.          Total Reward: -3.0
Steps done: 65042        Epsilon: 0.20473797619026082
Episode 138 training loss: 65.36228713206947.          Total Reward: -15.0
Steps done: 65547        Epsilon: 0.20229486383826162
Episode 139 training loss: 48.48502417653799.          Total Reward: -26.0
Steps done: 65922        Epsilon: 0.2005005236017577
Episode 140 training loss: 105.48416145518422.          Total Reward: -5.0
Steps done: 66737        Epsilon: 0.19665835049119496
Episode 141 training loss: 58.04431286081672.          Total Reward: -24.0
Steps done: 67230        Epsilon: 0.19437190548233965
Episode 142 training loss: 73.271269781515.          Total Reward: -6.0
Steps done: 67757        Epsilon: 0.1919587372796478
Episode 143 training loss: 70.20575528033078.          Total Reward: 1.0
Steps done: 68344        Epsilon: 0.1893079902374277
Episode 144 training loss: 83.0618777894415.          Total Reward: -16.0
Steps done: 69021        Epsilon: 0.18629874011618594
Episode 145 training loss: 67.6914331605658.          Total Reward: -21.0
Steps done: 69560        Epsilon: 0.18393904871900413
Episode 146 training loss: 96.27212525811046.          Total Reward: -12.0
Steps done: 70359        Epsilon: 0.1804990872145068
Episode 147 training loss: 57.82801645155996.          Total Reward: -22.0
Steps done: 70798        Epsilon: 0.1786380906308928
Episode 148 training loss: 63.460635277442634.          Total Reward: -14.0
Steps done: 71315        Epsilon: 0.17647246878883474
Episode 149 training loss: 63.97366131469607.          Total Reward: -20.0
Steps done: 71840        Epsilon: 0.17430179385122607
Episode 150 training loss: 77.31013336731121.          Total Reward: 5.0
Steps done: 72521        Epsilon: 0.1715282327427232
Episode 151 training loss: 81.57288178149611.          Total Reward: -14.0
Steps done: 73226        Epsilon: 0.16870623950778257
Episode 152 training loss: 43.96704506780952.          Total Reward: -25.0
Steps done: 73633        Epsilon: 0.16709959120544704
Episode 153 training loss: 47.06545405462384.          Total Reward: -24.0
Steps done: 74062        Epsilon: 0.16542370111454238
Episode 154 training loss: 70.42831664346159.          Total Reward: -9.0
Steps done: 74677        Epsilon: 0.16305233827554239
Episode 155 training loss: 51.325186434201896.          Total Reward: -8.0
Steps done: 75152        Epsilon: 0.16124559055470114
Episode 156 training loss: 59.492467023432255.          Total Reward: -6.0
Steps done: 75711        Epsilon: 0.1591466340458203
Episode 157 training loss: 59.824528101831675.          Total Reward: -14.0
Steps done: 76221        Epsilon: 0.15725708592838755
Episode 158 training loss: 43.997251510154456.          Total Reward: -22.0
Steps done: 76628        Epsilon: 0.15576634209974227
Episode 159 training loss: 81.14646323490888.          Total Reward: -2.0
Steps done: 77325        Epsilon: 0.15324836517354365
Episode 160 training loss: 55.689536596648395.          Total Reward: -21.0
Steps done: 77796        Epsilon: 0.15157150754763277
Episode 161 training loss: 35.04764279490337.          Total Reward: -34.0
Steps done: 78089        Epsilon: 0.15053828505208208
Episode 162 training loss: 42.22283773124218.          Total Reward: -24.0
Steps done: 78452        Epsilon: 0.1492686697081759
Episode 163 training loss: 73.57551425509155.          Total Reward: 0.0
Steps done: 79015        Epsilon: 0.14732219364123644
Episode 164 training loss: 74.51391331851482.          Total Reward: -4.0
Steps done: 79636        Epsilon: 0.1452067303585888
Episode 165 training loss: 62.70441327104345.          Total Reward: -2.0
Steps done: 80161        Epsilon: 0.14344373697523433
Episode 166 training loss: 54.95314696803689.          Total Reward: -12.0
Steps done: 80588        Epsilon: 0.14202680143210755
Episode 167 training loss: 59.62052795384079.          Total Reward: -21.0
Steps done: 81091        Epsilon: 0.1403769595259044
Episode 168 training loss: 69.95250072190538.          Total Reward: -14.0
Steps done: 81652        Epsilon: 0.13856118554713845
Episode 169 training loss: 58.055282645858824.          Total Reward: -19.0
Steps done: 82108        Epsilon: 0.13710391028316266
Episode 170 training loss: 60.84430024120957.          Total Reward: -17.0
Steps done: 82575        Epsilon: 0.1356286010062189
Episode 171 training loss: 73.77225550450385.          Total Reward: -12.0
Steps done: 83124        Epsilon: 0.13391612719123988
Episode 172 training loss: 60.932763141579926.          Total Reward: -8.0
Steps done: 83595        Epsilon: 0.1324655716990202
Episode 173 training loss: 88.27307830471545.          Total Reward: -9.0
Steps done: 84246        Epsilon: 0.1304885759604141
Episode 174 training loss: 86.10665794089437.          Total Reward: -3.0
Steps done: 84929        Epsilon: 0.12844869854059887
Episode 175 training loss: 80.63693592743948.          Total Reward: -10.0
Steps done: 85564        Epsilon: 0.12658317224455842
Episode 176 training loss: 55.23615018744022.          Total Reward: -23.0
Steps done: 86001        Epsilon: 0.1253164332488941
Episode 177 training loss: 51.761055142618716.          Total Reward: -19.0
Steps done: 86408        Epsilon: 0.12414903773700152
Episode 178 training loss: 62.19549287017435.          Total Reward: -6.0
Steps done: 86937        Epsilon: 0.12264935522145083
Episode 179 training loss: 55.46019616164267.          Total Reward: -23.0
Steps done: 87348        Epsilon: 0.12149780929499483
Episode 180 training loss: 71.03505549579859.          Total Reward: -7.0
Steps done: 87915        Epsilon: 0.11992847676967064
Episode 181 training loss: 56.863153078593314.          Total Reward: -4.0
Steps done: 88396        Epsilon: 0.11861450293759561
Episode 182 training loss: 84.82179578673095.          Total Reward: -14.0
Steps done: 89035        Epsilon: 0.11689317199100883
Episode 183 training loss: 70.21063951216638.          Total Reward: -17.0
Steps done: 89575        Epsilon: 0.115459811124084
Episode 184 training loss: 70.89184026047587.          Total Reward: -3.0
Steps done: 90122        Epsilon: 0.11402746420039427
Episode 185 training loss: 72.62080683233216.          Total Reward: -11.0
Steps done: 90699        Epsilon: 0.11253763922548814
Episode 186 training loss: 74.72597543429583.          Total Reward: -17.0
Steps done: 91274        Epsilon: 0.11107420430048408
Episode 187 training loss: 53.361514212563634.          Total Reward: -18.0
Steps done: 91719        Epsilon: 0.10995598540332124
Episode 188 training loss: 56.43121455796063.          Total Reward: -19.0
Steps done: 92148        Epsilon: 0.10888968571292315
Episode 189 training loss: 73.08392616640776.          Total Reward: -11.0
Steps done: 92747        Epsilon: 0.1074198455650907
Episode 190 training loss: 80.67037276923656.          Total Reward: 18.0
Steps done: 93396        Epsilon: 0.10585196241819356
Episode 191 training loss: 65.61964212637395.          Total Reward: 1.0
Steps done: 93935        Epsilon: 0.10456902045858489
Episode 192 training loss: 63.16999549139291.          Total Reward: -18.0
Steps done: 94444        Epsilon: 0.10337325387354084
Episode 193 training loss: 65.99916076567024.          Total Reward: -19.0
Steps done: 94979        Epsilon: 0.10213270129191891
Episode 194 training loss: 97.59618217870593.          Total Reward: -5.0
Steps done: 95750        Epsilon: 0.10037384886929847
Episode 195 training loss: 109.72080904152244.          Total Reward: -4.0
Steps done: 96605        Epsilon: 0.09846260701551579
Episode 196 training loss: 75.37081546895206.          Total Reward: -13.0
Steps done: 97202        Epsilon: 0.09715210654227976
Episode 197 training loss: 729.2756796516478.          Total Reward: 72.0
Steps done: 116943        Epsilon: 0.06320380642491825
Episode 198 training loss: 5.05738332105102.          Total Reward: -17.0
Steps done: 117412        Epsilon: 0.06258363465643767
Episode 199 training loss: 10.312649654399138.          Total Reward: 8.0
Steps done: 118009        Epsilon: 0.06180465153095
Beginning to save execution
-------------------------------------------------------------
Target_net saved to target_neth.pth
Policy_net saved to policy_net.pth
Replay memory saved to replay_memory.pkl
Hyperparameters saved to hyperparameters.pkl
Figure plotted to Rewards_Plot.png
Finished saving execution to previous_run/
-------------------------------------------------------------
Episode 200 training loss: 9.100259689847007.          Total Reward: -18.0
Steps done: 118456        Epsilon: 0.0612289572330573
Episode 201 training loss: 12.443902031867765.          Total Reward: -14.0
Steps done: 118921        Epsilon: 0.0606368687872329
Episode 202 training loss: 18.818595091055613.          Total Reward: -16.0
Steps done: 119443        Epsilon: 0.059980350746967746
Episode 203 training loss: 16.496791976271197.          Total Reward: -19.0
Steps done: 119864        Epsilon: 0.05945706617102589
Episode 204 training loss: 22.806697873747908.          Total Reward: -21.0
Steps done: 120335        Epsilon: 0.058878124425592405
Episode 205 training loss: 41.17438458336983.          Total Reward: -14.0
Steps done: 121070        Epsilon: 0.05798819019966102
Episode 206 training loss: 25.382991172140464.          Total Reward: -10.0
Steps done: 121551        Epsilon: 0.05741458790820828
Episode 207 training loss: 25.59904280421324.          Total Reward: -22.0
Steps done: 121956        Epsilon: 0.056936937391922814
Episode 208 training loss: 38.98585218633525.          Total Reward: -18.0
Steps done: 122469        Epsilon: 0.0563388148290809
Episode 209 training loss: 51.751778301782906.          Total Reward: -11.0
Steps done: 123148        Epsilon: 0.055558852109743116
Episode 210 training loss: 52.109941059490666.          Total Reward: -12.0
Steps done: 123734        Epsilon: 0.05489628011638249
Episode 211 training loss: 46.127538186032325.          Total Reward: -7.0
Steps done: 124225        Epsilon: 0.05434854686825116
Episode 212 training loss: 40.95726048247889.          Total Reward: -13.0
Steps done: 124706        Epsilon: 0.05381844919212735
Episode 213 training loss: 57.33449892094359.          Total Reward: 3.0
Steps done: 125263        Epsilon: 0.053212505958178474
Episode 214 training loss: 67.17247638618574.          Total Reward: 2.0
Steps done: 125882        Epsilon: 0.052548940012251896
Episode 215 training loss: 59.52086508832872.          Total Reward: -16.0
Steps done: 126395        Epsilon: 0.05200673418331525
Episode 216 training loss: 61.11855146475136.          Total Reward: -6.0
Steps done: 126928        Epsilon: 0.0514507072071699
Episode 217 training loss: 64.44184606801718.          Total Reward: -1.0
Steps done: 127441        Epsilon: 0.050922496279828304
Episode 218 training loss: 100.42256665648893.          Total Reward: -6.0
Steps done: 128238        Epsilon: 0.05011518508794879
Episode 219 training loss: 86.97025166964158.          Total Reward: -9.0
Steps done: 128919        Epsilon: 0.04943800491473001
Episode 220 training loss: 85.58733823243529.          Total Reward: 10.0
Steps done: 129700        Epsilon: 0.048675446570021326
Episode 221 training loss: 67.22952873306349.          Total Reward: -1.0
Steps done: 130295        Epsilon: 0.0481044069387974
Episode 222 training loss: 49.95488940831274.          Total Reward: -9.0
Steps done: 130732        Epsilon: 0.04769038202210717
Episode 223 training loss: 47.52439738903195.          Total Reward: -20.0
Steps done: 131125        Epsilon: 0.04732188721373417
Episode 224 training loss: 73.29424812551588.          Total Reward: -2.0
Steps done: 131720        Epsilon: 0.04677083276960445
Episode 225 training loss: 65.61439117975533.          Total Reward: -9.0
Steps done: 132295        Epsilon: 0.04624603308333327
Episode 226 training loss: 48.534374627284706.          Total Reward: -17.0
Steps done: 132706        Epsilon: 0.0458755119057797
Episode 227 training loss: 64.672438332811.          Total Reward: 4.0
Steps done: 133269        Epsilon: 0.04537410103239285
Episode 228 training loss: 53.258562750183046.          Total Reward: -14.0
Steps done: 133692        Epsilon: 0.04500199091399547
Episode 229 training loss: 59.607426513917744.          Total Reward: -7.0
Steps done: 134151        Epsilon: 0.04460263873346254
Episode 230 training loss: 54.536871472373605.          Total Reward: -10.0
Steps done: 134604        Epsilon: 0.04421297448830467
Episode 231 training loss: 47.64754568785429.          Total Reward: -24.0
Steps done: 134945        Epsilon: 0.04392254858013036
Episode 232 training loss: 92.03740453347564.          Total Reward: 6.0
Steps done: 135620        Epsilon: 0.04335490850626501
Episode 233 training loss: 61.173180248588324.          Total Reward: -6.0
Steps done: 136069        Epsilon: 0.042982593187331726
Episode 234 training loss: 65.43726824596524.          Total Reward: -5.0
Steps done: 136552        Epsilon: 0.04258672324933894
Episode 235 training loss: 73.8934350926429.          Total Reward: -5.0
Steps done: 137121        Epsilon: 0.04212645850532098
Episode 236 training loss: 53.56769967637956.          Total Reward: -19.0
Steps done: 137536        Epsilon: 0.041794869590190006
Episode 237 training loss: 45.828752781264484.          Total Reward: -30.0
Steps done: 137881        Epsilon: 0.041521818067370805
Episode 238 training loss: 65.82004583440721.          Total Reward: -22.0
Steps done: 138366        Epsilon: 0.04114192378656947
Episode 239 training loss: 96.23790500871837.          Total Reward: -1.0
Steps done: 139057        Epsilon: 0.040608567184679124
Episode 240 training loss: 58.921682404354215.          Total Reward: -16.0
Steps done: 139458        Epsilon: 0.04030324926179041
Episode 241 training loss: 58.95216100476682.          Total Reward: -24.0
Steps done: 139847        Epsilon: 0.04000997850313526
Episode 242 training loss: 70.24716433044523.          Total Reward: -5.0
Steps done: 140348        Epsilon: 0.03963644764254245
Episode 243 training loss: 83.27366756554693.          Total Reward: 0.0
Steps done: 140933        Epsilon: 0.039206168680042564
Episode 244 training loss: 65.93550319317728.          Total Reward: -21.0
Steps done: 141388        Epsilon: 0.038875830869481605
Episode 245 training loss: 56.63190920744091.          Total Reward: -23.0
Steps done: 141765        Epsilon: 0.03860495467278585
Episode 246 training loss: 60.831034566275775.          Total Reward: -21.0
Steps done: 142174        Epsilon: 0.03831395926060964
Episode 247 training loss: 57.615896047092974.          Total Reward: -20.0
Steps done: 142549        Epsilon: 0.038049756279094876
Episode 248 training loss: 68.9514622092247.          Total Reward: -13.0
Steps done: 142996        Epsilon: 0.037738045182312226
Episode 249 training loss: 56.31588421668857.          Total Reward: -23.0
Steps done: 143377        Epsilon: 0.037475094592163
Episode 250 training loss: 79.71727521531284.          Total Reward: -13.0
Steps done: 143860        Epsilon: 0.03714532779878901
Episode 251 training loss: 81.54696147330105.          Total Reward: -10.0
Steps done: 144367        Epsilon: 0.03680343211014269
Episode 252 training loss: 76.108593467623.          Total Reward: 2.0
Steps done: 144860        Epsilon: 0.03647510726741716
Episode 253 training loss: 61.567725617438555.          Total Reward: -26.0
Steps done: 145237        Epsilon: 0.03622675159598644
Episode 254 training loss: 59.044935391284525.          Total Reward: -26.0
Steps done: 145618        Epsilon: 0.03597812773786902
Episode 255 training loss: 98.06792268157005.          Total Reward: -13.0
Steps done: 146237        Epsilon: 0.03557921079187047
Episode 256 training loss: 71.24529798235744.          Total Reward: -16.0
Steps done: 146683        Epsilon: 0.035295586734061635
Episode 257 training loss: 65.2017325903289.          Total Reward: -14.0
Steps done: 147090        Epsilon: 0.03503950914310549
Episode 258 training loss: 99.06309032719582.          Total Reward: 12.0
Steps done: 147739        Epsilon: 0.0346365211875783
Episode 259 training loss: 77.05396897159517.          Total Reward: -3.0
Steps done: 148232        Epsilon: 0.0343347396130778
Episode 260 training loss: 66.61013629194349.          Total Reward: -21.0
Steps done: 148665        Epsilon: 0.034072736705968006
Episode 261 training loss: 87.17441604379565.          Total Reward: -13.0
Steps done: 149232        Epsilon: 0.0337339127512633
Episode 262 training loss: 65.9041693015024.          Total Reward: -20.0
Steps done: 149627        Epsilon: 0.033500693776736055
Episode 263 training loss: 121.98962446860969.          Total Reward: 4.0
Steps done: 150442        Epsilon: 0.03302671222539238
Episode 264 training loss: 72.24624501820654.          Total Reward: 0.0
Steps done: 150929        Epsilon: 0.032748061730969266
Episode 265 training loss: 66.10066598281264.          Total Reward: -18.0
Steps done: 151350        Epsilon: 0.03250989393785685
Episode 266 training loss: 55.029495015740395.          Total Reward: -22.0
Steps done: 151723        Epsilon: 0.03230096482284636
Episode 267 training loss: 46.1902368273586.          Total Reward: -31.0
Steps done: 152030        Epsilon: 0.0321304600668056
Episode 268 training loss: 66.36637574899942.          Total Reward: -14.0
Steps done: 152453        Epsilon: 0.031897663532750725
Episode 269 training loss: 68.27818613313138.          Total Reward: -17.0
Steps done: 152920        Epsilon: 0.0316434949074009
Episode 270 training loss: 55.484874876216054.          Total Reward: -22.0
Steps done: 153293        Epsilon: 0.03144260741103059
Episode 271 training loss: 51.910062374547124.          Total Reward: -25.0
Steps done: 153634        Epsilon: 0.03126058615084748
Episode 272 training loss: 79.44853918347508.          Total Reward: -7.0
Steps done: 154129        Epsilon: 0.030999107632469998
Episode 273 training loss: 62.31640514638275.          Total Reward: -12.0
Steps done: 154548        Epsilon: 0.03078029003799207
Episode 274 training loss: 50.487929882481694.          Total Reward: -26.0
Steps done: 154871        Epsilon: 0.030613164871917398
Episode 275 training loss: 131.32934887893498.          Total Reward: 6.0
Steps done: 155661        Epsilon: 0.03021004874078065
Episode 276 training loss: 61.87187891174108.          Total Reward: -16.0
Steps done: 156064        Epsilon: 0.03000745478049155
Episode 277 training loss: 87.16438412014395.          Total Reward: -5.0
Steps done: 156601        Epsilon: 0.029740649636783377
Episode 278 training loss: 73.20872010663152.          Total Reward: -9.0
Steps done: 157104        Epsilon: 0.029493965246393236
Episode 279 training loss: 99.39122616872191.          Total Reward: 13.0
Steps done: 157722        Epsilon: 0.029195098176454486
Episode 280 training loss: 89.8650408629328.          Total Reward: -1.0
Steps done: 158325        Epsilon: 0.02890790224962976
Episode 281 training loss: 70.26398538332433.          Total Reward: -14.0
Steps done: 158756        Epsilon: 0.02870526328087296
Episode 282 training loss: 68.41133543569595.          Total Reward: -9.0
Steps done: 159211        Epsilon: 0.028493696478466862
Episode 283 training loss: 87.89931509271264.          Total Reward: -6.0
Steps done: 159764        Epsilon: 0.028239780364042275
Episode 284 training loss: 100.32560222875327.          Total Reward: 9.0
Steps done: 160411        Epsilon: 0.027947125146329937
Episode 285 training loss: 87.28085817862302.          Total Reward: -1.0
Steps done: 160998        Epsilon: 0.027685674173382857
Episode 286 training loss: 95.92021174356341.          Total Reward: -5.0
Steps done: 161631        Epsilon: 0.027408001261298484
Episode 287 training loss: 101.04437288176268.          Total Reward: -6.0
Steps done: 162322        Epsilon: 0.027109860643459285
Episode 288 training loss: 78.50244748685509.          Total Reward: -14.0
Steps done: 162897        Epsilon: 0.026865665752522423
Episode 289 training loss: 63.81114980671555.          Total Reward: -12.0
Steps done: 163354        Epsilon: 0.02667407208419574
Episode 290 training loss: 99.52882790751755.          Total Reward: 4.0
Steps done: 164093        Epsilon: 0.02636884680269618
Episode 291 training loss: 128.2934703240171.          Total Reward: -4.0
Steps done: 165110        Epsilon: 0.025957914979873042
Episode 292 training loss: 53.83004729729146.          Total Reward: -14.0
Steps done: 165527        Epsilon: 0.02579241786875762
Episode 293 training loss: 81.89871851727366.          Total Reward: -7.0
Steps done: 166158        Epsilon: 0.025545247161525425
Episode 294 training loss: 61.498051192611456.          Total Reward: -13.0
Steps done: 166617        Epsilon: 0.025367885011865647
Episode 295 training loss: 54.97703860513866.          Total Reward: -12.0
Steps done: 167056        Epsilon: 0.025200144632889464
Episode 296 training loss: 62.92492270749062.          Total Reward: -10.0
Steps done: 167527        Epsilon: 0.025022212560773107
Episode 297 training loss: 53.97493146546185.          Total Reward: -13.0
Steps done: 167950        Epsilon: 0.02486418968156378
Episode 298 training loss: 50.91443760693073.          Total Reward: -20.0
Steps done: 168359        Epsilon: 0.024712977730608765
Episode 299 training loss: 69.89218890946358.          Total Reward: -14.0
Steps done: 168894        Epsilon: 0.02451750181272148
Beginning to save execution
-------------------------------------------------------------
Target_net saved to target_neth.pth
Policy_net saved to policy_net.pth
Replay memory saved to replay_memory.pkl
Hyperparameters saved to hyperparameters.pkl
Figure plotted to Rewards_Plot.png
Finished saving execution to previous_run/
-------------------------------------------------------------
Episode 300 training loss: 53.69386041071266.          Total Reward: -18.0
Steps done: 169279        Epsilon: 0.024378441160715622
Episode 301 training loss: 77.79925741162151.          Total Reward: -10.0
Steps done: 169860        Epsilon: 0.02417110373615121
Episode 302 training loss: 56.67000246234238.          Total Reward: -17.0
Steps done: 170283        Epsilon: 0.0240220339100586
Episode 303 training loss: 113.04668141994625.          Total Reward: -4.0
Steps done: 171056        Epsilon: 0.023753659623396855
Episode 304 training loss: 53.04501935001463.          Total Reward: -19.0
Steps done: 171445        Epsilon: 0.02362055356083595
Episode 305 training loss: 83.62725317664444.          Total Reward: -3.0
Steps done: 172064        Epsilon: 0.023411398009515073
Episode 306 training loss: 108.4003169387579.          Total Reward: -1.0
Steps done: 172865        Epsilon: 0.023145505894360166
Episode 307 training loss: 92.33220561221242.          Total Reward: -2.0
Steps done: 173576        Epsilon: 0.02291390894273021
Episode 308 training loss: 55.652513411827385.          Total Reward: -19.0
Steps done: 173995        Epsilon: 0.022779341772562196
Episode 309 training loss: 59.862136317417026.          Total Reward: -11.0
Steps done: 174440        Epsilon: 0.02263795949246135
Episode 310 training loss: 105.02743817865849.          Total Reward: 8.0
Steps done: 175175        Epsilon: 0.02240785752291059
Episode 311 training loss: 92.1588285760954.          Total Reward: 10.0
Steps done: 175834        Epsilon: 0.02220511276597864
Episode 312 training loss: 87.0787181602791.          Total Reward: 4.0
Steps done: 176517        Epsilon: 0.021998479616411014
Episode 313 training loss: 79.11831066943705.          Total Reward: 9.0
Steps done: 177096        Epsilon: 0.02182605257531982
Episode 314 training loss: 66.32865846622735.          Total Reward: -3.0
Steps done: 177558        Epsilon: 0.02169024745238504
Episode 315 training loss: 93.48261325340718.          Total Reward: 2.0
Steps done: 178281        Epsilon: 0.021480844410737002
Episode 316 training loss: 59.5726686231792.          Total Reward: -16.0
Steps done: 178759        Epsilon: 0.021344464811078434
Episode 317 training loss: 92.54983190819621.          Total Reward: 12.0
Steps done: 179464        Epsilon: 0.021146270338153843
Episode 318 training loss: 60.87743904348463.          Total Reward: -7.0
Steps done: 179955        Epsilon: 0.021010286179977695
Episode 319 training loss: 56.155035133473575.          Total Reward: -13.0
Steps done: 180410        Epsilon: 0.020885753795391808
Episode 320 training loss: 73.21643967647105.          Total Reward: -2.0
Steps done: 180957        Epsilon: 0.020737904336961356
Episode 321 training loss: 56.986534723080695.          Total Reward: -15.0
Steps done: 181400        Epsilon: 0.020619638154248193
Episode 322 training loss: 81.24405298568308.          Total Reward: -4.0
Steps done: 181977        Epsilon: 0.020467549450863216
Episode 323 training loss: 99.05447910912335.          Total Reward: 10.0
Steps done: 182740        Epsilon: 0.020269773232566103
Episode 324 training loss: 42.3923213025555.          Total Reward: -22.0
Steps done: 183081        Epsilon: 0.0201825955386526
Episode 325 training loss: 105.70760081615299.          Total Reward: 3.0
Steps done: 183860        Epsilon: 0.01998620802103412
Episode 326 training loss: 54.312139187939465.          Total Reward: -18.0
Steps done: 184243        Epsilon: 0.01989104639256769
Episode 327 training loss: 66.09310618881136.          Total Reward: -5.0
Steps done: 184724        Epsilon: 0.019772818827576453
Episode 328 training loss: 89.99245866015553.          Total Reward: 16.0
Steps done: 185387        Epsilon: 0.01961216941543841
Episode 329 training loss: 55.32897460181266.          Total Reward: -17.0
Steps done: 185774        Epsilon: 0.019519620105557463
Episode 330 training loss: 68.61378483194858.          Total Reward: -4.0
Steps done: 186273        Epsilon: 0.019401600522458855
Episode 331 training loss: 56.61710776761174.          Total Reward: -15.0
Steps done: 186694        Epsilon: 0.019303167588935116
Episode 332 training loss: 95.9384297169745.          Total Reward: 1.0
Steps done: 187351        Epsilon: 0.019151611125973383
Episode 333 training loss: 67.31928827986121.          Total Reward: -4.0
Steps done: 187836        Epsilon: 0.01904131784531792
Episode 334 training loss: 108.02353244833648.          Total Reward: 20.0
Steps done: 188595        Epsilon: 0.018871376258937728
Episode 335 training loss: 62.97400211635977.          Total Reward: -14.0
Steps done: 189058        Epsilon: 0.018769282088635333
Episode 336 training loss: 95.97612660564482.          Total Reward: 0.0
Steps done: 189745        Epsilon: 0.01861995567997909
Episode 337 training loss: 77.63692546915263.          Total Reward: 7.0
Steps done: 190354        Epsilon: 0.01848971085934136
Episode 338 training loss: 68.12140028271824.          Total Reward: -7.0
Steps done: 190835        Epsilon: 0.01838823344203455
Episode 339 training loss: 77.34537345357239.          Total Reward: 7.0
Steps done: 191399        Epsilon: 0.0182707892776108
Episode 340 training loss: 95.80309988744557.          Total Reward: -1.0
Steps done: 192088        Epsilon: 0.018129544891833986
Episode 341 training loss: 90.69092633202672.          Total Reward: 1.0
Steps done: 192755        Epsilon: 0.017995108707496564
Episode 342 training loss: 67.58041422907263.          Total Reward: -12.0
Steps done: 193280        Epsilon: 0.017890858543964525
Episode 343 training loss: 85.56080817244947.          Total Reward: 9.0
Steps done: 193914        Epsilon: 0.0177667744005954
Episode 344 training loss: 70.44492980930954.          Total Reward: -5.0
Steps done: 194429        Epsilon: 0.01766741815848002
Episode 345 training loss: 95.99485098198056.          Total Reward: 4.0
Steps done: 195160        Epsilon: 0.01752856869296486
Episode 346 training loss: 87.9412000020966.          Total Reward: -3.0
Steps done: 195839        Epsilon: 0.017401849808760656
Episode 347 training loss: 89.45082340855151.          Total Reward: 8.0
Steps done: 196608        Epsilon: 0.017260908386584308
Episode 348 training loss: 97.21171711105853.          Total Reward: 14.0
Steps done: 197381        Epsilon: 0.01712193845388659
Episode 349 training loss: 107.28360930643976.          Total Reward: 9.0
Steps done: 198222        Epsilon: 0.016973762852291623
Episode 350 training loss: 82.09802908916026.          Total Reward: 1.0
Steps done: 198905        Epsilon: 0.016855696709836675
Episode 351 training loss: 52.92173116840422.          Total Reward: -4.0
Steps done: 199376        Epsilon: 0.0167754442944259
Episode 352 training loss: 82.68184471130371.          Total Reward: -4.0
Steps done: 200103        Epsilon: 0.01665341291375326
Episode 353 training loss: 81.8734266012907.          Total Reward: 7.0
Steps done: 200815        Epsilon: 0.016536029971360344
Episode 354 training loss: 97.64156886935234.          Total Reward: 6.0
Steps done: 201648        Epsilon: 0.016401324634746944
Episode 355 training loss: 54.82232243847102.          Total Reward: -3.0
Steps done: 202125        Epsilon: 0.016325442186813838
Episode 356 training loss: 105.64886740688235.          Total Reward: 13.0
Steps done: 203046        Epsilon: 0.016181462803948134
Episode 357 training loss: 57.649016281589866.          Total Reward: -1.0
Steps done: 203559        Epsilon: 0.016102691742608168
Episode 358 training loss: 74.38073090091348.          Total Reward: 2.0
Steps done: 204234        Epsilon: 0.01600057287075015
Episode 359 training loss: 81.17287179920822.          Total Reward: 22.0
Steps done: 204929        Epsilon: 0.015897213452325303
Episode 360 training loss: 59.60012713633478.          Total Reward: 3.0
Steps done: 205455        Epsilon: 0.015820172748226072
Episode 361 training loss: 58.15319406799972.          Total Reward: -20.0
Steps done: 205990        Epsilon: 0.015742846211677652
Episode 362 training loss: 64.31817323807627.          Total Reward: -3.0
Steps done: 206509        Epsilon: 0.01566881410398948
Episode 363 training loss: 79.41529304813594.          Total Reward: 10.0
Steps done: 207188        Epsilon: 0.01557339811891786
Episode 364 training loss: 89.4868452148512.          Total Reward: -5.0
Steps done: 207931        Epsilon: 0.015470827819654287
Episode 365 training loss: 76.82574740890414.          Total Reward: 1.0
Steps done: 208546        Epsilon: 0.015387357166870544
Episode 366 training loss: 91.07681080698967.          Total Reward: 10.0
Steps done: 209331        Epsilon: 0.015282660974070751
Episode 367 training loss: 71.54909517709166.          Total Reward: 6.0
Steps done: 209936        Epsilon: 0.01520336193753709
Episode 368 training loss: 55.19722472503781.          Total Reward: -7.0
Steps done: 210379        Epsilon: 0.015146052640087936
Episode 369 training loss: 57.151191713288426.          Total Reward: -11.0
Steps done: 210842        Epsilon: 0.015086830490188375
Episode 370 training loss: 72.96768285799772.          Total Reward: -7.0
Steps done: 211419        Epsilon: 0.01501397966021142
Episode 371 training loss: 115.91759510803968.          Total Reward: 27.0
Steps done: 212350        Epsilon: 0.014898626908680709
Episode 372 training loss: 69.1764970952645.          Total Reward: -6.0
Steps done: 212881        Epsilon: 0.014834027364613516
Episode 373 training loss: 52.30585799738765.          Total Reward: -15.0
Steps done: 213306        Epsilon: 0.014782937718238468
Episode 374 training loss: 149.1181081207469.          Total Reward: 37.0
Steps done: 214438        Epsilon: 0.01464947794371944
Episode 375 training loss: 62.85890356358141.          Total Reward: -15.0
Steps done: 214903        Epsilon: 0.01459574071543529
Episode 376 training loss: 69.97652395255864.          Total Reward: -5.0
Steps done: 215442        Epsilon: 0.014534228478746908
Episode 377 training loss: 63.16853568702936.          Total Reward: -15.0
Steps done: 215955        Epsilon: 0.014476448305840151
Episode 378 training loss: 59.39845948945731.          Total Reward: -10.0
Steps done: 216424        Epsilon: 0.01442426845163625
Episode 379 training loss: 53.05351247731596.          Total Reward: -15.0
Steps done: 216829        Epsilon: 0.01437969874844278
Episode 380 training loss: 52.85575793311.          Total Reward: -13.0
Steps done: 217252        Epsilon: 0.014333627465434467
Episode 381 training loss: 55.84780681366101.          Total Reward: -11.0
Steps done: 217703        Epsilon: 0.01428504024096201
Episode 382 training loss: 91.48788745794445.          Total Reward: 20.0
Steps done: 218374        Epsilon: 0.014213758240259552
Episode 383 training loss: 61.65792014170438.          Total Reward: -10.0
Steps done: 218823        Epsilon: 0.014166723281586666
Episode 384 training loss: 70.62168794032186.          Total Reward: 2.0
Steps done: 219360        Epsilon: 0.014111158832428451
Episode 385 training loss: 52.6905934875831.          Total Reward: -7.0
Steps done: 219787        Epsilon: 0.014067505625427896
Episode 386 training loss: 62.61742750182748.          Total Reward: -7.0
Steps done: 220242        Epsilon: 0.01402149990254558
Episode 387 training loss: 68.33352547511458.          Total Reward: -17.0
Steps done: 220737        Epsilon: 0.01397204050247486
Episode 388 training loss: 72.6272606998682.          Total Reward: 0.0
Steps done: 221258        Epsilon: 0.01392064014642207
Episode 389 training loss: 59.52799629047513.          Total Reward: -10.0
Steps done: 221695        Epsilon: 0.013878040278312277
Episode 390 training loss: 75.48999888263643.          Total Reward: -5.0
Steps done: 222250        Epsilon: 0.013824604040622803
Episode 391 training loss: 72.28792939893901.          Total Reward: 2.0
Steps done: 222779        Epsilon: 0.013774356645442467
Episode 392 training loss: 66.68777508754283.          Total Reward: -9.0
Steps done: 223284        Epsilon: 0.013727004929450915
Episode 393 training loss: 68.94407959841192.          Total Reward: -14.0
Steps done: 223785        Epsilon: 0.013680615314123932
Episode 394 training loss: 110.69384887535125.          Total Reward: -5.0
Steps done: 224546        Epsilon: 0.013611253504107097
Episode 395 training loss: 74.48526650760323.          Total Reward: -3.0
Steps done: 225067        Epsilon: 0.013564521927278432
Episode 396 training loss: 64.95804111752659.          Total Reward: 6.0
Steps done: 225582        Epsilon: 0.013518922881218191
Episode 397 training loss: 71.91667633783072.          Total Reward: -2.0
Steps done: 226075        Epsilon: 0.01347581833412916
Episode 398 training loss: 64.20858288556337.          Total Reward: -6.0
Steps done: 226514        Epsilon: 0.01343787979644691
Episode 399 training loss: 82.63839919213206.          Total Reward: 1.0
Steps done: 227085        Epsilon: 0.013389152679596231
Beginning to save execution
-------------------------------------------------------------
Target_net saved to target_neth.pth
Policy_net saved to policy_net.pth
Replay memory saved to replay_memory.pkl
Hyperparameters saved to hyperparameters.pkl
Figure plotted to Rewards_Plot.png
Finished saving execution to previous_run/
-------------------------------------------------------------
Episode 400 training loss: 73.10331365093589.          Total Reward: 8.0
Steps done: 227620        Epsilon: 0.013344124559318039
Episode 401 training loss: 70.41684128250927.          Total Reward: 4.0
Steps done: 228133        Epsilon: 0.013301510011735178
Episode 402 training loss: 73.61311092134565.          Total Reward: 4.0
Steps done: 228650        Epsilon: 0.0132591125784718
Episode 403 training loss: 70.04591105785221.          Total Reward: -2.0
Steps done: 229137        Epsilon: 0.013219673455661628
Episode 404 training loss: 110.77489026915282.          Total Reward: 16.0
Steps done: 229907        Epsilon: 0.013158287477282135
Episode 405 training loss: 54.81471559032798.          Total Reward: -9.0
Steps done: 230308        Epsilon: 0.013126783821242601
Episode 406 training loss: 67.98024802654982.          Total Reward: -3.0
Steps done: 230777        Epsilon: 0.013090336371663722
Episode 407 training loss: 64.82618271093816.          Total Reward: -5.0
Steps done: 231236        Epsilon: 0.013055077446774664
Episode 408 training loss: 72.93690670188516.          Total Reward: -6.0
Steps done: 231769        Epsilon: 0.013014638562208991
Episode 409 training loss: 56.420453439466655.          Total Reward: -12.0
Steps done: 232174        Epsilon: 0.012984269350344474
Episode 410 training loss: 74.04386696219444.          Total Reward: 9.0
Steps done: 232721        Epsilon: 0.01294373723694634
Episode 411 training loss: 62.06456804834306.          Total Reward: -13.0
Steps done: 233138        Epsilon: 0.012913208185424761
Episode 412 training loss: 64.17966725118458.          Total Reward: -9.0
Steps done: 233597        Epsilon: 0.012879970189218937
Episode 413 training loss: 117.03857688233256.          Total Reward: 19.0
Steps done: 234396        Epsilon: 0.01282301353309155
Episode 414 training loss: 73.33026737626642.          Total Reward: -5.0
Steps done: 234928        Epsilon: 0.012785716031283095
Episode 415 training loss: 75.27184632234275.          Total Reward: -1.0
Steps done: 235445        Epsilon: 0.012749942337092484
Episode 416 training loss: 61.90825904533267.          Total Reward: -11.0
Steps done: 235866        Epsilon: 0.01272115097432244
Episode 417 training loss: 95.66775850206614.          Total Reward: -9.0
Steps done: 236545        Epsilon: 0.012675349278239155
Episode 418 training loss: 85.24378590099514.          Total Reward: -7.0
Steps done: 237092        Epsilon: 0.012639012893149552
Episode 419 training loss: 72.8696068469435.          Total Reward: -8.0
Steps done: 237617        Epsilon: 0.012604602163322194
Episode 420 training loss: 54.43945431802422.          Total Reward: -19.0
Steps done: 237994        Epsilon: 0.012580169109565399
Episode 421 training loss: 63.33803129661828.          Total Reward: -7.0
Steps done: 238445        Epsilon: 0.012551241091016671
Episode 422 training loss: 93.10475710686296.          Total Reward: 1.0
Steps done: 239064        Epsilon: 0.012512064545470209
Episode 423 training loss: 54.61863530986011.          Total Reward: -14.0
Steps done: 239479        Epsilon: 0.012486136609553045
Episode 424 training loss: 74.81187873892486.          Total Reward: -8.0
Steps done: 239965        Epsilon: 0.01245611281365513
Episode 425 training loss: 69.82666254788637.          Total Reward: 3.0
Steps done: 240458        Epsilon: 0.012426027007854376
Episode 426 training loss: 81.6254187002778.          Total Reward: -4.0
Steps done: 241041        Epsilon: 0.012390924098078777
Episode 427 training loss: 106.73880314640701.          Total Reward: 9.0
Steps done: 241774        Epsilon: 0.012347509415907947
Episode 428 training loss: 82.47797303274274.          Total Reward: -6.0
Steps done: 242423        Epsilon: 0.012309728402921992
Episode 429 training loss: 76.94520885590464.          Total Reward: 3.0
Steps done: 242977        Epsilon: 0.012277959174285943
Episode 430 training loss: 75.97612206079066.          Total Reward: -12.0
Steps done: 243528        Epsilon: 0.012246795419796135
Episode 431 training loss: 77.7856798004359.          Total Reward: 3.0
Steps done: 244075        Epsilon: 0.01221627961976385
Episode 432 training loss: 48.48650064598769.          Total Reward: -23.0
Steps done: 244436        Epsilon: 0.012196367683958919
Episode 433 training loss: 65.94334176182747.          Total Reward: -11.0
Steps done: 244877        Epsilon: 0.012172285725967624
Episode 434 training loss: 101.74910105392337.          Total Reward: -1.0
Steps done: 245588        Epsilon: 0.01213401449044072
Episode 435 training loss: 53.52404383011162.          Total Reward: -19.0
Steps done: 245961        Epsilon: 0.012114207299872067
Episode 436 training loss: 51.31445069331676.          Total Reward: -26.0
Steps done: 246300        Epsilon: 0.012096365106095543
Episode 437 training loss: 92.71621842402965.          Total Reward: 4.0
Steps done: 246915        Epsilon: 0.012064380008109055
Episode 438 training loss: 87.50362602900714.          Total Reward: -1.0
Steps done: 247500        Epsilon: 0.012034408153897364
Episode 439 training loss: 58.761660567484796.          Total Reward: -18.0
Steps done: 247899        Epsilon: 0.012014215809309833
Episode 440 training loss: 55.226590214297175.          Total Reward: -19.0
Steps done: 248306        Epsilon: 0.011993825077221404
Episode 441 training loss: 60.48653240595013.          Total Reward: -12.0
Steps done: 248761        Epsilon: 0.011971273820400755
Episode 442 training loss: 78.89161852933466.          Total Reward: -10.0
Steps done: 249336        Epsilon: 0.011943139459425498
Episode 443 training loss: 93.00899011082947.          Total Reward: -11.0
Steps done: 249997        Epsilon: 0.01191129293646029
Episode 444 training loss: 103.64688777923584.          Total Reward: -2.0
Steps done: 250772        Epsilon: 0.011874618070853157
Episode 445 training loss: 111.56517242919654.          Total Reward: 8.0
Steps done: 251593        Epsilon: 0.011836533712666382
Episode 446 training loss: 85.30903800297529.          Total Reward: 0.0
Steps done: 252268        Epsilon: 0.011805802232398865
Episode 447 training loss: 66.31697847880423.          Total Reward: -12.0
Steps done: 252749        Epsilon: 0.011784217498861202
Episode 448 training loss: 82.19925340730697.          Total Reward: -7.0
Steps done: 253368        Epsilon: 0.011756819273599365
Episode 449 training loss: 91.5938666826114.          Total Reward: -1.0
Steps done: 254077        Epsilon: 0.011725954003519628
Episode 450 training loss: 97.33221732825041.          Total Reward: 1.0
Steps done: 254842        Epsilon: 0.011693258777857436
Episode 451 training loss: 82.35568034555763.          Total Reward: -5.0
Steps done: 255489        Epsilon: 0.011666090631838854
Episode 452 training loss: 70.56911861337721.          Total Reward: 0.0
Steps done: 256068        Epsilon: 0.01164214767514584
Episode 453 training loss: 86.68486309517175.          Total Reward: 0.0
Steps done: 256753        Epsilon: 0.011614265320280523
Episode 454 training loss: 53.966673822142184.          Total Reward: -9.0
Steps done: 257246        Epsilon: 0.011594491606033017
Episode 455 training loss: 82.51859039068222.          Total Reward: 6.0
Steps done: 257937        Epsilon: 0.011567183317997734
Episode 456 training loss: 84.13817880768329.          Total Reward: -1.0
Steps done: 258666        Epsilon: 0.011538880098521371
Episode 457 training loss: 77.66969905979931.          Total Reward: 6.0
Steps done: 259417        Epsilon: 0.011510257163271562
Episode 458 training loss: 79.2503206981346.          Total Reward: 1.0
Steps done: 260158        Epsilon: 0.01148253719822833
Episode 459 training loss: 64.53064569737762.          Total Reward: 5.0
Steps done: 260743        Epsilon: 0.01146101287199277
Episode 460 training loss: 62.888935149647295.          Total Reward: -4.0
Steps done: 261286        Epsilon: 0.011441313633352478
Episode 461 training loss: 46.21315917558968.          Total Reward: -14.0
Steps done: 261683        Epsilon: 0.011427079350018722
Episode 462 training loss: 71.84223459754139.          Total Reward: -1.0
Steps done: 262292        Epsilon: 0.011405516629642943
Episode 463 training loss: 53.46532193291932.          Total Reward: -4.0
Steps done: 262751        Epsilon: 0.011389480509520452
Episode 464 training loss: 70.15707354340702.          Total Reward: 9.0
Steps done: 263346        Epsilon: 0.011368964949698463
Episode 465 training loss: 43.43213558476418.          Total Reward: -17.0
Steps done: 263751        Epsilon: 0.011355174113505475
Episode 466 training loss: 79.47590144630522.          Total Reward: 2.0
Steps done: 264410        Epsilon: 0.011333030528625023
Episode 467 training loss: 64.32984440494329.          Total Reward: 2.0
Steps done: 264975        Epsilon: 0.01131433382870731
Episode 468 training loss: 50.04281613882631.          Total Reward: -4.0
Steps done: 265392        Epsilon: 0.011300703072310458
Episode 469 training loss: 73.59097054228187.          Total Reward: 6.0
Steps done: 265965        Epsilon: 0.011282203321617277
Episode 470 training loss: 69.303561296314.          Total Reward: -4.0
Steps done: 266462        Epsilon: 0.01126637051037544
Episode 471 training loss: 55.99656589701772.          Total Reward: -6.0
Steps done: 266903        Epsilon: 0.011252485457496996
Episode 472 training loss: 128.89409931376576.          Total Reward: 20.0
Steps done: 267896        Epsilon: 0.011221775273333652
Episode 473 training loss: 87.83089376334101.          Total Reward: 9.0
Steps done: 268549        Epsilon: 0.01120199171466133
Episode 474 training loss: 54.16322028264403.          Total Reward: -11.0
Steps done: 268968        Epsilon: 0.011189466566441323
Episode 475 training loss: 90.16806711629033.          Total Reward: 10.0
Steps done: 269605        Epsilon: 0.011170674341610442
Episode 476 training loss: 54.42454664129764.          Total Reward: -8.0
Steps done: 270002        Epsilon: 0.011159112867490974
Episode 477 training loss: 84.44619710277766.          Total Reward: 10.0
Steps done: 270597        Epsilon: 0.011141998666024661
Episode 478 training loss: 61.2468630829826.          Total Reward: -10.0
Steps done: 271066        Epsilon: 0.011128686924254633
Episode 479 training loss: 49.54458252899349.          Total Reward: -18.0
Steps done: 271437        Epsilon: 0.011118266751284373
Episode 480 training loss: 145.41471894364804.          Total Reward: 30.0
Steps done: 272492        Epsilon: 0.011089158024468972
Episode 481 training loss: 68.78969260305166.          Total Reward: -9.0
Steps done: 273019        Epsilon: 0.011074902482088589
Episode 482 training loss: 574.4280777545646.          Total Reward: 24.0
Steps done: 278666        Epsilon: 0.010933377961374809
Episode 483 training loss: 58.90792295243591.          Total Reward: 20.0
Steps done: 279537        Epsilon: 0.01091327333971285
Episode 484 training loss: 40.462553372140974.          Total Reward: 7.0
Steps done: 280130        Epsilon: 0.01089983392823183
Episode 485 training loss: 40.30022463295609.          Total Reward: 5.0
Steps done: 280673        Epsilon: 0.010887701219733039
Episode 486 training loss: 30.520189182367176.          Total Reward: 0.0
Steps done: 281130        Epsilon: 0.010877616949383896
Episode 487 training loss: 26.410489018075168.          Total Reward: -8.0
Steps done: 281537        Epsilon: 0.010868732473346899
Episode 488 training loss: 35.368311785161495.          Total Reward: 3.0
Steps done: 282076        Epsilon: 0.010857104820520463
Episode 489 training loss: 36.85725881299004.          Total Reward: 4.0
Steps done: 282583        Epsilon: 0.010846309576306577
Episode 490 training loss: 67.26873977156356.          Total Reward: 6.0
Steps done: 283468        Epsilon: 0.010827790598560032
Episode 491 training loss: 43.22064308542758.          Total Reward: -4.0
Steps done: 284001        Epsilon: 0.01081683345294166
Episode 492 training loss: 46.23973481496796.          Total Reward: 5.0
Steps done: 284530        Epsilon: 0.01080610194900804
Episode 493 training loss: 69.61179843172431.          Total Reward: 15.0
Steps done: 285281        Epsilon: 0.010791108575636477
Episode 494 training loss: 77.0266952784732.          Total Reward: 14.0
Steps done: 286042        Epsilon: 0.010776200002465186
Episode 495 training loss: 81.96489763632417.          Total Reward: 12.0
Steps done: 286807        Epsilon: 0.010761496230413416
Episode 496 training loss: 96.83924737200141.          Total Reward: 13.0
Steps done: 287636        Epsilon: 0.010745876638143586
Episode 497 training loss: 80.08065844979137.          Total Reward: 3.0
Steps done: 288291        Epsilon: 0.010733762364502289
Episode 498 training loss: 81.03512753266841.          Total Reward: -2.0
Steps done: 288918        Epsilon: 0.010722350315042463
Episode 499 training loss: 57.68408858124167.          Total Reward: -5.0
Steps done: 289373        Epsilon: 0.010714180136196232
Beginning to save execution
-------------------------------------------------------------
Target_net saved to target_neth.pth
Policy_net saved to policy_net.pth
Replay memory saved to replay_memory.pkl
Hyperparameters saved to hyperparameters.pkl
Figure plotted to Rewards_Plot.png
Finished saving execution to previous_run/
-------------------------------------------------------------
Episode 500 training loss: 63.374804756604135.          Total Reward: -3.0
Steps done: 289884        Epsilon: 0.010705114514904909
Episode 501 training loss: 68.55278935469687.          Total Reward: 1.0
Steps done: 290447        Epsilon: 0.010695259545150477
Episode 502 training loss: 106.4258710257709.          Total Reward: 14.0
Steps done: 291272        Epsilon: 0.010681066684034282
Episode 503 training loss: 86.4566870899871.          Total Reward: 3.0
Steps done: 291975        Epsilon: 0.01066920150770803
Episode 504 training loss: 90.75692426785827.          Total Reward: -1.0
Steps done: 292724        Epsilon: 0.010656787300219956
Episode 505 training loss: 70.88567991927266.          Total Reward: 0.0
Steps done: 293290        Epsilon: 0.010647559202684126
Episode 506 training loss: 49.37309701554477.          Total Reward: -12.0
Steps done: 293713        Epsilon: 0.010640747345292769
Episode 507 training loss: 62.7126868898049.          Total Reward: -11.0
Steps done: 294186        Epsilon: 0.010633215129927357
Episode 508 training loss: 77.28361573442817.          Total Reward: 1.0
Steps done: 294771        Epsilon: 0.010624021749113616
Episode 509 training loss: 72.7926133312285.          Total Reward: -6.0
Steps done: 295318        Epsilon: 0.01061554633442122
Episode 510 training loss: 79.31462271139026.          Total Reward: -6.0
Steps done: 295891        Epsilon: 0.010606791489469048
Episode 511 training loss: 59.50680228229612.          Total Reward: -5.0
Steps done: 296390        Epsilon: 0.010599268786060628
Episode 512 training loss: 88.67675263714045.          Total Reward: 23.0
Steps done: 297075        Epsilon: 0.010589093681101712
Episode 513 training loss: 77.08239421248436.          Total Reward: 0.0
Steps done: 297635        Epsilon: 0.010580903832275168
Episode 514 training loss: 58.716308161616325.          Total Reward: -7.0
Steps done: 298090        Epsilon: 0.01057433349084482
Episode 515 training loss: 75.4754801671952.          Total Reward: -10.0
Steps done: 298605        Epsilon: 0.01056698634588758
Episode 516 training loss: 64.18887895718217.          Total Reward: -2.0
Steps done: 299086        Epsilon: 0.010560209164546287
Episode 517 training loss: 74.25180723890662.          Total Reward: -1.0
Steps done: 299625        Epsilon: 0.010552710978539223
Episode 518 training loss: 70.53795497119427.          Total Reward: 4.0
Steps done: 300114        Epsilon: 0.010545995220536683
Episode 519 training loss: 64.78739784285426.          Total Reward: 0.0
Steps done: 300601        Epsilon: 0.010539388031604716
Episode 520 training loss: 62.620925256982446.          Total Reward: -2.0
Steps done: 301052        Epsilon: 0.010533340588076546
Episode 521 training loss: 69.14331764169037.          Total Reward: 1.0
Steps done: 301531        Epsilon: 0.010526991923032976
Episode 522 training loss: 95.52641836926341.          Total Reward: 2.0
Steps done: 302166        Epsilon: 0.01051869198135078
Episode 523 training loss: 74.34446329064667.          Total Reward: -1.0
Steps done: 302677        Epsilon: 0.010512107837055173
Episode 524 training loss: 98.21115745324641.          Total Reward: 8.0
Steps done: 303322        Epsilon: 0.010503916319783433
Episode 525 training loss: 109.04793887492269.          Total Reward: 15.0
Steps done: 304093        Epsilon: 0.010494296343082209
Episode 526 training loss: 51.12179340608418.          Total Reward: -21.0
Steps done: 304458        Epsilon: 0.010489806405446792
Episode 527 training loss: 81.6515530878678.          Total Reward: 6.0
Steps done: 305009        Epsilon: 0.01048310558010313
Episode 528 training loss: 70.12999063171446.          Total Reward: -14.0
Steps done: 305464        Epsilon: 0.010477641390624896
Episode 529 training loss: 76.77289776690304.          Total Reward: -3.0
Steps done: 306001        Epsilon: 0.010471271905787128
Episode 530 training loss: 79.65118493977934.          Total Reward: 12.0
Steps done: 306554        Epsilon: 0.010464801402105279
Episode 531 training loss: 117.89649200905114.          Total Reward: 10.0
Steps done: 307367        Epsilon: 0.01045544967249511
Episode 532 training loss: 92.1463923221454.          Total Reward: 6.0
Steps done: 307997        Epsilon: 0.01044833253473713
Episode 533 training loss: 59.03926494345069.          Total Reward: -7.0
Steps done: 308432        Epsilon: 0.010443483333743323
Episode 534 training loss: 89.09809982590377.          Total Reward: -5.0
Steps done: 309085        Epsilon: 0.01043630224345217
Episode 535 training loss: 67.54622508957982.          Total Reward: -14.0
Steps done: 309564        Epsilon: 0.010431108682595632
Episode 536 training loss: 96.47342195082456.          Total Reward: 16.0
Steps done: 310263        Epsilon: 0.010423640501647378
Episode 537 training loss: 74.6381932515651.          Total Reward: 0.0
Steps done: 310816        Epsilon: 0.010417823971122156
Episode 538 training loss: 114.71599248144776.          Total Reward: 12.0
Steps done: 311639        Epsilon: 0.010409315078321792
Episode 539 training loss: 65.20096931327134.          Total Reward: -7.0
Steps done: 312144        Epsilon: 0.01040417995910534
Episode 540 training loss: 61.37278858665377.          Total Reward: -9.0
Steps done: 312605        Epsilon: 0.010399548524980113
Episode 541 training loss: 102.25378028582782.          Total Reward: 13.0
Steps done: 313361        Epsilon: 0.010392067971761943
Episode 542 training loss: 63.90797541849315.          Total Reward: 3.0
Steps done: 313854        Epsilon: 0.010387265390710476
Episode 543 training loss: 72.91640653926879.          Total Reward: 3.0
Steps done: 314397        Epsilon: 0.010382043784867725
Episode 544 training loss: 59.59469873085618.          Total Reward: -12.0
Steps done: 314852        Epsilon: 0.010377722659806297
Episode 545 training loss: 77.48291552253067.          Total Reward: 7.0
Steps done: 315435        Epsilon: 0.010372257277762134
Episode 546 training loss: 58.863221312873065.          Total Reward: -9.0
Steps done: 315850        Epsilon: 0.010368415074399995
Episode 547 training loss: 68.9844599943608.          Total Reward: 7.0
Steps done: 316363        Epsilon: 0.010363720320529506
Episode 548 training loss: 62.90016273222864.          Total Reward: 0.0
Steps done: 316864        Epsilon: 0.010359193134202855
Episode 549 training loss: 80.65059821307659.          Total Reward: 12.0
Steps done: 317431        Epsilon: 0.010354137488070056
Episode 550 training loss: 79.49575555324554.          Total Reward: 5.0
Steps done: 318021        Epsilon: 0.01034895229492873
Episode 551 training loss: 63.92268307041377.          Total Reward: 1.0
Steps done: 318476        Epsilon: 0.010345005452795488
Episode 552 training loss: 89.70525942370296.          Total Reward: 3.0
Steps done: 319105        Epsilon: 0.01033962267505892
Episode 553 training loss: 78.80743507109582.          Total Reward: -14.0
Steps done: 319696        Epsilon: 0.010334641638059056
Episode 554 training loss: 75.50556150544435.          Total Reward: 5.0
Steps done: 320283        Epsilon: 0.0103297666298811
Episode 555 training loss: 68.39686309825629.          Total Reward: -6.0
Steps done: 320804        Epsilon: 0.010325499271031246
Episode 556 training loss: 59.229260109364986.          Total Reward: -6.0
Steps done: 321279        Epsilon: 0.01032165682685367
Episode 557 training loss: 78.07415078114718.          Total Reward: 7.0
Steps done: 321846        Epsilon: 0.010317129504536166
Episode 558 training loss: 79.5666361823678.          Total Reward: 4.0
Steps done: 322435        Epsilon: 0.010312493985349856
Episode 559 training loss: 87.2119186585769.          Total Reward: 12.0
Steps done: 323070        Epsilon: 0.010307572312472
Episode 560 training loss: 107.32918281853199.          Total Reward: 12.0
Steps done: 323804        Epsilon: 0.01030197982850393
Episode 561 training loss: 97.16614142712206.          Total Reward: 10.0
Steps done: 324491        Epsilon: 0.010296837610153405
Episode 562 training loss: 67.57534317299724.          Total Reward: -3.0
Steps done: 325002        Epsilon: 0.010293069628908498
Episode 563 training loss: 72.96216150000691.          Total Reward: -5.0
Steps done: 325531        Epsilon: 0.010289219299488065
Episode 564 training loss: 62.830302357673645.          Total Reward: -13.0
Steps done: 325970        Epsilon: 0.010286062472451299
Episode 565 training loss: 89.99476038478315.          Total Reward: -2.0
Steps done: 326657        Epsilon: 0.010281191300417977
Episode 566 training loss: 107.45238319039345.          Total Reward: 9.0
Steps done: 327460        Epsilon: 0.010275602668639802
Episode 567 training loss: 61.379154931753874.          Total Reward: -4.0
Steps done: 327929        Epsilon: 0.01027239009785035
Episode 568 training loss: 80.47181979380548.          Total Reward: -4.0
Steps done: 328546        Epsilon: 0.010268220719589086
Episode 569 training loss: 87.99388269428164.          Total Reward: 7.0
Steps done: 329223        Epsilon: 0.010263719284756905
Episode 570 training loss: 49.25079052709043.          Total Reward: -23.0
Steps done: 329568        Epsilon: 0.010261454486906567
Episode 571 training loss: 76.23257680609822.          Total Reward: 8.0
Steps done: 330119        Epsilon: 0.010257877643417804
Episode 572 training loss: 67.89089362323284.          Total Reward: -7.0
Steps done: 330582        Epsilon: 0.010254909918537714
Episode 573 training loss: 73.58225423283875.          Total Reward: 7.0
Steps done: 331157        Epsilon: 0.010251271800083497
Episode 574 training loss: 83.73639665730298.          Total Reward: 6.0
Steps done: 331790        Epsilon: 0.010247326721610953
Episode 575 training loss: 68.83150797151029.          Total Reward: -2.0
Steps done: 332307        Epsilon: 0.01024415059367662
Episode 576 training loss: 60.94351344462484.          Total Reward: -8.0
Steps done: 332756        Epsilon: 0.01024142532743476
Episode 577 training loss: 59.914913090877235.          Total Reward: -4.0
Steps done: 333223        Epsilon: 0.010238623076705729
Episode 578 training loss: 76.38053961470723.          Total Reward: 6.0
Steps done: 333756        Epsilon: 0.010235464514861807
Episode 579 training loss: 92.16184578090906.          Total Reward: 5.0
Steps done: 334380        Epsilon: 0.010231819771344497
Episode 580 training loss: 67.85424565896392.          Total Reward: -6.0
Steps done: 334833        Epsilon: 0.010229209222567872
Episode 581 training loss: 55.885965375229716.          Total Reward: -12.0
Steps done: 335240        Epsilon: 0.010226888843675015
Episode 582 training loss: 85.03080438263714.          Total Reward: -3.0
Steps done: 335815        Epsilon: 0.010223650646848603
Episode 583 training loss: 52.36122353374958.          Total Reward: -19.0
Steps done: 336184        Epsilon: 0.010221596956840757
Episode 584 training loss: 74.81147120613605.          Total Reward: -5.0
Steps done: 336691        Epsilon: 0.010218805940842624
Episode 585 training loss: 135.2498683296144.          Total Reward: 30.0
Steps done: 337624        Epsilon: 0.010213761353481836
Episode 586 training loss: 64.77388140559196.          Total Reward: -2.0
Steps done: 338077        Epsilon: 0.010211354162599948
Episode 587 training loss: 78.71434746868908.          Total Reward: -1.0
Steps done: 338572        Epsilon: 0.010208754771741322
Episode 588 training loss: 69.8420301489532.          Total Reward: -5.0
Steps done: 339039        Epsilon: 0.01020633173179967
Episode 589 training loss: 81.9687206512317.          Total Reward: 0.0
Steps done: 339564        Epsilon: 0.010203641322254419
Episode 590 training loss: 80.03716986440122.          Total Reward: 3.0
Steps done: 340085        Epsilon: 0.010201006093216745
Episode 591 training loss: 61.815138183534145.          Total Reward: -6.0
Steps done: 340526        Epsilon: 0.010198802172476065
Episode 592 training loss: 83.83450294844806.          Total Reward: 6.0
Steps done: 341071        Epsilon: 0.010196111862233714
Episode 593 training loss: 113.45682246703655.          Total Reward: 24.0
Steps done: 341844        Epsilon: 0.010192358385279482
Episode 594 training loss: 78.30489166919142.          Total Reward: -10.0
Steps done: 342383        Epsilon: 0.010189783741656841
Episode 595 training loss: 113.3317825999111.          Total Reward: 11.0
Steps done: 343142        Epsilon: 0.010186216545958368
Episode 596 training loss: 72.1953657483682.          Total Reward: -1.0
Steps done: 343649        Epsilon: 0.010183871146606786
Episode 597 training loss: 95.68829755857587.          Total Reward: 4.0
Steps done: 344330        Epsilon: 0.010180767237335618
Episode 598 training loss: 83.53946250863373.          Total Reward: 4.0
Steps done: 344881        Epsilon: 0.010178294240511216
Episode 599 training loss: 89.06355920061469.          Total Reward: -1.0
Steps done: 345474        Epsilon: 0.01017567052474209
Beginning to save execution
-------------------------------------------------------------
Target_net saved to target_neth.pth
Policy_net saved to policy_net.pth
Replay memory saved to replay_memory.pkl
Hyperparameters saved to hyperparameters.pkl
Figure plotted to Rewards_Plot.png
Finished saving execution to previous_run/
-------------------------------------------------------------
Episode 600 training loss: 75.73866979032755.          Total Reward: 2.0
Steps done: 345995        Epsilon: 0.010173397252978094
Episode 601 training loss: 86.20164229348302.          Total Reward: 5.0
Steps done: 346634        Epsilon: 0.010170649240055955
Episode 602 training loss: 104.84751545079052.          Total Reward: 29.0
Steps done: 347371        Epsilon: 0.010167533816779843
Episode 603 training loss: 74.77835055161268.          Total Reward: -4.0
Steps done: 347898        Epsilon: 0.010165341035409649
Episode 604 training loss: 52.44975212030113.          Total Reward: -13.0
Steps done: 348305        Epsilon: 0.010163667220349377
Episode 605 training loss: 71.79664939828217.          Total Reward: 2.0
Steps done: 348800        Epsilon: 0.01016165431901259
Episode 606 training loss: 66.49281682819128.          Total Reward: -3.0
Steps done: 349281        Epsilon: 0.010159722066776716
Episode 607 training loss: 87.00261037331074.          Total Reward: 11.0
Steps done: 349908        Epsilon: 0.010157237943559088
Episode 608 training loss: 92.2479903511703.          Total Reward: 20.0
Steps done: 350593        Epsilon: 0.010154568168966363
Episode 609 training loss: 91.17803773004562.          Total Reward: 6.0
Steps done: 351286        Epsilon: 0.010151913339305794
Episode 610 training loss: 87.38845662865788.          Total Reward: 9.0
Steps done: 351915        Epsilon: 0.010149543186213786
Episode 611 training loss: 78.0748470555991.          Total Reward: 2.0
Steps done: 352492        Epsilon: 0.010147401509730938
Episode 612 training loss: 73.75948721729219.          Total Reward: 2.0
Steps done: 353035        Epsilon: 0.010145414054608679
Episode 613 training loss: 61.61592744477093.          Total Reward: -6.0
Steps done: 353492        Epsilon: 0.010143762153488525
Episode 614 training loss: 66.04444860760123.          Total Reward: -10.0
Steps done: 353973        Epsilon: 0.010142043766103585
Episode 615 training loss: 64.0330920824781.          Total Reward: -3.0
Steps done: 354440        Epsilon: 0.010140395048252199
Episode 616 training loss: 114.48313007131219.          Total Reward: 23.0
Steps done: 355285        Epsilon: 0.010137460310167474
Episode 617 training loss: 105.76507586799562.          Total Reward: 11.0
Steps done: 356064        Epsilon: 0.01013480916989755
Episode 618 training loss: 65.51616381853819.          Total Reward: -8.0
Steps done: 356585        Epsilon: 0.01013306466620289
Episode 619 training loss: 77.46926047094166.          Total Reward: -7.0
Steps done: 357120        Epsilon: 0.010131296775416902
Episode 620 training loss: 126.694844244048.          Total Reward: 24.0
Steps done: 358017        Epsilon: 0.010128385213133282
Episode 621 training loss: 56.06250898167491.          Total Reward: -10.0
Steps done: 358446        Epsilon: 0.01012701563919068
Episode 622 training loss: 67.547652522102.          Total Reward: 2.0
Steps done: 359003        Epsilon: 0.010125259203976921
Episode 623 training loss: 70.52822096832097.          Total Reward: -5.0
Steps done: 359562        Epsilon: 0.010123520881421398
Episode 624 training loss: 78.62672888673842.          Total Reward: -1.0
Steps done: 360171        Epsilon: 0.010121654519731963
Episode 625 training loss: 59.25726045668125.          Total Reward: -12.0
Steps done: 360620        Epsilon: 0.010120296583423873
Episode 626 training loss: 62.6890923557803.          Total Reward: 6.0
Steps done: 361121        Epsilon: 0.010118799265245922
Episode 627 training loss: 62.886216764338315.          Total Reward: 2.0
Steps done: 361646        Epsilon: 0.010117250212783662
Episode 628 training loss: 64.03720333520323.          Total Reward: -6.0
Steps done: 362093        Epsilon: 0.010115947235600505
Episode 629 training loss: 83.61003783810884.          Total Reward: 12.0
Steps done: 362694        Epsilon: 0.010114218150664567
Episode 630 training loss: 70.51325668487698.          Total Reward: 0.0
Steps done: 363213        Epsilon: 0.010112745743060694
Episode 631 training loss: 68.36605337075889.          Total Reward: -11.0
Steps done: 363700        Epsilon: 0.01011138138601569
Episode 632 training loss: 64.15820950642228.          Total Reward: -11.0
Steps done: 364195        Epsilon: 0.010110011534799757
Episode 633 training loss: 111.0498351957649.          Total Reward: 15.0
Steps done: 365036        Epsilon: 0.01010772268809645
Episode 634 training loss: 59.594885129481554.          Total Reward: -9.0
Steps done: 365501        Epsilon: 0.010106477662579242
Episode 635 training loss: 59.7483732663095.          Total Reward: -5.0
Steps done: 365954        Epsilon: 0.01010527860552655
Episode 636 training loss: 64.53385777771473.          Total Reward: -4.0
Steps done: 366435        Epsilon: 0.01010402021155254
Episode 637 training loss: 48.21188160870224.          Total Reward: -20.0
Steps done: 366784        Epsilon: 0.010103116583018655
Episode 638 training loss: 70.7007279470563.          Total Reward: -1.0
Steps done: 367311        Epsilon: 0.010101766932383653
Episode 639 training loss: 56.129370383918285.          Total Reward: -10.0
Steps done: 367702        Epsilon: 0.010100777006763394
Episode 640 training loss: 64.0606449637562.          Total Reward: -7.0
Steps done: 368109        Epsilon: 0.010099756799824252
Episode 641 training loss: 81.97007702477276.          Total Reward: 3.0
Steps done: 368648        Epsilon: 0.010098421593105245
Episode 642 training loss: 84.97611556109041.          Total Reward: 17.0
Steps done: 369235        Epsilon: 0.010096987802396897
Episode 643 training loss: 96.56687153596431.          Total Reward: 3.0
Steps done: 369880        Epsilon: 0.010095436415753311
Episode 644 training loss: 54.41890780441463.          Total Reward: -10.0
Steps done: 370269        Epsilon: 0.01009451279499537
Episode 645 training loss: 72.13382054679096.          Total Reward: -4.0
Steps done: 370770        Epsilon: 0.01009333640476077
Episode 646 training loss: 106.75859080813825.          Total Reward: 19.0
Steps done: 371523        Epsilon: 0.01009159578195657
Episode 647 training loss: 83.58911479823291.          Total Reward: 1.0
Steps done: 372038        Epsilon: 0.010090424045503388
Episode 648 training loss: 80.53052967227995.          Total Reward: 5.0
Steps done: 372615        Epsilon: 0.010089129041320036
Episode 649 training loss: 80.56475787237287.          Total Reward: 2.0
Steps done: 373186        Epsilon: 0.010087865762360813
Episode 650 training loss: 78.10297036357224.          Total Reward: 6.0
Steps done: 373729        Epsilon: 0.010086681044105254
Episode 651 training loss: 74.03617249336094.          Total Reward: 6.0
Steps done: 374250        Epsilon: 0.010085559344432941
Episode 652 training loss: 113.93580720759928.          Total Reward: 20.0
Steps done: 375007        Epsilon: 0.010083955359420464
Episode 653 training loss: 80.32658848911524.          Total Reward: 9.0
Steps done: 375612        Epsilon: 0.010082695089426505
Episode 654 training loss: 81.6654569786042.          Total Reward: 9.0
Steps done: 376195        Epsilon: 0.01008149854946482
Episode 655 training loss: 97.46993273030967.          Total Reward: 25.0
Steps done: 376912        Epsilon: 0.010080050703055664
Episode 656 training loss: 69.07790490984917.          Total Reward: 12.0
Steps done: 377423        Epsilon: 0.010079034559759
Episode 657 training loss: 65.7023514918983.          Total Reward: 2.0
Steps done: 377918        Epsilon: 0.010078062533896695
Episode 658 training loss: 61.39999704435468.          Total Reward: -7.0
Steps done: 378383        Epsilon: 0.01007716031126972
Episode 659 training loss: 102.37322328425944.          Total Reward: 21.0
Steps done: 379140        Epsilon: 0.01007571378332289
Episode 660 training loss: 110.98816052731127.          Total Reward: 27.0
Steps done: 380001        Epsilon: 0.010074101459029192
Episode 661 training loss: 55.56130641512573.          Total Reward: -9.0
Steps done: 380408        Epsilon: 0.010073351299591736
Episode 662 training loss: 102.1432994324714.          Total Reward: 6.0
Steps done: 381163        Epsilon: 0.010071979778263065
Episode 663 training loss: 77.19845616072416.          Total Reward: -2.0
Steps done: 381696        Epsilon: 0.010071027009636097
Episode 664 training loss: 93.15609621815383.          Total Reward: 8.0
Steps done: 382397        Epsilon: 0.010069793104962081
Episode 665 training loss: 76.01154052466154.          Total Reward: 3.0
Steps done: 382974        Epsilon: 0.01006879356593027
Episode 666 training loss: 81.47641587350518.          Total Reward: 9.0
Steps done: 383589        Epsilon: 0.010067743954419029
Episode 667 training loss: 77.06364556029439.          Total Reward: 6.0
Steps done: 384152        Epsilon: 0.010066797137118104
Episode 668 training loss: 69.5553569085896.          Total Reward: 0.0
Steps done: 384675        Epsilon: 0.010065929449419917
Episode 669 training loss: 91.1647993735969.          Total Reward: 12.0
Steps done: 385338        Epsilon: 0.010064845675385141
Episode 670 training loss: 111.34991894848645.          Total Reward: 19.0
Steps done: 386121        Epsilon: 0.010063588664422538
Episode 671 training loss: 91.7138539403677.          Total Reward: 8.0
Steps done: 386796        Epsilon: 0.01006252460892905
Episode 672 training loss: 129.00891662668437.          Total Reward: 35.0
Steps done: 387748        Epsilon: 0.010061054091802994
Episode 673 training loss: 102.19921665079892.          Total Reward: 14.0
Steps done: 388543        Epsilon: 0.010059852620895276
Episode 674 training loss: 116.53219729661942.          Total Reward: 16.0
Steps done: 389460        Epsilon: 0.010058496108000041
Episode 675 training loss: 74.59020592086017.          Total Reward: -4.0
Steps done: 390033        Epsilon: 0.010057664124561577
Episode 676 training loss: 70.33487837389112.          Total Reward: 7.0
Steps done: 390620        Epsilon: 0.010056824082418456
Episode 677 training loss: 74.32541085593402.          Total Reward: 6.0
Steps done: 391223        Epsilon: 0.010055973883848691
Episode 678 training loss: 82.81820601597428.          Total Reward: 6.0
Steps done: 391814        Epsilon: 0.01005515294930294
Episode 679 training loss: 137.54760055989027.          Total Reward: 46.0
Steps done: 392909        Epsilon: 0.010053663615577703
Episode 680 training loss: 62.054574004374444.          Total Reward: 2.0
Steps done: 393422        Epsilon: 0.01005297977421386
Episode 681 training loss: 77.21175380889326.          Total Reward: 16.0
Steps done: 394045        Epsilon: 0.010052161006932042
Episode 682 training loss: 86.8027820289135.          Total Reward: 20.0
Steps done: 394774        Epsilon: 0.010051218982849504
Episode 683 training loss: 70.29947568010539.          Total Reward: 5.0
Steps done: 395357        Epsilon: 0.010050477880080266
Episode 684 training loss: 80.97098352387547.          Total Reward: 24.0
Steps done: 395996        Epsilon: 0.01004967790277751
Episode 685 training loss: 84.82070304173976.          Total Reward: 7.0
Steps done: 396757        Epsilon: 0.010048741714406706
Episode 686 training loss: 66.03974817693233.          Total Reward: -8.0
Steps done: 397318        Epsilon: 0.010048062883292512
Episode 687 training loss: 98.73479411564767.          Total Reward: 25.0
Steps done: 398097        Epsilon: 0.010047135914298844
Episode 688 training loss: 68.81197058130056.          Total Reward: 9.0
Steps done: 398650        Epsilon: 0.010046488744155084
Episode 689 training loss: 72.42146499734372.          Total Reward: 6.0
Steps done: 399201        Epsilon: 0.010045852752155866
Episode 690 training loss: 73.87808470055461.          Total Reward: 12.0
Steps done: 399754        Epsilon: 0.010045223199666095
Episode 691 training loss: 81.62182754371315.          Total Reward: 18.0
Steps done: 400369        Epsilon: 0.010044533210852422
Episode 692 training loss: 73.98833080008626.          Total Reward: -3.0
Steps done: 400918        Epsilon: 0.010043926167895078
Episode 693 training loss: 103.46768053248525.          Total Reward: 21.0
Steps done: 401627        Epsilon: 0.010043154436245713
Episode 694 training loss: 157.65923657547683.          Total Reward: 30.0
Steps done: 402844        Epsilon: 0.010041861235101411
Episode 695 training loss: 96.83420771919191.          Total Reward: 22.0
Steps done: 403581        Epsilon: 0.010041097003944219
Episode 696 training loss: 80.10806686989963.          Total Reward: 0.0
Steps done: 404186        Epsilon: 0.010040480088939983
Episode 697 training loss: 71.94233305379748.          Total Reward: 10.0
Steps done: 404713        Epsilon: 0.010039950261669301
Episode 698 training loss: 74.64190416689962.          Total Reward: -3.0
Steps done: 405237        Epsilon: 0.010039430326253894
Episode 699 training loss: 112.86170177999884.          Total Reward: 23.0
Steps done: 406102        Epsilon: 0.010038586798959569
Beginning to save execution
-------------------------------------------------------------
Target_net saved to target_neth.pth
Policy_net saved to policy_net.pth
Replay memory saved to replay_memory.pkl
Hyperparameters saved to hyperparameters.pkl
Figure plotted to Rewards_Plot.png
Finished saving execution to previous_run/
-------------------------------------------------------------
Episode 700 training loss: 90.32326931972057.          Total Reward: 12.0
Steps done: 406785        Epsilon: 0.010037933522586492
Episode 701 training loss: 99.7574268616736.          Total Reward: 21.0
Steps done: 407538        Epsilon: 0.010037226103497159
Episode 702 training loss: 58.194826574996114.          Total Reward: -9.0
Steps done: 407977        Epsilon: 0.010036819780785635
Episode 703 training loss: 88.4999592192471.          Total Reward: 9.0
Steps done: 408656        Epsilon: 0.010036200039938725
Episode 704 training loss: 84.22547837626189.          Total Reward: 6.0
Steps done: 409269        Epsilon: 0.010035649503586135
Episode 705 training loss: 106.861686386168.          Total Reward: 23.0
Steps done: 410118        Epsilon: 0.010034900816421843
Episode 706 training loss: 59.36294945329428.          Total Reward: 0.0
Steps done: 410625        Epsilon: 0.010034461240272559
Episode 707 training loss: 87.28395644761622.          Total Reward: 8.0
Steps done: 411304        Epsilon: 0.010033881197758008
Episode 708 training loss: 81.300417996943.          Total Reward: 5.0
Steps done: 411921        Epsilon: 0.010033362590325091
Episode 709 training loss: 78.1636807192117.          Total Reward: 11.0
Steps done: 412528        Epsilon: 0.010032860135038502
Episode 710 training loss: 89.33306051231921.          Total Reward: 4.0
Steps done: 413151        Epsilon: 0.010032352303439653
Episode 711 training loss: 105.0452194493264.          Total Reward: 13.0
Steps done: 413922        Epsilon: 0.010031734684217768
Episode 712 training loss: 123.5479725021869.          Total Reward: 42.0
Steps done: 414883        Epsilon: 0.0100309813441622
Episode 713 training loss: 95.29665407538414.          Total Reward: 9.0
Steps done: 415626        Epsilon: 0.010030411177510815
Episode 714 training loss: 73.69450235832483.          Total Reward: 16.0
Steps done: 416247        Epsilon: 0.01002994269002383
Episode 715 training loss: 65.47734292596579.          Total Reward: 0.0
Steps done: 416740        Epsilon: 0.010029575911286224
Episode 716 training loss: 80.42682826984674.          Total Reward: 10.0
Steps done: 417318        Epsilon: 0.0100291516123111
Episode 717 training loss: 103.06994663458318.          Total Reward: 20.0
Steps done: 418043        Epsilon: 0.010028627998918847
Episode 718 training loss: 109.76707138959318.          Total Reward: 23.0
Steps done: 418886        Epsilon: 0.01002803097705689
Episode 719 training loss: 71.95187100488693.          Total Reward: -2.0
Steps done: 419427        Epsilon: 0.010027654410364743
Episode 720 training loss: 70.88986220397055.          Total Reward: 5.0
Steps done: 419978        Epsilon: 0.010027276082576916
Episode 721 training loss: 106.03214578796178.          Total Reward: 6.0
Steps done: 420783        Epsilon: 0.01002673263816627
Episode 722 training loss: 69.07751005701721.          Total Reward: 3.0
Steps done: 421313        Epsilon: 0.010026380767004944
Episode 723 training loss: 68.33715362008661.          Total Reward: -1.0
Steps done: 421852        Epsilon: 0.010026027670500048
Episode 724 training loss: 72.7809928720817.          Total Reward: 1.0
Steps done: 422393        Epsilon: 0.010025678016124298
Episode 725 training loss: 116.75136415474117.          Total Reward: 20.0
Steps done: 423308        Epsilon: 0.010025097298782284
Episode 726 training loss: 153.76873488910496.          Total Reward: 29.0
Steps done: 424433        Epsilon: 0.010024401271024507
Episode 727 training loss: 62.84983248077333.          Total Reward: -9.0
Steps done: 424944        Epsilon: 0.010024091527486534
Episode 728 training loss: 81.13374438416213.          Total Reward: 3.0
Steps done: 425527        Epsilon: 0.01002374293997577
Episode 729 training loss: 70.53122747410089.          Total Reward: -5.0
Steps done: 426058        Epsilon: 0.010023429835278099
Episode 730 training loss: 84.03246249258518.          Total Reward: 7.0
Steps done: 426635        Epsilon: 0.010023094285872721
Episode 731 training loss: 72.42262092139572.          Total Reward: 4.0
Steps done: 427171        Epsilon: 0.010022786886616746
Episode 732 training loss: 96.10997997131199.          Total Reward: 15.0
Steps done: 427892        Epsilon: 0.010022379832580926
Episode 733 training loss: 116.41492915339768.          Total Reward: 40.0
Steps done: 428759        Epsilon: 0.010021899969017836
Episode 734 training loss: 80.98093252722174.          Total Reward: 13.0
Steps done: 429382        Epsilon: 0.010021561519517613
Episode 735 training loss: 110.57389018684626.          Total Reward: 38.0
Steps done: 430225        Epsilon: 0.0100211118653673
Episode 736 training loss: 93.36324662156403.          Total Reward: 15.0
Steps done: 430916        Epsilon: 0.010020750289992284
Episode 737 training loss: 67.69599028956145.          Total Reward: 3.0
Steps done: 431419        Epsilon: 0.010020490988868392
Episode 738 training loss: 74.29150825180113.          Total Reward: 4.0
Steps done: 431994        Epsilon: 0.010020198537930528
Episode 739 training loss: 82.20925046969205.          Total Reward: 16.0
Steps done: 432623        Epsilon: 0.010019883400185885
Episode 740 training loss: 135.39778140187263.          Total Reward: 37.0
Steps done: 433554        Epsilon: 0.010019425958178405
Episode 741 training loss: 69.643947891891.          Total Reward: 2.0
Steps done: 434071        Epsilon: 0.010019176493308538
Episode 742 training loss: 101.99442077614367.          Total Reward: 18.0
Steps done: 434812        Epsilon: 0.010018824518997743
Episode 743 training loss: 82.48168792761862.          Total Reward: 6.0
Steps done: 435399        Epsilon: 0.010018550286285424
Episode 744 training loss: 65.96319310925901.          Total Reward: 0.0
Steps done: 435862        Epsilon: 0.010018336804630277
Episode 745 training loss: 77.99896985478699.          Total Reward: 9.0
Steps done: 436427        Epsilon: 0.010018079617922051
Episode 746 training loss: 65.23624088428915.          Total Reward: 1.0
Steps done: 436876        Epsilon: 0.010017877808982549
Episode 747 training loss: 97.17805239371955.          Total Reward: 16.0
Steps done: 437549        Epsilon: 0.010017579531145081
Episode 748 training loss: 75.00845469161868.          Total Reward: 4.0
Steps done: 438056        Epsilon: 0.010017358116765728
Episode 749 training loss: 109.91386247240007.          Total Reward: 28.0
Steps done: 438803        Epsilon: 0.010017036962050932
Episode 750 training loss: 66.21480137109756.          Total Reward: 3.0
Steps done: 439270        Epsilon: 0.010016839212130346
Episode 751 training loss: 68.03784301877022.          Total Reward: -8.0
Steps done: 439751        Epsilon: 0.010016637933219346
Episode 752 training loss: 107.26449697464705.          Total Reward: 28.0
Steps done: 440466        Epsilon: 0.010016343172435901
Episode 753 training loss: 72.58421554602683.          Total Reward: 6.0
Steps done: 440969        Epsilon: 0.010016138943821161
Episode 754 training loss: 81.38172397762537.          Total Reward: 9.0
Steps done: 441520        Epsilon: 0.010015918154050805
Episode 755 training loss: 75.89722839929163.          Total Reward: -1.0
Steps done: 442016        Epsilon: 0.01001572198768558
Episode 756 training loss: 142.45328070037067.          Total Reward: 30.0
Steps done: 442965        Epsilon: 0.010015353373503637
Episode 757 training loss: 90.74166246131063.          Total Reward: 4.0
Steps done: 443562        Epsilon: 0.010015125925953525
Episode 758 training loss: 78.29084058105946.          Total Reward: 7.0
Steps done: 444105        Epsilon: 0.010014921978931068
Episode 759 training loss: 119.99423791095614.          Total Reward: 22.0
Steps done: 444942        Epsilon: 0.010014612980690661
Episode 760 training loss: 70.42034614086151.          Total Reward: -1.0
Steps done: 445421        Epsilon: 0.010014439033832374
Episode 761 training loss: 88.04852648079395.          Total Reward: 6.0
Steps done: 445974        Epsilon: 0.010014240787723434
Episode 762 training loss: 162.217065744102.          Total Reward: 12.0
Steps done: 447047        Epsilon: 0.010013863856781425
Episode 763 training loss: 86.47628474608064.          Total Reward: 19.0
Steps done: 447624        Epsilon: 0.010013665306136744
Episode 764 training loss: 91.62197545915842.          Total Reward: 19.0
Steps done: 448303        Epsilon: 0.010013435295305127
Episode 765 training loss: 44.76153062470257.          Total Reward: -15.0
Steps done: 448636        Epsilon: 0.010013323910753207
Episode 766 training loss: 109.72500132583082.          Total Reward: 7.0
Steps done: 449345        Epsilon: 0.010013089825147422
Episode 767 training loss: 66.53228428214788.          Total Reward: -18.0
Steps done: 449776        Epsilon: 0.01001294953942804
Episode 768 training loss: 98.28800213523209.          Total Reward: 5.0
Steps done: 450415        Epsilon: 0.010012744314137139
Episode 769 training loss: 99.3697915636003.          Total Reward: 4.0
Steps done: 451039        Epsilon: 0.010012547045532307
Episode 770 training loss: 65.96081281080842.          Total Reward: -5.0
Steps done: 451466        Epsilon: 0.010012413818187368
Episode 771 training loss: 134.51395842432976.          Total Reward: 45.0
Steps done: 452368        Epsilon: 0.01001213701922486
Episode 772 training loss: 73.1235531065613.          Total Reward: -7.0
Steps done: 452859        Epsilon: 0.010011988947960484
Episode 773 training loss: 82.6830841191113.          Total Reward: 4.0
Steps done: 453366        Epsilon: 0.01001183794703504
Episode 774 training loss: 130.98046973347664.          Total Reward: 19.0
Steps done: 454203        Epsilon: 0.01001159281166655
Episode 775 training loss: 74.16251274012029.          Total Reward: 3.0
Steps done: 454704        Epsilon: 0.010011448517230683
Episode 776 training loss: 68.9719139393419.          Total Reward: -9.0
Steps done: 455153        Epsilon: 0.010011320726193772
Episode 777 training loss: 74.85225673764944.          Total Reward: 8.0
Steps done: 455636        Epsilon: 0.010011184850425882
Episode 778 training loss: 106.33698550611734.          Total Reward: 31.0
Steps done: 456345        Epsilon: 0.010010988345620645
Episode 779 training loss: 78.03249773010612.          Total Reward: -3.0
Steps done: 456828        Epsilon: 0.010010856459213933
Episode 780 training loss: 88.75230392813683.          Total Reward: 7.0
Steps done: 457353        Epsilon: 0.010010714899206455
Episode 781 training loss: 81.96188433282077.          Total Reward: 2.0
Steps done: 457896        Epsilon: 0.010010570427271593
Episode 782 training loss: 95.48486693203449.          Total Reward: 16.0
Steps done: 458475        Epsilon: 0.010010418522400661
Episode 783 training loss: 76.7939317021519.          Total Reward: 1.0
Steps done: 458950        Epsilon: 0.010010295534135247
Episode 784 training loss: 77.48319105431437.          Total Reward: -10.0
Steps done: 459405        Epsilon: 0.010010179085988898
Episode 785 training loss: 83.2260941453278.          Total Reward: 2.0
Steps done: 459922        Epsilon: 0.01001004836788798
Episode 786 training loss: 75.02975137531757.          Total Reward: -7.0
Steps done: 460369        Epsilon: 0.010009936702469425
Episode 787 training loss: 92.96202821284533.          Total Reward: -4.0
Steps done: 460934        Epsilon: 0.010009797333159981
Episode 788 training loss: 99.24830062128603.          Total Reward: 13.0
Steps done: 461513        Epsilon: 0.010009656538224174
Episode 789 training loss: 67.07663281168789.          Total Reward: -10.0
Steps done: 461908        Epsilon: 0.010009561649194889
Episode 790 training loss: 58.8221439011395.          Total Reward: -11.0
Steps done: 462261        Epsilon: 0.010009477638881482
Episode 791 training loss: 89.8477091640234.          Total Reward: 9.0
Steps done: 462780        Epsilon: 0.010009355460860962
Episode 792 training loss: 109.15316291712224.          Total Reward: 11.0
Steps done: 463425        Epsilon: 0.010009205813826328
Episode 793 training loss: 76.27213294245303.          Total Reward: -9.0
Steps done: 463832        Epsilon: 0.010009112619600306
Episode 794 training loss: 109.34989237226546.          Total Reward: 12.0
Steps done: 464398        Epsilon: 0.01000898458402098
Episode 795 training loss: 107.69259906932712.          Total Reward: -4.0
Steps done: 464993        Epsilon: 0.010008851927413208
Episode 796 training loss: 126.02090892195702.          Total Reward: 15.0
Steps done: 465719        Epsilon: 0.010008692714161594
Episode 797 training loss: 84.36315352097154.          Total Reward: -7.0
Steps done: 466200        Epsilon: 0.010008588810248124
Episode 798 training loss: 93.95101981796324.          Total Reward: 0.0
Steps done: 466723        Epsilon: 0.010008477242517593
Episode 799 training loss: 103.21383220143616.          Total Reward: 13.0
Steps done: 467352        Epsilon: 0.010008344980514422
Beginning to save execution
-------------------------------------------------------------
Target_net saved to target_neth.pth
Policy_net saved to policy_net.pth
Replay memory saved to replay_memory.pkl
Hyperparameters saved to hyperparameters.pkl
Figure plotted to Rewards_Plot.png
Finished saving execution to previous_run/
-------------------------------------------------------------
Episode 800 training loss: 96.6531034167856.          Total Reward: 2.0
Steps done: 467963        Epsilon: 0.010008218479547847
Episode 801 training loss: 87.20038817916065.          Total Reward: 1.0
Steps done: 468470        Epsilon: 0.010008114967711649
Episode 802 training loss: 117.83677744306624.          Total Reward: 23.0
Steps done: 469217        Epsilon: 0.010007964826992113
Episode 803 training loss: 96.61495459266007.          Total Reward: 13.0
Steps done: 469800        Epsilon: 0.01000784958153014
Episode 804 training loss: 108.85633214376867.          Total Reward: 19.0
Steps done: 470481        Epsilon: 0.010007717073579132
Episode 805 training loss: 92.73766854964197.          Total Reward: 16.0
Steps done: 471099        Epsilon: 0.010007598761109609
Episode 806 training loss: 93.9713825872168.          Total Reward: 12.0
Steps done: 471650        Epsilon: 0.010007494805811234
Episode 807 training loss: 70.70958003774285.          Total Reward: 7.0
Steps done: 472137        Epsilon: 0.01000740410978288
Episode 808 training loss: 83.21445897128433.          Total Reward: -8.0
Steps done: 472648        Epsilon: 0.010007310123893482
Episode 809 training loss: 92.84762118756771.          Total Reward: 22.0
Steps done: 473261        Epsilon: 0.010007198950288367
Episode 810 training loss: 147.3363697817549.          Total Reward: 32.0
Steps done: 474238        Epsilon: 0.010007025245927713
Episode 811 training loss: 82.91584447585046.          Total Reward: 8.0
Steps done: 474829        Epsilon: 0.0100069222109643
Episode 812 training loss: 71.5523564722389.          Total Reward: 4.0
Steps done: 475334        Epsilon: 0.010006835367404349
Episode 813 training loss: 112.27789669111371.          Total Reward: 23.0
Steps done: 476153        Epsilon: 0.010006696836308454
Episode 814 training loss: 105.81258089002222.          Total Reward: 30.0
Steps done: 476888        Epsilon: 0.010006574905610287
Episode 815 training loss: 103.4679193161428.          Total Reward: 13.0
Steps done: 477611        Epsilon: 0.010006457131778813
Episode 816 training loss: 104.70742118358612.          Total Reward: 32.0
Steps done: 478302        Epsilon: 0.010006346542789927
Episode 817 training loss: 91.62279201671481.          Total Reward: 17.0
Steps done: 478955        Epsilon: 0.01000624377659029
Episode 818 training loss: 84.55717246234417.          Total Reward: 16.0
Steps done: 479526        Epsilon: 0.010006155279827891
Episode 819 training loss: 98.39259489253163.          Total Reward: 12.0
Steps done: 480223        Epsilon: 0.010006048953138494
Episode 820 training loss: 115.82641116715968.          Total Reward: 17.0
Steps done: 481000        Epsilon: 0.01000593258609771
Episode 821 training loss: 66.60356942750514.          Total Reward: 2.0
Steps done: 481481        Epsilon: 0.010005861673963584
Episode 822 training loss: 95.51268295198679.          Total Reward: -1.0
Steps done: 482120        Epsilon: 0.01000576877770646
Episode 823 training loss: 77.7346604410559.          Total Reward: 5.0
Steps done: 482659        Epsilon: 0.010005691564817036
Episode 824 training loss: 80.68076705187559.          Total Reward: 11.0
Steps done: 483246        Epsilon: 0.010005608650971679
Episode 825 training loss: 72.89475186355412.          Total Reward: 3.0
Steps done: 483741        Epsilon: 0.010005539671606022
Episode 826 training loss: 89.35644977539778.          Total Reward: 18.0
Steps done: 484362        Epsilon: 0.010005454332364274
Episode 827 training loss: 80.91425890661776.          Total Reward: -1.0
Steps done: 484889        Epsilon: 0.010005382942846473
Episode 828 training loss: 71.16996612027287.          Total Reward: 4.0
Steps done: 485362        Epsilon: 0.010005319664418373
Episode 829 training loss: 79.6969165597111.          Total Reward: 15.0
Steps done: 485893        Epsilon: 0.010005249512536545
Episode 830 training loss: 88.66812573932111.          Total Reward: 20.0
Steps done: 486500        Epsilon: 0.01000517045256847
Episode 831 training loss: 110.69769925251603.          Total Reward: 22.0
Steps done: 487203        Epsilon: 0.010005080375733338
Episode 832 training loss: 80.16623683087528.          Total Reward: 8.0
Steps done: 487710        Epsilon: 0.010005016388347634
Episode 833 training loss: 145.30466482415795.          Total Reward: 28.0
Steps done: 488659        Epsilon: 0.010004898775236363
Episode 834 training loss: 83.66263440810144.          Total Reward: 9.0
Steps done: 489220        Epsilon: 0.010004830549465228
Episode 835 training loss: 97.59951939433813.          Total Reward: 20.0
Steps done: 489857        Epsilon: 0.010004754232253657
Episode 836 training loss: 83.99930776841938.          Total Reward: 5.0
Steps done: 490372        Epsilon: 0.010004693413871854
Episode 837 training loss: 95.37295318953693.          Total Reward: 21.0
Steps done: 490986        Epsilon: 0.010004621920087506
Episode 838 training loss: 78.4239581245929.          Total Reward: 12.0
Steps done: 491499        Epsilon: 0.010004563022450771
Episode 839 training loss: 85.2417031954974.          Total Reward: 17.0
Steps done: 492082        Epsilon: 0.010004496998715307
Episode 840 training loss: 105.39582461304963.          Total Reward: 19.0
Steps done: 492747        Epsilon: 0.010004422854146128
Episode 841 training loss: 94.1046877335757.          Total Reward: 9.0
Steps done: 493322        Epsilon: 0.010004359730406644
Episode 842 training loss: 87.64061455614865.          Total Reward: 13.0
Steps done: 493879        Epsilon: 0.010004299441893691
Episode 843 training loss: 84.42368260025978.          Total Reward: 4.0
Steps done: 494405        Epsilon: 0.010004243274343813
Episode 844 training loss: 130.60239707678556.          Total Reward: 30.0
Steps done: 495228        Epsilon: 0.010004156860999895
Episode 845 training loss: 168.12538920901716.          Total Reward: 20.0
Steps done: 496337        Epsilon: 0.010004043195004465
Episode 846 training loss: 101.45627389103174.          Total Reward: 7.0
Steps done: 497032        Epsilon: 0.010003973551273233
Episode 847 training loss: 113.67493694834411.          Total Reward: 25.0
Steps done: 497809        Epsilon: 0.010003897109880403
Episode 848 training loss: 106.57105858623981.          Total Reward: 10.0
Steps done: 498554        Epsilon: 0.010003825197967357
Episode 849 training loss: 75.17234861664474.          Total Reward: 11.0
Steps done: 499059        Epsilon: 0.010003777208414492
Episode 850 training loss: 72.50300935097039.          Total Reward: 16.0
Steps done: 499546        Epsilon: 0.010003731499718352
Episode 851 training loss: 107.46760681085289.          Total Reward: 21.0
Steps done: 500275        Epsilon: 0.01000366410909832
Episode 852 training loss: 58.003656420856714.          Total Reward: -13.0
Steps done: 500664        Epsilon: 0.010003628648344729
Episode 853 training loss: 102.0721460338682.          Total Reward: 23.0
Steps done: 501313        Epsilon: 0.010003570248574614
Episode 854 training loss: 94.45080680027604.          Total Reward: 10.0
Steps done: 501930        Epsilon: 0.010003515600050633
Episode 855 training loss: 72.85273398086429.          Total Reward: 13.0
Steps done: 502405        Epsilon: 0.010003474099199026
Episode 856 training loss: 109.93928472884.          Total Reward: 19.0
Steps done: 503066        Epsilon: 0.010003417161453572
Episode 857 training loss: 83.03714735619724.          Total Reward: 13.0
Steps done: 503599        Epsilon: 0.010003371929802338
Episode 858 training loss: 75.38208251260221.          Total Reward: 6.0
Steps done: 504070        Epsilon: 0.010003332458174188
Episode 859 training loss: 146.33250951953232.          Total Reward: 38.0
Steps done: 505033        Epsilon: 0.010003253187295629
Episode 860 training loss: 122.03612857684493.          Total Reward: 34.0
Steps done: 505794        Epsilon: 0.010003191880437974
Episode 861 training loss: 95.47400110960007.          Total Reward: 12.0
Steps done: 506395        Epsilon: 0.010003144280921228
Episode 862 training loss: 100.89753162302077.          Total Reward: 17.0
Steps done: 506968        Epsilon: 0.010003099560174126
Episode 863 training loss: 100.76787094771862.          Total Reward: 14.0
Steps done: 507557        Epsilon: 0.010003054253539295
Episode 864 training loss: 102.75181554444134.          Total Reward: 21.0
Steps done: 508160        Epsilon: 0.010003008555977973
Episode 865 training loss: 130.05040582455695.          Total Reward: 19.0
Steps done: 508913        Epsilon: 0.010002952449669224
Episode 866 training loss: 112.80347179435194.          Total Reward: 19.0
Steps done: 509564        Epsilon: 0.010002904787454175
Episode 867 training loss: 138.89557179622352.          Total Reward: 28.0
Steps done: 510395        Epsilon: 0.010002845063030343
Episode 868 training loss: 111.47673818655312.          Total Reward: 12.0
Steps done: 511078        Epsilon: 0.010002796895975606
Episode 869 training loss: 101.31328084506094.          Total Reward: 26.0
Steps done: 511693        Epsilon: 0.010002754222592244
Episode 870 training loss: 99.04292185790837.          Total Reward: 9.0
Steps done: 512298        Epsilon: 0.010002712878428946
Episode 871 training loss: 86.73617283441126.          Total Reward: 1.0
Steps done: 512832        Epsilon: 0.01000267690217771
Episode 872 training loss: 121.47346442192793.          Total Reward: 17.0
Steps done: 513588        Epsilon: 0.010002626783836762
Episode 873 training loss: 94.98302018083632.          Total Reward: 14.0
Steps done: 514193        Epsilon: 0.01000258735268105
Episode 874 training loss: 92.07358418405056.          Total Reward: 4.0
Steps done: 514784        Epsilon: 0.010002549405569792
Episode 875 training loss: 62.64846792072058.          Total Reward: -17.0
Steps done: 515161        Epsilon: 0.01000252549030004
Episode 876 training loss: 92.14334565587342.          Total Reward: 9.0
Steps done: 515724        Epsilon: 0.01000249019301145
Episode 877 training loss: 71.95410614088178.          Total Reward: -10.0
Steps done: 516155        Epsilon: 0.010002463505220431
Episode 878 training loss: 67.57388851046562.          Total Reward: -10.0
Steps done: 516568        Epsilon: 0.01000243820039002
Episode 879 training loss: 180.92500698938966.          Total Reward: 53.0
Steps done: 517675        Epsilon: 0.010002371648355662
Episode 880 training loss: 113.44156916998327.          Total Reward: 25.0
Steps done: 518350        Epsilon: 0.010002331962580149
Episode 881 training loss: 148.72210558317602.          Total Reward: 29.0
Steps done: 519258        Epsilon: 0.010002279623327568
Episode 882 training loss: 124.73307963088155.          Total Reward: 14.0
Steps done: 520087        Epsilon: 0.010002232864347703
Episode 883 training loss: 98.39022772759199.          Total Reward: 7.0
Steps done: 520714        Epsilon: 0.010002198137085028
Episode 884 training loss: 77.78326543979347.          Total Reward: 2.0
Steps done: 521203        Epsilon: 0.010002171428448338
Episode 885 training loss: 108.70437500067055.          Total Reward: 14.0
Steps done: 521888        Epsilon: 0.010002134559329029
Episode 886 training loss: 102.37732444144785.          Total Reward: 8.0
Steps done: 522561        Epsilon: 0.01000209894580719
Episode 887 training loss: 72.46578200906515.          Total Reward: 3.0
Steps done: 523050        Epsilon: 0.010002073442401886
Episode 888 training loss: 85.98521615378559.          Total Reward: 6.0
Steps done: 523607        Epsilon: 0.010002044769812656
Episode 889 training loss: 99.83972232416272.          Total Reward: 21.0
Steps done: 524278        Epsilon: 0.010002010754896803
Episode 890 training loss: 82.3337189592421.          Total Reward: 7.0
Steps done: 524829        Epsilon: 0.01000198324664615
Episode 891 training loss: 126.51999898254871.          Total Reward: 34.0
Steps done: 525636        Epsilon: 0.010001943635565409
Episode 892 training loss: 73.66188113205135.          Total Reward: 5.0
Steps done: 526155        Epsilon: 0.010001918579794771
Episode 893 training loss: 73.79590286314487.          Total Reward: 7.0
Steps done: 526672        Epsilon: 0.010001893941717492
Episode 894 training loss: 62.28836129233241.          Total Reward: 3.0
Steps done: 527123        Epsilon: 0.010001872707457718
Episode 895 training loss: 71.81100613623857.          Total Reward: 4.0
Steps done: 527598        Epsilon: 0.010001850600576052
Episode 896 training loss: 77.7288205223158.          Total Reward: 6.0
Steps done: 528121        Epsilon: 0.010001826561471631
Episode 897 training loss: 74.66495647467673.          Total Reward: 2.0
Steps done: 528632        Epsilon: 0.010001803375564144
Episode 898 training loss: 134.8433311600238.          Total Reward: 22.0
Steps done: 529475        Epsilon: 0.010001765767115152
Episode 899 training loss: 97.01923159882426.          Total Reward: 15.0
Steps done: 530120        Epsilon: 0.010001737522454994
Beginning to save execution
-------------------------------------------------------------
Target_net saved to target_neth.pth
Policy_net saved to policy_net.pth
Replay memory saved to replay_memory.pkl
Hyperparameters saved to hyperparameters.pkl
Figure plotted to Rewards_Plot.png
Finished saving execution to previous_run/
-------------------------------------------------------------
Episode 900 training loss: 83.02913420181721.          Total Reward: 1.0
Steps done: 530663        Epsilon: 0.010001714094961547
Episode 901 training loss: 85.94424282759428.          Total Reward: 4.0
Steps done: 531181        Epsilon: 0.010001692040542375
Episode 902 training loss: 105.00034494139254.          Total Reward: 17.0
Steps done: 531824        Epsilon: 0.010001665058440325
Episode 903 training loss: 94.09593294002116.          Total Reward: 24.0
Steps done: 532425        Epsilon: 0.01000164022794349
Episode 904 training loss: 89.40112055465579.          Total Reward: 11.0
Steps done: 533004        Epsilon: 0.010001616656652789
Episode 905 training loss: 93.04349457845092.          Total Reward: 8.0
Steps done: 533585        Epsilon: 0.010001593344429785
Episode 906 training loss: 84.75374859198928.          Total Reward: -5.0
Steps done: 534152        Epsilon: 0.010001570918094652
Episode 907 training loss: 103.26218709722161.          Total Reward: 11.0
Steps done: 534859        Epsilon: 0.010001543396059812
Episode 908 training loss: 88.84295578952879.          Total Reward: 10.0
Steps done: 535416        Epsilon: 0.010001522053214116
Episode 909 training loss: 70.2453479822725.          Total Reward: -5.0
Steps done: 535845        Epsilon: 0.010001505816418847
Episode 910 training loss: 101.1694713961333.          Total Reward: 10.0
Steps done: 536478        Epsilon: 0.010001482174434606
Episode 911 training loss: 84.38680118881166.          Total Reward: 13.0
Steps done: 537007        Epsilon: 0.010001462701724816
Episode 912 training loss: 71.68397921696305.          Total Reward: -2.0
Steps done: 537432        Epsilon: 0.010001447242790012
Episode 913 training loss: 76.49418132007122.          Total Reward: 7.0
Steps done: 537921        Epsilon: 0.010001429657953224
Episode 914 training loss: 99.47858845070004.          Total Reward: 22.0
Steps done: 538552        Epsilon: 0.010001407282052946
Episode 915 training loss: 67.85157183557749.          Total Reward: 8.0
Steps done: 539005        Epsilon: 0.010001391434489899
Episode 916 training loss: 72.45744726806879.          Total Reward: 4.0
Steps done: 539432        Epsilon: 0.010001376659926257
Episode 917 training loss: 107.22101010382175.          Total Reward: 31.0
Steps done: 540099        Epsilon: 0.010001353894456593
Episode 918 training loss: 109.92329607717693.          Total Reward: 21.0
Steps done: 540766        Epsilon: 0.01000133150545362
Episode 919 training loss: 77.86001744493842.          Total Reward: 14.0
Steps done: 541251        Epsilon: 0.010001315458431663
Episode 920 training loss: 88.73253984563053.          Total Reward: 0.0
Steps done: 541796        Epsilon: 0.010001297656859134
Episode 921 training loss: 95.11528496444225.          Total Reward: 12.0
Steps done: 542367        Epsilon: 0.010001279264396003
Episode 922 training loss: 84.20825003273785.          Total Reward: 12.0
Steps done: 542856        Epsilon: 0.010001263720593838
Episode 923 training loss: 84.89012389630079.          Total Reward: 11.0
Steps done: 543403        Epsilon: 0.010001246556839365
Episode 924 training loss: 93.31343876942992.          Total Reward: 13.0
Steps done: 543954        Epsilon: 0.010001229503245192
Episode 925 training loss: 108.93331324122846.          Total Reward: 23.0
Steps done: 544605        Epsilon: 0.010001209655032811
Episode 926 training loss: 120.27087607327849.          Total Reward: 21.0
Steps done: 545298        Epsilon: 0.010001188878257867
Episode 927 training loss: 128.11034546233714.          Total Reward: 19.0
Steps done: 546085        Epsilon: 0.010001165715687125
Episode 928 training loss: 120.07144741714.          Total Reward: 29.0
Steps done: 546848        Epsilon: 0.010001143690394454
Episode 929 training loss: 126.70579440146685.          Total Reward: 34.0
Steps done: 547680        Epsilon: 0.01000112014733091
Episode 930 training loss: 92.54523860290647.          Total Reward: 23.0
Steps done: 548293        Epsilon: 0.010001103111940149
Episode 931 training loss: 125.67212976701558.          Total Reward: 31.0
Steps done: 549148        Epsilon: 0.010001079783137228
Episode 932 training loss: 107.18483344838023.          Total Reward: 35.0
Steps done: 549875        Epsilon: 0.010001060335345861
Episode 933 training loss: 142.69062069058418.          Total Reward: 26.0
Steps done: 550918        Epsilon: 0.010001033044452986
Episode 934 training loss: 86.05212818458676.          Total Reward: 9.0
Steps done: 551567        Epsilon: 0.01000101641854911
Episode 935 training loss: 125.64744219556451.          Total Reward: 25.0
Steps done: 552528        Epsilon: 0.010000992290097066
Episode 936 training loss: 100.17185843363404.          Total Reward: 25.0
Steps done: 553305        Epsilon: 0.010000973200866327
Episode 937 training loss: 109.85990233067423.          Total Reward: 23.0
Steps done: 554156        Epsilon: 0.01000095271471207
Episode 938 training loss: 47.999674120917916.          Total Reward: -12.0
Steps done: 554561        Epsilon: 0.010000943117145283
Episode 939 training loss: 61.41072849743068.          Total Reward: 4.0
Steps done: 555062        Epsilon: 0.010000931378271198
Episode 940 training loss: 70.0181471221149.          Total Reward: 10.0
Steps done: 555647        Epsilon: 0.010000917855986712
Episode 941 training loss: 104.14100734516978.          Total Reward: 23.0
Steps done: 556422        Epsilon: 0.01000090024369698
Episode 942 training loss: 83.30368192493916.          Total Reward: 10.0
Steps done: 557025        Epsilon: 0.01000088677430388
Episode 943 training loss: 77.68539820425212.          Total Reward: 14.0
Steps done: 557610        Epsilon: 0.0100008738996054
Episode 944 training loss: 87.84305189736187.          Total Reward: 19.0
Steps done: 558247        Epsilon: 0.010000860092981213
Episode 945 training loss: 63.97048327885568.          Total Reward: 3.0
Steps done: 558706        Epsilon: 0.010000850279824917
Episode 946 training loss: 75.69822693616152.          Total Reward: 9.0
Steps done: 559231        Epsilon: 0.010000839192819844
Episode 947 training loss: 93.10955746285617.          Total Reward: 16.0
Steps done: 559944        Epsilon: 0.010000824366737843
Episode 948 training loss: 60.80901147052646.          Total Reward: 0.0
Steps done: 560373        Epsilon: 0.010000815572647186
Episode 949 training loss: 100.72018411755562.          Total Reward: 23.0
Steps done: 561080        Epsilon: 0.010000801284048125
Episode 950 training loss: 82.59773480892181.          Total Reward: 18.0
Steps done: 561643        Epsilon: 0.010000790084973519
Episode 951 training loss: 90.7764564435929.          Total Reward: 19.0
Steps done: 562248        Epsilon: 0.010000778224856528
Episode 952 training loss: 70.72569052688777.          Total Reward: -2.0
Steps done: 562695        Epsilon: 0.010000769576605856
Episode 953 training loss: 89.2971970885992.          Total Reward: 17.0
Steps done: 563300        Epsilon: 0.010000758024343902
Episode 954 training loss: 117.85972655378282.          Total Reward: 39.0
Steps done: 564073        Epsilon: 0.010000743516160291
Episode 955 training loss: 78.23076371848583.          Total Reward: 2.0
Steps done: 564604        Epsilon: 0.010000733711207627
Episode 956 training loss: 143.31943092681468.          Total Reward: 25.0
Steps done: 565511        Epsilon: 0.010000717261509253
Episode 957 training loss: 104.04126296099275.          Total Reward: 22.0
Steps done: 566195        Epsilon: 0.010000705100609466
Episode 958 training loss: 99.59403424151242.          Total Reward: 27.0
Steps done: 566888        Epsilon: 0.010000692989952892
Episode 959 training loss: 88.75913503207266.          Total Reward: 6.0
Steps done: 567485        Epsilon: 0.01000068272387899
Episode 960 training loss: 95.61662448197603.          Total Reward: 26.0
Steps done: 568114        Epsilon: 0.010000672072015762
Episode 961 training loss: 106.14640894904733.          Total Reward: 17.0
Steps done: 568817        Epsilon: 0.010000660363539693
Episode 962 training loss: 82.48299508169293.          Total Reward: 8.0
Steps done: 569346        Epsilon: 0.010000651687727142
Episode 963 training loss: 83.02799507509917.          Total Reward: 16.0
Steps done: 569885        Epsilon: 0.010000642965135463
Episode 964 training loss: 73.35392338782549.          Total Reward: 2.0
Steps done: 570350        Epsilon: 0.010000635533943257
Episode 965 training loss: 113.00763712264597.          Total Reward: 17.0
Steps done: 571077        Epsilon: 0.010000624087448947
Episode 966 training loss: 82.90055923350155.          Total Reward: 11.0
Steps done: 571600        Epsilon: 0.010000615980619442
Episode 967 training loss: 86.02808286808431.          Total Reward: 4.0
Steps done: 572173        Epsilon: 0.010000607219597703
Episode 968 training loss: 83.64691979251802.          Total Reward: 14.0
Steps done: 572716        Epsilon: 0.010000599032288754
Episode 969 training loss: 78.15155735611916.          Total Reward: 6.0
Steps done: 573239        Epsilon: 0.010000591250923112
Episode 970 training loss: 94.6415903866291.          Total Reward: 7.0
Steps done: 573830        Epsilon: 0.01000058257940928
Episode 971 training loss: 99.70878290012479.          Total Reward: 4.0
Steps done: 574435        Epsilon: 0.010000573834198091
Episode 972 training loss: 167.75471741333604.          Total Reward: 41.0
Steps done: 575457        Epsilon: 0.010000559358449493
Episode 973 training loss: 94.42295288853347.          Total Reward: 17.0
Steps done: 576048        Epsilon: 0.010000551154682968
Episode 974 training loss: 70.79225384630263.          Total Reward: 1.0
Steps done: 576499        Epsilon: 0.010000544975315563
Episode 975 training loss: 100.78420444577932.          Total Reward: 13.0
Steps done: 577116        Epsilon: 0.01000053663357241
Episode 976 training loss: 85.40831905417144.          Total Reward: 3.0
Steps done: 577667        Epsilon: 0.010000529292125254
Episode 977 training loss: 108.14840290881693.          Total Reward: 26.0
Steps done: 578394        Epsilon: 0.010000519759134352
Episode 978 training loss: 90.59957738406956.          Total Reward: 5.0
Steps done: 578949        Epsilon: 0.010000512597276648
Episode 979 training loss: 92.97125626541674.          Total Reward: 5.0
Steps done: 579512        Epsilon: 0.0100005054330068
Episode 980 training loss: 167.0279510654509.          Total Reward: 49.0
Steps done: 580647        Epsilon: 0.010000491292906621
Episode 981 training loss: 78.1953613916412.          Total Reward: 12.0
Steps done: 581164        Epsilon: 0.010000484983806197
Episode 982 training loss: 71.16254971921444.          Total Reward: 6.0
Steps done: 581661        Epsilon: 0.010000478995163889
Episode 983 training loss: 66.33376712910831.          Total Reward: 4.0
Steps done: 582118        Epsilon: 0.010000473553787194
Episode 984 training loss: 87.68937516584992.          Total Reward: 6.0
Steps done: 582691        Epsilon: 0.010000466818485964
Episode 985 training loss: 134.05670123174787.          Total Reward: 30.0
Steps done: 583534        Epsilon: 0.01000045708323194
Episode 986 training loss: 86.81179635319859.          Total Reward: 15.0
Steps done: 584118        Epsilon: 0.010000450458296463
Episode 987 training loss: 114.35422612540424.          Total Reward: 7.0
Steps done: 584868        Epsilon: 0.01000044209089295
Episode 988 training loss: 94.41594380326569.          Total Reward: 19.0
Steps done: 585471        Epsilon: 0.010000435476355082
Episode 989 training loss: 73.64396491833031.          Total Reward: 1.0
Steps done: 585954        Epsilon: 0.010000430249598147
Episode 990 training loss: 80.74270795844495.          Total Reward: 4.0
Steps done: 586467        Epsilon: 0.01000042476688013
Episode 991 training loss: 86.72351426072419.          Total Reward: 2.0
Steps done: 587004        Epsilon: 0.010000419102492044
Episode 992 training loss: 96.1711870227009.          Total Reward: 14.0
Steps done: 587579        Epsilon: 0.010000413120988778
Episode 993 training loss: 81.8170352447778.          Total Reward: 3.0
Steps done: 588108        Epsilon: 0.010000407693432523
Episode 994 training loss: 114.28903333097696.          Total Reward: 23.0
Steps done: 588805        Epsilon: 0.010000400650910625
Episode 995 training loss: 97.14024278894067.          Total Reward: 15.0
Steps done: 589396        Epsilon: 0.01000039477481001
Episode 996 training loss: 83.3883687723428.          Total Reward: 0.0
Steps done: 589961        Epsilon: 0.01000038923781292
Episode 997 training loss: 85.32973208650947.          Total Reward: 16.0
Steps done: 590512        Epsilon: 0.010000383912822123
Episode 998 training loss: 93.45090611092746.          Total Reward: 24.0
Steps done: 591100        Epsilon: 0.010000378310580992
Episode 999 training loss: 114.59013306070119.          Total Reward: 24.0
Steps done: 591859        Epsilon: 0.010000371199814468
Beginning to save execution
-------------------------------------------------------------
Target_net saved to target_neth.pth
Policy_net saved to policy_net.pth
Replay memory saved to replay_memory.pkl
Hyperparameters saved to hyperparameters.pkl
Figure plotted to Rewards_Plot.png
Finished saving execution to previous_run/
-------------------------------------------------------------
Episode 1000 training loss: 93.22070578485727.          Total Reward: 27.0
Steps done: 592513        Epsilon: 0.010000365180043231
Episode 1001 training loss: 84.90703643672168.          Total Reward: -2.0
Steps done: 593050        Epsilon: 0.010000360310262694
Episode 1002 training loss: 113.55630926787853.          Total Reward: 23.0
Steps done: 593795        Epsilon: 0.010000353661591993
Episode 1003 training loss: 106.29559215344489.          Total Reward: 22.0
Steps done: 594457        Epsilon: 0.010000347856660947
Episode 1004 training loss: 159.72051679342985.          Total Reward: 25.0
Steps done: 595508        Epsilon: 0.010000338835758267
Episode 1005 training loss: 56.88207824528217.          Total Reward: -10.0
Steps done: 595915        Epsilon: 0.010000335405585028
Episode 1006 training loss: 85.2712732013315.          Total Reward: 1.0
Steps done: 596442        Epsilon: 0.01000033101559898
Episode 1007 training loss: 106.76163653098047.          Total Reward: 27.0
Steps done: 597199        Epsilon: 0.010000324810034138
Episode 1008 training loss: 123.95891791861504.          Total Reward: 26.0
Steps done: 598046        Epsilon: 0.010000318004489655
Episode 1009 training loss: 60.6999248676002.          Total Reward: -7.0
Steps done: 598491        Epsilon: 0.010000314486295946
Episode 1010 training loss: 72.70528183784336.          Total Reward: 10.0
Steps done: 599034        Epsilon: 0.010000310245990667
Episode 1011 training loss: 77.82023856043816.          Total Reward: 0.0
Steps done: 599571        Epsilon: 0.010000306108771465
Episode 1012 training loss: 71.32315673306584.          Total Reward: -12.0
Steps done: 600082        Epsilon: 0.010000302223104452
Episode 1013 training loss: 73.58377806656063.          Total Reward: 1.0
Steps done: 600547        Epsilon: 0.010000298730103269
Episode 1014 training loss: 101.0819536857307.          Total Reward: 6.0
Steps done: 601244        Epsilon: 0.01000029356982075
Episode 1015 training loss: 76.33114246465266.          Total Reward: 1.0
Steps done: 601773        Epsilon: 0.010000289712919842
Episode 1016 training loss: 75.38286292273551.          Total Reward: -4.0
Steps done: 602276        Epsilon: 0.010000286092590403
Episode 1017 training loss: 78.03793185576797.          Total Reward: 7.0
Steps done: 602797        Epsilon: 0.010000282390397285
Episode 1018 training loss: 123.55079037789255.          Total Reward: 38.0
Steps done: 603618        Epsilon: 0.0100002766534116
Episode 1019 training loss: 104.97813311591744.          Total Reward: 17.0
Steps done: 604313        Epsilon: 0.010000271888077299
Episode 1020 training loss: 119.24087022803724.          Total Reward: 14.0
Steps done: 605102        Epsilon: 0.010000266577631426
Episode 1021 training loss: 85.67362495884299.          Total Reward: -2.0
Steps done: 605653        Epsilon: 0.010000262930700457
Episode 1022 training loss: 99.97486116550863.          Total Reward: 12.0
Steps done: 606323        Epsilon: 0.010000258563290393
Episode 1023 training loss: 81.91353948134929.          Total Reward: 7.0
Steps done: 606884        Epsilon: 0.010000254962251558
Episode 1024 training loss: 80.38652620650828.          Total Reward: 0.0
Steps done: 607425        Epsilon: 0.010000251537101892
Episode 1025 training loss: 79.66524367779493.          Total Reward: 2.0
Steps done: 607940        Epsilon: 0.010000248319320622
Episode 1026 training loss: 98.62148636393249.          Total Reward: 10.0
Steps done: 608577        Epsilon: 0.010000244396156545
Episode 1027 training loss: 79.76733217854053.          Total Reward: 6.0
Steps done: 609112        Epsilon: 0.010000241149120908
Episode 1028 training loss: 134.2829795908183.          Total Reward: 42.0
Steps done: 610041        Epsilon: 0.010000235612969977
Episode 1029 training loss: 103.61053623259068.          Total Reward: 30.0
Steps done: 610786        Epsilon: 0.010000231265291842
Episode 1030 training loss: 74.94361061789095.          Total Reward: 12.0
Steps done: 611279        Epsilon: 0.010000228432440429
Episode 1031 training loss: 79.95734136644751.          Total Reward: 4.0
Steps done: 611854        Epsilon: 0.010000225172213122
Episode 1032 training loss: 77.61018212139606.          Total Reward: 11.0
Steps done: 612457        Epsilon: 0.01000022180319975
Episode 1033 training loss: 59.93839403241873.          Total Reward: 0.0
Steps done: 612878        Epsilon: 0.010000219480963279
Episode 1034 training loss: 100.64161082170904.          Total Reward: 17.0
Steps done: 613547        Epsilon: 0.010000215840670968
Episode 1035 training loss: 76.1120799575001.          Total Reward: 3.0
Steps done: 614120        Epsilon: 0.010000212770793849
Episode 1036 training loss: 100.7758244201541.          Total Reward: 26.0
Steps done: 614833        Epsilon: 0.0100002090117564
Episode 1037 training loss: 77.33571843802929.          Total Reward: 2.0
Steps done: 615378        Epsilon: 0.010000206183283943
Episode 1038 training loss: 97.50828299671412.          Total Reward: 31.0
Steps done: 616083        Epsilon: 0.010000202581140698
Episode 1039 training loss: 71.263652542606.          Total Reward: 10.0
Steps done: 616612        Epsilon: 0.010000199919643057
Episode 1040 training loss: 73.54489141143858.          Total Reward: 12.0
Steps done: 617131        Epsilon: 0.010000197342441439
Episode 1041 training loss: 74.28784859925508.          Total Reward: 9.0
Steps done: 617618        Epsilon: 0.010000194954364135
Episode 1042 training loss: 76.28153039515018.          Total Reward: 5.0
Steps done: 618113        Epsilon: 0.010000192556670208
Episode 1043 training loss: 60.59677536226809.          Total Reward: -7.0
Steps done: 618516        Epsilon: 0.01000019062640181
Episode 1044 training loss: 77.48112346231937.          Total Reward: 9.0
Steps done: 619031        Epsilon: 0.01000018818781895
Episode 1045 training loss: 74.29016874171793.          Total Reward: 6.0
Steps done: 619522        Epsilon: 0.010000185891933298
Episode 1046 training loss: 91.49032749421895.          Total Reward: 3.0
Steps done: 620107        Epsilon: 0.010000183193047482
Episode 1047 training loss: 89.23117637448013.          Total Reward: 5.0
Steps done: 620678        Epsilon: 0.01000018059654337
Episode 1048 training loss: 87.80130921676755.          Total Reward: 12.0
Steps done: 621207        Epsilon: 0.010000178223877915
Episode 1049 training loss: 96.53010487556458.          Total Reward: 22.0
Steps done: 621785        Epsilon: 0.010000175667060376
Episode 1050 training loss: 125.13638600707054.          Total Reward: 23.0
Steps done: 622530        Epsilon: 0.010000172425541722
Episode 1051 training loss: 68.96785836666822.          Total Reward: -9.0
Steps done: 622967        Epsilon: 0.010000170552045287
Episode 1052 training loss: 71.0376479877159.          Total Reward: 3.0
Steps done: 623406        Epsilon: 0.010000168690470667
Episode 1053 training loss: 80.79743070993572.          Total Reward: 6.0
Steps done: 623871        Epsilon: 0.010000166740798372
Episode 1054 training loss: 68.03867694362998.          Total Reward: 0.0
Steps done: 624294        Epsilon: 0.010000164986805015
Episode 1055 training loss: 115.05574033036828.          Total Reward: 22.0
Steps done: 625015        Epsilon: 0.0100001620395597
Episode 1056 training loss: 173.14944959059358.          Total Reward: 34.0
Steps done: 626106        Epsilon: 0.010000157679659135
Episode 1057 training loss: 78.31037771049887.          Total Reward: 4.0
Steps done: 626597        Epsilon: 0.010000155755972103
Episode 1058 training loss: 75.9885932393372.          Total Reward: 4.0
Steps done: 627096        Epsilon: 0.01000015382498592
Episode 1059 training loss: 120.59577514510602.          Total Reward: 25.0
Steps done: 627837        Epsilon: 0.010000151001610315
Episode 1060 training loss: 124.1565355239436.          Total Reward: 25.0
Steps done: 628620        Epsilon: 0.010000148074496387
Episode 1061 training loss: 158.89287833496928.          Total Reward: 31.0
Steps done: 629701        Epsilon: 0.010000144126372438
Episode 1062 training loss: 63.52648581750691.          Total Reward: 5.0
Steps done: 630204        Epsilon: 0.010000142325331085
Episode 1063 training loss: 56.980506367981434.          Total Reward: 1.0
Steps done: 630633        Epsilon: 0.010000140807048254
Episode 1064 training loss: 59.14209036715329.          Total Reward: -5.0
Steps done: 631056        Epsilon: 0.010000139325859308
Episode 1065 training loss: 106.31851633358747.          Total Reward: 9.0
Steps done: 631779        Epsilon: 0.010000136830167166
Episode 1066 training loss: 116.65610021911561.          Total Reward: 20.0
Steps done: 632580        Epsilon: 0.010000134117395348
Episode 1067 training loss: 113.18631683476269.          Total Reward: 20.0
Steps done: 633399        Epsilon: 0.01000013139926351
Episode 1068 training loss: 71.88529554568231.          Total Reward: 5.0
Steps done: 633966        Epsilon: 0.010000129549817865
Episode 1069 training loss: 64.99276891164482.          Total Reward: 15.0
Steps done: 634467        Epsilon: 0.010000127937325708
Episode 1070 training loss: 82.12438758648932.          Total Reward: 0.0
Steps done: 635068        Epsilon: 0.0100001260294363
Episode 1071 training loss: 120.17335264198482.          Total Reward: 24.0
Steps done: 635981        Epsilon: 0.010000123185395506
Episode 1072 training loss: 97.12844520807266.          Total Reward: 24.0
Steps done: 636732        Epsilon: 0.010000120894165927
Episode 1073 training loss: 85.9783030860126.          Total Reward: 22.0
Steps done: 637399        Epsilon: 0.010000118894970328
Episode 1074 training loss: 127.81231234502047.          Total Reward: 26.0
Steps done: 638376        Epsilon: 0.010000116026138903
Episode 1075 training loss: 65.50422621984035.          Total Reward: 10.0
Steps done: 638875        Epsilon: 0.010000114587703715
Episode 1076 training loss: 97.35807639081031.          Total Reward: 26.0
Steps done: 639572        Epsilon: 0.010000112608308541
Episode 1077 training loss: 106.42670444771647.          Total Reward: 17.0
Steps done: 640359        Epsilon: 0.010000110414393483
Episode 1078 training loss: 95.50278915185481.          Total Reward: 24.0
Steps done: 641114        Epsilon: 0.010000108349867066
Episode 1079 training loss: 57.6876078825444.          Total Reward: -11.0
Steps done: 641583        Epsilon: 0.010000107086883585
Episode 1080 training loss: 72.3646107679233.          Total Reward: 9.0
Steps done: 642120        Epsilon: 0.010000105658849302
Episode 1081 training loss: 93.31937376223505.          Total Reward: 19.0
Steps done: 642833        Epsilon: 0.010000103792166547
Episode 1082 training loss: 96.37531662732363.          Total Reward: 26.0
Steps done: 643516        Epsilon: 0.010000102034960146
Episode 1083 training loss: 101.69905157387257.          Total Reward: 24.0
Steps done: 644307        Epsilon: 0.010000100037038369
Episode 1084 training loss: 61.0865285648033.          Total Reward: 0.0
Steps done: 644790        Epsilon: 0.010000098836354845
Episode 1085 training loss: 64.81457359995693.          Total Reward: 7.0
Steps done: 645279        Epsilon: 0.010000097635435981
Episode 1086 training loss: 104.12953533604741.          Total Reward: 17.0
Steps done: 646038        Epsilon: 0.010000095800269785
Episode 1087 training loss: 84.82661884278059.          Total Reward: 9.0
Steps done: 646683        Epsilon: 0.010000094267878542
Episode 1088 training loss: 92.1897953171283.          Total Reward: 19.0
Steps done: 647338        Epsilon: 0.010000092736811851
Episode 1089 training loss: 72.68277799896896.          Total Reward: 15.0
Steps done: 647863        Epsilon: 0.010000091527594046
Episode 1090 training loss: 74.18432115390897.          Total Reward: 14.0
Steps done: 648407        Epsilon: 0.010000090291244997
Episode 1091 training loss: 81.45258683152497.          Total Reward: 4.0
Steps done: 648990        Epsilon: 0.01000008898479399
Episode 1092 training loss: 131.25361435022205.          Total Reward: 16.0
Steps done: 649957        Epsilon: 0.010000086859381037
Episode 1093 training loss: 131.8747638873756.          Total Reward: 22.0
Steps done: 650892        Epsilon: 0.010000084852588763
Episode 1094 training loss: 60.24281728081405.          Total Reward: -5.0
Steps done: 651327        Epsilon: 0.010000083934816294
Episode 1095 training loss: 72.20745361316949.          Total Reward: 6.0
Steps done: 651820        Epsilon: 0.010000082906668657
Episode 1096 training loss: 133.6076716920361.          Total Reward: 51.0
Steps done: 652839        Epsilon: 0.01000008082129648
Episode 1097 training loss: 76.00187989138067.          Total Reward: 11.0
Steps done: 653395        Epsilon: 0.01000007970565215
Episode 1098 training loss: 53.75717216171324.          Total Reward: 1.0
Steps done: 653804        Epsilon: 0.01000007889481433
Episode 1099 training loss: 67.27715450152755.          Total Reward: 4.0
Steps done: 654245        Epsilon: 0.010000078029776286
Beginning to save execution
-------------------------------------------------------------
Target_net saved to target_neth.pth
Policy_net saved to policy_net.pth
Replay memory saved to replay_memory.pkl
Hyperparameters saved to hyperparameters.pkl
Figure plotted to Rewards_Plot.png
Finished saving execution to previous_run/
-------------------------------------------------------------
Episode 1100 training loss: 65.84072450362146.          Total Reward: -4.0
Steps done: 654658        Epsilon: 0.010000077228263774
Episode 1101 training loss: 87.28769035451114.          Total Reward: 21.0
Steps done: 655220        Epsilon: 0.01000007615079362
Episode 1102 training loss: 66.6389914881438.          Total Reward: 7.0
Steps done: 655687        Epsilon: 0.010000075266902858
Episode 1103 training loss: 70.85772954113781.          Total Reward: -2.0
Steps done: 656146        Epsilon: 0.010000074408151656
Episode 1104 training loss: 105.47071656305343.          Total Reward: 16.0
Steps done: 656843        Epsilon: 0.010000073122820582
Episode 1105 training loss: 70.0018479116261.          Total Reward: 10.0
Steps done: 657330        Epsilon: 0.010000072237947834
Episode 1106 training loss: 93.65834161546081.          Total Reward: 23.0
Steps done: 657937        Epsilon: 0.010000071150012562
Episode 1107 training loss: 99.08033222332597.          Total Reward: 20.0
Steps done: 658586        Epsilon: 0.010000070004918307
Episode 1108 training loss: 75.99285127222538.          Total Reward: 7.0
Steps done: 659107        Epsilon: 0.010000069099016736
Episode 1109 training loss: 80.34398929588497.          Total Reward: 4.0
Steps done: 659604        Epsilon: 0.010000068245773206
Episode 1110 training loss: 112.2791485954076.          Total Reward: 7.0
Steps done: 660295        Epsilon: 0.010000067076952232
Episode 1111 training loss: 101.41275421530008.          Total Reward: 11.0
Steps done: 660898        Epsilon: 0.010000066073350829
Episode 1112 training loss: 79.51104322634637.          Total Reward: 4.0
Steps done: 661409        Epsilon: 0.010000065234632491
Episode 1113 training loss: 86.55646835453808.          Total Reward: 4.0
Steps done: 661924        Epsilon: 0.0100000644001203
Episode 1114 training loss: 66.54244389850646.          Total Reward: -2.0
Steps done: 662351        Epsilon: 0.010000063716305371
Episode 1115 training loss: 91.68535137549043.          Total Reward: 9.0
Steps done: 662894        Epsilon: 0.010000062857200889
Episode 1116 training loss: 92.41919209621847.          Total Reward: 10.0
Steps done: 663467        Epsilon: 0.010000061963190126
Episode 1117 training loss: 68.97373640723526.          Total Reward: -8.0
Steps done: 663900        Epsilon: 0.010000061296055972
Episode 1118 training loss: 107.27149943262339.          Total Reward: 20.0
Steps done: 664563        Epsilon: 0.010000060288447467
Episode 1119 training loss: 98.0693566519767.          Total Reward: 11.0
Steps done: 665198        Epsilon: 0.010000059338925138
Episode 1120 training loss: 77.02774251438677.          Total Reward: -2.0
Steps done: 665696        Epsilon: 0.010000058604735336
Episode 1121 training loss: 88.95955534651875.          Total Reward: 14.0
Steps done: 666237        Epsilon: 0.01000005781744236
Episode 1122 training loss: 84.6453123241663.          Total Reward: 2.0
Steps done: 666764        Epsilon: 0.010000057060693587
Episode 1123 training loss: 77.97468014620245.          Total Reward: 16.0
Steps done: 667285        Epsilon: 0.010000056322297297
Episode 1124 training loss: 117.20570036116987.          Total Reward: 27.0
Steps done: 668060        Epsilon: 0.010000055241556274
Episode 1125 training loss: 115.87657962553203.          Total Reward: 26.0
Steps done: 668791        Epsilon: 0.010000054241185562
Episode 1126 training loss: 83.59604348335415.          Total Reward: 7.0
Steps done: 669328        Epsilon: 0.010000053517863807
Episode 1127 training loss: 96.23612933140248.          Total Reward: 14.0
Steps done: 669941        Epsilon: 0.01000005270395505
Episode 1128 training loss: 96.06161637417972.          Total Reward: 25.0
Steps done: 670604        Epsilon: 0.010000051837586855
Episode 1129 training loss: 78.2173439282924.          Total Reward: 10.0
Steps done: 671123        Epsilon: 0.0100000511693388
Episode 1130 training loss: 76.92286412976682.          Total Reward: 3.0
Steps done: 671646        Epsilon: 0.010000050504654537
Episode 1131 training loss: 91.12601852603257.          Total Reward: 10.0
Steps done: 672195        Epsilon: 0.010000049816213389
Episode 1132 training loss: 114.34938607737422.          Total Reward: 33.0
Steps done: 672982        Epsilon: 0.010000048845658532
Episode 1133 training loss: 68.78477124683559.          Total Reward: 10.0
Steps done: 673469        Epsilon: 0.010000048254568204
Episode 1134 training loss: 76.27404105849564.          Total Reward: 7.0
Steps done: 673970        Epsilon: 0.010000047653948966
Episode 1135 training loss: 81.64965209551156.          Total Reward: 4.0
Steps done: 674537        Epsilon: 0.010000046983219268
Episode 1136 training loss: 117.31633356399834.          Total Reward: 22.0
Steps done: 675286        Epsilon: 0.010000046111644076
Episode 1137 training loss: 61.34585903957486.          Total Reward: -6.0
Steps done: 675689        Epsilon: 0.010000045649401717
Episode 1138 training loss: 93.8569555580616.          Total Reward: 12.0
Steps done: 676356        Epsilon: 0.010000044894509352
Episode 1139 training loss: 76.79277238063514.          Total Reward: 13.0
Steps done: 676857        Epsilon: 0.010000044335712392
Episode 1140 training loss: 79.83059242367744.          Total Reward: 16.0
Steps done: 677444        Epsilon: 0.010000043689836518
Episode 1141 training loss: 100.63165189884603.          Total Reward: 21.0
Steps done: 678139        Epsilon: 0.010000042937282355
Episode 1142 training loss: 69.05265127308667.          Total Reward: -6.0
Steps done: 678608        Epsilon: 0.010000042436782633
Episode 1143 training loss: 136.45679886825383.          Total Reward: 30.0
Steps done: 679485        Epsilon: 0.010000041516481838
Episode 1144 training loss: 102.3142392784357.          Total Reward: 20.0
Steps done: 680150        Epsilon: 0.010000040831976047
Episode 1145 training loss: 69.9728477280587.          Total Reward: -9.0
Steps done: 680603        Epsilon: 0.010000040372162526
Episode 1146 training loss: 58.361619994044304.          Total Reward: -12.0
Steps done: 681006        Epsilon: 0.010000039967455127
Episode 1147 training loss: 138.84304993692786.          Total Reward: 29.0
Steps done: 681921        Epsilon: 0.01000003906357711
Episode 1148 training loss: 74.04557186178863.          Total Reward: 9.0
Steps done: 682430        Epsilon: 0.010000038569642414
Episode 1149 training loss: 131.85432446934283.          Total Reward: 33.0
Steps done: 683311        Epsilon: 0.010000037729432814
Episode 1150 training loss: 97.28097744099796.          Total Reward: 18.0
Steps done: 683918        Epsilon: 0.010000037161210958
Episode 1151 training loss: 87.65332332998514.          Total Reward: 18.0
Steps done: 684531        Epsilon: 0.010000036596056954
Episode 1152 training loss: 109.78288127295673.          Total Reward: 21.0
Steps done: 685267        Epsilon: 0.010000035928846665
Episode 1153 training loss: 69.72020560503006.          Total Reward: 3.0
Steps done: 685738        Epsilon: 0.010000035508265526
Episode 1154 training loss: 89.42348244413733.          Total Reward: 17.0
Steps done: 686351        Epsilon: 0.010000034968249796
Episode 1155 training loss: 80.2802664078772.          Total Reward: -3.0
Steps done: 686884        Epsilon: 0.01000003450538853
Episode 1156 training loss: 72.18619390949607.          Total Reward: 9.0
Steps done: 687377        Epsilon: 0.010000034082719662
Episode 1157 training loss: 75.95660519599915.          Total Reward: -5.0
Steps done: 687884        Epsilon: 0.01000003365344745
Episode 1158 training loss: 83.5611415617168.          Total Reward: 16.0
Steps done: 688457        Epsilon: 0.010000033174798325
Episode 1159 training loss: 96.52912683598697.          Total Reward: 11.0
Steps done: 689126        Epsilon: 0.010000032624563985
Episode 1160 training loss: 98.50262517854571.          Total Reward: 8.0
Steps done: 689801        Epsilon: 0.010000032078643625
Episode 1161 training loss: 113.80494489520788.          Total Reward: 12.0
Steps done: 690508        Epsilon: 0.010000031516634983
Episode 1162 training loss: 147.83832645975053.          Total Reward: 32.0
Steps done: 691581        Epsilon: 0.010000030682439912
Episode 1163 training loss: 66.69936240278184.          Total Reward: 3.0
Steps done: 692086        Epsilon: 0.010000030297509097
Episode 1164 training loss: 91.69563820771873.          Total Reward: 24.0
Steps done: 692769        Epsilon: 0.010000029784570801
Episode 1165 training loss: 112.54983620718122.          Total Reward: 26.0
Steps done: 693600        Epsilon: 0.010000029172179582
Episode 1166 training loss: 89.89766162447631.          Total Reward: 20.0
Steps done: 694233        Epsilon: 0.010000028714163452
Episode 1167 training loss: 82.36180451791734.          Total Reward: 13.0
Steps done: 694842        Epsilon: 0.010000028280301469
Episode 1168 training loss: 106.92563182115555.          Total Reward: 19.0
Steps done: 695587        Epsilon: 0.010000027758455628
Episode 1169 training loss: 101.37704847194254.          Total Reward: 26.0
Steps done: 696342        Epsilon: 0.010000027239428506
Episode 1170 training loss: 67.09724256023765.          Total Reward: 6.0
Steps done: 696827        Epsilon: 0.010000026911144677
Episode 1171 training loss: 95.19456326775253.          Total Reward: 26.0
Steps done: 697534        Epsilon: 0.010000026439669135
Episode 1172 training loss: 95.79983203485608.          Total Reward: 15.0
Steps done: 698257        Epsilon: 0.010000025966065204
Episode 1173 training loss: 91.66864074207842.          Total Reward: 21.0
Steps done: 698966        Epsilon: 0.010000025509871658
Episode 1174 training loss: 77.82491464726627.          Total Reward: -7.0
Steps done: 699519        Epsilon: 0.010000025159624346
Episode 1175 training loss: 65.56421911716461.          Total Reward: 4.0
Steps done: 700000        Epsilon: 0.010000024858891642
Episode 1176 training loss: 116.54236701875925.          Total Reward: 27.0
Steps done: 700813        Epsilon: 0.010000024358734733
Episode 1177 training loss: 74.69451513700187.          Total Reward: 13.0
Steps done: 701362        Epsilon: 0.010000024026694934
Episode 1178 training loss: 129.49747933261096.          Total Reward: 27.0
Steps done: 702247        Epsilon: 0.010000023500941898
Episode 1179 training loss: 117.23160455562174.          Total Reward: 22.0
Steps done: 703044        Epsilon: 0.010000023037319804
Episode 1180 training loss: 109.02064390294254.          Total Reward: 27.0
Steps done: 703811        Epsilon: 0.010000022599787444
Episode 1181 training loss: 82.16689307894558.          Total Reward: 11.0
Steps done: 704418        Epsilon: 0.010000022259424703
Episode 1182 training loss: 121.70661502704024.          Total Reward: 23.0
Steps done: 705260        Epsilon: 0.010000021795760995
Episode 1183 training loss: 74.80292020365596.          Total Reward: 7.0
Steps done: 705779        Epsilon: 0.010000021514787752
Episode 1184 training loss: 176.10796503722668.          Total Reward: 55.0
Steps done: 707042        Epsilon: 0.010000020846071248
Episode 1185 training loss: 98.45649994537234.          Total Reward: 23.0
Steps done: 707795        Epsilon: 0.010000020457314608
Episode 1186 training loss: 94.29678419046104.          Total Reward: 30.0
Steps done: 708514        Epsilon: 0.010000020092879551
Episode 1187 training loss: 89.32502813264728.          Total Reward: 17.0
Steps done: 709188        Epsilon: 0.010000019757150987
Episode 1188 training loss: 94.81029000505805.          Total Reward: 28.0
Steps done: 709885        Epsilon: 0.010000019415864723
Episode 1189 training loss: 149.7186655625701.          Total Reward: 37.0
Steps done: 711078        Epsilon: 0.010000018845336845
Episode 1190 training loss: 75.41618213243783.          Total Reward: 19.0
Steps done: 711727        Epsilon: 0.010000018542038417
Episode 1191 training loss: 70.1099948771298.          Total Reward: 5.0
Steps done: 712266        Epsilon: 0.010000018293860305
Episode 1192 training loss: 92.59834134951234.          Total Reward: 25.0
Steps done: 713003        Epsilon: 0.010000017959882151
Episode 1193 training loss: 78.52566293254495.          Total Reward: 9.0
Steps done: 713608        Epsilon: 0.010000017690282918
Episode 1194 training loss: 87.31820818223059.          Total Reward: 15.0
Steps done: 714263        Epsilon: 0.010000017402963383
Episode 1195 training loss: 78.34286023490131.          Total Reward: 22.0
Steps done: 714853        Epsilon: 0.010000017148153515
Episode 1196 training loss: 113.7934255078435.          Total Reward: 33.0
Steps done: 715731        Epsilon: 0.010000016775852497
Episode 1197 training loss: 87.64755602367222.          Total Reward: 18.0
Steps done: 716406        Epsilon: 0.0100000164951352
Episode 1198 training loss: 77.81020769104362.          Total Reward: -16.0
Steps done: 716917        Epsilon: 0.010000016285750143
Episode 1199 training loss: 95.87380656972528.          Total Reward: 27.0
Steps done: 717604        Epsilon: 0.010000016008430682
Beginning to save execution
-------------------------------------------------------------
Target_net saved to target_neth.pth
Policy_net saved to policy_net.pth
Replay memory saved to replay_memory.pkl
Hyperparameters saved to hyperparameters.pkl
Figure plotted to Rewards_Plot.png
Finished saving execution to previous_run/
-------------------------------------------------------------
Episode 1200 training loss: 78.341472171247.          Total Reward: -1.0
Steps done: 718137        Epsilon: 0.010000015796533245
Episode 1201 training loss: 69.48872005939484.          Total Reward: 1.0
Steps done: 718604        Epsilon: 0.01000001561318112
Episode 1202 training loss: 102.48705669678748.          Total Reward: 19.0
Steps done: 719273        Epsilon: 0.010000015354222246
Episode 1203 training loss: 71.84782175719738.          Total Reward: 0.0
Steps done: 719746        Epsilon: 0.010000015173727844
Episode 1204 training loss: 78.78826932609081.          Total Reward: 17.0
Steps done: 720283        Epsilon: 0.010000014971381834
Episode 1205 training loss: 87.78036028705537.          Total Reward: 0.0
Steps done: 720822        Epsilon: 0.010000014770995599
Episode 1206 training loss: 161.5968884434551.          Total Reward: 32.0
Steps done: 721809        Epsilon: 0.010000014410981226
Episode 1207 training loss: 62.12156590633094.          Total Reward: -2.0
Steps done: 722234        Epsilon: 0.010000014258675109
Episode 1208 training loss: 124.17631605453789.          Total Reward: 37.0
Steps done: 723015        Epsilon: 0.010000013982974761
Episode 1209 training loss: 94.7098936419934.          Total Reward: 11.0
Steps done: 723570        Epsilon: 0.010000013790300754
Episode 1210 training loss: 161.78062349185348.          Total Reward: 39.0
Steps done: 724539        Epsilon: 0.010000013460244664
Episode 1211 training loss: 107.94549989141524.          Total Reward: 30.0
Steps done: 725205        Epsilon: 0.01000001323798702
Episode 1212 training loss: 103.35486112721264.          Total Reward: 10.0
Steps done: 725820        Epsilon: 0.010000013036009649
Episode 1213 training loss: 119.26701823342592.          Total Reward: 25.0
Steps done: 726500        Epsilon: 0.010000012816270559
Episode 1214 training loss: 78.43159990757704.          Total Reward: -10.0
Steps done: 726963        Epsilon: 0.010000012668777489
Episode 1215 training loss: 99.97488373704255.          Total Reward: 13.0
Steps done: 727546        Epsilon: 0.010000012485469162
Episode 1216 training loss: 87.09124656394124.          Total Reward: 6.0
Steps done: 728113        Epsilon: 0.010000012309736088
Episode 1217 training loss: 97.4855312872678.          Total Reward: 11.0
Steps done: 728720        Epsilon: 0.010000012124346046
Episode 1218 training loss: 94.23063109070063.          Total Reward: 5.0
Steps done: 729255        Epsilon: 0.010000011963262567
Episode 1219 training loss: 88.09281973354518.          Total Reward: 2.0
Steps done: 729816        Epsilon: 0.010000011796648918
Episode 1220 training loss: 126.88287702389061.          Total Reward: 26.0
Steps done: 730577        Epsilon: 0.0100000115743391
Episode 1221 training loss: 79.9224093509838.          Total Reward: 3.0
Steps done: 731097        Epsilon: 0.010000011424846498
Episode 1222 training loss: 91.11598743870854.          Total Reward: 14.0
Steps done: 731670        Epsilon: 0.010000011262352216
Episode 1223 training loss: 80.25130182877183.          Total Reward: 4.0
Steps done: 732205        Epsilon: 0.010000011112721145
Episode 1224 training loss: 80.66580440662801.          Total Reward: 10.0
Steps done: 732744        Epsilon: 0.01000001096398161
Episode 1225 training loss: 99.6003381088376.          Total Reward: 14.0
Steps done: 733391        Epsilon: 0.010000010788065762
Episode 1226 training loss: 114.9232003390789.          Total Reward: 22.0
Steps done: 734098        Epsilon: 0.01000001059906194
Episode 1227 training loss: 88.15118108317256.          Total Reward: 9.0
Steps done: 734665        Epsilon: 0.010000010449880062
Episode 1228 training loss: 102.24754210747778.          Total Reward: 20.0
Steps done: 735316        Epsilon: 0.010000010281184746
Episode 1229 training loss: 98.39355850033462.          Total Reward: 11.0
Steps done: 735929        Epsilon: 0.010000010124826743
Episode 1230 training loss: 72.92530311085284.          Total Reward: 3.0
Steps done: 736374        Epsilon: 0.010000010012812283
Episode 1231 training loss: 110.72960895858705.          Total Reward: 17.0
Steps done: 737047        Epsilon: 0.010000009845756016
Episode 1232 training loss: 75.04590252786875.          Total Reward: 4.0
Steps done: 737540        Epsilon: 0.010000009725151825
Episode 1233 training loss: 72.17991925030947.          Total Reward: -2.0
Steps done: 738007        Epsilon: 0.010000009612270901
Episode 1234 training loss: 95.41513714380562.          Total Reward: 16.0
Steps done: 738632        Epsilon: 0.010000009463246454
Episode 1235 training loss: 119.27443629689515.          Total Reward: 11.0
Steps done: 739377        Epsilon: 0.010000009288624701
Episode 1236 training loss: 100.22045771591365.          Total Reward: 18.0
Steps done: 740020        Epsilon: 0.01000000914050377
Episode 1237 training loss: 143.6497160308063.          Total Reward: 30.0
Steps done: 740943        Epsilon: 0.010000008932001493
Episode 1238 training loss: 120.39254363812506.          Total Reward: 25.0
Steps done: 741676        Epsilon: 0.010000008769813155
Episode 1239 training loss: 137.96610765904188.          Total Reward: 35.0
Steps done: 742551        Epsilon: 0.010000008580056521
Episode 1240 training loss: 140.90566926077008.          Total Reward: 28.0
Steps done: 743506        Epsilon: 0.01000000837763371
Episode 1241 training loss: 77.77750449068844.          Total Reward: 15.0
Steps done: 744025        Epsilon: 0.010000008269636063
Episode 1242 training loss: 142.48965111374855.          Total Reward: 44.0
Steps done: 744966        Epsilon: 0.01000000807736335
Episode 1243 training loss: 96.89996453560889.          Total Reward: 20.0
Steps done: 745615        Epsilon: 0.010000007947365587
Episode 1244 training loss: 126.94700564444065.          Total Reward: 21.0
Steps done: 746414        Epsilon: 0.010000007790191957
Episode 1245 training loss: 52.75074394233525.          Total Reward: -19.0
Steps done: 746793        Epsilon: 0.010000007716728472
Episode 1246 training loss: 112.81487338617444.          Total Reward: 23.0
Steps done: 747496        Epsilon: 0.010000007582291791
Episode 1247 training loss: 102.51773270778358.          Total Reward: 24.0
Steps done: 748163        Epsilon: 0.01000000745690539
Episode 1248 training loss: 107.84748788550496.          Total Reward: 28.0
Steps done: 748910        Epsilon: 0.010000007318939944
Episode 1249 training loss: 121.30648071691394.          Total Reward: 34.0
Steps done: 749727        Epsilon: 0.010000007170966914
Episode 1250 training loss: 95.5627609025687.          Total Reward: 28.0
Steps done: 750396        Epsilon: 0.010000007052029877
Episode 1251 training loss: 71.93486804515123.          Total Reward: -13.0
Steps done: 750865        Epsilon: 0.010000006969827679
Episode 1252 training loss: 80.66179409250617.          Total Reward: 11.0
Steps done: 751410        Epsilon: 0.01000000687550779
Episode 1253 training loss: 128.7512014415115.          Total Reward: 30.0
Steps done: 752229        Epsilon: 0.010000006736163176
Episode 1254 training loss: 124.63191861100495.          Total Reward: 20.0
Steps done: 753074        Epsilon: 0.01000000659535426
Episode 1255 training loss: 145.3730814959854.          Total Reward: 31.0
Steps done: 754049        Epsilon: 0.01000000643653596
Episode 1256 training loss: 73.10828822664917.          Total Reward: 8.0
Steps done: 754524        Epsilon: 0.01000000636055413
Episode 1257 training loss: 76.63878392986953.          Total Reward: 1.0
Steps done: 755007        Epsilon: 0.010000006284212281
Episode 1258 training loss: 119.03887005802244.          Total Reward: 28.0
Steps done: 755786        Epsilon: 0.010000006163011273
Episode 1259 training loss: 78.54658707417548.          Total Reward: 2.0
Steps done: 756279        Epsilon: 0.01000000608751834
Episode 1260 training loss: 164.63787161000073.          Total Reward: 38.0
Steps done: 757322        Epsilon: 0.010000005930837897
Episode 1261 training loss: 137.56627940014005.          Total Reward: 34.0
Steps done: 758203        Epsilon: 0.010000005801639216
Episode 1262 training loss: 114.0211775302887.          Total Reward: 17.0
Steps done: 758912        Epsilon: 0.010000005699711167
Episode 1263 training loss: 91.09546429663897.          Total Reward: 21.0
Steps done: 759572        Epsilon: 0.010000005606437556
Episode 1264 training loss: 106.80540390126407.          Total Reward: 6.0
Steps done: 760247        Epsilon: 0.010000005512622711
Episode 1265 training loss: 137.61918692104518.          Total Reward: 32.0
Steps done: 761186        Epsilon: 0.010000005384721013
Episode 1266 training loss: 84.48670842684805.          Total Reward: 17.0
Steps done: 761777        Epsilon: 0.01000000530574662
Episode 1267 training loss: 74.79117099568248.          Total Reward: 12.0
Steps done: 762296        Epsilon: 0.010000005237349245
Episode 1268 training loss: 86.20922242291272.          Total Reward: 23.0
Steps done: 762899        Epsilon: 0.010000005158988336
Episode 1269 training loss: 98.43772090412676.          Total Reward: 22.0
Steps done: 763566        Epsilon: 0.010000005073675476
Episode 1270 training loss: 110.12627493217587.          Total Reward: 22.0
Steps done: 764327        Epsilon: 0.010000004978061215
Episode 1271 training loss: 83.54561840370297.          Total Reward: 20.0
Steps done: 764920        Epsilon: 0.010000004904805807
Episode 1272 training loss: 67.19335479289293.          Total Reward: 12.0
Steps done: 765427        Epsilon: 0.010000004843029726
Episode 1273 training loss: 108.74387452751398.          Total Reward: 15.0
Steps done: 766186        Epsilon: 0.010000004751999615
Episode 1274 training loss: 116.74164754711092.          Total Reward: 20.0
Steps done: 766979        Epsilon: 0.010000004658718923
Episode 1275 training loss: 94.91636082343757.          Total Reward: 22.0
Steps done: 767620        Epsilon: 0.01000000458465795
Episode 1276 training loss: 83.95047153532505.          Total Reward: 9.0
Steps done: 768181        Epsilon: 0.010000004520806925
Episode 1277 training loss: 85.46422984823585.          Total Reward: 3.0
Steps done: 768752        Epsilon: 0.010000004456730837
Episode 1278 training loss: 73.88611994870007.          Total Reward: -2.0
Steps done: 769211        Epsilon: 0.010000004405882152
Episode 1279 training loss: 78.98668112978339.          Total Reward: 6.0
Steps done: 769742        Epsilon: 0.01000000434778057
Episode 1280 training loss: 134.75046003982425.          Total Reward: 11.0
Steps done: 770609        Epsilon: 0.010000004254556393
Episode 1281 training loss: 123.50695628114045.          Total Reward: 40.0
Steps done: 771376        Epsilon: 0.010000004173752458
Episode 1282 training loss: 111.88934529013932.          Total Reward: 12.0
Steps done: 772061        Epsilon: 0.010000004102885478
Episode 1283 training loss: 104.26973896101117.          Total Reward: 19.0
Steps done: 772696        Epsilon: 0.010000004038266442
Episode 1284 training loss: 113.77157100476325.          Total Reward: 31.0
Steps done: 773476        Epsilon: 0.010000003960283055
Episode 1285 training loss: 108.34939374774694.          Total Reward: 7.0
Steps done: 774169        Epsilon: 0.010000003892262084
Episode 1286 training loss: 99.88769765011966.          Total Reward: 12.0
Steps done: 774784        Epsilon: 0.010000003832876253
Episode 1287 training loss: 139.12636581249535.          Total Reward: 31.0
Steps done: 775677        Epsilon: 0.010000003748255385
Episode 1288 training loss: 68.43513356894255.          Total Reward: -14.0
Steps done: 776126        Epsilon: 0.01000000370641648
Episode 1289 training loss: 99.7543420419097.          Total Reward: 19.0
Steps done: 776779        Epsilon: 0.010000003646400444
Episode 1290 training loss: 82.13255036622286.          Total Reward: 13.0
Steps done: 777310        Epsilon: 0.010000003598314355
Episode 1291 training loss: 74.76496071740985.          Total Reward: 1.0
Steps done: 777795        Epsilon: 0.010000003554948232
Episode 1292 training loss: 92.09550180099905.          Total Reward: 19.0
Steps done: 778368        Epsilon: 0.010000003504386611
Episode 1293 training loss: 135.44866885058582.          Total Reward: 41.0
Steps done: 779221        Epsilon: 0.010000003430446752
Episode 1294 training loss: 90.46957174129784.          Total Reward: 4.0
Steps done: 779796        Epsilon: 0.010000003381486823
Episode 1295 training loss: 146.98975448310375.          Total Reward: 44.0
Steps done: 780761        Epsilon: 0.010000003300884627
Episode 1296 training loss: 64.94022300466895.          Total Reward: 0.0
Steps done: 781214        Epsilon: 0.01000000326371299
Episode 1297 training loss: 100.58720366936177.          Total Reward: 13.0
Steps done: 781867        Epsilon: 0.010000003210865418
Episode 1298 training loss: 91.98642326518893.          Total Reward: 20.0
Steps done: 782532        Epsilon: 0.010000003157926058
Episode 1299 training loss: 98.7861246932298.          Total Reward: 17.0
Steps done: 783155        Epsilon: 0.010000003109122404
Beginning to save execution
-------------------------------------------------------------
Target_net saved to target_neth.pth
Policy_net saved to policy_net.pth
Replay memory saved to replay_memory.pkl
Hyperparameters saved to hyperparameters.pkl
Figure plotted to Rewards_Plot.png
Finished saving execution to previous_run/
-------------------------------------------------------------
Episode 1300 training loss: 80.52698758803308.          Total Reward: 10.0
Steps done: 783672        Epsilon: 0.01000000306919558
Episode 1301 training loss: 76.25275068730116.          Total Reward: 6.0
Steps done: 784195        Epsilon: 0.010000003029327057
Episode 1302 training loss: 90.2967359740287.          Total Reward: 10.0
Steps done: 784764        Epsilon: 0.010000002986539924
Episode 1303 training loss: 100.03373998217285.          Total Reward: 1.0
Steps done: 785417        Epsilon: 0.010000002938180468
Episode 1304 training loss: 75.84717883449048.          Total Reward: 1.0
Steps done: 785880        Epsilon: 0.010000002904367101
Episode 1305 training loss: 73.71418632753193.          Total Reward: 4.0
Steps done: 786377        Epsilon: 0.010000002868503603
Episode 1306 training loss: 83.87926176004112.          Total Reward: 17.0
Steps done: 786922        Epsilon: 0.010000002829685292
Episode 1307 training loss: 80.01352558471262.          Total Reward: -3.0
Steps done: 787415        Epsilon: 0.010000002795023463
Episode 1308 training loss: 77.1075888723135.          Total Reward: -3.0
Steps done: 787894        Epsilon: 0.010000002761752664
Episode 1309 training loss: 71.83238376304507.          Total Reward: 7.0
Steps done: 788353        Epsilon: 0.010000002730242687
Episode 1310 training loss: 74.23806820437312.          Total Reward: -5.0
Steps done: 788794        Epsilon: 0.010000002700307084
Episode 1311 training loss: 134.2727629384026.          Total Reward: 19.0
Steps done: 789575        Epsilon: 0.010000002648094967
Episode 1312 training loss: 85.82557400502264.          Total Reward: 12.0
Steps done: 790078        Epsilon: 0.01000000261500367
Episode 1313 training loss: 117.3208785597235.          Total Reward: 26.0
Steps done: 790791        Epsilon: 0.010000002568804206
Episode 1314 training loss: 75.4080949537456.          Total Reward: 1.0
Steps done: 791266        Epsilon: 0.010000002538480062
Episode 1315 training loss: 124.36095254588872.          Total Reward: 17.0
Steps done: 791957        Epsilon: 0.01000000249500442
Episode 1316 training loss: 147.97974653728306.          Total Reward: 36.0
Steps done: 792861        Epsilon: 0.010000002439249723
Episode 1317 training loss: 111.31977394036949.          Total Reward: 21.0
Steps done: 793532        Epsilon: 0.010000002398672601
Episode 1318 training loss: 105.0952681042254.          Total Reward: 20.0
Steps done: 794165        Epsilon: 0.010000002361012379
Episode 1319 training loss: 110.55648405663669.          Total Reward: 20.0
Steps done: 794846        Epsilon: 0.01000000232115638
Episode 1320 training loss: 73.19406511634588.          Total Reward: 5.0
Steps done: 795305        Epsilon: 0.010000002294673347
Episode 1321 training loss: 71.26332231983542.          Total Reward: -1.0
Steps done: 795748        Epsilon: 0.01000000226940005
Episode 1322 training loss: 90.7065663151443.          Total Reward: 6.0
Steps done: 796259        Epsilon: 0.01000000224059286