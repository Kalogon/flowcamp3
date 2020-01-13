package com.example.flowcamp3;

import android.os.AsyncTask;

public class OpenRiotAPITask extends AsyncTask<String, Void, String> {
    @Override
    public String doInBackground(String... params) {
        OpenRiotAPIClient client = new OpenRiotAPIClient();
        String summonerID = params[0];
        String accountId = client.getAccountId(summonerID);
        String matchId = client.getMostRecentMatchId(accountId);
        String champId = client.getMostRecentChampionId(accountId);
        String ret = accountId+" "+matchId+" "+champId
                +"\n" +"kill:"+ client.getKills(matchId, champId)
                +"\n" +"death:"+ client.getDeaths(matchId, champId)
                +"\n" +"assist:"+ client.getAssists(matchId, champId)
                +"\n" + "딜량:"+client.getTotalDealtDamage(matchId, champId)
                +"\n" +"피해량:"+ client.getTotalTakenDamage(matchId, champId)
                +"\n" +"힐량:"+ client.getTotalHeal(matchId, champId)
                +"\n" +"시야:"+ client.getVisionScore(matchId, champId)
                +"\n" +"골드:"+ client.getGold(matchId, champId)
                +"\n" +"포탑:"+ client.getTurrets(matchId, champId)
                +"\n" +"CS:"+ client.getMinions(matchId, champId)
                +"\n" +"레벨:"+ client.getChampLevel(matchId, champId)
                +"\n" +"라인:"+ client.getLane(matchId, champId)
                +"\n" +"포지션:"+client.getRole(matchId, champId)
                +"\n" +"How long:"+client.getGameDuration(matchId, champId);
        int kill = Integer.parseInt(client.getKills(matchId, champId));
        return ret;
    }
}