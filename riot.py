import requests
import pprint
import json
import csv
import time

api_key = 'RGAPI-eaef0d4b-a43f-40c1-9aa7-0d988735d743'
getuserid = "https://kr.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/DIAMOND/I"+'?api_key=' + api_key
req1 = requests.get(getuserid)
count = 0
for i in range(10):
    print(pprint.pprint(req1.json()[i]["summonerName"]))
    summonerName = req1.json()[i]["summonerName"]
    getaccountId = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+ str(summonerName) +'?api_key=' + api_key
    req2 = requests.get(getaccountId)
    print(pprint.pprint(req2.json()))
    accountId = req2.json()["accountId"]
    getgameList = "https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/" + accountId +'?api_key=' + api_key
    req3 = requests.get(getgameList)
    for j in range(5):
        gameId = req3.json()["matches"][j]["gameId"]
        print(gameId)
        getgameContent = "https://kr.api.riotgames.com/lol/match/v4/matches/"+ str(gameId) +'?api_key=' + api_key
        req4 = requests.get(getgameContent)
        gameContent = req4.json()
        print(pprint.pprint(gameContent))
        f = open('C:\\Users\q\datas\\dia'+str(count)+'.csv','w', newline = '')
        csv_file = csv.writer(f)
        index = ['gameDuration','gameId',
                'participants.0.stats.kills','participants.0.stats.deaths','participants.0.stats.assists','participants.0.stats.totalDamageDealtToChampions','participants.0.stats.totalDamageTaken','participants.0.stats.totalHeal','participants.0.stats.visionScore','participants.0.stats.goldEarned','participants.0.stats.turretKills','participants.0.stats.totalMinionsKilled','participants.0.stats.champLevel','participants.0.timeline.lane','participants.0.timeline.role',
                'participants.1.stats.kills','participants.1.stats.deaths','participants.1.stats.assists','participants.1.stats.totalDamageDealtToChampions','participants.1.stats.totalDamageTaken','participants.1.stats.totalHeal','participants.1.stats.visionScore','participants.1.stats.goldEarned','participants.1.stats.turretKills','participants.1.stats.totalMinionsKilled','participants.1.stats.champLevel','participants.1.timeline.lane','participants.1.timeline.role',
                'participants.2.stats.kills','participants.2.stats.deaths','participants.2.stats.assists','participants.2.stats.totalDamageDealtToChampions','participants.2.stats.totalDamageTaken','participants.2.stats.totalHeal','participants.2.stats.visionScore','participants.2.stats.goldEarned','participants.2.stats.turretKills','participants.2.stats.totalMinionsKilled','participants.2.stats.champLevel','participants.2.timeline.lane','participants.2.timeline.role',
                'participants.3.stats.kills','participants.3.stats.deaths','participants.3.stats.assists','participants.3.stats.totalDamageDealtToChampions','participants.3.stats.totalDamageTaken','participants.3.stats.totalHeal','participants.3.stats.visionScore','participants.3.stats.goldEarned','participants.3.stats.turretKills','participants.3.stats.totalMinionsKilled','participants.3.stats.champLevel','participants.3.timeline.lane','participants.3.timeline.role',
                'participants.4.stats.kills','participants.4.stats.deaths','participants.4.stats.assists','participants.4.stats.totalDamageDealtToChampions','participants.4.stats.totalDamageTaken','participants.4.stats.totalHeal','participants.4.stats.visionScore','participants.4.stats.goldEarned','participants.4.stats.turretKills','participants.4.stats.totalMinionsKilled','participants.4.stats.champLevel','participants.4.timeline.lane','participants.4.timeline.role',
                'participants.5.stats.kills','participants.5.stats.deaths','participants.5.stats.assists','participants.5.stats.totalDamageDealtToChampions','participants.5.stats.totalDamageTaken','participants.5.stats.totalHeal','participants.5.stats.visionScore','participants.5.stats.goldEarned','participants.5.stats.turretKills','participants.5.stats.totalMinionsKilled','participants.5.stats.champLevel','participants.5.timeline.lane','participants.5.timeline.role',
                'participants.6.stats.kills','participants.6.stats.deaths','participants.6.stats.assists','participants.6.stats.totalDamageDealtToChampions','participants.6.stats.totalDamageTaken','participants.6.stats.totalHeal','participants.6.stats.visionScore','participants.6.stats.goldEarned','participants.6.stats.turretKills','participants.6.stats.totalMinionsKilled','participants.6.stats.champLevel','participants.6.timeline.lane','participants.6.timeline.role',
                'participants.7.stats.kills','participants.7.stats.deaths','participants.7.stats.assists','participants.7.stats.totalDamageDealtToChampions','participants.7.stats.totalDamageTaken','participants.7.stats.totalHeal','participants.7.stats.visionScore','participants.7.stats.goldEarned','participants.7.stats.turretKills','participants.7.stats.totalMinionsKilled','participants.7.stats.champLevel','participants.7.timeline.lane','participants.7.timeline.role',
                'participants.8.stats.kills','participants.8.stats.deaths','participants.8.stats.assists','participants.8.stats.totalDamageDealtToChampions','participants.8.stats.totalDamageTaken','participants.8.stats.totalHeal','participants.8.stats.visionScore','participants.8.stats.goldEarned','participants.8.stats.turretKills','participants.8.stats.totalMinionsKilled','participants.8.stats.champLevel','participants.8.timeline.lane','participants.8.timeline.role',
                'participants.9.stats.kills','participants.9.stats.deaths','participants.9.stats.assists','participants.9.stats.totalDamageDealtToChampions','participants.9.stats.totalDamageTaken','participants.9.stats.totalHeal','participants.9.stats.visionScore','participants.9.stats.goldEarned','participants.9.stats.turretKills','participants.9.stats.totalMinionsKilled','participants.9.stats.champLevel','participants.9.timeline.lane','participants.9.timeline.role',
                ]
        csv_file.writerow(index)
        input_list = []
        gameDuration = gameContent["gameDuration"]
        gameId = gameContent["gameId"]
        input_list.append(gameDuration)
        input_list.append(gameId)
        participants = gameContent["participants"]
        for k in range(10):
            input_list.append(participants[k]["stats"]["kills"])
            input_list.append(participants[k]["stats"]["deaths"])
            input_list.append(participants[k]["stats"]["assists"])
            input_list.append(participants[k]["stats"]["totalDamageDealtToChampions"])
            input_list.append(participants[k]["stats"]["totalDamageTaken"])
            input_list.append(participants[k]["stats"]["totalHeal"])
            input_list.append(participants[k]["stats"]["visionScore"])
            input_list.append(participants[k]["stats"]["goldEarned"])
            input_list.append(participants[k]["stats"]["turretKills"])
            input_list.append(participants[k]["stats"]["totalMinionsKilled"])
            input_list.append(participants[k]["stats"]["champLevel"])
            input_list.append(participants[k]["timeline"]["lane"])
            input_list.append(participants[k]["timeline"]["role"])
            
            
        csv_file.writerow(input_list)
        time.sleep(1)
        count+=1
        f.close()
        


# participants.n.stats.kills
# participants.n.stats.deaths
# participants.n.stats.assists
# participants.n.stats.totalDamageDealtToChampions
# participants.n.stats.totalDamageTaken
# participants.n.stats.totalHeal
# participants.n.stats.visionScore
# participants.n.stats.goldEarned
# participants.n.stats.turretKills
# participants.n.stats.totalMinionsKilled
# participants.n.stats.champLevel
# participants.n.timeline.lane
# participants.n.timeline.role

# gameId
# gameDuration