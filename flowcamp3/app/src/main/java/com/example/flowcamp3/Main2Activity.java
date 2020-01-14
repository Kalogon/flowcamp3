package com.example.flowcamp3;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;

import java.util.concurrent.ExecutionException;

public class Main2Activity extends AppCompatActivity {
    double IRON = 10.0;
    double BRONZE = 20.0;
    double SILVER = 30.0;
    double GOLD = 40.0;
    double PLATINUM = 50.0;
    double DIA = 60.0;
    double MASTER = 70.0;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);
        String username = getIntent().getStringExtra("userid");
        Double db = 0.;
        String str;
        OpenRiotAPITask t = new OpenRiotAPITask();
        try {
            str = t.execute(username).get();
            Log.e("client", Double.toString(db));
        } catch (InterruptedException e) {
            e.printStackTrace();
        } catch (ExecutionException e) {
            e.printStackTrace();
        }

        if (db < IRON) {
            // IRON
        } else if (db < BRONZE) {
            // BRONZE
        } else if (db < SILVER) {
            // SILVER
        } else if (db < GOLD) {
            // GOLD
        } else if (db < PLATINUM) {
            // PLATINUM
        } else if (db < DIA) {
            // DIAMOND
        } else {
            // MASTER
        }
    }
}
