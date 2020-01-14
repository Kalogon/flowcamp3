package com.example.flowcamp3;

import android.os.AsyncTask;
import android.util.Log;

public class OpenRiotAPITask extends AsyncTask<String, Void, String> {
    double top_kda = -0.0078;
    double top_deal = -0.0245;
    double top_dealtaken = 0.0099;
    double top_heal = 0.0049;
    double top_vision = 0.0039;
    double top_gold = 0.1096;
    double top_turret = -0.0093;
    double top_cs = 0.0115;
    double top_level = -0.0047;

    double mid_kda = -0.0032;
    double mid_deal = -0.0213;
    double mid_dealtaken = 0.0107;
    double mid_heal = 0.0034;
    double mid_vision = 0.0045;
    double mid_gold = 0.1066;
    double mid_turret = 0.0043;
    double mid_cs = -0.0033;
    double mid_level = -0.0084;

    double jungle_kda = -0.0037;
    double jungle_deal = -0.0044;
    double jungle_dealtaken = 0.0061;
    double jungle_heal = 0.0032;
    double jungle_vision = 0.0052;
    double jungle_gold = 0.0866;
    double jungle_turret = -0.0087;
    double jungle_cs = 0.0064;
    double jungle_level = 0.0051;

    double sup_kda = 0.0299;
    double sup_deal = -0.0473;
    double sup_dealtaken = 0.0164;
    double sup_heal = -0.0009;
    double sup_vision = 0.1618;
    double sup_gold = 0.1553;
    double sup_turret = 0.0089;
    double sup_cs = 0.0211;
    double sup_level = 0.0155;

    double bot_kda = -0.1151;
    double bot_deal = -0.0256;
    double bot_dealtaken = -0.0027;
    double bot_heal = 0.0250;
    double bot_vision = 0.0433;
    double bot_gold = 0.1271;
    double bot_turret = 0.0056;
    double bot_cs = 0.1954;
    double bot_level = 0.0072;

    @Override
    public String doInBackground(String... params) {
        OpenRiotAPIClient client = new OpenRiotAPIClient();
        String summonerID = params[0];
        String accountId = client.getAccountId(summonerID);
        String matchId = client.getMostRecentMatchId(accountId);
        String champId = client.getMostRecentChampionId(accountId);

        int kill = Integer.parseInt(client.getKills(matchId, champId));
        int death = Integer.parseInt(client.getDeaths(matchId, champId));
        int assists = Integer.parseInt(client.getAssists(matchId, champId));

        double kda;
        if (death != 0) kda = ((double)kill + (double)assists) / (double)death;
        else kda = ((double)kill + (double)assists) * (double)3.0;

        double gameDuration = Double.parseDouble(client.getGameDuration(matchId, champId));

        double Deal = Double.parseDouble(client.getTotalDealtDamage(matchId, champId))/gameDuration*60;
        double DealTaken = Double.parseDouble(client.getTotalTakenDamage(matchId, champId))/gameDuration*60;
        double Heal = Double.parseDouble(client.getTotalHeal(matchId, champId))/gameDuration*60;
        double visionScore = Double.parseDouble(client.getVisionScore(matchId, champId))/gameDuration*60;
        double gold = Double.parseDouble(client.getGold(matchId, champId))/gameDuration*60;
        double turret = Double.parseDouble(client.getTurrets(matchId, champId))/gameDuration*60;
        double cs = Double.parseDouble(client.getMinions(matchId, champId))/gameDuration*60;
        double championLevel = Double.parseDouble(client.getChampLevel(matchId, champId))/gameDuration*60;
        String lane = client.getLane(matchId, champId);
        String role = client.getRole(matchId, champId);

        String ret = Double.toString(kda)
                +" " + Double.toString(Deal)
                +" " + Double.toString(DealTaken)
                +" " + Double.toString(Heal)
                +" " + Double.toString(visionScore)
                +" " + Double.toString(gold)
                +" " + Double.toString(turret)
                +" " + Double.toString(cs)
                +" " + Double.toString(championLevel)
                +" " + lane
                +" " + role
                +" " + Double.toString(gameDuration / 60);
        Log.e("Str", ret);
        double result = 0.;

        if (lane.equals("TOP")) {
            result += kda*top_kda;
            result += Deal*top_deal;
            result += DealTaken*top_dealtaken;
            result += Heal*top_heal;
            result += visionScore*top_vision;
            result += gold*top_gold;
            result += turret*top_turret;
            result += cs*top_cs;
            result += championLevel*top_level;
        }
        else if (lane.equals("MIDDLE")) {
            result += kda*mid_kda;
            result += Deal*mid_deal;
            result += DealTaken*mid_dealtaken;
            result += Heal*mid_heal;
            result += visionScore*mid_vision;
            result += gold*mid_gold;
            result += turret*mid_turret;
            result += cs*mid_cs;
            result += championLevel*mid_level;
        }
        else if (lane.equals("JUNGLE")) {
            result += kda*jungle_kda;
            result += Deal*jungle_deal;
            result += DealTaken*jungle_dealtaken;
            result += Heal*jungle_heal;
            result += visionScore*jungle_vision;
            result += gold*jungle_gold;
            result += turret*jungle_turret;
            result += cs*jungle_cs;
            result += championLevel*jungle_level;
        }
        else if (lane.equals("BOTTOM")) {
            if (role.equals("DUO_CARRY")) {
                result += kda * bot_kda;
                result += Deal * bot_deal;
                result += DealTaken * bot_dealtaken;
                result += Heal * bot_heal;
                result += visionScore * bot_vision;
                result += gold * bot_gold;
                result += turret * bot_turret;
                result += cs * bot_cs;
                result += championLevel * bot_level;
            } else if (role.equals("DUO_SUPPORT")) {
                result += kda * sup_kda;
                result += Deal * sup_deal;
                result += DealTaken * sup_dealtaken;
                result += Heal * sup_heal;
                result += visionScore * sup_vision;
                result += gold * sup_gold;
                result += turret * sup_turret;
                result += cs * sup_cs;
                result += championLevel * sup_level;
            }
        }

        ret = Double.toString(result) + " " + ret;

        return ret;
    }
}