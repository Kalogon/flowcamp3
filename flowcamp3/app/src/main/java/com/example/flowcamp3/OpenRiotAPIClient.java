package com.example.flowcamp3;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

public class OpenRiotAPIClient {
    final static String openRiotURL = "https://kr.api.riotgames.com";
    final static String API_Key = "RGAPI-eaef0d4b-a43f-40c1-9aa7-0d988735d743";
    public String getAccountId(String summonerName) {
        String ret = "";
        String urlString = openRiotURL + "/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" + API_Key;
        try {
            URL url = new URL(urlString);
            HttpURLConnection urlConnection = (HttpURLConnection) url.openConnection();
            InputStream in = new BufferedInputStream(urlConnection.getInputStream());
            JSONObject json = new JSONObject(IStoStr(in));
            ret = json.getString("accountId");
        } catch(MalformedURLException e) {
            System.err.println("Malformed URL");
            e.printStackTrace();
            return null;
        } catch (JSONException e) {
            System.err.println("JSON parsing error");
            e.printStackTrace();
            return null;
        } catch (IOException e) {
            System.err.println("URL Connection failed");
            e.printStackTrace();
            return null;
        }
        return ret;
    }

    public String getMostRecentMatchId(String accountId) {
        String ret = "";
        String urlString = openRiotURL + "/lol/match/v4/matchlists/by-account/" + accountId + "?api_key=" + API_Key;
        try {
            URL url = new URL(urlString);
            HttpURLConnection urlConnection = (HttpURLConnection) url.openConnection();
            InputStream in = new BufferedInputStream(urlConnection.getInputStream());
            JSONObject json = new JSONObject(IStoStr(in));
            ret = json.getJSONArray("matches").getJSONObject(0).getString("gameId");
        } catch(MalformedURLException e) {
            System.err.println("Malformed URL");
            e.printStackTrace();
            return null;
        } catch (JSONException e) {
            System.err.println("JSON parsing error");
            e.printStackTrace();
            return null;
        } catch (IOException e) {
            System.err.println("URL Connection failed");
            e.printStackTrace();
            return null;
        }
        return ret;
    }

    public String getMostRecentChampionId(String accountId) {
        String ret = "";
        String urlString = openRiotURL + "/lol/match/v4/matchlists/by-account/" + accountId + "?api_key=" + API_Key;
        try {
            URL url = new URL(urlString);
            HttpURLConnection urlConnection = (HttpURLConnection) url.openConnection();
            InputStream in = new BufferedInputStream(urlConnection.getInputStream());
            JSONObject json = new JSONObject(IStoStr(in));
            ret = json.getJSONArray("matches").getJSONObject(0).getString("champion");
        } catch(MalformedURLException e) {
            System.err.println("Malformed URL");
            e.printStackTrace();
            return null;
        } catch (JSONException e) {
            System.err.println("JSON parsing error");
            e.printStackTrace();
            return null;
        } catch (IOException e) {
            System.err.println("URL Connection failed");
            e.printStackTrace();
            return null;
        }
        return ret;
    }

    public String getKills(String matchId, String championId) {
        String ret;
        String urlString = openRiotURL + "/lol/match/v4/matches/" + matchId + "?api_key=" + API_Key;
        try {
            URL url = new URL(urlString);
            HttpURLConnection urlConnection = (HttpURLConnection) url.openConnection();
            InputStream in = new BufferedInputStream(urlConnection.getInputStream());
            JSONObject json = new JSONObject(IStoStr(in));
            JSONArray tmp = json.getJSONArray("participants");
            int idx = whereAmI(tmp, championId);
            JSONObject target = tmp.getJSONObject(idx).getJSONObject("stats");
            ret = target.getString("kills");
        } catch(MalformedURLException e) {
            System.err.println("Malformed URL");
            e.printStackTrace();
            return null;
        } catch (JSONException e) {
            System.err.println("JSON parsing error");
            e.printStackTrace();
            return null;
        } catch (IOException e) {
            System.err.println("URL Connection failed");
            e.printStackTrace();
            return null;
        }
        return ret;
    }

    public String getDeaths(String matchId, String championId) {
        String ret;
        String urlString = openRiotURL + "/lol/match/v4/matches/" + matchId + "?api_key=" + API_Key;
        try {
            URL url = new URL(urlString);
            HttpURLConnection urlConnection = (HttpURLConnection) url.openConnection();
            InputStream in = new BufferedInputStream(urlConnection.getInputStream());
            JSONObject json = new JSONObject(IStoStr(in));
            JSONArray tmp = json.getJSONArray("participants");
            int idx = whereAmI(tmp, championId);
            JSONObject target = tmp.getJSONObject(idx).getJSONObject("stats");
            ret = target.getString("deaths");
        } catch(MalformedURLException e) {
            System.err.println("Malformed URL");
            e.printStackTrace();
            return null;
        } catch (JSONException e) {
            System.err.println("JSON parsing error");
            e.printStackTrace();
            return null;
        } catch (IOException e) {
            System.err.println("URL Connection failed");
            e.printStackTrace();
            return null;
        }
        return ret;
    }

