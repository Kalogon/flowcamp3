import tensorflow as tf
import pandas as pd


# data = pd.read_csv('C:\\Users\q\PycharmProjects\\tensorflowpractice\lol.csv', sep=',')
# data = pd.read_csv('C:\\Users\q\PycharmProjects\\tensorflowpractice\cs.csv', sep=',',dtype='unicode')
# data = np.array(data, dtype='unicode')

# data_col_output = data[["participants.1.stats.goldSpent"]]
# print(data_col_output)



# data_iron = pd.read_csv('C:\\Users\q\PycharmProjects\\tensorflowpractice\\lol\\iron' + str(0) + '.csv', sep=',', dtype='unicode')
# data_col_kills = data_iron[["participants." + str(0)+ ".stats.kills"]]
# input_list1 = []
# input_list1.append(float(list(data_col_kills.values)[0][0]))
# print(input_list1)

# temp_output = list(data_col_output.values)[:100]
# temp_input1 = list(data_col_input1.values)[:100]
# temp_input2 = list(data_col_input2.values)[:100]
# temp_input3 = list(data_col_input3.values)[:100]
# temp_input4 = list(data_col_input4.values)[:100]
# temp_input5 = list(data_col_input5.values)[:100]
# temp_input6 = list(data_col_input6.values)[:100]
#
# output = []
# input1 = []
# input2 = []
# input3 = []
# input4 = []
# input5 = []
# input6 = []
#
# for i in range(len(temp_output)):
#     if(temp_output[i][0]=="1"):
#         output.append(1)
#     else:
#         output.append(-1)
#
#     if(temp_input1[i][0]=="1"):
#         input1.append(1)
#     else:
#         input1.append(-1)
#
#     if(temp_input2[i][0]=="1"):
#         input2.append(1)
#     else:
#         input2.append(-1)
#
#     if(temp_input3[i][0]=="1"):
#         input3.append(1)
#     else:
#         input3.append(-1)
#
#     if(temp_input4[i][0]=="1"):
#         input4.append(1)
#     else:
#         input4.append(-1)
#
#     if(temp_input5[i][0]=="1"):
#         input5.append(1)
#     else:
#         input5.append(-1)
#
#     if(temp_input6[i][0]=="1"):
#         input6.append(1)
#     else:
#         input6.append(-1)
#
#
#


Top_list_kda = []
Top_list_totalDamageDealtToChampions = []
Top_list_totalDamageTaken = []
Top_list_totalHeal = []
Top_list_visionScore = []
Top_list_goldEarned = []
Top_list_turretKills = []
Top_list_totalMinionsKilled = []
Top_list_champLevel = []
Top_list_timeline_lane = []
Top_list_timeline_role = []
Top_list_col_gameId = []
Top_list_col_gameDuration = []
Top_list_col_Tier = []


Jungle_list_kda = []
Jungle_list_totalDamageDealtToChampions = []
Jungle_list_totalDamageTaken = []
Jungle_list_totalHeal = []
Jungle_list_visionScore = []
Jungle_list_goldEarned = []
Jungle_list_turretKills = []
Jungle_list_totalMinionsKilled = []
Jungle_list_champLevel = []
Jungle_list_timeline_lane = []
Jungle_list_timeline_role = []
Jungle_list_col_gameId = []
Jungle_list_col_gameDuration = []
Jungle_list_col_Tier = []


Mid_list_kda = []
Mid_list_totalDamageDealtToChampions = []
Mid_list_totalDamageTaken = []
Mid_list_totalHeal = []
Mid_list_visionScore = []
Mid_list_goldEarned = []
Mid_list_turretKills = []
Mid_list_totalMinionsKilled = []
Mid_list_champLevel = []
Mid_list_timeline_lane = []
Mid_list_timeline_role = []
Mid_list_col_gameId = []
Mid_list_col_gameDuration = []
Mid_list_col_Tier = []


Bot_list_kda = []
Bot_list_totalDamageDealtToChampions = []
Bot_list_totalDamageTaken = []
Bot_list_totalHeal = []
Bot_list_visionScore = []
Bot_list_goldEarned = []
Bot_list_turretKills = []
Bot_list_totalMinionsKilled = []
Bot_list_champLevel = []
Bot_list_timeline_lane = []
Bot_list_timeline_role = []
Bot_list_col_gameId = []
Bot_list_col_gameDuration = []
Bot_list_col_Tier = []


Sup_list_kda = []
Sup_list_totalDamageDealtToChampions = []
Sup_list_totalDamageTaken = []
Sup_list_totalHeal = []
Sup_list_visionScore = []
Sup_list_goldEarned = []
Sup_list_turretKills = []
Sup_list_totalMinionsKilled = []
Sup_list_champLevel = []
Sup_list_timeline_lane = []
Sup_list_timeline_rle = []
Sup_list_col_gameId = []
Sup_list_col_gameDuration = []
Sup_list_col_Tier = []




iron_jungle_sum_kda = 0
iron_jungle_sum_totalDamageDealtToChampions = 0
iron_jungle_sum_totalDamageTaken = 0
iron_jungle_sum_totaloHeal = 0
iron_jungle_sum_visionScore = 0
iron_jungle_sum_goldEarned = 0
iron_jungle_sum_turretKills = 0
iron_jungle_sum_totalMinionsKilled = 0
iron_jungle_sum_champLevel = 0

iron_middle_sum_kda = 0
iron_middle_sum_totalDamageDealtToChampions = 0
iron_middle_sum_totalDamageTaken = 0
iron_middle_sum_totaloHeal = 0
iron_middle_sum_visionScore = 0
iron_middle_sum_goldEarned = 0
iron_middle_sum_turretKills = 0
iron_middle_sum_totalMinionsKilled = 0
iron_middle_sum_champLevel = 0

iron_top_sum_kda = 0
iron_top_sum_totalDamageDealtToChampions = 0
iron_top_sum_totalDamageTaken = 0
iron_top_sum_totaloHeal = 0
iron_top_sum_visionScore = 0
iron_top_sum_goldEarned = 0
iron_top_sum_turretKills = 0
iron_top_sum_totalMinionsKilled = 0
iron_top_sum_champLevel = 0

iron_bottom_car_sum_kda = 0
iron_bottom_car_sum_totalDamageDealtToChampions = 0
iron_bottom_car_sum_totalDamageTaken = 0
iron_bottom_car_sum_totaloHeal = 0
iron_bottom_car_sum_visionScore = 0
iron_bottom_car_sum_goldEarned = 0
iron_bottom_car_sum_turretKills = 0
iron_bottom_car_sum_totalMinionsKilled = 0
iron_bottom_car_sum_champLevel = 0

iron_bottom_sup_sum_kda = 0
iron_bottom_sup_sum_totalDamageDealtToChampions = 0
iron_bottom_sup_sum_totalDamageTaken = 0
iron_bottom_sup_sum_totaloHeal = 0
iron_bottom_sup_sum_visionScore = 0
iron_bottom_sup_sum_goldEarned = 0
iron_bottom_sup_sum_turretKills = 0
iron_bottom_sup_sum_totalMinionsKilled = 0
iron_bottom_sup_sum_champLevel = 0



bronze_jungle_sum_kda = 0
bronze_jungle_sum_totalDamageDealtToChampions = 0
bronze_jungle_sum_totalDamageTaken = 0
bronze_jungle_sum_totaloHeal = 0
bronze_jungle_sum_visionScore = 0
bronze_jungle_sum_goldEarned = 0
bronze_jungle_sum_turretKills = 0
bronze_jungle_sum_totalMinionsKilled = 0
bronze_jungle_sum_champLevel = 0

bronze_middle_sum_kda = 0
bronze_middle_sum_totalDamageDealtToChampions = 0
bronze_middle_sum_totalDamageTaken = 0
bronze_middle_sum_totaloHeal = 0
bronze_middle_sum_visionScore = 0
bronze_middle_sum_goldEarned = 0
bronze_middle_sum_turretKills = 0
bronze_middle_sum_totalMinionsKilled = 0
bronze_middle_sum_champLevel = 0

bronze_top_sum_kda = 0
bronze_top_sum_totalDamageDealtToChampions = 0
bronze_top_sum_totalDamageTaken = 0
bronze_top_sum_totaloHeal = 0
bronze_top_sum_visionScore = 0
bronze_top_sum_goldEarned = 0
bronze_top_sum_turretKills = 0
bronze_top_sum_totalMinionsKilled = 0
bronze_top_sum_champLevel = 0

bronze_bottom_car_sum_kda = 0
bronze_bottom_car_sum_totalDamageDealtToChampions = 0
bronze_bottom_car_sum_totalDamageTaken = 0
bronze_bottom_car_sum_totaloHeal = 0
bronze_bottom_car_sum_visionScore = 0
bronze_bottom_car_sum_goldEarned = 0
bronze_bottom_car_sum_turretKills = 0
bronze_bottom_car_sum_totalMinionsKilled = 0
bronze_bottom_car_sum_champLevel = 0

bronze_bottom_sup_sum_kda = 0
bronze_bottom_sup_sum_totalDamageDealtToChampions = 0
bronze_bottom_sup_sum_totalDamageTaken = 0
bronze_bottom_sup_sum_totaloHeal = 0
bronze_bottom_sup_sum_visionScore = 0
bronze_bottom_sup_sum_goldEarned = 0
bronze_bottom_sup_sum_turretKills = 0
bronze_bottom_sup_sum_totalMinionsKilled = 0
bronze_bottom_sup_sum_champLevel = 0



silver_jungle_sum_kda = 0
silver_jungle_sum_totalDamageDealtToChampions = 0
silver_jungle_sum_totalDamageTaken = 0
silver_jungle_sum_totaloHeal = 0
silver_jungle_sum_visionScore = 0
silver_jungle_sum_goldEarned = 0
silver_jungle_sum_turretKills = 0
silver_jungle_sum_totalMinionsKilled = 0
silver_jungle_sum_champLevel = 0

silver_middle_sum_kda = 0
silver_middle_sum_totalDamageDealtToChampions = 0
silver_middle_sum_totalDamageTaken = 0
silver_middle_sum_totaloHeal = 0
silver_middle_sum_visionScore = 0
silver_middle_sum_goldEarned = 0
silver_middle_sum_turretKills = 0
silver_middle_sum_totalMinionsKilled = 0
silver_middle_sum_champLevel = 0


silver_top_sum_kda = 0
silver_top_sum_totalDamageDealtToChampions = 0
silver_top_sum_totalDamageTaken = 0
silver_top_sum_totaloHeal = 0
silver_top_sum_visionScore = 0
silver_top_sum_goldEarned = 0
silver_top_sum_turretKills = 0
silver_top_sum_totalMinionsKilled = 0
silver_top_sum_champLevel = 0

silver_bottom_car_sum_kda = 0
silver_bottom_car_sum_totalDamageDealtToChampions = 0
silver_bottom_car_sum_totalDamageTaken = 0
silver_bottom_car_sum_totaloHeal = 0
silver_bottom_car_sum_visionScore = 0
silver_bottom_car_sum_goldEarned = 0
silver_bottom_car_sum_turretKills = 0
silver_bottom_car_sum_totalMinionsKilled = 0
silver_bottom_car_sum_champLevel = 0

silver_bottom_sup_sum_kda = 0
silver_bottom_sup_sum_totalDamageDealtToChampions = 0
silver_bottom_sup_sum_totalDamageTaken = 0
silver_bottom_sup_sum_totaloHeal = 0
silver_bottom_sup_sum_visionScore = 0
silver_bottom_sup_sum_goldEarned = 0
silver_bottom_sup_sum_turretKills = 0
silver_bottom_sup_sum_totalMinionsKilled = 0
silver_bottom_sup_sum_champLevel = 0


gold_jungle_sum_kda = 0
gold_jungle_sum_totalDamageDealtToChampions = 0
gold_jungle_sum_totalDamageTaken = 0
gold_jungle_sum_totaloHeal = 0
gold_jungle_sum_visionScore = 0
gold_jungle_sum_goldEarned = 0
gold_jungle_sum_turretKills = 0
gold_jungle_sum_totalMinionsKilled = 0
gold_jungle_sum_champLevel = 0

gold_middle_sum_kda = 0
gold_middle_sum_totalDamageDealtToChampions = 0
gold_middle_sum_totalDamageTaken = 0
gold_middle_sum_totaloHeal = 0
gold_middle_sum_visionScore = 0
gold_middle_sum_goldEarned = 0
gold_middle_sum_turretKills = 0
gold_middle_sum_totalMinionsKilled = 0
gold_middle_sum_champLevel = 0

gold_top_sum_kda = 0
gold_top_sum_totalDamageDealtToChampions = 0
gold_top_sum_totalDamageTaken = 0
gold_top_sum_totaloHeal = 0
gold_top_sum_visionScore = 0
gold_top_sum_goldEarned = 0
gold_top_sum_turretKills = 0
gold_top_sum_totalMinionsKilled = 0
gold_top_sum_champLevel = 0

gold_bottom_car_sum_kda = 0
gold_bottom_car_sum_totalDamageDealtToChampions = 0
gold_bottom_car_sum_totalDamageTaken = 0
gold_bottom_car_sum_totaloHeal = 0
gold_bottom_car_sum_visionScore = 0
gold_bottom_car_sum_goldEarned = 0
gold_bottom_car_sum_turretKills = 0
gold_bottom_car_sum_totalMinionsKilled = 0
gold_bottom_car_sum_champLevel = 0

gold_bottom_sup_sum_kda = 0
gold_bottom_sup_sum_totalDamageDealtToChampions = 0
gold_bottom_sup_sum_totalDamageTaken = 0
gold_bottom_sup_sum_totaloHeal = 0
gold_bottom_sup_sum_visionScore = 0
gold_bottom_sup_sum_goldEarned = 0
gold_bottom_sup_sum_turretKills = 0
gold_bottom_sup_sum_totalMinionsKilled = 0
gold_bottom_sup_sum_champLevel = 0



platinum_jungle_sum_kda = 0
platinum_jungle_sum_totalDamageDealtToChampions = 0
platinum_jungle_sum_totalDamageTaken = 0
platinum_jungle_sum_totaloHeal = 0
platinum_jungle_sum_visionScore = 0
platinum_jungle_sum_goldEarned = 0
platinum_jungle_sum_turretKills = 0
platinum_jungle_sum_totalMinionsKilled = 0
platinum_jungle_sum_champLevel = 0

platinum_middle_sum_kda = 0
platinum_middle_sum_totalDamageDealtToChampions = 0
platinum_middle_sum_totalDamageTaken = 0
platinum_middle_sum_totaloHeal = 0
platinum_middle_sum_visionScore = 0
platinum_middle_sum_goldEarned = 0
platinum_middle_sum_turretKills = 0
platinum_middle_sum_totalMinionsKilled = 0
platinum_middle_sum_champLevel = 0

platinum_top_sum_kda = 0
platinum_top_sum_totalDamageDealtToChampions = 0
platinum_top_sum_totalDamageTaken = 0
platinum_top_sum_totaloHeal = 0
platinum_top_sum_visionScore = 0
platinum_top_sum_goldEarned = 0
platinum_top_sum_turretKills = 0
platinum_top_sum_totalMinionsKilled = 0
platinum_top_sum_champLevel = 0

platinum_bottom_car_sum_kda = 0
platinum_bottom_car_sum_totalDamageDealtToChampions = 0
platinum_bottom_car_sum_totalDamageTaken = 0
platinum_bottom_car_sum_totaloHeal = 0
platinum_bottom_car_sum_visionScore = 0
platinum_bottom_car_sum_goldEarned = 0
platinum_bottom_car_sum_turretKills = 0
platinum_bottom_car_sum_totalMinionsKilled = 0
platinum_bottom_car_sum_champLevel = 0

platinum_bottom_sup_sum_kda = 0
platinum_bottom_sup_sum_totalDamageDealtToChampions = 0
platinum_bottom_sup_sum_totalDamageTaken = 0
platinum_bottom_sup_sum_totaloHeal = 0
platinum_bottom_sup_sum_visionScore = 0
platinum_bottom_sup_sum_goldEarned = 0
platinum_bottom_sup_sum_turretKills = 0
platinum_bottom_sup_sum_totalMinionsKilled = 0
platinum_bottom_sup_sum_champLevel = 0


dia_jungle_sum_kda = 0
dia_jungle_sum_totalDamageDealtToChampions = 0
dia_jungle_sum_totalDamageTaken = 0
dia_jungle_sum_totaloHeal = 0
dia_jungle_sum_visionScore = 0
dia_jungle_sum_goldEarned = 0
dia_jungle_sum_turretKills = 0
dia_jungle_sum_totalMinionsKilled = 0
dia_jungle_sum_champLevel = 0

dia_middle_sum_kda = 0
dia_middle_sum_totalDamageDealtToChampions = 0
dia_middle_sum_totalDamageTaken = 0
dia_middle_sum_totaloHeal = 0
dia_middle_sum_visionScore = 0
dia_middle_sum_goldEarned = 0
dia_middle_sum_turretKills = 0
dia_middle_sum_totalMinionsKilled = 0
dia_middle_sum_champLevel = 0

dia_top_sum_kda = 0
dia_top_sum_totalDamageDealtToChampions = 0
dia_top_sum_totalDamageTaken = 0
dia_top_sum_totaloHeal = 0
dia_top_sum_visionScore = 0
dia_top_sum_goldEarned = 0
dia_top_sum_turretKills = 0
dia_top_sum_totalMinionsKilled = 0
dia_top_sum_champLevel = 0

dia_bottom_car_sum_kda = 0
dia_bottom_car_sum_totalDamageDealtToChampions = 0
dia_bottom_car_sum_totalDamageTaken = 0
dia_bottom_car_sum_totaloHeal = 0
dia_bottom_car_sum_visionScore = 0
dia_bottom_car_sum_goldEarned = 0
dia_bottom_car_sum_turretKills = 0
dia_bottom_car_sum_totalMinionsKilled = 0
dia_bottom_car_sum_champLevel = 0

dia_bottom_sup_sum_kda = 0
dia_bottom_sup_sum_totalDamageDealtToChampions = 0
dia_bottom_sup_sum_totalDamageTaken = 0
dia_bottom_sup_sum_totaloHeal = 0
dia_bottom_sup_sum_visionScore = 0
dia_bottom_sup_sum_goldEarned = 0
dia_bottom_sup_sum_turretKills = 0
dia_bottom_sup_sum_totalMinionsKilled = 0
dia_bottom_sup_sum_champLevel = 0


master_jungle_sum_kda = 0
master_jungle_sum_totalDamageDealtToChampions = 0
master_jungle_sum_totalDamageTaken = 0
master_jungle_sum_totaloHeal = 0
master_jungle_sum_visionScore = 0
master_jungle_sum_goldEarned = 0
master_jungle_sum_turretKills = 0
master_jungle_sum_totalMinionsKilled = 0
master_jungle_sum_champLevel = 0

master_middle_sum_kda = 0
master_middle_sum_totalDamageDealtToChampions = 0
master_middle_sum_totalDamageTaken = 0
master_middle_sum_totaloHeal = 0
master_middle_sum_visionScore = 0
master_middle_sum_goldEarned = 0
master_middle_sum_turretKills = 0
master_middle_sum_totalMinionsKilled = 0
master_middle_sum_champLevel = 0

master_top_sum_kda = 0
master_top_sum_totalDamageDealtToChampions = 0
master_top_sum_totalDamageTaken = 0
master_top_sum_totaloHeal = 0
master_top_sum_visionScore = 0
master_top_sum_goldEarned = 0
master_top_sum_turretKills = 0
master_top_sum_totalMinionsKilled = 0
master_top_sum_champLevel = 0

master_bottom_car_sum_kda = 0
master_bottom_car_sum_totalDamageDealtToChampions = 0
master_bottom_car_sum_totalDamageTaken = 0
master_bottom_car_sum_totaloHeal = 0
master_bottom_car_sum_visionScore = 0
master_bottom_car_sum_goldEarned = 0
master_bottom_car_sum_turretKills = 0
master_bottom_car_sum_totalMinionsKilled = 0
master_bottom_car_sum_champLevel = 0

master_bottom_sup_sum_kda = 0
master_bottom_sup_sum_totalDamageDealtToChampions = 0
master_bottom_sup_sum_totalDamageTaken = 0
master_bottom_sup_sum_totaloHeal = 0
master_bottom_sup_sum_visionScore = 0
master_bottom_sup_sum_goldEarned = 0
master_bottom_sup_sum_turretKills = 0
master_bottom_sup_sum_totalMinionsKilled = 0
master_bottom_sup_sum_champLevel = 0

iron_jungle_num=0
iron_middle_num=0
iron_top_num=0
iron_bottom_car_num=0
iron_bottom_sup_num=0

bronze_jungle_num=0
bronze_middle_num=0
bronze_top_num=0
bronze_bottom_car_num=0
bronze_bottom_sup_num=0

silver_jungle_num=0
silver_middle_num=0
silver_top_num=0
silver_bottom_car_num=0
silver_bottom_sup_num=0

gold_jungle_num=0
gold_middle_num=0
gold_top_num=0
gold_bottom_car_num=0
gold_bottom_sup_num=0

platinum_jungle_num=0
platinum_middle_num=0
platinum_top_num=0
platinum_bottom_car_num=0
platinum_bottom_sup_num=0

dia_jungle_num=0
dia_middle_num=0
dia_top_num=0
dia_bottom_car_num=0
dia_bottom_sup_num=0