    public String getAssists(String matchId, String championId) {
        String ret;
        String urlString = openRiotURL + "/lol/match/v4/matches/" + matchId + "?api_key=" + API_Key;
        try {
            URL url = new URL(urlString);
            HttpURLConnection urlConnection = (HttpURLConnection) url.openConnection();
            InputStream in = new BufferedInputStream(urlConnection.getInputStream());
            JSONObject json = new JSONObject(IStoStr(in));
            JSONArray tmp = json.getJSONArray("participants");
            int idx = whereAmI(tmp, championId);
            JSONObject target = tmp.getJSONObject(idx).getJSONObject("stats");
            ret = target.getString("assists");
        } catch(MalformedURLException e) {
            System.err.println("Malformed URL");
            e.printStackTrace();
            return null;
        } catch (JSONException e) {
            System.err.println("JSON parsing error");
            e.printStackTrace();
            return null;
        } catch (IOException e) {
            System.err.println("URL Connection failed");
            e.printStackTrace();
            return null;
        }
        return ret;
    }

    public String getTotalDealtDamage(String matchId, String championId) {
        String ret;
        String urlString = openRiotURL + "/lol/match/v4/matches/" + matchId + "?api_key=" + API_Key;
        try {
            URL url = new URL(urlString);
            HttpURLConnection urlConnection = (HttpURLConnection) url.openConnection();
            InputStream in = new BufferedInputStream(urlConnection.getInputStream());
            JSONObject json = new JSONObject(IStoStr(in));
            JSONArray tmp = json.getJSONArray("participants");
            int idx = whereAmI(tmp, championId);
            JSONObject target = tmp.getJSONObject(idx).getJSONObject("stats");
            ret = target.getString("totalDamageDealtToChampions");
        } catch(MalformedURLException e) {
            System.err.println("Malformed URL");
            e.printStackTrace();
            return null;
        } catch (JSONException e) {
            System.err.println("JSON parsing error");
            e.printStackTrace();
            return null;
        } catch (IOException e) {
            System.err.println("URL Connection failed");
            e.printStackTrace();
            return null;
        }
        return ret;
    }

    public String getTotalTakenDamage(String matchId, String championId) {
        String ret;
        String urlString = openRiotURL + "/lol/match/v4/matches/" + matchId + "?api_key=" + API_Key;
        try {
            URL url = new URL(urlString);
            HttpURLConnection urlConnection = (HttpURLConnection) url.openConnection();
            InputStream in = new BufferedInputStream(urlConnection.getInputStream());
            JSONObject json = new JSONObject(IStoStr(in));
            JSONArray tmp = json.getJSONArray("participants");
            int idx = whereAmI(tmp, championId);
            JSONObject target = tmp.getJSONObject(idx).getJSONObject("stats");
            ret = target.getString("totalDamageTaken");
        } catch(MalformedURLException e) {
            System.err.println("Malformed URL");
            e.printStackTrace();
            return null;
        } catch (JSONException e) {
            System.err.println("JSON parsing error");
            e.printStackTrace();
            return null;
        } catch (IOException e) {
            System.err.println("URL Connection failed");
            e.printStackTrace();
            return null;
        }
        return ret;
    }

    public String getTotalHeal(String matchId, String championId) {
        String ret;
        String urlString = openRiotURL + "/lol/match/v4/matches/" + matchId + "?api_key=" + API_Key;
        try {
            URL url = new URL(urlString);
            HttpURLConnection urlConnection = (HttpURLConnection) url.openConnection();
            InputStream in = new BufferedInputStream(urlConnection.getInputStream());
            JSONObject json = new JSONObject(IStoStr(in));
            JSONArray tmp = json.getJSONArray("participants");
            int idx = whereAmI(tmp, championId);
            JSONObject target = tmp.getJSONObject(idx).getJSONObject("stats");
            ret = target.getString("totalHeal");
        } catch(MalformedURLException e) {
            System.err.println("Malformed URL");
            e.printStackTrace();
            return null;
        } catch (JSONException e) {
            System.err.println("JSON parsing error");
            e.printStackTrace();
            return null;
        } catch (IOException e) {
            System.err.println("URL Connection failed");
            e.printStackTrace();
            return null;
        }
        return ret;
    }

    public String getVisionScore(String matchId, String championId) {
        String ret;
        String urlString = openRiotURL + "/lol/match/v4/matches/" + matchId + "?api_key=" + API_Key;
        try {
            URL url = new URL(urlString);
            HttpURLConnection urlConnection = (HttpURLConnection) url.openConnection();
            InputStream in = new BufferedInputStream(urlConnection.getInputStream());
            JSONObject json = new JSONObject(IStoStr(in));
            JSONArray tmp = json.getJSONArray("participants");
            int idx = whereAmI(tmp, championId);
            JSONObject target = tmp.getJSONObject(idx).getJSONObject("stats");
            ret = target.getString("visionScore");
        } catch(MalformedURLException e) {
            System.err.println("Malformed URL");
            e.printStackTrace();
            return null;
        } catch (JSONException e) {
            System.err.println("JSON parsing error");
            e.printStackTrace();
            return null;
        } catch (IOException e) {
            System.err.println("URL Connection failed");
            e.printStackTrace();
            return null;
        }
        return ret;
    }

    public String getGold(String matchId, String championId) {
        String ret;
        String urlString = openRiotURL + "/lol/match/v4/matches/" + matchId + "?api_key=" + API_Key;
        try {
            URL url = new URL(urlString);
            HttpURLConnection urlConnection = (HttpURLConnection) url.openConnection();
            InputStream in = new BufferedInputStream(urlConnection.getInputStream());
            JSONObject json = new JSONObject(IStoStr(in));
            JSONArray tmp = json.getJSONArray("participants");
            int idx = whereAmI(tmp, championId);
            JSONObject target = tmp.getJSONObject(idx).getJSONObject("stats");
            ret = target.getString("goldEarned");
        } catch(MalformedURLException e) {
            System.err.println("Malformed URL");
            e.printStackTrace();
            return null;
        } catch (JSONException e) {
            System.err.println("JSON parsing error");
            e.printStackTrace();
            return null;
        } catch (IOException e) {
            System.err.println("URL Connection failed");
            e.printStackTrace();
            return null;
        }
        return ret;
    }

    public String getTurrets(String matchId, String championId) {
        String ret;
        String urlString = openRiotURL + "/lol/match/v4/matches/" + matchId + "?api_key=" + API_Key;
        try {
            URL url = new URL(urlString);
            HttpURLConnection urlConnection = (HttpURLConnection) url.openConnection();
            InputStream in = new BufferedInputStream(urlConnection.getInputStream());
            JSONObject json = new JSONObject(IStoStr(in));
            JSONArray tmp = json.getJSONArray("participants");
            int idx = whereAmI(tmp, championId);
            JSONObject target = tmp.getJSONObject(idx).getJSONObject("stats");
            ret = target.getString("turretKills");
        } catch(MalformedURLException e) {
            System.err.println("Malformed URL");
            e.printStackTrace();
            return null;
        } catch (JSONException e) {
            System.err.println("JSON parsing error");
            e.printStackTrace();
            return null;
        } catch (IOException e) {
            System.err.println("URL Connection failed");
            e.printStackTrace();
            return null;
        }
        return ret;
    }

    public String getMinions(String matchId, String championId) {
        String ret;
        String urlString = openRiotURL + "/lol/match/v4/matches/" + matchId + "?api_key=" + API_Key;
        try {
            URL url = new URL(urlString);
            HttpURLConnection urlConnection = (HttpURLConnection) url.openConnection();
            InputStream in = new BufferedInputStream(urlConnection.getInputStream());
            JSONObject json = new JSONObject(IStoStr(in));
            JSONArray tmp = json.getJSONArray("participants");
            int idx = whereAmI(tmp, championId);
            JSONObject target = tmp.getJSONObject(idx).getJSONObject("stats");
            ret = target.getString("totalMinionsKilled");
        } catch(MalformedURLException e) {
            System.err.println("Malformed URL");
            e.printStackTrace();
            return null;
        } catch (JSONException e) {
            System.err.println("JSON parsing error");
            e.printStackTrace();
            return null;
        } catch (IOException e) {
            System.err.println("URL Connection failed");
            e.printStackTrace();
            return null;
        }
        return ret;
    }