master_jungle_num=0
master_middle_num=0
master_top_num=0
master_bottom_car_num=0
master_bottom_sup_num=0



#IRON
for i in range(20):
    data_iron = pd.read_csv('C:\\Users\q\PycharmProjects\\tensorflowpractice\\lol\\iron' + str(i) + '.csv', sep=',',dtype='unicode')
    for j in range(10):
        data_col_kills = data_iron[["participants." + str(j)+ ".stats.kills"]]
        data_col_deaths = data_iron[["participants." + str(j)+ ".stats.deaths"]]
        data_col_assists = data_iron[["participants." + str(j)+ ".stats.assists"]]
        data_col_totalDamageDealtToChampions = data_iron[["participants." + str(j)+ ".stats.totalDamageDealtToChampions"]]
        data_col_totalDamageTaken = data_iron[["participants." + str(j)+ ".stats.totalDamageTaken"]]
        data_col_totalHeal = data_iron[["participants." + str(j)+ ".stats.totalHeal"]]
        data_col_visionScore = data_iron[["participants." + str(j)+ ".stats.visionScore"]]
        data_col_goldEarned = data_iron[["participants." + str(j)+ ".stats.goldEarned"]]
        data_col_turretKills = data_iron[["participants." + str(j)+ ".stats.turretKills"]]
        data_col_totalMinionsKilled = data_iron[["participants." + str(j)+ ".stats.totalMinionsKilled"]]
        data_col_champLevel = data_iron[["participants." + str(j)+ ".stats.champLevel"]]
        data_col_timeline_lane = data_iron[["participants." + str(j)+ ".timeline.lane"]]
        data_col_timeline_role = data_iron[["participants." + str(j)+ ".timeline.role"]]
        data_col_gameId = data_iron[["gameId"]]
        data_col_gameDuration = data_iron[["gameDuration"]]
        data_col_Tier = 'iron'



        kills= float(list(data_col_kills.values)[0][0])
        deaths = float(list(data_col_deaths.values)[0][0])
        assists= float(list(data_col_assists.values)[0][0])
        if(deaths==0):
            kda = (kills + assists)*1.5

        else:
            kda = (kills+assists)/deaths
        duration = float(list(data_col_gameDuration.values)[0][0])
        lane = str(list(data_col_timeline_lane.values)[0][0])
        role = str(list(data_col_timeline_role.values)[0][0])



        #JUNGLE    BOTTOM     MIDDLE  TOP
        if(lane=='JUNGLE'):
            Jungle_list_kda.append(kda)
            Jungle_list_totalDamageDealtToChampions.append(
                (float(list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60)
            Jungle_list_totalDamageTaken.append((float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60)
            Jungle_list_totalHeal.append((float(list(data_col_totalHeal.values)[0][0])) / duration * 60)
            Jungle_list_visionScore.append((float(list(data_col_visionScore.values)[0][0])) / duration * 60)
            Jungle_list_goldEarned.append((float(list(data_col_goldEarned.values)[0][0])) / duration * 60)
            Jungle_list_turretKills.append((float(list(data_col_turretKills.values)[0][0])) / duration * 60)
            Jungle_list_totalMinionsKilled.append((float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60)
            Jungle_list_champLevel.append((float(list(data_col_champLevel.values)[0][0])) / duration * 60)
            Jungle_list_col_Tier.append(10)

            iron_jungle_sum_kda += kda
            iron_jungle_sum_totalDamageDealtToChampions += (float(
                list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60
            iron_jungle_sum_totalDamageTaken += (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60
            iron_jungle_sum_totaloHeal += (float(list(data_col_totalHeal.values)[0][0])) / duration * 60
            iron_jungle_sum_visionScore += (float(list(data_col_visionScore.values)[0][0])) / duration * 60
            iron_jungle_sum_goldEarned += (float(list(data_col_goldEarned.values)[0][0])) / duration * 60
            iron_jungle_sum_turretKills += (float(list(data_col_turretKills.values)[0][0])) / duration * 60
            iron_jungle_sum_totalMinionsKilled += (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60
            iron_jungle_sum_champLevel += (float(list(data_col_champLevel.values)[0][0])) / duration * 60
            iron_jungle_num +=1

        elif (lane == 'MIDDLE'):
            Mid_list_kda.append(kda)
            Mid_list_totalDamageDealtToChampions.append(
                (float(list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60)
            Mid_list_totalDamageTaken.append(
                (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60)
            Mid_list_totalHeal.append((float(list(data_col_totalHeal.values)[0][0])) / duration * 60)
            Mid_list_visionScore.append((float(list(data_col_visionScore.values)[0][0])) / duration * 60)
            Mid_list_goldEarned.append((float(list(data_col_goldEarned.values)[0][0])) / duration * 60)
            Mid_list_turretKills.append((float(list(data_col_turretKills.values)[0][0])) / duration * 60)
            Mid_list_totalMinionsKilled.append(
                (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60)
            Mid_list_champLevel.append((float(list(data_col_champLevel.values)[0][0])) / duration * 60)

            Mid_list_col_Tier.append(10)
            iron_middle_sum_kda += kda
            iron_middle_sum_totalDamageDealtToChampions += (float(
                list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60
            iron_middle_sum_totalDamageTaken += (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60
            iron_middle_sum_totaloHeal += (float(list(data_col_totalHeal.values)[0][0])) / duration * 60
            iron_middle_sum_visionScore += (float(list(data_col_visionScore.values)[0][0])) / duration * 60
            iron_middle_sum_goldEarned += (float(list(data_col_goldEarned.values)[0][0])) / duration * 60
            iron_middle_sum_turretKills += (float(list(data_col_turretKills.values)[0][0])) / duration * 60
            iron_middle_sum_totalMinionsKilled += (float(
                list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60
            iron_middle_sum_champLevel += (float(list(data_col_champLevel.values)[0][0])) / duration * 60
            iron_middle_num +=1



        elif(lane == 'TOP'):
            Top_list_kda.append(kda)
            Top_list_totalDamageDealtToChampions.append(
                (float(list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60)
            Top_list_totalDamageTaken.append(
                (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60)
            Top_list_totalHeal.append((float(list(data_col_totalHeal.values)[0][0])) / duration * 60)
            Top_list_visionScore.append((float(list(data_col_visionScore.values)[0][0])) / duration * 60)
            Top_list_goldEarned.append((float(list(data_col_goldEarned.values)[0][0])) / duration * 60)
            Top_list_turretKills.append((float(list(data_col_turretKills.values)[0][0])) / duration * 60)
            Top_list_totalMinionsKilled.append(
                (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60)
            Top_list_champLevel.append((float(list(data_col_champLevel.values)[0][0])) / duration * 60)
            Top_list_col_Tier.append(10)

            iron_top_sum_kda += kda
            iron_top_sum_totalDamageDealtToChampions += (float(
                list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60
            iron_top_sum_totalDamageTaken += (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60
            iron_top_sum_totaloHeal += (float(list(data_col_totalHeal.values)[0][0])) / duration * 60
            iron_top_sum_visionScore += (float(list(data_col_visionScore.values)[0][0])) / duration * 60
            iron_top_sum_goldEarned += (float(list(data_col_goldEarned.values)[0][0])) / duration * 60
            iron_top_sum_turretKills += (float(list(data_col_turretKills.values)[0][0])) / duration * 60
            iron_top_sum_totalMinionsKilled += (float(
                list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60
            iron_top_sum_champLevel += (float(list(data_col_champLevel.values)[0][0])) / duration * 60
            iron_top_num +=1

        elif(lane == "BOTTOM"):
            if(role == 'DUO_CARRY'):
                Bot_list_kda.append(kda)
                Bot_list_totalDamageDealtToChampions.append(
                    (float(list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60)
                Bot_list_totalDamageTaken.append(
                    (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60)
                Bot_list_totalHeal.append((float(list(data_col_totalHeal.values)[0][0])) / duration * 60)
                Bot_list_visionScore.append((float(list(data_col_visionScore.values)[0][0])) / duration * 60)
                Bot_list_goldEarned.append((float(list(data_col_goldEarned.values)[0][0])) / duration * 60)
                Bot_list_turretKills.append((float(list(data_col_turretKills.values)[0][0])) / duration * 60)
                Bot_list_totalMinionsKilled.append(
                    (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60)
                Bot_list_champLevel.append((float(list(data_col_champLevel.values)[0][0])) / duration * 60)
                Bot_list_col_Tier.append(10)
                iron_bottom_car_sum_kda += kda
                iron_bottom_car_sum_totalDamageDealtToChampions += (float(
                    list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60
                iron_bottom_car_sum_totalDamageTaken += (float(
                    list(data_col_totalDamageTaken.values)[0][0])) / duration * 60
                iron_bottom_car_sum_totaloHeal += (float(list(data_col_totalHeal.values)[0][0])) / duration * 60
                iron_bottom_car_sum_visionScore += (float(list(data_col_visionScore.values)[0][0])) / duration * 60
                iron_bottom_car_sum_goldEarned += (float(list(data_col_goldEarned.values)[0][0])) / duration * 60
                iron_bottom_car_sum_turretKills += (float(list(data_col_turretKills.values)[0][0])) / duration * 60
                iron_bottom_car_sum_totalMinionsKilled += (float(
                    list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60
                iron_bottom_car_sum_champLevel += (float(list(data_col_champLevel.values)[0][0])) / duration * 60
                iron_bottom_car_num +=1
            elif(role == 'DUO_SUPPORT'):
                Sup_list_kda.append(kda)
                Sup_list_totalDamageDealtToChampions.append(
                    (float(list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60)
                Sup_list_totalDamageTaken.append(
                    (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60)
                Sup_list_totalHeal.append((float(list(data_col_totalHeal.values)[0][0])) / duration * 60)
                Sup_list_visionScore.append((float(list(data_col_visionScore.values)[0][0])) / duration * 60)
                Sup_list_goldEarned.append((float(list(data_col_goldEarned.values)[0][0])) / duration * 60)
                Sup_list_turretKills.append((float(list(data_col_turretKills.values)[0][0])) / duration * 60)
                Sup_list_totalMinionsKilled.append(
                    (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60)
                Sup_list_champLevel.append((float(list(data_col_champLevel.values)[0][0])) / duration * 60)
                Sup_list_col_Tier.append(10)
                iron_bottom_sup_sum_kda += kda
                iron_bottom_sup_sum_totalDamageDealtToChampions += (float(
                    list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60
                iron_bottom_sup_sum_totalDamageTaken += (float(
                    list(data_col_totalDamageTaken.values)[0][0])) / duration * 60
                iron_bottom_sup_sum_totaloHeal += (float(list(data_col_totalHeal.values)[0][0])) / duration * 60
                iron_bottom_sup_sum_visionScore += (float(list(data_col_visionScore.values)[0][0])) / duration * 60
                iron_bottom_sup_sum_goldEarned += (float(list(data_col_goldEarned.values)[0][0])) / duration * 60
                iron_bottom_sup_sum_turretKills += (float(list(data_col_turretKills.values)[0][0])) / duration * 60
                iron_bottom_sup_sum_totalMinionsKilled += (float(
                    list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60
                iron_bottom_sup_sum_champLevel += (float(list(data_col_champLevel.values)[0][0])) / duration * 60
                iron_bottom_sup_num +=1
        else:
            print("망함")


#BRONZE
for i in range(20):
    data_bronze = pd.read_csv('C:\\Users\q\PycharmProjects\\tensorflowpractice\\lol\\bronze' + str(i) + '.csv', sep=',',dtype='unicode')
    for j in range(10):
        data_col_kills = data_bronze[["participants." + str(j)+ ".stats.kills"]]
        data_col_deaths = data_bronze[["participants." + str(j)+ ".stats.deaths"]]
        data_col_assists = data_bronze[["participants." + str(j)+ ".stats.assists"]]
        data_col_totalDamageDealtToChampions = data_bronze[["participants." + str(j)+ ".stats.totalDamageDealtToChampions"]]
        data_col_totalDamageTaken = data_bronze[["participants." + str(j)+ ".stats.totalDamageTaken"]]
        data_col_totalHeal = data_bronze[["participants." + str(j)+ ".stats.totalHeal"]]
        data_col_visionScore = data_bronze[["participants." + str(j)+ ".stats.visionScore"]]
        data_col_goldEarned = data_bronze[["participants." + str(j)+ ".stats.goldEarned"]]
        data_col_turretKills = data_bronze[["participants." + str(j)+ ".stats.turretKills"]]
        data_col_totalMinionsKilled =data_bronze[["participants." + str(j)+ ".stats.totalMinionsKilled"]]
        data_col_champLevel = data_bronze[["participants." + str(j)+ ".stats.champLevel"]]
        data_col_timeline_lane = data_bronze[["participants." + str(j)+ ".timeline.lane"]]
        data_col_timeline_role = data_bronze[["participants." + str(j)+ ".timeline.role"]]
        data_col_gameId = data_bronze[["gameId"]]
        data_col_gameDuration = data_bronze[["gameDuration"]]
        data_col_Tier = 'bronze'



        kills = float(list(data_col_kills.values)[0][0])
        deaths = float(list(data_col_deaths.values)[0][0])
        assists = float(list(data_col_assists.values)[0][0])

        if (deaths == 0):
            kda = (kills + assists) * 1.5
        else:
            kda = (kills + assists) / deaths
        duration = float(list(data_col_gameDuration.values)[0][0])
        lane = str(list(data_col_timeline_lane.values)[0][0])
        role = str(list(data_col_timeline_role.values)[0][0])


        if (lane == 'JUNGLE'):
            Jungle_list_kda.append(kda)
            Jungle_list_totalDamageDealtToChampions.append(
                (float(list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60)
            Jungle_list_totalDamageTaken.append((float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60)
            Jungle_list_totalHeal.append((float(list(data_col_totalHeal.values)[0][0])) / duration * 60)
            Jungle_list_visionScore.append((float(list(data_col_visionScore.values)[0][0])) / duration * 60)
            Jungle_list_goldEarned.append((float(list(data_col_goldEarned.values)[0][0])) / duration * 60)
            Jungle_list_turretKills.append((float(list(data_col_turretKills.values)[0][0])) / duration * 60)
            Jungle_list_totalMinionsKilled.append(
                (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60)
            Jungle_list_champLevel.append((float(list(data_col_champLevel.values)[0][0])) / duration * 60)
            Jungle_list_col_Tier.append(20)

            bronze_jungle_sum_kda += kda
            bronze_jungle_sum_totalDamageDealtToChampions += (float(
                list(data_col_totalDamageDealtToChampions.values)[0][0]) / duration * 60)
            bronze_jungle_sum_totalDamageTaken += (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60
            bronze_jungle_sum_totaloHeal += (float(list(data_col_totalHeal.values)[0][0])) / duration * 60
            bronze_jungle_sum_visionScore += (float(list(data_col_visionScore.values)[0][0])) / duration * 60
            bronze_jungle_sum_goldEarned += (float(list(data_col_goldEarned.values)[0][0])) / duration * 60
            bronze_jungle_sum_turretKills += (float(list(data_col_turretKills.values)[0][0])) / duration * 60
            bronze_jungle_sum_totalMinionsKilled += (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60
            bronze_jungle_sum_champLevel += (float(list(data_col_champLevel.values)[0][0])) / duration * 60
            bronze_jungle_num +=1


        elif (lane == 'MIDDLE'):
            Mid_list_kda.append(kda)
            Mid_list_totalDamageDealtToChampions.append(
                (float(list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60)
            Mid_list_totalDamageTaken.append(
                (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60)
            Mid_list_totalHeal.append((float(list(data_col_totalHeal.values)[0][0])) / duration * 60)
            Mid_list_visionScore.append((float(list(data_col_visionScore.values)[0][0])) / duration * 60)
            Mid_list_goldEarned.append((float(list(data_col_goldEarned.values)[0][0])) / duration * 60)
            Mid_list_turretKills.append((float(list(data_col_turretKills.values)[0][0])) / duration * 60)
            Mid_list_totalMinionsKilled.append(
                (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60)
            Mid_list_champLevel.append((float(list(data_col_champLevel.values)[0][0])) / duration * 60)
            Mid_list_col_Tier.append(20)

            bronze_middle_sum_kda += kda
            bronze_middle_sum_totalDamageDealtToChampions += (float(
                list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60
            bronze_middle_sum_totalDamageTaken += (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60
            bronze_middle_sum_totaloHeal += (float(list(data_col_totalHeal.values)[0][0])) / duration * 60
            bronze_middle_sum_visionScore += (float(list(data_col_visionScore.values)[0][0])) / duration * 60
            bronze_middle_sum_goldEarned += (float(list(data_col_goldEarned.values)[0][0])) / duration * 60
            bronze_middle_sum_turretKills += (float(list(data_col_turretKills.values)[0][0])) / duration * 60
            bronze_middle_sum_totalMinionsKilled += (float(
                list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60
            bronze_middle_sum_champLevel += (float(list(data_col_champLevel.values)[0][0])) / duration * 60
            bronze_middle_num +=1

        elif (lane == 'TOP'):
            Top_list_kda.append(kda)
            Top_list_totalDamageDealtToChampions.append(
                (float(list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60)
            Top_list_totalDamageTaken.append(
                (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60)
            Top_list_totalHeal.append((float(list(data_col_totalHeal.values)[0][0])) / duration * 60)
            Top_list_visionScore.append((float(list(data_col_visionScore.values)[0][0])) / duration * 60)
            Top_list_goldEarned.append((float(list(data_col_goldEarned.values)[0][0])) / duration * 60)
            Top_list_turretKills.append((float(list(data_col_turretKills.values)[0][0])) / duration * 60)
            Top_list_totalMinionsKilled.append(
                (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60)
            Top_list_champLevel.append((float(list(data_col_champLevel.values)[0][0])) / duration * 60)
            Top_list_col_Tier.append(20)

            bronze_top_sum_kda += kda
            bronze_top_sum_totalDamageDealtToChampions += (float(list(data_col_totalDamageDealtToChampions.values)[0][0]) / duration * 60)
            bronze_top_sum_totalDamageTaken += (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60
            bronze_top_sum_totaloHeal += (float(list(data_col_totalHeal.values)[0][0])) / duration * 60
            bronze_top_sum_visionScore += (float(list(data_col_visionScore.values)[0][0])) / duration * 60
            bronze_top_sum_goldEarned += (float(list(data_col_goldEarned.values)[0][0])) / duration * 60
            bronze_top_sum_turretKills += (float(list(data_col_turretKills.values)[0][0])) / duration * 60
            bronze_top_sum_totalMinionsKilled += (float(
                list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60
            bronze_top_sum_champLevel += (float(list(data_col_champLevel.values)[0][0])) / duration * 60
            bronze_top_num +=1


        elif (lane == "BOTTOM"):
            if (role == 'DUO_CARRY'):
                Bot_list_kda.append(kda)
                Bot_list_totalDamageDealtToChampions.append(
                    (float(list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60)
                Bot_list_totalDamageTaken.append(
                    (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60)
                Bot_list_totalHeal.append((float(list(data_col_totalHeal.values)[0][0])) / duration * 60)
                Bot_list_visionScore.append((float(list(data_col_visionScore.values)[0][0])) / duration * 60)
                Bot_list_goldEarned.append((float(list(data_col_goldEarned.values)[0][0])) / duration * 60)
                Bot_list_turretKills.append((float(list(data_col_turretKills.values)[0][0])) / duration * 60)
                Bot_list_totalMinionsKilled.append(
                    (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60)
                Bot_list_champLevel.append((float(list(data_col_champLevel.values)[0][0])) / duration * 60)
                Bot_list_col_Tier.append(20)
                bronze_bottom_car_sum_kda += kda
                bronze_bottom_car_sum_totalDamageDealtToChampions += (float(
                    list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60
                bronze_bottom_car_sum_totalDamageTaken += (float(
                    list(data_col_totalDamageTaken.values)[0][0])) / duration * 60
                bronze_bottom_car_sum_totaloHeal += (float(list(data_col_totalHeal.values)[0][0])) / duration * 60
                bronze_bottom_car_sum_visionScore += (float(list(data_col_visionScore.values)[0][0])) / duration * 60
                bronze_bottom_car_sum_goldEarned += (float(list(data_col_goldEarned.values)[0][0])) / duration * 60
                bronze_bottom_car_sum_turretKills += (float(list(data_col_turretKills.values)[0][0])) / duration * 60
                bronze_bottom_car_sum_totalMinionsKilled += (float(
                    list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60
                bronze_bottom_car_sum_champLevel += (float(list(data_col_champLevel.values)[0][0])) / duration * 60
                bronze_bottom_car_num +=1
            elif (role == 'DUO_SUPPORT'):
                Sup_list_kda.append(kda)
                Sup_list_totalDamageDealtToChampions.append(
                    (float(list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60)
                Sup_list_totalDamageTaken.append(
                    (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60)
                Sup_list_totalHeal.append((float(list(data_col_totalHeal.values)[0][0])) / duration * 60)
                Sup_list_visionScore.append((float(list(data_col_visionScore.values)[0][0])) / duration * 60)
                Sup_list_goldEarned.append((float(list(data_col_goldEarned.values)[0][0])) / duration * 60)
                Sup_list_turretKills.append((float(list(data_col_turretKills.values)[0][0])) / duration * 60)
                Sup_list_totalMinionsKilled.append(
                    (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60)
                Sup_list_champLevel.append((float(list(data_col_champLevel.values)[0][0])) / duration * 60)
                Sup_list_col_Tier.append(20)
                bronze_bottom_sup_sum_kda += kda
                bronze_bottom_sup_sum_totalDamageDealtToChampions += (float(
                    list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60
                bronze_bottom_sup_sum_totalDamageTaken += (float(
                    list(data_col_totalDamageTaken.values)[0][0])) / duration * 60
                bronze_bottom_sup_sum_totaloHeal += (float(list(data_col_totalHeal.values)[0][0])) / duration * 60
                bronze_bottom_sup_sum_visionScore += (float(list(data_col_visionScore.values)[0][0])) / duration * 60
                bronze_bottom_sup_sum_goldEarned += (float(list(data_col_goldEarned.values)[0][0])) / duration * 60
                bronze_bottom_sup_sum_turretKills += (float(list(data_col_turretKills.values)[0][0])) / duration * 60
                bronze_bottom_sup_sum_totalMinionsKilled += (float(
                    list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60
                bronze_bottom_sup_sum_champLevel += (float(list(data_col_champLevel.values)[0][0])) / duration * 60
                bronze_bottom_sup_num +=1
        else:
            print("망함")

#SILVER
for i in range(20):
    data_silver = pd.read_csv('C:\\Users\q\PycharmProjects\\tensorflowpractice\\lol\\silver' + str(i) + '.csv', sep=',',dtype='unicode')
    for j in range(10):
        data_col_kills = data_silver[["participants." + str(j)+ ".stats.kills"]]
        data_col_deaths = data_silver[["participants." + str(j)+ ".stats.deaths"]]
        data_col_assists = data_silver[["participants." + str(j)+ ".stats.assists"]]
        data_col_totalDamageDealtToChampions = data_silver[
            ["participants." + str(j)+ ".stats.totalDamageDealtToChampions"]]
        data_col_totalDamageTaken = data_silver[["participants." + str(j)+ ".stats.totalDamageTaken"]]
        data_col_totalHeal = data_silver[["participants." + str(j)+ ".stats.totalHeal"]]
        data_col_visionScore = data_silver[["participants." + str(j)+ ".stats.visionScore"]]
        data_col_goldEarned = data_silver[["participants." + str(j)+ ".stats.goldEarned"]]
        data_col_turretKills = data_silver[["participants." + str(j)+ ".stats.turretKills"]]
        data_col_totalMinionsKilled = data_silver[["participants." + str(j)+ ".stats.totalMinionsKilled"]]
        data_col_champLevel = data_silver[["participants." + str(j)+ ".stats.champLevel"]]
        data_col_timeline_lane = data_silver[["participants." + str(j)+ ".timeline.lane"]]
        data_col_timeline_role = data_silver[["participants." + str(j)+ ".timeline.role"]]
        data_col_gameId = data_silver[["gameId"]]
        data_col_gameDuration = data_silver[["gameDuration"]]
        data_col_Tier = 'silver'


        kills = float(list(data_col_kills.values)[0][0])
        deaths = float(list(data_col_deaths.values)[0][0])
        assists = float(list(data_col_assists.values)[0][0])
        if (deaths == 0):
            kda = (kills + assists) * 1.5
        else:
            kda = (kills + assists) / deaths
        duration = float(list(data_col_gameDuration.values)[0][0])
        lane = str(list(data_col_timeline_lane.values)[0][0])
        role = str(list(data_col_timeline_role.values)[0][0])


        if (lane == 'JUNGLE'):
            Jungle_list_kda.append(kda)
            Jungle_list_totalDamageDealtToChampions.append(
                (float(list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60)
            Jungle_list_totalDamageTaken.append((float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60)
            Jungle_list_totalHeal.append((float(list(data_col_totalHeal.values)[0][0])) / duration * 60)
            Jungle_list_visionScore.append((float(list(data_col_visionScore.values)[0][0])) / duration * 60)
            Jungle_list_goldEarned.append((float(list(data_col_goldEarned.values)[0][0])) / duration * 60)
            Jungle_list_turretKills.append((float(list(data_col_turretKills.values)[0][0])) / duration * 60)
            Jungle_list_totalMinionsKilled.append(
                (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60)
            Jungle_list_champLevel.append((float(list(data_col_champLevel.values)[0][0])) / duration * 60)
            Jungle_list_col_Tier.append(30)

            silver_jungle_sum_kda += kda
            silver_jungle_sum_totalDamageDealtToChampions += (float(
                list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60
            silver_jungle_sum_totalDamageTaken += (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60
            silver_jungle_sum_totaloHeal += (float(list(data_col_totalHeal.values)[0][0])) / duration * 60
            silver_jungle_sum_visionScore += (float(list(data_col_visionScore.values)[0][0])) / duration * 60
            silver_jungle_sum_goldEarned += (float(list(data_col_goldEarned.values)[0][0])) / duration * 60
            silver_jungle_sum_turretKills += (float(list(data_col_turretKills.values)[0][0])) / duration * 60
            silver_jungle_sum_totalMinionsKilled += (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60
            silver_jungle_sum_champLevel += (float(list(data_col_champLevel.values)[0][0])) / duration * 60
            silver_jungle_num +=1

        elif (lane == 'MIDDLE'):
            Mid_list_kda.append(kda)
            Mid_list_totalDamageDealtToChampions.append(
                (float(list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60)
            Mid_list_totalDamageTaken.append(
                (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60)
            Mid_list_totalHeal.append((float(list(data_col_totalHeal.values)[0][0])) / duration * 60)
            Mid_list_visionScore.append((float(list(data_col_visionScore.values)[0][0])) / duration * 60)
            Mid_list_goldEarned.append((float(list(data_col_goldEarned.values)[0][0])) / duration * 60)
            Mid_list_turretKills.append((float(list(data_col_turretKills.values)[0][0])) / duration * 60)
            Mid_list_totalMinionsKilled.append(
                (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60)
            Mid_list_champLevel.append((float(list(data_col_champLevel.values)[0][0])) / duration * 60)
            Mid_list_col_Tier.append(30)

            silver_middle_sum_kda += kda
            silver_middle_sum_totalDamageDealtToChampions += (float(
                list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60
            silver_middle_sum_totalDamageTaken += (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60
            silver_middle_sum_totaloHeal += (float(list(data_col_totalHeal.values)[0][0])) / duration * 60
            silver_middle_sum_visionScore += (float(list(data_col_visionScore.values)[0][0])) / duration * 60
            silver_middle_sum_goldEarned += (float(list(data_col_goldEarned.values)[0][0])) / duration * 60
            silver_middle_sum_turretKills += (float(list(data_col_turretKills.values)[0][0])) / duration * 60
            silver_middle_sum_totalMinionsKilled += (float(
                list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60
            silver_middle_sum_champLevel += (float(list(data_col_champLevel.values)[0][0])) / duration * 60
            silver_middle_num +=1

        elif (lane == 'TOP'):
            Top_list_kda.append(kda)
            Top_list_totalDamageDealtToChampions.append(
                (float(list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60)
            Top_list_totalDamageTaken.append(
                (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60)
            Top_list_totalHeal.append((float(list(data_col_totalHeal.values)[0][0])) / duration * 60)
            Top_list_visionScore.append((float(list(data_col_visionScore.values)[0][0])) / duration * 60)
            Top_list_goldEarned.append((float(list(data_col_goldEarned.values)[0][0])) / duration * 60)
            Top_list_turretKills.append((float(list(data_col_turretKills.values)[0][0])) / duration * 60)
            Top_list_totalMinionsKilled.append(
                (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60)
            Top_list_champLevel.append((float(list(data_col_champLevel.values)[0][0])) / duration * 60)
            Top_list_col_Tier.append(30)

            silver_top_sum_kda += kda
            silver_top_sum_totalDamageDealtToChampions += (float(
                list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60
            silver_top_sum_totalDamageTaken += (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60
            silver_top_sum_totaloHeal += (float(list(data_col_totalHeal.values)[0][0])) / duration * 60
            silver_top_sum_visionScore += (float(list(data_col_visionScore.values)[0][0])) / duration * 60
            silver_top_sum_goldEarned += (float(list(data_col_goldEarned.values)[0][0])) / duration * 60
            silver_top_sum_turretKills += (float(list(data_col_turretKills.values)[0][0])) / duration * 60
            silver_top_sum_totalMinionsKilled += (float(
                list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60
            silver_top_sum_champLevel += (float(list(data_col_champLevel.values)[0][0])) / duration * 60
            silver_top_num +=1



        elif (lane == "BOTTOM"):
            if (role == 'DUO_CARRY'):
                Bot_list_kda.append(kda)
                Bot_list_totalDamageDealtToChampions.append(
                    (float(list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60)
                Bot_list_totalDamageTaken.append(
                    (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60)
                Bot_list_totalHeal.append((float(list(data_col_totalHeal.values)[0][0])) / duration * 60)
                Bot_list_visionScore.append((float(list(data_col_visionScore.values)[0][0])) / duration * 60)
                Bot_list_goldEarned.append((float(list(data_col_goldEarned.values)[0][0])) / duration * 60)
                Bot_list_turretKills.append((float(list(data_col_turretKills.values)[0][0])) / duration * 60)
                Bot_list_totalMinionsKilled.append(
                    (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60)
                Bot_list_champLevel.append((float(list(data_col_champLevel.values)[0][0])) / duration * 60)
                Bot_list_col_Tier.append(30)
                silver_bottom_car_sum_kda += kda
                silver_bottom_car_sum_totalDamageDealtToChampions += (float(
                    list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60
                silver_bottom_car_sum_totalDamageTaken += (float(
                    list(data_col_totalDamageTaken.values)[0][0])) / duration * 60
                silver_bottom_car_sum_totaloHeal += (float(list(data_col_totalHeal.values)[0][0])) / duration * 60
                silver_bottom_car_sum_visionScore += (float(list(data_col_visionScore.values)[0][0])) / duration * 60
                silver_bottom_car_sum_goldEarned += (float(list(data_col_goldEarned.values)[0][0])) / duration * 60
                silver_bottom_car_sum_turretKills += (float(list(data_col_turretKills.values)[0][0])) / duration * 60
                silver_bottom_car_sum_totalMinionsKilled += (float(
                    list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60
                silver_bottom_car_sum_champLevel += (float(list(data_col_champLevel.values)[0][0])) / duration * 60
                silver_bottom_car_num +=1
            elif (role == 'DUO_SUPPORT'):
                Sup_list_kda.append(kda)
                Sup_list_totalDamageDealtToChampions.append(
                    (float(list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60)
                Sup_list_totalDamageTaken.append(
                    (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60)
                Sup_list_totalHeal.append((float(list(data_col_totalHeal.values)[0][0])) / duration * 60)
                Sup_list_visionScore.append((float(list(data_col_visionScore.values)[0][0])) / duration * 60)
                Sup_list_goldEarned.append((float(list(data_col_goldEarned.values)[0][0])) / duration * 60)
                Sup_list_turretKills.append((float(list(data_col_turretKills.values)[0][0])) / duration * 60)
                Sup_list_totalMinionsKilled.append(
                    (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60)
                Sup_list_champLevel.append((float(list(data_col_champLevel.values)[0][0])) / duration * 60)
                Sup_list_col_Tier.append(30)
                silver_bottom_sup_sum_kda += kda
                silver_bottom_sup_sum_totalDamageDealtToChampions += (float(
                    list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60
                silver_bottom_sup_sum_totalDamageTaken += (float(
                    list(data_col_totalDamageTaken.values)[0][0])) / duration * 60
                silver_bottom_sup_sum_totaloHeal += (float(list(data_col_totalHeal.values)[0][0])) / duration * 60
                silver_bottom_sup_sum_visionScore += (float(list(data_col_visionScore.values)[0][0])) / duration * 60
                silver_bottom_sup_sum_goldEarned += (float(list(data_col_goldEarned.values)[0][0])) / duration * 60
                silver_bottom_sup_sum_turretKills += (float(list(data_col_turretKills.values)[0][0])) / duration * 60
                silver_bottom_sup_sum_totalMinionsKilled += (float(
                    list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60
                silver_bottom_sup_sum_champLevel += (float(list(data_col_champLevel.values)[0][0])) / duration * 60
                silver_bottom_sup_num +=1

        else:
            print("망함")

#GOLD
for i in range(20):
    data_gold = pd.read_csv('C:\\Users\q\PycharmProjects\\tensorflowpractice\\lol\\gold' + str(i) + '.csv', sep=',',dtype='unicode')
    for j in range(10):
        data_col_kills = data_gold[["participants." + str(j)+ ".stats.kills"]]
        data_col_deaths =data_gold[["participants." + str(j)+ ".stats.deaths"]]
        data_col_assists = data_gold[["participants." + str(j)+ ".stats.assists"]]
        data_col_totalDamageDealtToChampions = data_gold[
            ["participants." + str(j)+ ".stats.totalDamageDealtToChampions"]]
        data_col_totalDamageTaken = data_gold[["participants." + str(j)+ ".stats.totalDamageTaken"]]
        data_col_totalHeal = data_gold[["participants." + str(j)+ ".stats.totalHeal"]]
        data_col_visionScore = data_gold[["participants." + str(j)+ ".stats.visionScore"]]
        data_col_goldEarned = data_gold[["participants." + str(j)+ ".stats.goldEarned"]]
        data_col_turretKills = data_gold[["participants." + str(j)+ ".stats.turretKills"]]
        data_col_totalMinionsKilled = data_gold[["participants." + str(j)+ ".stats.totalMinionsKilled"]]
        data_col_champLevel = data_gold[["participants." + str(j)+ ".stats.champLevel"]]
        data_col_timeline_lane = data_gold[["participants." + str(j)+ ".timeline.lane"]]
        data_col_timeline_role = data_gold[["participants." + str(j)+ ".timeline.role"]]
        data_col_gameId = data_gold[["gameId"]]
        data_col_gameDuration = data_gold[["gameDuration"]]
        data_col_Tier = 'gold'


        kills = float(list(data_col_kills.values)[0][0])
        deaths = float(list(data_col_deaths.values)[0][0])
        assists = float(list(data_col_assists.values)[0][0])
        if (deaths == 0):
            kda = (kills + assists) * 1.5
        else:
            kda = (kills + assists) / deaths
        duration = float(list(data_col_gameDuration.values)[0][0])
        lane = str(list(data_col_timeline_lane.values)[0][0])
        role = str(list(data_col_timeline_role.values)[0][0])



        if (lane == 'JUNGLE'):
            Jungle_list_kda.append(kda)
            Jungle_list_totalDamageDealtToChampions.append(
                (float(list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60)
            Jungle_list_totalDamageTaken.append((float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60)
            Jungle_list_totalHeal.append((float(list(data_col_totalHeal.values)[0][0])) / duration * 60)
            Jungle_list_visionScore.append((float(list(data_col_visionScore.values)[0][0])) / duration * 60)
            Jungle_list_goldEarned.append((float(list(data_col_goldEarned.values)[0][0])) / duration * 60)
            Jungle_list_turretKills.append((float(list(data_col_turretKills.values)[0][0])) / duration * 60)
            Jungle_list_totalMinionsKilled.append(
                (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60)
            Jungle_list_champLevel.append((float(list(data_col_champLevel.values)[0][0])) / duration * 60)
            Jungle_list_col_Tier.append(40)

            gold_jungle_sum_kda += kda
            gold_jungle_sum_totalDamageDealtToChampions += (float(
                list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60
            gold_jungle_sum_totalDamageTaken += (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60
            gold_jungle_sum_totaloHeal += (float(list(data_col_totalHeal.values)[0][0])) / duration * 60
            gold_jungle_sum_visionScore += (float(list(data_col_visionScore.values)[0][0])) / duration * 60
            gold_jungle_sum_goldEarned += (float(list(data_col_goldEarned.values)[0][0])) / duration * 60
            gold_jungle_sum_turretKills += (float(list(data_col_turretKills.values)[0][0])) / duration * 60
            gold_jungle_sum_totalMinionsKilled += (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60
            gold_jungle_sum_champLevel += (float(list(data_col_champLevel.values)[0][0])) / duration * 60
            gold_jungle_num +=1

        elif (lane == 'MIDDLE'):
            Mid_list_kda.append(kda)
            Mid_list_totalDamageDealtToChampions.append(
                (float(list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60)
            Mid_list_totalDamageTaken.append(
                (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60)
            Mid_list_totalHeal.append((float(list(data_col_totalHeal.values)[0][0])) / duration * 60)
            Mid_list_visionScore.append((float(list(data_col_visionScore.values)[0][0])) / duration * 60)
            Mid_list_goldEarned.append((float(list(data_col_goldEarned.values)[0][0])) / duration * 60)
            Mid_list_turretKills.append((float(list(data_col_turretKills.values)[0][0])) / duration * 60)
            Mid_list_totalMinionsKilled.append(
                (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60)
            Mid_list_champLevel.append((float(list(data_col_champLevel.values)[0][0])) / duration * 60)
            Mid_list_col_Tier.append(40)

            gold_middle_sum_kda += kda
            gold_middle_sum_totalDamageDealtToChampions += (float(
                list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60
            gold_middle_sum_totalDamageTaken += (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60
            gold_middle_sum_totaloHeal += (float(list(data_col_totalHeal.values)[0][0])) / duration * 60
            gold_middle_sum_visionScore += (float(list(data_col_visionScore.values)[0][0])) / duration * 60
            gold_middle_sum_goldEarned += (float(list(data_col_goldEarned.values)[0][0])) / duration * 60
            gold_middle_sum_turretKills += (float(list(data_col_turretKills.values)[0][0])) / duration * 60
            gold_middle_sum_totalMinionsKilled += (float(
                list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60
            gold_middle_sum_champLevel += (float(list(data_col_champLevel.values)[0][0])) / duration * 60
            gold_middle_num +=1

        elif (lane == 'TOP'):
            Top_list_kda.append(kda)
            Top_list_totalDamageDealtToChampions.append(
                (float(list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60)
            Top_list_totalDamageTaken.append(
                (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60)
            Top_list_totalHeal.append((float(list(data_col_totalHeal.values)[0][0])) / duration * 60)
            Top_list_visionScore.append((float(list(data_col_visionScore.values)[0][0])) / duration * 60)
            Top_list_goldEarned.append((float(list(data_col_goldEarned.values)[0][0])) / duration * 60)
            Top_list_turretKills.append((float(list(data_col_turretKills.values)[0][0])) / duration * 60)
            Top_list_totalMinionsKilled.append(
                (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60)
            Top_list_champLevel.append((float(list(data_col_champLevel.values)[0][0])) / duration * 60)
            Top_list_col_Tier.append(40)

            gold_top_sum_kda += kda
            gold_top_sum_totalDamageDealtToChampions += (float(
                list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60
            gold_top_sum_totalDamageTaken += (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60
            gold_top_sum_totaloHeal += (float(list(data_col_totalHeal.values)[0][0])) / duration * 60
            gold_top_sum_visionScore += (float(list(data_col_visionScore.values)[0][0])) / duration * 60
            gold_top_sum_goldEarned += (float(list(data_col_goldEarned.values)[0][0])) / duration * 60
            gold_top_sum_turretKills += (float(list(data_col_turretKills.values)[0][0])) / duration * 60
            gold_top_sum_totalMinionsKilled += (float(
                list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60
            gold_top_sum_champLevel += (float(list(data_col_champLevel.values)[0][0])) / duration * 60
            gold_top_num +=1


        elif (lane == "BOTTOM"):
            if (role == 'DUO_CARRY'):
                Bot_list_kda.append(kda)
                Bot_list_totalDamageDealtToChampions.append(
                    (float(list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60)
                Bot_list_totalDamageTaken.append(
                    (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60)
                Bot_list_totalHeal.append((float(list(data_col_totalHeal.values)[0][0])) / duration * 60)
                Bot_list_visionScore.append((float(list(data_col_visionScore.values)[0][0])) / duration * 60)
                Bot_list_goldEarned.append((float(list(data_col_goldEarned.values)[0][0])) / duration * 60)
                Bot_list_turretKills.append((float(list(data_col_turretKills.values)[0][0])) / duration * 60)
                Bot_list_totalMinionsKilled.append(
                    (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60)
                Bot_list_champLevel.append((float(list(data_col_champLevel.values)[0][0])) / duration * 60)
                Bot_list_col_Tier.append(40)

                gold_bottom_car_sum_kda += kda
                gold_bottom_car_sum_totalDamageDealtToChampions += (float(
                    list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60
                gold_bottom_car_sum_totalDamageTaken += (float(
                    list(data_col_totalDamageTaken.values)[0][0])) / duration * 60
                gold_bottom_car_sum_totaloHeal += (float(list(data_col_totalHeal.values)[0][0])) / duration * 60
                gold_bottom_car_sum_visionScore += (float(list(data_col_visionScore.values)[0][0])) / duration * 60
                gold_bottom_car_sum_goldEarned += (float(list(data_col_goldEarned.values)[0][0])) / duration * 60
                gold_bottom_car_sum_turretKills += (float(list(data_col_turretKills.values)[0][0])) / duration * 60
                gold_bottom_car_sum_totalMinionsKilled += (float(
                    list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60
                gold_bottom_car_sum_champLevel += (float(list(data_col_champLevel.values)[0][0])) / duration * 60
                gold_bottom_car_num +=1
            elif (role == 'DUO_SUPPORT'):
                Sup_list_kda.append(kda)
                Sup_list_totalDamageDealtToChampions.append(
                    (float(list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60)
                Sup_list_totalDamageTaken.append(
                    (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60)
                Sup_list_totalHeal.append((float(list(data_col_totalHeal.values)[0][0])) / duration * 60)
                Sup_list_visionScore.append((float(list(data_col_visionScore.values)[0][0])) / duration * 60)
                Sup_list_goldEarned.append((float(list(data_col_goldEarned.values)[0][0])) / duration * 60)
                Sup_list_turretKills.append((float(list(data_col_turretKills.values)[0][0])) / duration * 60)
                Sup_list_totalMinionsKilled.append(
                    (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60)
                Sup_list_champLevel.append((float(list(data_col_champLevel.values)[0][0])) / duration * 60)
                Sup_list_col_Tier.append(40)

                gold_bottom_sup_sum_kda += kda
                gold_bottom_sup_sum_totalDamageDealtToChampions += (float(
                    list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60
                gold_bottom_sup_sum_totalDamageTaken += (float(
                    list(data_col_totalDamageTaken.values)[0][0])) / duration * 60
                gold_bottom_sup_sum_totaloHeal += (float(list(data_col_totalHeal.values)[0][0])) / duration * 60
                gold_bottom_sup_sum_visionScore += (float(list(data_col_visionScore.values)[0][0])) / duration * 60
                gold_bottom_sup_sum_goldEarned += (float(list(data_col_goldEarned.values)[0][0])) / duration * 60
                gold_bottom_sup_sum_turretKills += (float(list(data_col_turretKills.values)[0][0])) / duration * 60
                gold_bottom_sup_sum_totalMinionsKilled += (float(
                    list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60
                gold_bottom_sup_sum_champLevel += (float(list(data_col_champLevel.values)[0][0])) / duration * 60
                gold_bottom_sup_num =+1
        else:
            print("망함")


#PLATINUM
for i in range(20):
    data_platinum = pd.read_csv('C:\\Users\q\PycharmProjects\\tensorflowpractice\\lol\\platinum' + str(i) + '.csv', sep=',',dtype='unicode')
    for j in range(10):
        data_col_kills = data_platinum[["participants." + str(j)+ ".stats.kills"]]
        data_col_deaths = data_platinum[["participants." + str(j)+ ".stats.deaths"]]
        data_col_assists = data_platinum[["participants." + str(j)+ ".stats.assists"]]
        data_col_totalDamageDealtToChampions = data_platinum[
            ["participants." + str(j)+ ".stats.totalDamageDealtToChampions"]]
        data_col_totalDamageTaken = data_platinum[["participants." + str(j)+ ".stats.totalDamageTaken"]]
        data_col_totalHeal =data_platinum[["participants." + str(j)+ ".stats.totalHeal"]]
        data_col_visionScore = data_platinum[["participants." + str(j)+ ".stats.visionScore"]]
        data_col_goldEarned = data_platinum[["participants." + str(j)+ ".stats.goldEarned"]]
        data_col_turretKills = data_platinum[["participants." + str(j)+ ".stats.turretKills"]]
        data_col_totalMinionsKilled = data_platinum[["participants." + str(j)+ ".stats.totalMinionsKilled"]]
        data_col_champLevel = data_platinum[["participants." + str(j)+ ".stats.champLevel"]]
        data_col_timeline_lane = data_platinum[["participants." + str(j)+ ".timeline.lane"]]
        data_col_timeline_role = data_platinum[["participants." + str(j)+ ".timeline.role"]]
        data_col_gameId = data_platinum[["gameId"]]
        data_col_gameDuration = data_platinum[["gameDuration"]]
        data_col_Tier = 'platinum'


        kills = float(list(data_col_kills.values)[0][0])
        deaths = float(list(data_col_deaths.values)[0][0])
        assists = float(list(data_col_assists.values)[0][0])
        if (deaths == 0):
            kda = (kills + assists) * 1.5
        else:
            kda = (kills + assists) / deaths
        duration = float(list(data_col_gameDuration.values)[0][0])
        lane = str(list(data_col_timeline_lane.values)[0][0])
        role = str(list(data_col_timeline_role.values)[0][0])



        if (lane == 'JUNGLE'):
            Jungle_list_kda.append(kda)
            Jungle_list_totalDamageDealtToChampions.append(
                (float(list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60)
            Jungle_list_totalDamageTaken.append((float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60)
            Jungle_list_totalHeal.append((float(list(data_col_totalHeal.values)[0][0])) / duration * 60)
            Jungle_list_visionScore.append((float(list(data_col_visionScore.values)[0][0])) / duration * 60)
            Jungle_list_goldEarned.append((float(list(data_col_goldEarned.values)[0][0])) / duration * 60)
            Jungle_list_turretKills.append((float(list(data_col_turretKills.values)[0][0])) / duration * 60)
            Jungle_list_totalMinionsKilled.append(
                (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60)
            Jungle_list_champLevel.append((float(list(data_col_champLevel.values)[0][0])) / duration * 60)
            Jungle_list_col_Tier.append(50)
            platinum_jungle_sum_kda += kda
            platinum_jungle_sum_totalDamageDealtToChampions += (float(
                list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60
            platinum_jungle_sum_totalDamageTaken += (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60
            platinum_jungle_sum_totaloHeal += (float(list(data_col_totalHeal.values)[0][0])) / duration * 60
            platinum_jungle_sum_visionScore += (float(list(data_col_visionScore.values)[0][0])) / duration * 60
            platinum_jungle_sum_goldEarned += (float(list(data_col_goldEarned.values)[0][0])) / duration * 60
            platinum_jungle_sum_turretKills += (float(list(data_col_turretKills.values)[0][0])) / duration * 60
            platinum_jungle_sum_totalMinionsKilled += (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60
            platinum_jungle_sum_champLevel += (float(list(data_col_champLevel.values)[0][0])) / duration * 60
            platinum_jungle_num +=1

        elif (lane == 'MIDDLE'):
            Mid_list_kda.append(kda)
            Mid_list_totalDamageDealtToChampions.append(
                (float(list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60)
            Mid_list_totalDamageTaken.append(
                (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60)
            Mid_list_totalHeal.append((float(list(data_col_totalHeal.values)[0][0])) / duration * 60)
            Mid_list_visionScore.append((float(list(data_col_visionScore.values)[0][0])) / duration * 60)
            Mid_list_goldEarned.append((float(list(data_col_goldEarned.values)[0][0])) / duration * 60)
            Mid_list_turretKills.append((float(list(data_col_turretKills.values)[0][0])) / duration * 60)
            Mid_list_totalMinionsKilled.append(
                (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60)
            Mid_list_champLevel.append((float(list(data_col_champLevel.values)[0][0])) / duration * 60)
            Mid_list_col_Tier.append(50)
            platinum_middle_sum_kda += kda
            platinum_middle_sum_totalDamageDealtToChampions += (float(
                list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60
            platinum_middle_sum_totalDamageTaken += (float(
                list(data_col_totalDamageTaken.values)[0][0])) / duration * 60
            platinum_middle_sum_totaloHeal += (float(list(data_col_totalHeal.values)[0][0])) / duration * 60
            platinum_middle_sum_visionScore += (float(list(data_col_visionScore.values)[0][0])) / duration * 60
            platinum_middle_sum_goldEarned += (float(list(data_col_goldEarned.values)[0][0])) / duration * 60
            platinum_middle_sum_turretKills += (float(list(data_col_turretKills.values)[0][0])) / duration * 60
            platinum_middle_sum_totalMinionsKilled += (float(
                list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60
            platinum_middle_sum_champLevel += (float(list(data_col_champLevel.values)[0][0])) / duration * 60
            platinum_middle_num += 1




        elif (lane == 'TOP'):
            Top_list_kda.append(kda)
            Top_list_totalDamageDealtToChampions.append(
                (float(list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60)
            Top_list_totalDamageTaken.append(
                (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60)
            Top_list_totalHeal.append((float(list(data_col_totalHeal.values)[0][0])) / duration * 60)
            Top_list_visionScore.append((float(list(data_col_visionScore.values)[0][0])) / duration * 60)
            Top_list_goldEarned.append((float(list(data_col_goldEarned.values)[0][0])) / duration * 60)
            Top_list_turretKills.append((float(list(data_col_turretKills.values)[0][0])) / duration * 60)
            Top_list_totalMinionsKilled.append(
                (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60)
            Top_list_champLevel.append((float(list(data_col_champLevel.values)[0][0])) / duration * 60)
            Top_list_col_Tier.append(50)
            platinum_top_sum_kda += kda
            platinum_top_sum_totalDamageDealtToChampions += (float(
                list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60
            platinum_top_sum_totalDamageTaken += (float(
                list(data_col_totalDamageTaken.values)[0][0])) / duration * 60
            platinum_top_sum_totaloHeal += (float(list(data_col_totalHeal.values)[0][0])) / duration * 60
            platinum_top_sum_visionScore += (float(list(data_col_visionScore.values)[0][0])) / duration * 60
            platinum_top_sum_goldEarned += (float(list(data_col_goldEarned.values)[0][0])) / duration * 60
            platinum_top_sum_turretKills += (float(list(data_col_turretKills.values)[0][0])) / duration * 60
            platinum_top_sum_totalMinionsKilled += (float(
                list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60
            platinum_top_sum_champLevel += (float(list(data_col_champLevel.values)[0][0])) / duration * 60
            platinum_top_num +=1


        elif (lane == "BOTTOM"):
            if (role == 'DUO_CARRY'):
                Bot_list_kda.append(kda)
                Bot_list_totalDamageDealtToChampions.append(
                    (float(list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60)
                Bot_list_totalDamageTaken.append(
                    (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60)
                Bot_list_totalHeal.append((float(list(data_col_totalHeal.values)[0][0])) / duration * 60)
                Bot_list_visionScore.append((float(list(data_col_visionScore.values)[0][0])) / duration * 60)
                Bot_list_goldEarned.append((float(list(data_col_goldEarned.values)[0][0])) / duration * 60)
                Bot_list_turretKills.append((float(list(data_col_turretKills.values)[0][0])) / duration * 60)
                Bot_list_totalMinionsKilled.append(
                    (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60)
                Bot_list_champLevel.append((float(list(data_col_champLevel.values)[0][0])) / duration * 60)
                Bot_list_col_Tier.append(50)
                platinum_bottom_car_sum_kda += kda
                platinum_bottom_car_sum_totalDamageDealtToChampions += (float(
                    list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60
                platinum_bottom_car_sum_totalDamageTaken += (float(
                    list(data_col_totalDamageTaken.values)[0][0])) / duration * 60
                platinum_bottom_car_sum_totaloHeal += (float(list(data_col_totalHeal.values)[0][0])) / duration * 60
                platinum_bottom_car_sum_visionScore += (float(list(data_col_visionScore.values)[0][0])) / duration * 60
                platinum_bottom_car_sum_goldEarned += (float(list(data_col_goldEarned.values)[0][0])) / duration * 60
                platinum_bottom_car_sum_turretKills += (float(list(data_col_turretKills.values)[0][0])) / duration * 60
                platinum_bottom_car_sum_totalMinionsKilled += (float(
                    list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60
                platinum_bottom_car_sum_champLevel += (float(list(data_col_champLevel.values)[0][0])) / duration * 60
                platinum_bottom_car_num +=1

            elif (role == 'DUO_SUPPORT'):
                Sup_list_kda.append(kda)
                Sup_list_totalDamageDealtToChampions.append(
                    (float(list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60)
                Sup_list_totalDamageTaken.append(
                    (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60)
                Sup_list_totalHeal.append((float(list(data_col_totalHeal.values)[0][0])) / duration * 60)
                Sup_list_visionScore.append((float(list(data_col_visionScore.values)[0][0])) / duration * 60)
                Sup_list_goldEarned.append((float(list(data_col_goldEarned.values)[0][0])) / duration * 60)
                Sup_list_turretKills.append((float(list(data_col_turretKills.values)[0][0])) / duration * 60)
                Sup_list_totalMinionsKilled.append(
                    (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60)
                Sup_list_champLevel.append((float(list(data_col_champLevel.values)[0][0])) / duration * 60)
                Sup_list_col_Tier.append(50)
                platinum_bottom_sup_sum_kda += kda
                platinum_bottom_sup_sum_totalDamageDealtToChampions += (float(
                    list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60
                platinum_bottom_sup_sum_totalDamageTaken += (float(
                    list(data_col_totalDamageTaken.values)[0][0])) / duration * 60
                platinum_bottom_sup_sum_totaloHeal += (float(list(data_col_totalHeal.values)[0][0])) / duration * 60
                platinum_bottom_sup_sum_visionScore += (float(list(data_col_visionScore.values)[0][0])) / duration * 60
                platinum_bottom_sup_sum_goldEarned += (float(list(data_col_goldEarned.values)[0][0])) / duration * 60
                platinum_bottom_sup_sum_turretKills += (float(list(data_col_turretKills.values)[0][0])) / duration * 60
                platinum_bottom_sup_sum_totalMinionsKilled += (float(
                    list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60
                platinum_bottom_sup_sum_champLevel += (float(list(data_col_champLevel.values)[0][0])) / duration * 60
                platinum_bottom_sup_num +=1
        else:
            print("망함")


#DIA
for i in range(20):
    data_dia = pd.read_csv('C:\\Users\q\PycharmProjects\\tensorflowpractice\\lol\\dia' + str(i) + '.csv', sep=',',dtype='unicode')
    for j in range(10):
        data_col_kills = data_dia[["participants." + str(j)+ ".stats.kills"]]
        data_col_deaths = data_dia[["participants." + str(j)+ ".stats.deaths"]]
        data_col_assists = data_dia[["participants." + str(j)+ ".stats.assists"]]
        data_col_totalDamageDealtToChampions = data_dia[
            ["participants." + str(j)+ ".stats.totalDamageDealtToChampions"]]
        data_col_totalDamageTaken = data_dia[["participants." + str(j)+ ".stats.totalDamageTaken"]]
        data_col_totalHeal = data_dia[["participants." + str(j)+ ".stats.totalHeal"]]
        data_col_visionScore = data_dia[["participants." + str(j)+ ".stats.visionScore"]]
        data_col_goldEarned = data_dia[["participants." + str(j)+ ".stats.goldEarned"]]
        data_col_turretKills = data_dia[["participants." + str(j)+ ".stats.turretKills"]]
        data_col_totalMinionsKilled = data_dia[["participants." + str(j)+ ".stats.totalMinionsKilled"]]
        data_col_champLevel = data_dia[["participants." + str(j)+ ".stats.champLevel"]]
        data_col_timeline_lane = data_dia[["participants." + str(j)+ ".timeline.lane"]]
        data_col_timeline_role = data_dia[["participants." + str(j)+ ".timeline.role"]]
        data_col_gameId = data_dia[["gameId"]]
        data_col_gameDuration = data_dia[["gameDuration"]]
        data_col_Tier = 'dia'


        kills = float(list(data_col_kills.values)[0][0])
        deaths = float(list(data_col_deaths.values)[0][0])
        assists = float(list(data_col_assists.values)[0][0])
        if (deaths == 0):
            kda = (kills + assists) * 1.5
        else:
            kda = (kills + assists) / deaths
        duration = float(list(data_col_gameDuration.values)[0][0])
        lane = str(list(data_col_timeline_lane.values)[0][0])
        role = str(list(data_col_timeline_role.values)[0][0])



        if (lane == 'JUNGLE'):
            Jungle_list_kda.append(kda)
            Jungle_list_totalDamageDealtToChampions.append(
                (float(list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60)
            Jungle_list_totalDamageTaken.append((float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60)
            Jungle_list_totalHeal.append((float(list(data_col_totalHeal.values)[0][0])) / duration * 60)
            Jungle_list_visionScore.append((float(list(data_col_visionScore.values)[0][0])) / duration * 60)
            Jungle_list_goldEarned.append((float(list(data_col_goldEarned.values)[0][0])) / duration * 60)
            Jungle_list_turretKills.append((float(list(data_col_turretKills.values)[0][0])) / duration * 60)
            Jungle_list_totalMinionsKilled.append(
                (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60)
            Jungle_list_champLevel.append((float(list(data_col_champLevel.values)[0][0])) / duration * 60)
            Jungle_list_col_Tier.append(60)
            dia_jungle_sum_kda += kda
            dia_jungle_sum_totalDamageDealtToChampions += (float(
                list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60
            dia_jungle_sum_totalDamageTaken += (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60
            dia_jungle_sum_totaloHeal += (float(list(data_col_totalHeal.values)[0][0])) / duration * 60
            dia_jungle_sum_visionScore += (float(list(data_col_visionScore.values)[0][0])) / duration * 60
            dia_jungle_sum_goldEarned += (float(list(data_col_goldEarned.values)[0][0])) / duration * 60
            dia_jungle_sum_turretKills += (float(list(data_col_turretKills.values)[0][0])) / duration * 60
            dia_jungle_sum_totalMinionsKilled += (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60
            dia_jungle_sum_champLevel += (float(list(data_col_champLevel.values)[0][0])) / duration * 60
            dia_jungle_num +=1

        elif (lane == 'MIDDLE'):
            Mid_list_kda.append(kda)
            Mid_list_totalDamageDealtToChampions.append(
                (float(list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60)
            Mid_list_totalDamageTaken.append(
                (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60)
            Mid_list_totalHeal.append((float(list(data_col_totalHeal.values)[0][0])) / duration * 60)
            Mid_list_visionScore.append((float(list(data_col_visionScore.values)[0][0])) / duration * 60)
            Mid_list_goldEarned.append((float(list(data_col_goldEarned.values)[0][0])) / duration * 60)
            Mid_list_turretKills.append((float(list(data_col_turretKills.values)[0][0])) / duration * 60)
            Mid_list_totalMinionsKilled.append(
                (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60)
            Mid_list_champLevel.append((float(list(data_col_champLevel.values)[0][0])) / duration * 60)
            Mid_list_col_Tier.append(60)
            dia_middle_sum_kda += kda
            dia_middle_sum_totalDamageDealtToChampions += (float(
                list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60
            dia_middle_sum_totalDamageTaken += (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60
            dia_middle_sum_totaloHeal += (float(list(data_col_totalHeal.values)[0][0])) / duration * 60
            dia_middle_sum_visionScore += (float(list(data_col_visionScore.values)[0][0])) / duration * 60
            dia_middle_sum_goldEarned += (float(list(data_col_goldEarned.values)[0][0])) / duration * 60
            dia_middle_sum_turretKills += (float(list(data_col_turretKills.values)[0][0])) / duration * 60
            dia_middle_sum_totalMinionsKilled += (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60
            dia_middle_sum_champLevel += (float(list(data_col_champLevel.values)[0][0])) / duration * 60
            dia_middle_num +=1

        elif (lane == 'TOP'):
            Top_list_kda.append(kda)
            Top_list_totalDamageDealtToChampions.append(
                (float(list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60)
            Top_list_totalDamageTaken.append(
                (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60)
            Top_list_totalHeal.append((float(list(data_col_totalHeal.values)[0][0])) / duration * 60)
            Top_list_visionScore.append((float(list(data_col_visionScore.values)[0][0])) / duration * 60)
            Top_list_goldEarned.append((float(list(data_col_goldEarned.values)[0][0])) / duration * 60)
            Top_list_turretKills.append((float(list(data_col_turretKills.values)[0][0])) / duration * 60)
            Top_list_totalMinionsKilled.append(
                (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60)
            Top_list_champLevel.append((float(list(data_col_champLevel.values)[0][0])) / duration * 60)
            Top_list_col_Tier.append(60)
            dia_top_sum_kda += kda
            dia_top_sum_totalDamageDealtToChampions += (float(
                list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60
            dia_top_sum_totalDamageTaken += (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60
            dia_top_sum_totaloHeal += (float(list(data_col_totalHeal.values)[0][0])) / duration * 60
            dia_top_sum_visionScore += (float(list(data_col_visionScore.values)[0][0])) / duration * 60
            dia_top_sum_goldEarned += (float(list(data_col_goldEarned.values)[0][0])) / duration * 60
            dia_top_sum_turretKills += (float(list(data_col_turretKills.values)[0][0])) / duration * 60
            dia_top_sum_totalMinionsKilled += (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60
            dia_top_sum_champLevel += (float(list(data_col_champLevel.values)[0][0])) / duration * 60
            dia_top_num +=1


        elif (lane == "BOTTOM"):
            if (role == 'DUO_CARRY'):
                Bot_list_kda.append(kda)
                Bot_list_totalDamageDealtToChampions.append(
                    (float(list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60)
                Bot_list_totalDamageTaken.append(
                    (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60)
                Bot_list_totalHeal.append((float(list(data_col_totalHeal.values)[0][0])) / duration * 60)
                Bot_list_visionScore.append((float(list(data_col_visionScore.values)[0][0])) / duration * 60)
                Bot_list_goldEarned.append((float(list(data_col_goldEarned.values)[0][0])) / duration * 60)
                Bot_list_turretKills.append((float(list(data_col_turretKills.values)[0][0])) / duration * 60)
                Bot_list_totalMinionsKilled.append(
                    (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60)
                Bot_list_champLevel.append((float(list(data_col_champLevel.values)[0][0])) / duration * 60)
                Bot_list_col_Tier.append(60)
                dia_bottom_car_sum_kda += kda
                dia_bottom_car_sum_totalDamageDealtToChampions += (float(
                    list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60
                dia_bottom_car_sum_totalDamageTaken += (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60
                dia_bottom_car_sum_totaloHeal += (float(list(data_col_totalHeal.values)[0][0])) / duration * 60
                dia_bottom_car_sum_visionScore += (float(list(data_col_visionScore.values)[0][0])) / duration * 60
                dia_bottom_car_sum_goldEarned += (float(list(data_col_goldEarned.values)[0][0])) / duration * 60
                dia_bottom_car_sum_turretKills += (float(list(data_col_turretKills.values)[0][0])) / duration * 60
                dia_bottom_car_sum_totalMinionsKilled += (float(
                    list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60
                dia_bottom_car_sum_champLevel += (float(list(data_col_champLevel.values)[0][0])) / duration * 60
                dia_bottom_car_num +=1
            elif (role == 'DUO_SUPPORT'):
                Sup_list_kda.append(kda)
                Sup_list_totalDamageDealtToChampions.append(
                    (float(list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60)
                Sup_list_totalDamageTaken.append(
                    (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60)
                Sup_list_totalHeal.append((float(list(data_col_totalHeal.values)[0][0])) / duration * 60)
                Sup_list_visionScore.append((float(list(data_col_visionScore.values)[0][0])) / duration * 60)
                Sup_list_goldEarned.append((float(list(data_col_goldEarned.values)[0][0])) / duration * 60)
                Sup_list_turretKills.append((float(list(data_col_turretKills.values)[0][0])) / duration * 60)
                Sup_list_totalMinionsKilled.append(
                    (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60)
                Sup_list_champLevel.append((float(list(data_col_champLevel.values)[0][0])) / duration * 60)
                Sup_list_col_Tier.append(60)
                dia_bottom_sup_sum_kda += kda
                dia_bottom_sup_sum_totalDamageDealtToChampions += (float(
                    list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60
                dia_bottom_sup_sum_totalDamageTaken += (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60
                dia_bottom_sup_sum_totaloHeal += (float(list(data_col_totalHeal.values)[0][0])) / duration * 60
                dia_bottom_sup_sum_visionScore += (float(list(data_col_visionScore.values)[0][0])) / duration * 60
                dia_bottom_sup_sum_goldEarned += (float(list(data_col_goldEarned.values)[0][0])) / duration * 60
                dia_bottom_sup_sum_turretKills += (float(list(data_col_turretKills.values)[0][0])) / duration * 60
                dia_bottom_sup_sum_totalMinionsKilled += (float(
                    list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60
                dia_bottom_sup_sum_champLevel += (float(list(data_col_champLevel.values)[0][0])) / duration * 60
                dia_bottom_sup_num +=1
        else:
            print("망함")

#MASTER
for i in range(20):
    data_master = pd.read_csv('C:\\Users\q\PycharmProjects\\tensorflowpractice\\lol\\master' + str(i) + '.csv', sep=',',dtype='unicode')
    for j in range(10):
        data_col_kills = data_master[["participants." + str(j)+ ".stats.kills"]]
        data_col_deaths = data_master[["participants." + str(j)+ ".stats.deaths"]]
        data_col_assists = data_master[["participants." + str(j)+ ".stats.assists"]]
        data_col_totalDamageDealtToChampions = data_master[["participants." + str(j)+ ".stats.totalDamageDealtToChampions"]]
        data_col_totalDamageTaken = data_master[["participants." + str(j)+ ".stats.totalDamageTaken"]]
        data_col_totalHeal = data_master[["participants." + str(j)+ ".stats.totalHeal"]]
        data_col_visionScore = data_master[["participants." + str(j)+ ".stats.visionScore"]]
        data_col_goldEarned = data_master[["participants." + str(j)+ ".stats.goldEarned"]]
        data_col_turretKills = data_master[["participants." + str(j)+ ".stats.turretKills"]]
        data_col_totalMinionsKilled = data_master[["participants." + str(j)+ ".stats.totalMinionsKilled"]]
        data_col_champLevel = data_master[["participants." + str(j)+ ".stats.champLevel"]]
        data_col_timeline_lane = data_master[["participants." + str(j)+ ".timeline.lane"]]
        data_col_timeline_role = data_master[["participants." + str(j)+ ".timeline.role"]]
        data_col_gameId = data_master[["gameId"]]
        data_col_gameDuration = data_master[["gameDuration"]]
        data_col_Tier = 'master'


        kills = float(list(data_col_kills.values)[0][0])
        deaths = float(list(data_col_deaths.values)[0][0])
        assists = float(list(data_col_assists.values)[0][0])
        if (deaths == 0):
            kda = (kills + assists) * 1.5
        else:
            kda = (kills + assists) / deaths
        duration = float(list(data_col_gameDuration.values)[0][0])
        lane = str(list(data_col_timeline_lane.values)[0][0])
        role = str(list(data_col_timeline_role.values)[0][0])



        if (lane == 'JUNGLE'):
            Jungle_list_kda.append(kda)
            Jungle_list_totalDamageDealtToChampions.append(
                (float(list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60)
            Jungle_list_totalDamageTaken.append((float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60)
            Jungle_list_totalHeal.append((float(list(data_col_totalHeal.values)[0][0])) / duration * 60)
            Jungle_list_visionScore.append((float(list(data_col_visionScore.values)[0][0])) / duration * 60)
            Jungle_list_goldEarned.append((float(list(data_col_goldEarned.values)[0][0])) / duration * 60)
            Jungle_list_turretKills.append((float(list(data_col_turretKills.values)[0][0])) / duration * 60)
            Jungle_list_totalMinionsKilled.append(
                (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60)
            Jungle_list_champLevel.append((float(list(data_col_champLevel.values)[0][0])) / duration * 60)
            Jungle_list_col_Tier.append(70)
            master_jungle_sum_kda += kda
            master_jungle_sum_totalDamageDealtToChampions += (float(
                list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60
            master_jungle_sum_totalDamageTaken += (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60
            master_jungle_sum_totaloHeal += (float(list(data_col_totalHeal.values)[0][0])) / duration * 60
            master_jungle_sum_visionScore += (float(list(data_col_visionScore.values)[0][0])) / duration * 60
            master_jungle_sum_goldEarned += (float(list(data_col_goldEarned.values)[0][0])) / duration * 60
            master_jungle_sum_turretKills += (float(list(data_col_turretKills.values)[0][0])) / duration * 60
            master_jungle_sum_totalMinionsKilled += (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60
            master_jungle_sum_champLevel += (float(list(data_col_champLevel.values)[0][0])) / duration * 60
            master_jungle_num +=1

        elif (lane == 'MIDDLE'):
            Mid_list_kda.append(kda)
            Mid_list_totalDamageDealtToChampions.append(
                (float(list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60)
            Mid_list_totalDamageTaken.append(
                (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60)
            Mid_list_totalHeal.append((float(list(data_col_totalHeal.values)[0][0])) / duration * 60)
            Mid_list_visionScore.append((float(list(data_col_visionScore.values)[0][0])) / duration * 60)
            Mid_list_goldEarned.append((float(list(data_col_goldEarned.values)[0][0])) / duration * 60)
            Mid_list_turretKills.append((float(list(data_col_turretKills.values)[0][0])) / duration * 60)
            Mid_list_totalMinionsKilled.append(
                (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60)
            Mid_list_champLevel.append((float(list(data_col_champLevel.values)[0][0])) / duration * 60)
            Mid_list_col_Tier.append(70)
            master_middle_sum_kda += kda
            master_middle_sum_totalDamageDealtToChampions += (float(
                list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60
            master_middle_sum_totalDamageTaken += (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60
            master_middle_sum_totaloHeal += (float(list(data_col_totalHeal.values)[0][0])) / duration * 60
            master_middle_sum_visionScore += (float(list(data_col_visionScore.values)[0][0])) / duration * 60
            master_middle_sum_goldEarned += (float(list(data_col_goldEarned.values)[0][0])) / duration * 60
            master_middle_sum_turretKills += (float(list(data_col_turretKills.values)[0][0])) / duration * 60
            master_middle_sum_totalMinionsKilled += (float(
                list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60
            master_middle_sum_champLevel += (float(list(data_col_champLevel.values)[0][0])) / duration * 60
            master_middle_num +=1

        elif (lane == 'TOP'):
            Top_list_kda.append(kda)
            Top_list_totalDamageDealtToChampions.append(
                (float(list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60)
            Top_list_totalDamageTaken.append(
                (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60)
            Top_list_totalHeal.append((float(list(data_col_totalHeal.values)[0][0])) / duration * 60)
            Top_list_visionScore.append((float(list(data_col_visionScore.values)[0][0])) / duration * 60)
            Top_list_goldEarned.append((float(list(data_col_goldEarned.values)[0][0])) / duration * 60)
            Top_list_turretKills.append((float(list(data_col_turretKills.values)[0][0])) / duration * 60)
            Top_list_totalMinionsKilled.append(
                (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60)
            Top_list_champLevel.append((float(list(data_col_champLevel.values)[0][0])) / duration * 60)
            Top_list_col_Tier.append(70)
            master_top_sum_kda += kda
            master_top_sum_totalDamageDealtToChampions += (float(
                list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60
            master_top_sum_totalDamageTaken += (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60
            master_top_sum_totaloHeal += (float(list(data_col_totalHeal.values)[0][0])) / duration * 60
            master_top_sum_visionScore += (float(list(data_col_visionScore.values)[0][0])) / duration * 60
            master_top_sum_goldEarned += (float(list(data_col_goldEarned.values)[0][0])) / duration * 60
            master_top_sum_turretKills += (float(list(data_col_turretKills.values)[0][0])) / duration * 60
            master_top_sum_totalMinionsKilled += (float(
                list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60
            master_top_sum_champLevel += (float(list(data_col_champLevel.values)[0][0])) / duration * 60
            master_top_num +=1


        elif (lane == "BOTTOM"):
            if (role == 'DUO_CARRY'):
                Bot_list_kda.append(kda)
                Bot_list_totalDamageDealtToChampions.append(
                    (float(list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60)
                Bot_list_totalDamageTaken.append(
                    (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60)
                Bot_list_totalHeal.append((float(list(data_col_totalHeal.values)[0][0])) / duration * 60)
                Bot_list_visionScore.append((float(list(data_col_visionScore.values)[0][0])) / duration * 60)
                Bot_list_goldEarned.append((float(list(data_col_goldEarned.values)[0][0])) / duration * 60)
                Bot_list_turretKills.append((float(list(data_col_turretKills.values)[0][0])) / duration * 60)
                Bot_list_totalMinionsKilled.append(
                    (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60)
                Bot_list_champLevel.append((float(list(data_col_champLevel.values)[0][0])) / duration * 60)
                Bot_list_col_Tier.append(70)
                master_bottom_car_sum_kda += kda
                master_bottom_car_sum_totalDamageDealtToChampions += (float(
                    list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60
                master_bottom_car_sum_totalDamageTaken += (float(
                    list(data_col_totalDamageTaken.values)[0][0])) / duration * 60
                master_bottom_car_sum_totaloHeal += (float(list(data_col_totalHeal.values)[0][0])) / duration * 60
                master_bottom_car_sum_visionScore += (float(list(data_col_visionScore.values)[0][0])) / duration * 60
                master_bottom_car_sum_goldEarned += (float(list(data_col_goldEarned.values)[0][0])) / duration * 60
                master_bottom_car_sum_turretKills += (float(list(data_col_turretKills.values)[0][0])) / duration * 60
                master_bottom_car_sum_totalMinionsKilled += (float(
                    list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60
                master_bottom_car_sum_champLevel += (float(list(data_col_champLevel.values)[0][0])) / duration * 60
                master_bottom_car_num +=1
            elif (role == 'DUO_SUPPORT'):
                Sup_list_kda.append(kda)
                Sup_list_totalDamageDealtToChampions.append(
                    (float(list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60)
                Sup_list_totalDamageTaken.append(
                    (float(list(data_col_totalDamageTaken.values)[0][0])) / duration * 60)
                Sup_list_totalHeal.append((float(list(data_col_totalHeal.values)[0][0])) / duration * 60)
                Sup_list_visionScore.append((float(list(data_col_visionScore.values)[0][0])) / duration * 60)
                Sup_list_goldEarned.append((float(list(data_col_goldEarned.values)[0][0])) / duration * 60)
                Sup_list_turretKills.append((float(list(data_col_turretKills.values)[0][0])) / duration * 60)
                Sup_list_totalMinionsKilled.append(
                    (float(list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60)
                Sup_list_champLevel.append((float(list(data_col_champLevel.values)[0][0])) / duration * 60)
                Sup_list_col_Tier.append(70)
                master_bottom_sup_sum_kda += kda
                master_bottom_sup_sum_totalDamageDealtToChampions += (float(
                    list(data_col_totalDamageDealtToChampions.values)[0][0])) / duration * 60
                master_bottom_sup_sum_totalDamageTaken += (float(
                    list(data_col_totalDamageTaken.values)[0][0])) / duration * 60
                master_bottom_sup_sum_totaloHeal += (float(list(data_col_totalHeal.values)[0][0])) / duration * 60
                master_bottom_sup_sum_visionScore += (float(list(data_col_visionScore.values)[0][0])) / duration * 60
                master_bottom_sup_sum_goldEarned += (float(list(data_col_goldEarned.values)[0][0])) / duration * 60
                master_bottom_sup_sum_turretKills += (float(list(data_col_turretKills.values)[0][0])) / duration * 60
                master_bottom_sup_sum_totalMinionsKilled += (float(
                    list(data_col_totalMinionsKilled.values)[0][0])) / duration * 60
                master_bottom_sup_sum_champLevel += (float(list(data_col_champLevel.values)[0][0])) / duration * 60
                master_bottom_sup_num +=1
        else:
            print("망함")



Top_W1 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Top_W2 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Top_W3 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Top_W4 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Top_W5 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Top_W6 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Top_W7 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Top_W8 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Top_W9 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Top_b = tf.Variable(tf.random_uniform([1],-0.01,0.01))

Bot_W1 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Bot_W2 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Bot_W3 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Bot_W4 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Bot_W5 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Bot_W6 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Bot_W7 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Bot_W8 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Bot_W9 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Bot_b = tf.Variable(tf.random_uniform([1],-0.01,0.01))


Mid_W1 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Mid_W2 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Mid_W3 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Mid_W4 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Mid_W5 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Mid_W6 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Mid_W7 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Mid_W8 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Mid_W9 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Mid_b = tf.Variable(tf.random_uniform([1],-0.01,0.01))


Sup_W1 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Sup_W2 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Sup_W3 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Sup_W4 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Sup_W5 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Sup_W6 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Sup_W7 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Sup_W8 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Sup_W9 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Sup_b = tf.Variable(tf.random_uniform([1],-0.01,0.01))

Jungle_W1 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Jungle_W2 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Jungle_W3 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Jungle_W4 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Jungle_W5 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Jungle_W6 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Jungle_W7 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Jungle_W8 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Jungle_W9 = tf.Variable(tf.random_uniform([1],-0.01,0.01))
Jungle_b = tf.Variable(tf.random_uniform([1],-0.01,0.01))
init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)
print(sess.run(Top_W1))

print(len(Top_list_kda))
print(len(Top_list_totalDamageDealtToChampions))
print(len(Top_list_totalDamageTaken))
print(len(Top_list_totalHeal))
print(len(Top_list_visionScore))
print(len(Top_list_goldEarned))

print(len(Top_list_turretKills))
print(len(Top_list_totalMinionsKilled))
print(len(Top_list_champLevel))
print(len(Top_list_timeline_lane))
print(len(Top_list_timeline_role))
print(len(Top_list_col_gameId))
print(len(Top_list_col_gameDuration))
print(len(Top_list_col_Tier))

#hypothesis
Top_hypothesis = Top_W1 * Top_list_kda + Top_W2 * Top_list_totalDamageDealtToChampions + Top_W3 * Top_list_totalDamageTaken + Top_W4 * Top_list_totalHeal + Top_W5 * Top_list_visionScore + Top_W6 * Top_list_goldEarned + Top_W7 * Top_list_turretKills +\
             Top_W8 * Top_list_totalMinionsKilled+ Top_W9 * Top_list_champLevel+ Top_b
Bot_hypothesis = Bot_W1 * Bot_list_kda + Bot_W2 * Bot_list_totalDamageDealtToChampions + Bot_W3 * Bot_list_totalDamageTaken + Bot_W4 * Bot_list_totalHeal + Bot_W5 * Bot_list_visionScore + Bot_W6 * Bot_list_goldEarned + Bot_W7 * Bot_list_turretKills +\
             Bot_W8 * Bot_list_totalMinionsKilled+ Bot_W9 * Bot_list_champLevel+ Bot_b
Mid_hypothesis = Mid_W1 * Mid_list_kda + Mid_W2 * Mid_list_totalDamageDealtToChampions + Mid_W3 * Mid_list_totalDamageTaken + Mid_W4 * Mid_list_totalHeal + Mid_W5 * Mid_list_visionScore + Mid_W6 * Mid_list_goldEarned + Mid_W7 * Mid_list_turretKills +\
             Mid_W8 * Mid_list_totalMinionsKilled+ Mid_W9 * Mid_list_champLevel+ Mid_b
Sup_hypothesis = Sup_W1 * Sup_list_kda + Sup_W2 * Sup_list_totalDamageDealtToChampions + Sup_W3 * Sup_list_totalDamageTaken + Sup_W4 * Sup_list_totalHeal + Sup_W5 * Sup_list_visionScore + Sup_W6 * Sup_list_goldEarned + Sup_W7 * Sup_list_turretKills +\
             Sup_W8 * Sup_list_totalMinionsKilled+ Sup_W9 * Sup_list_champLevel+ Sup_b
Jungle_hypothesis = Jungle_W1 * Jungle_list_kda + Jungle_W2 * Jungle_list_totalDamageDealtToChampions + Jungle_W3 * Jungle_list_totalDamageTaken + Jungle_W4 * Jungle_list_totalHeal + Jungle_W5 * Jungle_list_visionScore + Jungle_W6 * Jungle_list_goldEarned + Jungle_W7 * Jungle_list_turretKills +\
             Jungle_W8 * Jungle_list_totalMinionsKilled+ Jungle_W9 * Jungle_list_champLevel+ Jungle_b


print(sess.run(Top_hypothesis))

Top_cost = tf.reduce_mean(tf.square(Top_hypothesis - Top_list_col_Tier))
Bot_cost = tf.reduce_mean(tf.square(Bot_hypothesis - Bot_list_col_Tier))
Mid_cost = tf.reduce_mean(tf.square(Mid_hypothesis - Mid_list_col_Tier))
Sup_cost = tf.reduce_mean(tf.square(Sup_hypothesis - Sup_list_col_Tier))
Jungle_cost = tf.reduce_mean(tf.square(Jungle_hypothesis - Jungle_list_col_Tier))

print(sess.run(Top_cost))
#minimize
a = tf.Variable(0.00000001) #alpha, learning rate
b = tf.Variable(0.000001) #alpha, learning rate
c = tf.Variable(0.00000001) #alpha, learning rate
d = tf.Variable(0.000001) #alpha, learning rate
e = tf.Variable(0.00000001) #alpha, learning rate
optimizer1 = tf.train.GradientDescentOptimizer(a)
optimizer2 = tf.train.GradientDescentOptimizer(b)
optimizer3 = tf.train.GradientDescentOptimizer(c)
optimizer4 = tf.train.GradientDescentOptimizer(d)
optimizer5 = tf.train.GradientDescentOptimizer(e)

train1 = optimizer1.minimize(Top_cost)
train2 = optimizer2.minimize(Bot_cost)
train3 = optimizer3.minimize(Mid_cost)
train4 = optimizer4.minimize(Sup_cost)
train5 = optimizer5.minimize(Jungle_cost)
print(sess.run(Top_cost))

# befor starting, initialize variables
init = tf.initialize_all_variables()

#launch
sess = tf.Session()
sess.run(init)

# fit the line
for step in range(10000):
    sess.run(train1)
    if step % 1000 == 0:
        print (step, sess.run(Top_cost), sess.run(Top_W1),
        sess.run(Top_W2), sess.run(Top_W3), sess.run(Top_W4), sess.run(Top_W5), sess.run(Top_W6), sess.run(Top_W7), sess.run(Top_W8), sess.run(Top_W9), sess.run(Top_b) )

for step in range(10000):
    sess.run(train2)
    if step % 1000 == 0:
        print (step, sess.run(Bot_cost), sess.run(Bot_W1),
        sess.run(Bot_W2), sess.run(Bot_W3), sess.run(Bot_W4), sess.run(Bot_W5), sess.run(Bot_W6), sess.run(Bot_W7), sess.run(Bot_W8), sess.run(Bot_W9), sess.run(Bot_b) )

for step in range(10000):
    sess.run(train3)
    if step % 1000 == 0:
        print (step, sess.run(Mid_cost), sess.run(Mid_W1),
        sess.run(Mid_W2), sess.run(Mid_W3), sess.run(Mid_W4), sess.run(Mid_W5), sess.run(Mid_W6), sess.run(Mid_W7), sess.run(Mid_W8), sess.run(Mid_W9), sess.run(Mid_b) )

for step in range(10000):
    sess.run(train4)
    if step % 1000 == 0:
        print (step, sess.run(Sup_cost), sess.run(Sup_W1),
        sess.run(Sup_W2), sess.run(Sup_W3), sess.run(Sup_W4), sess.run(Sup_W5), sess.run(Sup_W6), sess.run(Sup_W7), sess.run(Sup_W8), sess.run(Sup_W9), sess.run(Sup_b) )

for step in range(10000):
    sess.run(train5)
    if step % 1000 == 0:
        print (step, sess.run(Jungle_cost), sess.run(Jungle_W1),
        sess.run(Jungle_W2), sess.run(Jungle_W3), sess.run(Jungle_W4), sess.run(Jungle_W5), sess.run(Jungle_W6), sess.run(Jungle_W7), sess.run(Jungle_W8), sess.run(Jungle_W9), sess.run(Jungle_b) )
print()
print()
print('Top_W')
print(sess.run(Top_W1))
print(sess.run(Top_W2))
print(sess.run(Top_W3))
print(sess.run(Top_W4))
print(sess.run(Top_W5))
print(sess.run(Top_W6))
print(sess.run(Top_W7))
print(sess.run(Top_W8))
print(sess.run(Top_W9))

print()
print()
print('Bot_W')
print(sess.run(Bot_W1))
print(sess.run(Bot_W2))
print(sess.run(Bot_W3))
print(sess.run(Bot_W4))
print(sess.run(Bot_W5))
print(sess.run(Bot_W6))
print(sess.run(Bot_W7))
print(sess.run(Bot_W8))
print(sess.run(Bot_W9))

print()
print()
print('Mid_W')
print(sess.run(Mid_W1))
print(sess.run(Mid_W2))
print(sess.run(Mid_W3))
print(sess.run(Mid_W4))
print(sess.run(Mid_W5))
print(sess.run(Mid_W6))
print(sess.run(Mid_W7))
print(sess.run(Mid_W8))
print(sess.run(Mid_W9))

print()
print()
print('Sup_W')
print(sess.run(Sup_W1))
print(sess.run(Sup_W2))
print(sess.run(Sup_W3))
print(sess.run(Sup_W4))
print(sess.run(Sup_W5))
print(sess.run(Sup_W6))
print(sess.run(Sup_W7))
print(sess.run(Sup_W8))
print(sess.run(Sup_W9))

print()
print()
print('Jungle_W')
print(sess.run(Jungle_W1))
print(sess.run(Jungle_W2))
print(sess.run(Jungle_W3))
print(sess.run(Jungle_W4))
print(sess.run(Jungle_W5))
print(sess.run(Jungle_W6))
print(sess.run(Jungle_W7))
print(sess.run(Jungle_W8))
print(sess.run(Jungle_W9))


avg_iron_jungle_sum_kda = float((iron_jungle_sum_kda)/iron_jungle_num)
avg_iron_jungle_sum_totalDamageDealtToChampions = float((iron_jungle_sum_totalDamageDealtToChampions)/iron_jungle_num)
avg_iron_jungle_sum_totalDamageTaken = float((iron_jungle_sum_totalDamageTaken)/iron_jungle_num)
avg_iron_jungle_sum_totaloHeal = float((iron_jungle_sum_totaloHeal)/iron_jungle_num)
avg_iron_jungle_sum_visionScore = float((iron_jungle_sum_visionScore)/iron_jungle_num)
avg_iron_jungle_sum_goldEarned = float((iron_jungle_sum_goldEarned)/iron_jungle_num)
avg_iron_jungle_sum_turretKills = float((iron_jungle_sum_turretKills)/iron_jungle_num)
avg_iron_jungle_sum_totalMinionsKilled = float((iron_jungle_sum_totalMinionsKilled)/iron_jungle_num)
avg_iron_jungle_sum_champLevel = float((iron_jungle_sum_champLevel)/iron_jungle_num)
print()
print()
print('iron_jungle')
print(avg_iron_jungle_sum_kda)
print(avg_iron_jungle_sum_totalDamageDealtToChampions)
print(avg_iron_jungle_sum_totalDamageTaken)
print(avg_iron_jungle_sum_totaloHeal)
print(avg_iron_jungle_sum_visionScore)
print(avg_iron_jungle_sum_goldEarned)
print(avg_iron_jungle_sum_turretKills)
print(avg_iron_jungle_sum_totalMinionsKilled)
print(avg_iron_jungle_sum_champLevel)

avg_iron_middle_sum_kda = float((iron_middle_sum_kda)/iron_middle_num)
avg_iron_middle_sum_totalDamageDealtToChampions = float((iron_middle_sum_totalDamageDealtToChampions)/iron_middle_num)
avg_iron_middle_sum_totalDamageTaken = float((iron_middle_sum_totalDamageTaken)/iron_middle_num)
avg_iron_middle_sum_totaloHeal = float((iron_middle_sum_totaloHeal)/iron_middle_num)
avg_iron_middle_sum_visionScore = float((iron_middle_sum_visionScore)/iron_middle_num)
avg_iron_middle_sum_goldEarned = float((iron_middle_sum_goldEarned)/iron_middle_num)
avg_iron_middle_sum_turretKills = float((iron_middle_sum_turretKills)/iron_middle_num)
avg_iron_middle_sum_totalMinionsKilled = float((iron_middle_sum_totalMinionsKilled)/iron_middle_num)
avg_iron_middle_sum_champLevel = float((iron_middle_sum_champLevel)/iron_middle_num)
print()
print()
print('iron_middle')
print(avg_iron_middle_sum_kda)
print(avg_iron_middle_sum_totalDamageDealtToChampions)
print(avg_iron_middle_sum_totalDamageTaken)
print(avg_iron_middle_sum_totaloHeal)
print(avg_iron_middle_sum_visionScore)
print(avg_iron_middle_sum_goldEarned)
print(avg_iron_middle_sum_turretKills)
print(avg_iron_middle_sum_totalMinionsKilled)
print(avg_iron_middle_sum_champLevel)

avg_iron_top_sum_kda = float((iron_top_sum_kda)/iron_top_num)
avg_iron_top_sum_totalDamageDealtToChampions = float((iron_top_sum_totalDamageDealtToChampions)/iron_top_num)
avg_iron_top_sum_totalDamageTaken = float((iron_top_sum_totalDamageTaken)/iron_top_num)
avg_iron_top_sum_totaloHeal = float((iron_top_sum_totaloHeal)/iron_top_num)
avg_iron_top_sum_visionScore = float((iron_top_sum_visionScore)/iron_top_num)
avg_iron_top_sum_goldEarned = float((iron_top_sum_goldEarned)/iron_top_num)
avg_iron_top_sum_turretKills = float((iron_top_sum_turretKills)/iron_top_num)
avg_iron_top_sum_totalMinionsKilled = float((iron_top_sum_totalMinionsKilled)/iron_top_num)
avg_iron_top_sum_champLevel = float((iron_top_sum_champLevel)/iron_top_num)

print()
print()
print('iron_top')
print(avg_iron_top_sum_kda)
print(avg_iron_top_sum_totalDamageDealtToChampions)
print(avg_iron_top_sum_totalDamageTaken)
print(avg_iron_top_sum_totaloHeal)
print(avg_iron_top_sum_visionScore)
print(avg_iron_top_sum_goldEarned)
print(avg_iron_top_sum_turretKills)
print(avg_iron_top_sum_totalMinionsKilled)
print(avg_iron_top_sum_champLevel)

avg_iron_bottom_car_sum_kda = float((iron_bottom_car_sum_kda)/iron_bottom_car_num)
avg_iron_bottom_car_sum_totalDamageDealtToChampions = float((iron_bottom_car_sum_totalDamageDealtToChampions)/iron_bottom_car_num)
avg_iron_bottom_car_sum_totalDamageTaken = float((iron_bottom_car_sum_totalDamageTaken)/iron_bottom_car_num)
avg_iron_bottom_car_sum_totaloHeal = float((iron_bottom_car_sum_totaloHeal)/iron_bottom_car_num)
avg_iron_bottom_car_sum_visionScore = float((iron_bottom_car_sum_visionScore)/iron_bottom_car_num)
avg_iron_bottom_car_sum_goldEarned = float((iron_bottom_car_sum_goldEarned)/iron_bottom_car_num)
avg_iron_bottom_car_sum_turretKills = float((iron_bottom_car_sum_turretKills)/iron_bottom_car_num)
avg_iron_bottom_car_sum_totalMinionsKilled = float((iron_bottom_car_sum_totalMinionsKilled)/iron_bottom_car_num)
avg_iron_bottom_car_sum_champLevel = float((iron_bottom_car_sum_champLevel)/iron_bottom_car_num)
print()
print()
print('iron_bottom_car')
print(avg_iron_bottom_car_sum_kda)
print(avg_iron_bottom_car_sum_totalDamageDealtToChampions)
print(avg_iron_bottom_car_sum_totalDamageTaken)
print(avg_iron_bottom_car_sum_totaloHeal)
print(avg_iron_bottom_car_sum_visionScore)
print(avg_iron_bottom_car_sum_goldEarned)
print(avg_iron_bottom_car_sum_turretKills)
print(avg_iron_bottom_car_sum_totalMinionsKilled)
print(avg_iron_bottom_car_sum_champLevel)

avg_iron_bottom_sup_sum_kda = float((iron_bottom_sup_sum_kda)/iron_bottom_sup_num)
avg_iron_bottom_sup_sum_totalDamageDealtToChampions = float((iron_bottom_sup_sum_totalDamageDealtToChampions)/iron_bottom_sup_num)
avg_iron_bottom_sup_sum_totalDamageTaken = float((iron_bottom_sup_sum_totalDamageTaken)/iron_bottom_sup_num)
avg_iron_bottom_sup_sum_totaloHeal = float((iron_bottom_sup_sum_totaloHeal)/iron_bottom_sup_num)
avg_iron_bottom_sup_sum_visionScore = float((iron_bottom_sup_sum_visionScore)/iron_bottom_sup_num)
avg_iron_bottom_sup_sum_goldEarned = float((iron_bottom_sup_sum_goldEarned)/iron_bottom_sup_num)
avg_iron_bottom_sup_sum_turretKills = float((iron_bottom_sup_sum_turretKills)/iron_bottom_sup_num)
avg_iron_bottom_sup_sum_totalMinionsKilled = float((iron_bottom_sup_sum_totalMinionsKilled)/iron_bottom_sup_num)
avg_iron_bottom_sup_sum_champLevel = float((iron_bottom_sup_sum_champLevel)/iron_bottom_sup_num)
print()
print()
print('iron_bottom_sup')
print(avg_iron_bottom_sup_sum_kda)
print(avg_iron_bottom_sup_sum_totalDamageDealtToChampions)
print(avg_iron_bottom_sup_sum_totalDamageTaken)
print(avg_iron_bottom_sup_sum_totaloHeal)
print(avg_iron_bottom_sup_sum_visionScore)
print(avg_iron_bottom_sup_sum_goldEarned)
print(avg_iron_bottom_sup_sum_turretKills)
print(avg_iron_bottom_sup_sum_totalMinionsKilled)
print(avg_iron_bottom_sup_sum_champLevel)




avg_bronze_jungle_sum_kda = float((bronze_jungle_sum_kda)/bronze_jungle_num)
avg_bronze_jungle_sum_totalDamageDealtToChampions = float((bronze_jungle_sum_totalDamageDealtToChampions)/bronze_jungle_num)
avg_bronze_jungle_sum_totalDamageTaken = float((bronze_jungle_sum_totalDamageTaken)/bronze_jungle_num)
avg_bronze_jungle_sum_totaloHeal = float((bronze_jungle_sum_totaloHeal)/bronze_jungle_num)
avg_bronze_jungle_sum_visionScore = float((bronze_jungle_sum_visionScore)/bronze_jungle_num)
avg_bronze_jungle_sum_goldEarned = float((bronze_jungle_sum_goldEarned)/bronze_jungle_num)
avg_bronze_jungle_sum_turretKills = float((bronze_jungle_sum_turretKills)/bronze_jungle_num)
avg_bronze_jungle_sum_totalMinionsKilled = float((bronze_jungle_sum_totalMinionsKilled)/bronze_jungle_num)
avg_bronze_jungle_sum_champLevel = float((bronze_jungle_sum_champLevel)/bronze_jungle_num)
print()
print()
print()
print()
print('bronze_jungle')
print(avg_bronze_jungle_sum_kda)
print(avg_bronze_jungle_sum_totalDamageDealtToChampions)
print(avg_bronze_jungle_sum_totalDamageTaken)
print(avg_bronze_jungle_sum_totaloHeal)
print(avg_bronze_jungle_sum_visionScore)
print(avg_bronze_jungle_sum_goldEarned)
print(avg_bronze_jungle_sum_turretKills)
print(avg_bronze_jungle_sum_totalMinionsKilled)
print(avg_bronze_jungle_sum_champLevel)


avg_bronze_middle_sum_kda = float((bronze_middle_sum_kda)/bronze_middle_num)
avg_bronze_middle_sum_totalDamageDealtToChampions = float((bronze_middle_sum_totalDamageDealtToChampions)/bronze_middle_num)
avg_bronze_middle_sum_totalDamageTaken = float((bronze_middle_sum_totalDamageTaken)/bronze_middle_num)
avg_bronze_middle_sum_totaloHeal = float((bronze_middle_sum_totaloHeal)/bronze_middle_num)
avg_bronze_middle_sum_visionScore = float((bronze_middle_sum_visionScore)/bronze_middle_num)
avg_bronze_middle_sum_goldEarned = float((bronze_middle_sum_goldEarned)/bronze_middle_num)
avg_bronze_middle_sum_turretKills = float((bronze_middle_sum_turretKills)/bronze_middle_num)
avg_bronze_middle_sum_totalMinionsKilled = float((bronze_middle_sum_totalMinionsKilled)/bronze_middle_num)
avg_bronze_middle_sum_champLevel = float((bronze_middle_sum_champLevel)/bronze_middle_num)
print()
print()
print('bronze_middle')
print(avg_bronze_middle_sum_kda)
print(avg_bronze_middle_sum_totalDamageDealtToChampions)
print(avg_bronze_middle_sum_totalDamageTaken)
print(avg_bronze_middle_sum_totaloHeal)
print(avg_bronze_middle_sum_visionScore)
print(avg_bronze_middle_sum_goldEarned)
print(avg_bronze_middle_sum_turretKills)
print(avg_bronze_middle_sum_totalMinionsKilled)
print(avg_bronze_middle_sum_champLevel)

avg_bronze_top_sum_kda = float((bronze_top_sum_kda)/bronze_top_num)
avg_bronze_top_sum_totalDamageDealtToChampions = float((bronze_top_sum_totalDamageDealtToChampions)/bronze_top_num)
avg_bronze_top_sum_totalDamageTaken = float((bronze_top_sum_totalDamageTaken)/bronze_top_num)
avg_bronze_top_sum_totaloHeal = float((bronze_top_sum_totaloHeal)/bronze_top_num)
avg_bronze_top_sum_visionScore = float((bronze_top_sum_visionScore)/bronze_top_num)
avg_bronze_top_sum_goldEarned = float((bronze_top_sum_goldEarned)/bronze_top_num)
avg_bronze_top_sum_turretKills = float((bronze_top_sum_turretKills)/bronze_top_num)
avg_bronze_top_sum_totalMinionsKilled = float((bronze_top_sum_totalMinionsKilled)/bronze_top_num)
avg_bronze_top_sum_champLevel = float((bronze_top_sum_champLevel)/bronze_top_num)
print()
print()
print('bronze_top')
print(avg_bronze_top_sum_kda)
print(avg_bronze_top_sum_totalDamageDealtToChampions)
print(avg_bronze_top_sum_totalDamageTaken)
print(avg_bronze_top_sum_totaloHeal)
print(avg_bronze_top_sum_visionScore)
print(avg_bronze_top_sum_goldEarned)
print(avg_bronze_top_sum_turretKills)
print(avg_bronze_top_sum_totalMinionsKilled)
print(avg_bronze_top_sum_champLevel)

avg_bronze_bottom_car_sum_kda = float((bronze_bottom_car_sum_kda)/bronze_bottom_car_num)
avg_bronze_bottom_car_sum_totalDamageDealtToChampions = float((bronze_bottom_car_sum_totalDamageDealtToChampions)/bronze_bottom_car_num)
avg_bronze_bottom_car_sum_totalDamageTaken = float((bronze_bottom_car_sum_totalDamageTaken)/bronze_bottom_car_num)
avg_bronze_bottom_car_sum_totaloHeal = float((bronze_bottom_car_sum_totaloHeal)/bronze_bottom_car_num)
avg_bronze_bottom_car_sum_visionScore = float((bronze_bottom_car_sum_visionScore)/bronze_bottom_car_num)
avg_bronze_bottom_car_sum_goldEarned = float((bronze_bottom_car_sum_goldEarned)/bronze_bottom_car_num)
avg_bronze_bottom_car_sum_turretKills = float((bronze_bottom_car_sum_turretKills)/bronze_bottom_car_num)
avg_bronze_bottom_car_sum_totalMinionsKilled = float((bronze_bottom_car_sum_totalMinionsKilled)/bronze_bottom_car_num)
avg_bronze_bottom_car_sum_champLevel = float((bronze_bottom_car_sum_champLevel)/bronze_bottom_car_num)
print()
print()
print('bronze_bottom_car')
print(avg_bronze_bottom_car_sum_kda)
print(avg_bronze_bottom_car_sum_totalDamageDealtToChampions)
print(avg_bronze_bottom_car_sum_totalDamageTaken)
print(avg_bronze_bottom_car_sum_totaloHeal)
print(avg_bronze_bottom_car_sum_visionScore)
print(avg_bronze_bottom_car_sum_goldEarned)
print(avg_bronze_bottom_car_sum_turretKills)
print(avg_bronze_bottom_car_sum_totalMinionsKilled)
print(avg_bronze_bottom_car_sum_champLevel)

avg_bronze_bottom_sup_sum_kda = float((bronze_bottom_sup_sum_kda)/bronze_bottom_sup_num)
avg_bronze_bottom_sup_sum_totalDamageDealtToChampions = float((bronze_bottom_sup_sum_totalDamageDealtToChampions)/bronze_bottom_sup_num)
avg_bronze_bottom_sup_sum_totalDamageTaken = float((bronze_bottom_sup_sum_totalDamageTaken)/bronze_bottom_sup_num)
avg_bronze_bottom_sup_sum_totaloHeal = float((bronze_bottom_sup_sum_totaloHeal)/bronze_bottom_sup_num)
avg_bronze_bottom_sup_sum_visionScore = float((bronze_bottom_sup_sum_visionScore)/bronze_bottom_sup_num)
avg_bronze_bottom_sup_sum_goldEarned = float((bronze_bottom_sup_sum_goldEarned)/bronze_bottom_sup_num)
avg_bronze_bottom_sup_sum_turretKills = float((bronze_bottom_sup_sum_turretKills)/bronze_bottom_sup_num)
avg_bronze_bottom_sup_sum_totalMinionsKilled = float((bronze_bottom_sup_sum_totalMinionsKilled)/bronze_bottom_sup_num)
avg_bronze_bottom_sup_sum_champLevel = float((bronze_bottom_sup_sum_champLevel)/bronze_bottom_sup_num)
print()
print()
print('bronze_bottom_sup')
print(avg_bronze_bottom_sup_sum_kda)
print(avg_bronze_bottom_sup_sum_totalDamageDealtToChampions)
print(avg_bronze_bottom_sup_sum_totalDamageTaken)
print(avg_bronze_bottom_sup_sum_totaloHeal)
print(avg_bronze_bottom_sup_sum_visionScore)
print(avg_bronze_bottom_sup_sum_goldEarned)
print(avg_bronze_bottom_sup_sum_turretKills)
print(avg_bronze_bottom_sup_sum_totalMinionsKilled)
print(avg_bronze_bottom_sup_sum_champLevel)


avg_silver_jungle_sum_kda = float((silver_jungle_sum_kda)/silver_jungle_num)
avg_silver_jungle_sum_totalDamageDealtToChampions = float((silver_jungle_sum_totalDamageDealtToChampions)/silver_jungle_num)
avg_silver_jungle_sum_totalDamageTaken = float((silver_jungle_sum_totalDamageTaken)/silver_jungle_num)
avg_silver_jungle_sum_totaloHeal = float((silver_jungle_sum_totaloHeal)/silver_jungle_num)
avg_silver_jungle_sum_visionScore = float((silver_jungle_sum_visionScore)/silver_jungle_num)
avg_silver_jungle_sum_goldEarned = float((silver_jungle_sum_goldEarned)/silver_jungle_num)
avg_silver_jungle_sum_turretKills = float((silver_jungle_sum_turretKills)/silver_jungle_num)
avg_silver_jungle_sum_totalMinionsKilled = float((silver_jungle_sum_totalMinionsKilled)/silver_jungle_num)
avg_silver_jungle_sum_champLevel = float((silver_jungle_sum_champLevel)/silver_jungle_num)
print()
print()
print()
print()
print('silver_jungle')
print(avg_silver_jungle_sum_kda)
print(avg_silver_jungle_sum_totalDamageDealtToChampions)
print(avg_silver_jungle_sum_totalDamageTaken)
print(avg_silver_jungle_sum_totaloHeal)
print(avg_silver_jungle_sum_visionScore)
print(avg_silver_jungle_sum_goldEarned)
print(avg_silver_jungle_sum_turretKills)
print(avg_silver_jungle_sum_totalMinionsKilled)
print(avg_silver_jungle_sum_champLevel)

avg_silver_middle_sum_kda = float((silver_jungle_sum_kda)/silver_middle_num)
avg_silver_middle_sum_totalDamageDealtToChampions = float((silver_middle_sum_totalDamageDealtToChampions)/silver_middle_num)
avg_silver_middle_sum_totalDamageTaken = float((silver_middle_sum_totalDamageTaken)/silver_middle_num)
avg_silver_middle_sum_totaloHeal = float((silver_middle_sum_totaloHeal)/silver_middle_num)
avg_silver_middle_sum_visionScore = float((silver_middle_sum_visionScore)/silver_middle_num)
avg_silver_middle_sum_goldEarned = float((silver_middle_sum_goldEarned)/silver_middle_num)
avg_silver_middle_sum_turretKills = float((silver_middle_sum_turretKills)/silver_middle_num)
avg_silver_middle_sum_totalMinionsKilled = float((silver_middle_sum_totalMinionsKilled)/silver_middle_num)
avg_silver_middle_sum_champLevel = float((silver_middle_sum_champLevel)/silver_middle_num)
print()
print()
print('silver_middle')
print(avg_silver_middle_sum_kda)
print(avg_silver_middle_sum_totalDamageDealtToChampions)
print(avg_silver_middle_sum_totalDamageTaken)
print(avg_silver_middle_sum_totaloHeal)
print(avg_silver_middle_sum_visionScore)
print(avg_silver_middle_sum_goldEarned)
print(avg_silver_middle_sum_turretKills)
print(avg_silver_middle_sum_totalMinionsKilled)
print(avg_silver_middle_sum_champLevel)


avg_silver_top_sum_kda = float((silver_top_sum_kda)/silver_top_num)
avg_silver_top_sum_totalDamageDealtToChampions = float((silver_top_sum_totalDamageDealtToChampions)/silver_top_num)
avg_silver_top_sum_totalDamageTaken = float((silver_top_sum_totalDamageTaken)/silver_top_num)
avg_silver_top_sum_totaloHeal = float((silver_top_sum_totaloHeal)/silver_top_num)
avg_silver_top_sum_visionScore = float((silver_top_sum_visionScore)/silver_top_num)
avg_silver_top_sum_goldEarned = float((silver_top_sum_goldEarned)/silver_top_num)
avg_silver_top_sum_turretKills = float((silver_top_sum_turretKills)/silver_top_num)
avg_silver_top_sum_totalMinionsKilled = float((silver_top_sum_totalMinionsKilled)/silver_top_num)
avg_silver_top_sum_champLevel = float((silver_top_sum_champLevel)/silver_top_num)
print()
print()
print('silver_top')
print(avg_silver_top_sum_kda)
print(avg_silver_top_sum_totalDamageDealtToChampions)
print(avg_silver_top_sum_totalDamageTaken)
print(avg_silver_top_sum_totaloHeal)
print(avg_silver_top_sum_visionScore)
print(avg_silver_top_sum_goldEarned)
print(avg_silver_top_sum_turretKills)
print(avg_silver_top_sum_totalMinionsKilled)
print(avg_silver_top_sum_champLevel)

avg_silver_bottom_car_sum_kda = float((silver_bottom_car_sum_kda)/silver_bottom_car_num)
avg_silver_bottom_car_sum_totalDamageDealtToChampions = float((silver_bottom_car_sum_totalDamageDealtToChampions)/silver_bottom_car_num)
avg_silver_bottom_car_sum_totalDamageTaken = float((silver_bottom_car_sum_totalDamageTaken)/silver_bottom_car_num)
avg_silver_bottom_car_sum_totaloHeal = float((silver_bottom_car_sum_totaloHeal)/silver_bottom_car_num)
avg_silver_bottom_car_sum_visionScore = float((silver_bottom_car_sum_visionScore)/silver_bottom_car_num)
avg_silver_bottom_car_sum_goldEarned = float((silver_bottom_car_sum_goldEarned)/silver_bottom_car_num)
avg_silver_bottom_car_sum_turretKills = float((silver_bottom_car_sum_turretKills)/silver_bottom_car_num)
avg_silver_bottom_car_sum_totalMinionsKilled = float((silver_bottom_car_sum_totalMinionsKilled)/silver_bottom_car_num)
avg_silver_bottom_car_sum_champLevel = float((silver_bottom_car_sum_champLevel)/silver_bottom_car_num)
print()
print()
print('silver_bottom_car')
print(avg_silver_bottom_car_sum_kda)
print(avg_silver_bottom_car_sum_totalDamageDealtToChampions)
print(avg_silver_bottom_car_sum_totalDamageTaken)
print(avg_silver_bottom_car_sum_totaloHeal)
print(avg_silver_bottom_car_sum_visionScore)
print(avg_silver_bottom_car_sum_goldEarned)
print(avg_silver_bottom_car_sum_turretKills)
print(avg_silver_bottom_car_sum_totalMinionsKilled)
print(avg_silver_bottom_car_sum_champLevel)

avg_silver_bottom_sup_sum_kda = float((silver_bottom_sup_sum_kda)/bronze_bottom_sup_num)
avg_silver_bottom_sup_sum_totalDamageDealtToChampions = float((silver_bottom_sup_sum_totalDamageDealtToChampions)/bronze_bottom_sup_num)
avg_silver_bottom_sup_sum_totalDamageTaken = float((silver_bottom_sup_sum_totalDamageTaken)/bronze_bottom_sup_num)
avg_silver_bottom_sup_sum_totaloHeal = float((silver_bottom_sup_sum_totaloHeal)/bronze_bottom_sup_num)
avg_silver_bottom_sup_sum_visionScore = float((silver_bottom_sup_sum_visionScore)/bronze_bottom_sup_num)
avg_silver_bottom_sup_sum_goldEarned = float((silver_bottom_sup_sum_goldEarned)/bronze_bottom_sup_num)
avg_silver_bottom_sup_sum_turretKills = float((silver_bottom_sup_sum_turretKills)/bronze_bottom_sup_num)
avg_silver_bottom_sup_sum_totalMinionsKilled = float((silver_bottom_sup_sum_totalMinionsKilled)/bronze_bottom_sup_num)
avg_silver_bottom_sup_sum_champLevel = float((silver_bottom_sup_sum_champLevel)/bronze_bottom_sup_num)
print()
print()
print('silver_bottom_sup')
print(avg_silver_bottom_sup_sum_kda)
print(avg_silver_bottom_sup_sum_totalDamageDealtToChampions)
print(avg_silver_bottom_sup_sum_totalDamageTaken)
print(avg_silver_bottom_sup_sum_totaloHeal)
print(avg_silver_bottom_sup_sum_visionScore)
print(avg_silver_bottom_sup_sum_goldEarned)
print(avg_silver_bottom_sup_sum_turretKills)
print(avg_silver_bottom_sup_sum_totalMinionsKilled)
print(avg_silver_bottom_sup_sum_champLevel)


avg_gold_jungle_sum_kda = float((gold_jungle_sum_kda)/gold_jungle_num)
avg_gold_jungle_sum_totalDamageDealtToChampions = float((gold_jungle_sum_totalDamageDealtToChampions)/gold_jungle_num)
avg_gold_jungle_sum_totalDamageTaken = float((gold_jungle_sum_totalDamageTaken)/gold_jungle_num)
avg_gold_jungle_sum_totaloHeal = float((gold_jungle_sum_totaloHeal)/gold_jungle_num)
avg_gold_jungle_sum_visionScore = float((gold_jungle_sum_visionScore)/gold_jungle_num)
avg_gold_jungle_sum_goldEarned = float((gold_bottom_sup_sum_goldEarned)/gold_jungle_num)
avg_gold_jungle_sum_turretKills = float((gold_jungle_sum_turretKills)/gold_jungle_num)
avg_gold_jungle_sum_totalMinionsKilled = float((gold_jungle_sum_totalMinionsKilled)/gold_jungle_num)
avg_gold_jungle_sum_champLevel = float((gold_jungle_sum_champLevel)/gold_jungle_num)
print()
print()
print()
print()
print('gold_jungle')
print(avg_gold_jungle_sum_kda)
print(avg_gold_jungle_sum_totalDamageDealtToChampions)
print(avg_gold_jungle_sum_totalDamageTaken)
print(avg_gold_jungle_sum_totaloHeal)
print(avg_gold_jungle_sum_visionScore)
print(avg_gold_jungle_sum_goldEarned)
print(avg_gold_jungle_sum_turretKills)
print(avg_gold_jungle_sum_totalMinionsKilled)
print(avg_gold_jungle_sum_champLevel)

avg_gold_middle_sum_kda = float((gold_middle_sum_kda)/gold_middle_num)
avg_gold_middle_sum_totalDamageDealtToChampions = float((gold_middle_sum_totalDamageDealtToChampions)/gold_middle_num)
avg_gold_middle_sum_totalDamageTaken = float((gold_middle_sum_totalDamageTaken)/gold_middle_num)
avg_gold_middle_sum_totaloHeal = float((gold_middle_sum_totaloHeal)/gold_middle_num)
avg_gold_middle_sum_visionScore = float((gold_middle_sum_visionScore)/gold_middle_num)
avg_gold_middle_sum_goldEarned = float((gold_bottom_sup_sum_goldEarned)/gold_middle_num)
avg_gold_middle_sum_turretKills = float((gold_middle_sum_turretKills)/gold_middle_num)
avg_gold_middle_sum_totalMinionsKilled = float((gold_middle_sum_totalMinionsKilled)/gold_middle_num)
avg_gold_middle_sum_champLevel = float((gold_middle_sum_champLevel)/gold_middle_num)

print(avg_gold_middle_sum_kda)
print(avg_gold_middle_sum_totalDamageDealtToChampions)
print(avg_gold_middle_sum_totalDamageTaken)
print(avg_gold_middle_sum_totaloHeal)
print(avg_gold_middle_sum_visionScore)
print(avg_gold_middle_sum_goldEarned)
print(avg_gold_middle_sum_turretKills)
print(avg_gold_middle_sum_totalMinionsKilled)
print(avg_gold_middle_sum_champLevel)

avg_gold_top_sum_kda = float((gold_top_sum_kda)/gold_top_num)
avg_gold_top_sum_totalDamageDealtToChampions = float((gold_top_sum_totalDamageDealtToChampions)/gold_top_num)
avg_gold_top_sum_totalDamageTaken = float((gold_top_sum_totalDamageTaken)/gold_top_num)
avg_gold_top_sum_totaloHeal = float((gold_top_sum_totaloHeal)/gold_top_num)
avg_gold_top_sum_visionScore = float((gold_top_sum_visionScore)/gold_top_num)
avg_gold_top_sum_goldEarned = float((gold_top_sum_goldEarned)/gold_top_num)
avg_gold_top_sum_turretKills = float((gold_top_sum_turretKills)/gold_top_num)
avg_gold_top_sum_totalMinionsKilled = float((gold_top_sum_totalMinionsKilled)/gold_top_num)
avg_gold_top_sum_champLevel = float((gold_top_sum_champLevel)/gold_top_num)
print()
print()
print('gold_top')
print(avg_gold_top_sum_kda)
print(avg_gold_top_sum_totalDamageDealtToChampions)
print(avg_gold_top_sum_totalDamageTaken)
print(avg_gold_top_sum_totaloHeal)
print(avg_gold_top_sum_visionScore)
print(avg_gold_top_sum_goldEarned)
print(avg_gold_top_sum_turretKills)
print(avg_gold_top_sum_totalMinionsKilled)
print(avg_gold_top_sum_champLevel)

avg_gold_bottom_car_sum_kda = float((gold_bottom_car_sum_kda )/gold_bottom_car_num)
avg_gold_bottom_car_sum_totalDamageDealtToChampions = float((gold_bottom_car_sum_totalDamageDealtToChampions)/gold_bottom_car_num)
avg_gold_bottom_car_sum_totalDamageTaken = float((gold_bottom_car_sum_totalDamageTaken)/gold_bottom_car_num)
avg_gold_bottom_car_sum_totaloHeal = float((gold_bottom_car_sum_totaloHeal)/gold_bottom_car_num)
avg_gold_bottom_car_sum_visionScore = float((gold_bottom_car_sum_visionScore)/gold_bottom_car_num)
avg_gold_bottom_car_sum_goldEarned = float((gold_bottom_sup_sum_goldEarned)/gold_bottom_car_num)
avg_gold_bottom_car_sum_turretKills = float((gold_bottom_car_sum_turretKills)/gold_bottom_car_num)
avg_gold_bottom_car_sum_totalMinionsKilled = float((gold_bottom_car_sum_totalMinionsKilled)/gold_bottom_car_num)
avg_gold_bottom_car_sum_champLevel = float((gold_bottom_car_sum_champLevel)/gold_bottom_car_num)
print()
print()
print('gold_bottom_car')
print(avg_gold_bottom_car_sum_kda)
print(avg_gold_bottom_car_sum_totalDamageDealtToChampions)
print(avg_gold_bottom_car_sum_totalDamageTaken)
print(avg_gold_bottom_car_sum_totaloHeal)
print(avg_gold_bottom_car_sum_visionScore)
print(avg_gold_bottom_car_sum_goldEarned)
print(avg_gold_bottom_car_sum_turretKills)
print(avg_gold_bottom_car_sum_totalMinionsKilled)
print(avg_gold_bottom_car_sum_champLevel)

avg_gold_bottom_sup_sum_kda = float((gold_bottom_sup_sum_kda)/gold_bottom_sup_num)
avg_gold_bottom_sup_sum_totalDamageDealtToChampions = float((gold_bottom_sup_sum_totalDamageDealtToChampions)/gold_bottom_sup_num)
avg_gold_bottom_sup_sum_totalDamageTaken = float((gold_bottom_sup_sum_totalDamageTaken)/gold_bottom_sup_num)
avg_gold_bottom_sup_sum_totaloHeal = float((gold_bottom_sup_sum_totaloHeal)/gold_bottom_sup_num)
avg_gold_bottom_sup_sum_visionScore = float((gold_bottom_sup_sum_visionScore)/gold_bottom_sup_num)
avg_gold_bottom_sup_sum_goldEarned = float((gold_bottom_sup_sum_goldEarned)/gold_bottom_sup_num)
avg_gold_bottom_sup_sum_turretKills = float((gold_bottom_sup_sum_turretKills)/gold_bottom_sup_num)
avg_gold_bottom_sup_sum_totalMinionsKilled = float((gold_bottom_sup_sum_totalMinionsKilled)/gold_bottom_sup_num)
avg_gold_bottom_sup_sum_champLevel = float((gold_bottom_sup_sum_champLevel)/gold_bottom_sup_num)

print()
print()
print('gold_bottom_sup')
print(avg_gold_bottom_sup_sum_kda)
print(avg_gold_bottom_sup_sum_totalDamageDealtToChampions)
print(avg_gold_bottom_sup_sum_totalDamageTaken)
print(avg_gold_bottom_sup_sum_totaloHeal)
print(avg_gold_bottom_sup_sum_visionScore)
print(avg_gold_bottom_sup_sum_goldEarned)
print(avg_gold_bottom_sup_sum_turretKills)
print(avg_gold_bottom_sup_sum_totalMinionsKilled)
print(avg_gold_bottom_sup_sum_champLevel)



avg_platinum_jungle_sum_kda = float((platinum_jungle_sum_kda)/platinum_jungle_num)
avg_platinum_jungle_sum_totalDamageDealtToChampions = float((platinum_jungle_sum_totalDamageDealtToChampions)/platinum_jungle_num)
avg_platinum_jungle_sum_totalDamageTaken = float((platinum_jungle_sum_totalDamageTaken)/platinum_jungle_num)
avg_platinum_jungle_sum_totaloHeal = float((platinum_jungle_sum_totaloHeal)/platinum_jungle_num)
avg_platinum_jungle_sum_visionScore = float((platinum_jungle_sum_visionScore)/platinum_jungle_num)
avg_platinum_jungle_sum_goldEarned = float((platinum_jungle_sum_goldEarned)/platinum_jungle_num)
avg_platinum_jungle_sum_turretKills = float((platinum_jungle_sum_turretKills)/platinum_jungle_num)
avg_platinum_jungle_sum_totalMinionsKilled = float((platinum_jungle_sum_totalMinionsKilled)/platinum_jungle_num)
avg_platinum_jungle_sum_champLevel = float((platinum_jungle_sum_champLevel)/platinum_jungle_num)
print()
print()
print()
print()
print('platinum_jungle')
print(avg_platinum_jungle_sum_kda)
print(avg_platinum_jungle_sum_totalDamageDealtToChampions)
print(avg_platinum_jungle_sum_totalDamageTaken)
print(avg_platinum_jungle_sum_totaloHeal)
print(avg_platinum_jungle_sum_visionScore)
print(avg_platinum_jungle_sum_goldEarned)
print(avg_platinum_jungle_sum_turretKills)
print(avg_platinum_jungle_sum_totalMinionsKilled)
print(avg_platinum_jungle_sum_champLevel)

avg_platinum_middle_sum_kda = float((platinum_middle_sum_kda)/platinum_middle_num)
avg_platinum_middle_sum_totalDamageDealtToChampions = float((platinum_middle_sum_totalDamageDealtToChampions)/platinum_middle_num)
avg_platinum_middle_sum_totalDamageTaken = float((platinum_middle_sum_totalDamageTaken)/platinum_middle_num)
avg_platinum_middle_sum_totaloHeal = float((platinum_middle_sum_totaloHeal)/platinum_middle_num)
avg_platinum_middle_sum_visionScore = float((platinum_middle_sum_visionScore)/platinum_middle_num)
avg_platinum_middle_sum_goldEarned = float((platinum_middle_sum_goldEarned)/platinum_middle_num)
avg_platinum_middle_sum_turretKills = float((platinum_middle_sum_turretKills)/platinum_middle_num)
avg_platinum_middle_sum_totalMinionsKilled = float((platinum_middle_sum_totalMinionsKilled)/platinum_middle_num)
avg_platinum_middle_sum_champLevel = float((platinum_middle_sum_champLevel)/platinum_middle_num)
print()
print()
print('platinum_middle')
print(avg_platinum_middle_sum_kda)
print(avg_platinum_middle_sum_totalDamageDealtToChampions)
print(avg_platinum_middle_sum_totalDamageTaken)
print(avg_platinum_middle_sum_totaloHeal)
print(avg_platinum_middle_sum_visionScore)
print(avg_platinum_middle_sum_goldEarned)
print(avg_platinum_middle_sum_turretKills)
print(avg_platinum_middle_sum_totalMinionsKilled)
print(avg_platinum_middle_sum_champLevel)

avg_platinum_top_sum_kda = float((platinum_top_sum_kda)/platinum_top_num)
avg_platinum_top_sum_totalDamageDealtToChampions = float((platinum_top_sum_totalDamageDealtToChampions)/platinum_top_num)
avg_platinum_top_sum_totalDamageTaken = float((platinum_top_sum_totalDamageTaken)/platinum_top_num)
avg_platinum_top_sum_totaloHeal = float((platinum_top_sum_totaloHeal)/platinum_top_num)
avg_platinum_top_sum_visionScore = float((platinum_top_sum_visionScore)/platinum_top_num)
avg_platinum_top_sum_goldEarned = float((platinum_top_sum_goldEarned)/platinum_top_num)
avg_platinum_top_sum_turretKills = float((platinum_top_sum_turretKills)/platinum_top_num)
avg_platinum_top_sum_totalMinionsKilled = float((platinum_top_sum_totalMinionsKilled)/platinum_top_num)
avg_platinum_top_sum_champLevel = float((platinum_top_sum_champLevel)/platinum_top_num)
print()
print()
print('platinum_top')
print(avg_platinum_top_sum_kda)
print(avg_platinum_top_sum_totalDamageDealtToChampions)
print(avg_platinum_top_sum_totalDamageTaken)
print(avg_platinum_top_sum_totaloHeal)
print(avg_platinum_top_sum_visionScore)
print(avg_platinum_top_sum_goldEarned)
print(avg_platinum_top_sum_turretKills)
print(avg_platinum_top_sum_totalMinionsKilled)
print(avg_platinum_top_sum_champLevel)

avg_platinum_bottom_car_sum_kda = float((platinum_bottom_car_sum_kda)/platinum_bottom_car_num)
avg_platinum_bottom_car_sum_totalDamageDealtToChampions = float((platinum_bottom_car_sum_totalDamageDealtToChampions)/platinum_bottom_car_num)
avg_platinum_bottom_car_sum_totalDamageTaken = float((platinum_bottom_car_sum_totalDamageTaken)/platinum_bottom_car_num)
avg_platinum_bottom_car_sum_totaloHeal = float((platinum_bottom_car_sum_totaloHeal)/platinum_bottom_car_num)
avg_platinum_bottom_car_sum_visionScore = float((platinum_bottom_car_sum_visionScore)/platinum_bottom_car_num)
avg_platinum_bottom_car_sum_goldEarned = float((platinum_bottom_car_sum_goldEarned)/platinum_bottom_car_num)
avg_platinum_bottom_car_sum_turretKills = float((platinum_bottom_car_sum_turretKills)/platinum_bottom_car_num)
avg_platinum_bottom_car_sum_totalMinionsKilled = float((platinum_bottom_car_sum_totalMinionsKilled)/platinum_bottom_car_num)
avg_platinum_bottom_car_sum_champLevel = float((platinum_bottom_car_sum_champLevel)/platinum_bottom_car_num)
print()
print()
print('platinum_bottom_car')
print(avg_platinum_bottom_car_sum_kda)
print(avg_platinum_bottom_car_sum_totalDamageDealtToChampions)
print(avg_platinum_bottom_car_sum_totalDamageTaken)
print(avg_platinum_bottom_car_sum_totaloHeal)
print(avg_platinum_bottom_car_sum_visionScore)
print(avg_platinum_bottom_car_sum_goldEarned)
print(avg_platinum_bottom_car_sum_turretKills)
print(avg_platinum_bottom_car_sum_totalMinionsKilled)
print(avg_platinum_bottom_car_sum_champLevel)

avg_platinum_bottom_sup_sum_kda = float((platinum_bottom_sup_sum_kda)/platinum_bottom_sup_num)
avg_platinum_bottom_sup_sum_totalDamageDealtToChampions = float((platinum_bottom_sup_sum_totalDamageDealtToChampions)/platinum_bottom_sup_num)
avg_platinum_bottom_sup_sum_totalDamageTaken = float((platinum_bottom_sup_sum_totalDamageTaken)/platinum_bottom_sup_num)
avg_platinum_bottom_sup_sum_totaloHeal = float((platinum_bottom_sup_sum_totaloHeal)/platinum_bottom_sup_num)
avg_platinum_bottom_sup_sum_visionScore = float((platinum_bottom_sup_sum_visionScore)/platinum_bottom_sup_num)
avg_platinum_bottom_sup_sum_goldEarned = float((platinum_bottom_sup_sum_goldEarned)/platinum_bottom_sup_num)
avg_platinum_bottom_sup_sum_turretKills = float((platinum_bottom_sup_sum_turretKills)/platinum_bottom_sup_num)
avg_platinum_bottom_sup_sum_totalMinionsKilled = float((platinum_bottom_sup_sum_totalMinionsKilled)/platinum_bottom_sup_num)
avg_platinum_bottom_sup_sum_champLevel = float((platinum_bottom_sup_sum_champLevel)/platinum_bottom_sup_num)
print()
print()
print('platinum_bottom_sup')
print(avg_platinum_bottom_sup_sum_kda)
print(avg_platinum_bottom_sup_sum_totalDamageDealtToChampions)
print(avg_platinum_bottom_sup_sum_totalDamageTaken)
print(avg_platinum_bottom_sup_sum_totaloHeal)
print(avg_platinum_bottom_sup_sum_visionScore)
print(avg_platinum_bottom_sup_sum_goldEarned)
print(avg_platinum_bottom_sup_sum_turretKills)
print(avg_platinum_bottom_sup_sum_totalMinionsKilled)
print(avg_platinum_bottom_sup_sum_champLevel)



avg_dia_jungle_sum_kda = float((dia_jungle_sum_kda)/dia_jungle_num)
avg_dia_jungle_sum_totalDamageDealtToChampions = float((dia_jungle_sum_totalDamageDealtToChampions)/dia_jungle_num)
avg_dia_jungle_sum_totalDamageTaken = float((dia_jungle_sum_totalDamageTaken)/dia_jungle_num)
avg_dia_jungle_sum_totaloHeal = float((dia_jungle_sum_totaloHeal)/dia_jungle_num)
avg_dia_jungle_sum_visionScore = float((dia_jungle_sum_visionScore)/dia_jungle_num)
avg_dia_jungle_sum_goldEarned = float((dia_jungle_sum_goldEarned)/dia_jungle_num)
avg_dia_jungle_sum_turretKills = float((dia_jungle_sum_turretKills)/dia_jungle_num)
avg_dia_jungle_sum_totalMinionsKilled = float((dia_jungle_sum_totalMinionsKilled)/dia_jungle_num)
avg_dia_jungle_sum_champLevel = float((dia_jungle_sum_champLevel)/dia_jungle_num)
print()
print()
print()
print()
print('dia_jungle')
print(avg_dia_jungle_sum_kda)
print(avg_dia_jungle_sum_totalDamageDealtToChampions)
print(avg_dia_jungle_sum_totalDamageTaken)
print(avg_dia_jungle_sum_totaloHeal)
print(avg_dia_jungle_sum_visionScore)
print(avg_dia_jungle_sum_goldEarned)
print(avg_dia_jungle_sum_turretKills)
print(avg_dia_jungle_sum_totalMinionsKilled)
print(avg_dia_jungle_sum_champLevel)


avg_dia_middle_sum_kda = float((dia_middle_sum_kda)/dia_middle_num)
avg_dia_middle_sum_totalDamageDealtToChampions = float((dia_middle_sum_totalDamageDealtToChampions)/dia_middle_num)
avg_dia_middle_sum_totalDamageTaken = float((dia_middle_sum_totalDamageTaken)/dia_middle_num)
avg_dia_middle_sum_totaloHeal = float((dia_middle_sum_totaloHeal)/dia_middle_num)
avg_dia_middle_sum_visionScore = float((dia_middle_sum_visionScore)/dia_middle_num)
avg_dia_middle_sum_goldEarned = float((dia_middle_sum_goldEarned)/dia_middle_num)
avg_dia_middle_sum_turretKills = float((dia_middle_sum_turretKills)/dia_middle_num)
avg_dia_middle_sum_totalMinionsKilled = float((dia_middle_sum_totalMinionsKilled)/dia_middle_num)
avg_dia_middle_sum_champLevel = float((dia_middle_sum_champLevel)/dia_middle_num)

print('dia_middle')
print(avg_dia_middle_sum_kda)
print(avg_dia_middle_sum_totalDamageDealtToChampions)
print(avg_dia_middle_sum_totalDamageTaken)
print(avg_dia_middle_sum_totaloHeal)
print(avg_dia_middle_sum_visionScore)
print(avg_dia_middle_sum_goldEarned)
print(avg_dia_middle_sum_turretKills)
print(avg_dia_middle_sum_totalMinionsKilled)
print(avg_dia_middle_sum_champLevel)

avg_dia_top_sum_kda = float((dia_top_sum_kda)/dia_top_num)
avg_dia_top_sum_totalDamageDealtToChampions = float((dia_top_sum_totalDamageDealtToChampions)/dia_top_num)
avg_dia_top_sum_totalDamageTaken = float((dia_top_sum_totalDamageTaken)/dia_top_num)
avg_dia_top_sum_totaloHeal = float((dia_top_sum_totaloHeal)/dia_top_num)
avg_dia_top_sum_visionScore = float((dia_top_sum_visionScore)/dia_top_num)
avg_dia_top_sum_goldEarned = float((dia_top_sum_goldEarned)/dia_top_num)
avg_dia_top_sum_turretKills = float((dia_top_sum_turretKills)/dia_top_num)
avg_dia_top_sum_totalMinionsKilled = float((dia_top_sum_totalMinionsKilled)/dia_top_num)
avg_dia_top_sum_champLevel = float((dia_top_sum_champLevel)/dia_top_num)
print()
print()
print('dia_top')
print(avg_dia_top_sum_kda)
print(avg_dia_top_sum_totalDamageDealtToChampions)
print(avg_dia_top_sum_totalDamageTaken)
print(avg_dia_top_sum_totaloHeal)
print(avg_dia_top_sum_visionScore)
print(avg_dia_top_sum_goldEarned)
print(avg_dia_top_sum_turretKills)
print(avg_dia_top_sum_totalMinionsKilled)
print(avg_dia_top_sum_champLevel)

avg_dia_bottom_car_sum_kda = float((dia_bottom_car_sum_kda)/dia_bottom_car_num)
avg_dia_bottom_car_sum_totalDamageDealtToChampions = float((dia_bottom_car_sum_totalDamageDealtToChampions)/dia_bottom_car_num)
avg_dia_bottom_car_sum_totalDamageTaken = float((dia_bottom_car_sum_totalDamageTaken)/dia_bottom_car_num)
avg_dia_bottom_car_sum_totaloHeal = float((dia_bottom_car_sum_totaloHeal)/dia_bottom_car_num)
avg_dia_bottom_car_sum_visionScore = float((dia_bottom_car_sum_visionScore)/dia_bottom_car_num)
avg_dia_bottom_car_sum_goldEarned = float((dia_bottom_car_sum_goldEarned)/dia_bottom_car_num)
avg_dia_bottom_car_sum_turretKills = float((dia_bottom_car_sum_turretKills)/dia_bottom_car_num)
avg_dia_bottom_car_sum_totalMinionsKilled = float((dia_bottom_car_sum_totalMinionsKilled)/dia_bottom_car_num)
avg_dia_bottom_car_sum_champLevel = float((dia_bottom_car_sum_champLevel)/dia_bottom_car_num)
print()
print()
print('dia_bottom_car')
print(avg_dia_bottom_car_sum_kda)
print(avg_dia_bottom_car_sum_totalDamageDealtToChampions)
print(avg_dia_bottom_car_sum_totalDamageTaken)
print(avg_dia_bottom_car_sum_totaloHeal)
print(avg_dia_bottom_car_sum_visionScore)
print(avg_dia_bottom_car_sum_goldEarned)
print(avg_dia_bottom_car_sum_turretKills)
print(avg_dia_bottom_car_sum_totalMinionsKilled)
print(avg_dia_bottom_car_sum_champLevel)

avg_dia_bottom_sup_sum_kda = float((dia_bottom_sup_sum_kda)/dia_bottom_sup_num)
avg_dia_bottom_sup_sum_totalDamageDealtToChampions = float((dia_bottom_sup_sum_totalDamageDealtToChampions)/dia_bottom_sup_num)
avg_dia_bottom_sup_sum_totalDamageTaken = float((dia_bottom_sup_sum_totalDamageTaken)/dia_bottom_sup_num)
avg_dia_bottom_sup_sum_totaloHeal = float((dia_bottom_sup_sum_totaloHeal)/dia_bottom_sup_num)
avg_dia_bottom_sup_sum_visionScore = float((dia_bottom_sup_sum_visionScore)/dia_bottom_sup_num)
avg_dia_bottom_sup_sum_goldEarned = float((dia_bottom_sup_sum_goldEarned)/dia_bottom_sup_num)
avg_dia_bottom_sup_sum_turretKills = float((dia_bottom_sup_sum_turretKills)/dia_bottom_sup_num)
avg_dia_bottom_sup_sum_totalMinionsKilled = float((dia_bottom_sup_sum_totalMinionsKilled)/dia_bottom_sup_num)
avg_dia_bottom_sup_sum_champLevel = float((dia_bottom_sup_sum_champLevel)/dia_bottom_sup_num)
print()
print()
print('dia_dia_bottom_sup')
print(avg_dia_bottom_sup_sum_kda)
print(avg_dia_bottom_sup_sum_totalDamageDealtToChampions)
print(avg_dia_bottom_sup_sum_totalDamageTaken)
print(avg_dia_bottom_sup_sum_totaloHeal)
print(avg_dia_bottom_sup_sum_visionScore)
print(avg_dia_bottom_sup_sum_goldEarned)
print(avg_dia_bottom_sup_sum_turretKills)
print(avg_dia_bottom_sup_sum_totalMinionsKilled)
print(avg_dia_bottom_sup_sum_champLevel)


avg_master_jungle_sum_kda = float((master_jungle_sum_kda)/master_jungle_num)
avg_master_jungle_sum_totalDamageDealtToChampions = float((master_jungle_sum_totalDamageDealtToChampions)/master_jungle_num)
avg_master_jungle_sum_totalDamageTaken = float((master_jungle_sum_totalDamageTaken)/master_jungle_num)
avg_master_jungle_sum_totaloHeal = float((master_jungle_sum_totaloHeal)/master_jungle_num)
avg_master_jungle_sum_visionScore = float((master_jungle_sum_visionScore)/master_jungle_num)
avg_master_jungle_sum_goldEarned = float((master_jungle_sum_goldEarned)/master_jungle_num)
avg_master_jungle_sum_turretKills = float((master_jungle_sum_turretKills)/master_jungle_num)
avg_master_jungle_sum_totalMinionsKilled = float((master_jungle_sum_totalMinionsKilled)/master_jungle_num)
avg_master_jungle_sum_champLevel = float((master_jungle_sum_champLevel)/master_jungle_num)
print()
print()
print()
print()
print('master_jungle')
print(avg_master_jungle_sum_kda)
print(avg_master_jungle_sum_totalDamageDealtToChampions)
print(avg_master_jungle_sum_totalDamageTaken)
print(avg_master_jungle_sum_totaloHeal)
print(avg_master_jungle_sum_visionScore)
print(avg_master_jungle_sum_goldEarned)
print(avg_master_jungle_sum_turretKills)
print(avg_master_jungle_sum_totalMinionsKilled)
print(avg_master_jungle_sum_champLevel)

avg_master_middle_sum_kda = float((master_middle_sum_kda)/master_middle_num)
avg_master_middle_sum_totalDamageDealtToChampions = float((master_middle_sum_totalDamageDealtToChampions)/master_middle_num)
avg_master_middle_sum_totalDamageTaken = float((master_middle_sum_totalDamageTaken)/master_middle_num)
avg_master_middle_sum_totaloHeal = float((master_middle_sum_totaloHeal )/master_middle_num)
avg_master_middle_sum_visionScore = float((master_middle_sum_visionScore)/master_middle_num)
avg_master_middle_sum_goldEarned = float((master_middle_sum_goldEarned)/master_middle_num)
avg_master_middle_sum_turretKills = float((master_middle_sum_turretKills)/master_middle_num)
avg_master_middle_sum_totalMinionsKilled = float((master_middle_sum_totalMinionsKilled)/master_middle_num)
avg_master_middle_sum_champLevel = float((master_middle_sum_champLevel )/master_middle_num)

print()
print()
print('master_middle')
print(avg_master_middle_sum_kda)
print(avg_master_middle_sum_totalDamageDealtToChampions)
print(avg_master_middle_sum_totalDamageTaken)
print(avg_master_middle_sum_totaloHeal)
print(avg_master_middle_sum_visionScore)
print(avg_master_middle_sum_goldEarned)
print(avg_master_middle_sum_turretKills)
print(avg_master_middle_sum_totalMinionsKilled)
print(avg_master_middle_sum_champLevel)

avg_master_top_sum_kda = float((master_top_sum_kda)/master_top_num)
avg_master_top_sum_totalDamageDealtToChampions = float((master_top_sum_totalDamageDealtToChampions)/master_top_num)
avg_master_top_sum_totalDamageTaken = float((master_top_sum_totalDamageTaken)/master_top_num)
avg_master_top_sum_totaloHeal = float((master_top_sum_totaloHeal)/master_top_num)
avg_master_top_sum_visionScore = float((master_top_sum_visionScore)/master_top_num)
avg_master_top_sum_goldEarned = float((master_top_sum_goldEarned)/master_top_num)
avg_master_top_sum_turretKills = float((master_top_sum_turretKills)/master_top_num)
avg_master_top_sum_totalMinionsKilled = float((master_top_sum_totalMinionsKilled)/master_top_num)
avg_master_top_sum_champLevel = float((master_top_sum_champLevel)/master_top_num)
print()
print()
print('master_top')
print(avg_master_top_sum_kda)
print(avg_master_top_sum_totalDamageDealtToChampions)
print(avg_master_top_sum_totalDamageTaken)
print(avg_master_top_sum_totaloHeal)
print(avg_master_top_sum_visionScore)
print(avg_master_top_sum_goldEarned)
print(avg_master_top_sum_turretKills)
print(avg_master_top_sum_totalMinionsKilled)
print(avg_master_top_sum_champLevel)

avg_master_bottom_car_sum_kda = float((master_bottom_car_sum_kda)/master_bottom_car_num)
avg_master_bottom_car_sum_totalDamageDealtToChampions = float((master_bottom_car_sum_totalDamageDealtToChampions)/master_bottom_car_num)
avg_master_bottom_car_sum_totalDamageTaken = float((master_bottom_car_sum_totalDamageTaken)/master_bottom_car_num)
avg_master_bottom_car_sum_totaloHeal = float((master_bottom_car_sum_totaloHeal)/master_bottom_car_num)
avg_master_bottom_car_sum_visionScore = float((master_bottom_car_sum_visionScore)/master_bottom_car_num)
avg_master_bottom_car_sum_goldEarned = float((master_bottom_car_sum_goldEarned)/master_bottom_car_num)
avg_master_bottom_car_sum_turretKills = float((master_bottom_car_sum_turretKills)/master_bottom_car_num)
avg_master_bottom_car_sum_totalMinionsKilled = float((master_bottom_car_sum_totalMinionsKilled)/master_bottom_car_num)
avg_master_bottom_car_sum_champLevel = float((master_bottom_car_sum_champLevel)/master_bottom_car_num)
print()
print()
print('master_bottom_car')
print(avg_master_bottom_car_sum_kda)
print(avg_master_bottom_car_sum_totalDamageDealtToChampions)
print(avg_master_bottom_car_sum_totalDamageTaken)
print(avg_master_bottom_car_sum_totaloHeal)
print(avg_master_bottom_car_sum_visionScore)
print(avg_master_bottom_car_sum_goldEarned)
print(avg_master_bottom_car_sum_turretKills)
print(avg_master_bottom_car_sum_totalMinionsKilled)
print(avg_master_bottom_car_sum_champLevel)

avg_master_bottom_sup_sum_kda = float((master_bottom_sup_sum_kda)/master_bottom_sup_num)
avg_master_bottom_sup_sum_totalDamageDealtToChampions = float((master_bottom_sup_sum_totalDamageDealtToChampions)/master_bottom_sup_num)
avg_master_bottom_sup_sum_totalDamageTaken = float((master_bottom_sup_sum_totalDamageTaken)/master_bottom_sup_num)
avg_master_bottom_sup_sum_totaloHeal = float((master_bottom_sup_sum_totaloHeal)/master_bottom_sup_num)
avg_master_bottom_sup_sum_visionScore = float((master_bottom_sup_sum_visionScore)/master_bottom_sup_num)
avg_master_bottom_sup_sum_goldEarned = float((master_bottom_sup_sum_goldEarned)/master_bottom_sup_num)
avg_master_bottom_sup_sum_turretKills = float((master_bottom_sup_sum_turretKills)/master_bottom_sup_num)
avg_master_bottom_sup_sum_totalMinionsKilled = float((master_bottom_sup_sum_totalMinionsKilled)/master_bottom_sup_num)
avg_master_bottom_sup_sum_champLevel = float((master_bottom_sup_sum_champLevel)/master_bottom_sup_num)
print()
print()
print('master_bottom_sup')
print(avg_master_bottom_sup_sum_kda)
print(avg_master_bottom_sup_sum_totalDamageDealtToChampions)
print(avg_master_bottom_sup_sum_totalDamageTaken)
print(avg_master_bottom_sup_sum_totaloHeal)
print(avg_master_bottom_sup_sum_visionScore)
print(avg_master_bottom_sup_sum_goldEarned)
print(avg_master_bottom_sup_sum_turretKills)
print(avg_master_bottom_sup_sum_totalMinionsKilled)
print(avg_master_bottom_sup_sum_champLevel)








# temp_test_output = list(data_col_output.values)[40000:]
# temp_test_input1 = list(data_col_input1.values)[40000:]
# temp_test_input2 = list(data_col_input2.values)[40000:]
# temp_test_input3 = list(data_col_input3.values)[40000:]
# temp_test_input4 = list(data_col_input4.values)[40000:]
# temp_test_input5 = list(data_col_input5.values)[40000:]
# temp_test_input6 = list(data_col_input6.values)[40000:]
#
# test_output = []
# test_input1 = []
# test_input2 = []
# test_input3 = []
# test_input4 = []
# test_input5 = []
# test_input6 = []
#
# for i in range(len(temp_test_output)):
#     if(temp_test_output[i][0]=="1"):
#         test_output.append(1)
#     else:
#         test_output.append(-1)
#
#     if(temp_test_input1[i][0]=="1"):
#         test_input1.append(1)
#     else:
#         test_input1.append(-1)
#
#     if(temp_test_input2[i][0]=="1"):
#         test_input2.append(1)
#     else:
#         test_input2.append(-1)
#
#     if(temp_test_input3[i][0]=="1"):
#         test_input3.append(1)
#     else:
#         test_input3.append(-1)
#
#     if(temp_test_input4[i][0]=="1"):
#         test_input4.append(1)
#     else:
#         test_input4.append(-1)
#
#     if(temp_test_input5[i][0]=="1"):
#         test_input5.append(1)
#     else:
#         test_input5.append(-1)
#
#     if(temp_test_input6[i][0]=="1"):
#         test_input6.append(1)
#     else:
#         test_input6.append(-1)
#
# float_W1 = float(list(sess.run(W1))[0])
# float_W2 = float(list(sess.run(W2))[0])
# float_W3 = float(list(sess.run(W3))[0])
# float_W4 = float(list(sess.run(W4))[0])
# float_W5 = float(list(sess.run(W5))[0])
# float_W6 = float(list(sess.run(W6))[0])
# float_b = float(list(sess.run(b))[0])
# success = 0
# fail = 0
#
# for i in range(len(test_output)):
#     result = float_W1 * test_input1[i] + float_W2 * test_input2[i] + float_W3 * test_input3[i] + float_W4 * test_input4[i] + float_W5 * test_input5[i] + float_W6 * test_input6[i] + float_b
#     if(result>0):
#         if(1==test_output[i]):
#             success+=1
#         else:
#             fail+=1
#
#     else:
#         if(-1==test_output[i]):
#             success+=1
#         else:
#             fail+=1
#
# print(success)
# print(fail)
# percentage = success / (success + fail)
# print("성공률: %f" % percentage)