    public String getChampLevel(String matchId, String championId) {
        String ret;
        String urlString = openRiotURL + "/lol/match/v4/matches/" + matchId + "?api_key=" + API_Key;
        try {
            URL url = new URL(urlString);
            HttpURLConnection urlConnection = (HttpURLConnection) url.openConnection();
            InputStream in = new BufferedInputStream(urlConnection.getInputStream());
            JSONObject json = new JSONObject(IStoStr(in));
            JSONArray tmp = json.getJSONArray("participants");
            int idx = whereAmI(tmp, championId);
            JSONObject target = tmp.getJSONObject(idx).getJSONObject("stats");
            ret = target.getString("champLevel");
        } catch(MalformedURLException e) {
            System.err.println("Malformed URL");
            e.printStackTrace();
            return null;
        } catch (JSONException e) {
            System.err.println("JSON parsing error");
            e.printStackTrace();
            return null;
        } catch (IOException e) {
            System.err.println("URL Connection failed");
            e.printStackTrace();
            return null;
        }
        return ret;
    }

    public String getLane(String matchId, String championId) {
        String ret;
        String urlString = openRiotURL + "/lol/match/v4/matches/" + matchId + "?api_key=" + API_Key;
        try {
            URL url = new URL(urlString);
            HttpURLConnection urlConnection = (HttpURLConnection) url.openConnection();
            InputStream in = new BufferedInputStream(urlConnection.getInputStream());
            JSONObject json = new JSONObject(IStoStr(in));
            JSONArray tmp = json.getJSONArray("participants");
            int idx = whereAmI(tmp, championId);
            JSONObject target = tmp.getJSONObject(idx).getJSONObject("timeline");
            ret = target.getString("lane");
        } catch(MalformedURLException e) {
            System.err.println("Malformed URL");
            e.printStackTrace();
            return null;
        } catch (JSONException e) {
            System.err.println("JSON parsing error");
            e.printStackTrace();
            return null;
        } catch (IOException e) {
            System.err.println("URL Connection failed");
            e.printStackTrace();
            return null;
        }
        return ret;
    }

    public String getRole(String matchId, String championId) {
        String ret = "";
        String urlString = openRiotURL + "/lol/match/v4/matches/" + matchId + "?api_key=" + API_Key;
        try {
            URL url = new URL(urlString);
            HttpURLConnection urlConnection = (HttpURLConnection) url.openConnection();
            InputStream in = new BufferedInputStream(urlConnection.getInputStream());
            JSONObject json = new JSONObject(IStoStr(in));
            JSONArray tmp = json.getJSONArray("participants");
            int idx = whereAmI(tmp, championId);
            JSONObject target = tmp.getJSONObject(idx).getJSONObject("timeline");
            if (target.getString("lane").equals("BOTTOM"))
                ret = target.getString("role");
        } catch(MalformedURLException e) {
            System.err.println("Malformed URL");
            e.printStackTrace();
            return null;
        } catch (JSONException e) {
            System.err.println("JSON parsing error");
            e.printStackTrace();
            return null;
        } catch (IOException e) {
            System.err.println("URL Connection failed");
            e.printStackTrace();
            return null;
        }
        return ret;
    }

    public String getGameDuration(String matchId, String championId) {
        String ret;
        String urlString = openRiotURL + "/lol/match/v4/matches/" + matchId + "?api_key=" + API_Key;
        try {
            URL url = new URL(urlString);
            HttpURLConnection urlConnection = (HttpURLConnection) url.openConnection();
            InputStream in = new BufferedInputStream(urlConnection.getInputStream());
            JSONObject json = new JSONObject(IStoStr(in));
            ret = json.getString("gameDuration");
        } catch(MalformedURLException e) {
            System.err.println("Malformed URL");
            e.printStackTrace();
            return null;
        } catch (JSONException e) {
            System.err.println("JSON parsing error");
            e.printStackTrace();
            return null;
        } catch (IOException e) {
            System.err.println("URL Connection failed");
            e.printStackTrace();
            return null;
        }
        return ret;
    }

    public String IStoStr(InputStream is) {
        ByteArrayOutputStream buffer = new ByteArrayOutputStream();
        int nRead;
        byte[] data = new byte[16384];
        try {
            while ((nRead = is.read(data)) != -1) {
                buffer.write(data, 0, nRead);
            }
            buffer.flush();
        } catch (IOException e) {
            System.err.println("IOException errer");
            e.printStackTrace();
            return null;
        }

        String str = new String(buffer.toByteArray());
        return str;
    }

    private int whereAmI(JSONArray array, String championID) {
        for (int i=0; i<10; i++) {
            try {
                String thischamp = array.getJSONObject(i).getString("championId");
                if (championID.equals(thischamp))
                    return i;
            } catch (JSONException e) {
                e.printStackTrace();
            }
        }
        return -1;
    }
}