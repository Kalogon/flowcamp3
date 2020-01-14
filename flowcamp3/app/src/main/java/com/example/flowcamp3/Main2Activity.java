package com.example.flowcamp3;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.RelativeLayout;
import android.widget.TextView;

import org.w3c.dom.Text;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;
import java.util.concurrent.ExecutionException;

public class Main2Activity extends AppCompatActivity {
    double IRON = 10.0;
    double BRONZE = 20.0;
    double SILVER = 30.0;
    double GOLD = 40.0;
    double PLATINUM = 50.0;
    double DIA = 60.0;
    double MASTER = 70.0;

    // Iron
    double iron_mid_avg_kda = 3.8;
    double iron_mid_avg_deal = 645.0;
    double iron_mid_avg_dealtaken = 703.0;
    double iron_mid_avg_heal = 140.3;
    double iron_mid_avg_vision = 0.59;
    double iron_mid_avg_gold = 378.1;
    double iron_mid_avg_turret = 0.03;
    double iron_mid_avg_cs = 4.7;
    double iron_mid_avg_level = 0.50;

    double iron_top_avg_kda = 3.2;
    double iron_top_avg_deal = 619.6;
    double iron_top_avg_dealtaken = 838.5;
    double iron_top_avg_heal = 182.3;
    double iron_top_avg_vision = 0.50;
    double iron_top_avg_gold = 369.3;
    double iron_top_avg_turret = 0.04;
    double iron_top_avg_cs = 5.0;
    double iron_top_avg_level = 0.50;

    double iron_jungle_avg_kda = 3.4;
    double iron_jungle_avg_deal = 468.9;
    double iron_jungle_avg_dealtaken = 922.3;
    double iron_jungle_avg_heal = 340.6;
    double iron_jungle_avg_vision = 0.68;
    double iron_jungle_avg_gold = 359.6;
    double iron_jungle_avg_turret = 0.02;
    double iron_jungle_avg_cs = 1.5;
    double iron_jungle_avg_level = 0.47;

    double iron_bot_avg_kda = 3.6;
    double iron_bot_avg_deal = 619.6;
    double iron_bot_avg_dealtaken = 579.9;
    double iron_bot_avg_heal = 101.0;
    double iron_bot_avg_vision = 0.54;
    double iron_bot_avg_gold = 387.5;
    double iron_bot_avg_turret = 0.04;
    double iron_bot_avg_cs = 5.3;
    double iron_bot_avg_level = 0.46;

    double iron_sup_avg_kda = 3.7;
    double iron_sup_avg_deal = 373.3;
    double iron_sup_avg_dealtaken = 557.5;
    double iron_sup_avg_heal = 121.1;
    double iron_sup_avg_vision = 1.29;
    double iron_sup_avg_gold = 281.2;
    double iron_sup_avg_turret = 0.01;
    double iron_sup_avg_cs = 1.1;
    double iron_sup_avg_level = 0.43;


    // Bronze
    double bronze_mid_avg_kda = 3.6;
    double bronze_mid_avg_deal = 682.0;
    double bronze_mid_avg_dealtaken = 739.5;
    double bronze_mid_avg_heal = 157.4;
    double bronze_mid_avg_vision = 0.64;
    double bronze_mid_avg_gold = 392.8;
    double bronze_mid_avg_turret = 0.02;
    double bronze_mid_avg_cs = 5.0;
    double bronze_mid_avg_level = 0.51;

    double bronze_top_avg_kda = 3.1;
    double bronze_top_avg_deal = 624.8;
    double bronze_top_avg_dealtaken = 859.3;
    double bronze_top_avg_heal = 198.3;
    double bronze_top_avg_vision = 0.58;
    double bronze_top_avg_gold = 380.7;
    double bronze_top_avg_turret = 0.04;
    double bronze_top_avg_cs = 5.2;
    double bronze_top_avg_level = 0.52;

    double bronze_jungle_avg_kda = 3.6;
    double bronze_jungle_avg_deal = 481.9;
    double bronze_jungle_avg_dealtaken = 937.9;
    double bronze_jungle_avg_heal = 367.8;
    double bronze_jungle_avg_vision = 0.77;
    double bronze_jungle_avg_gold = 365.9;
    double bronze_jungle_avg_turret = 0.02;
    double bronze_jungle_avg_cs = 1.5;
    double bronze_jungle_avg_level = 0.47;

    double bronze_bot_avg_kda = 3.7;
    double bronze_bot_avg_deal = 657.3;
    double bronze_bot_avg_dealtaken = 593.4;
    double bronze_bot_avg_heal = 105.9;
    double bronze_bot_avg_vision = 0.61;
    double bronze_bot_avg_gold = 402.8;
    double bronze_bot_avg_turret = 0.04;
    double bronze_bot_avg_cs = 5.8;
    double bronze_bot_avg_level = 0.47;

    double bronze_sup_avg_kda = 3.9;
    double bronze_sup_avg_deal = 365.7;
    double bronze_sup_avg_dealtaken = 564.5;
    double bronze_sup_avg_heal = 130.9;
    double bronze_sup_avg_vision = 1.49;
    double bronze_sup_avg_gold = 281.4;
    double bronze_sup_avg_turret = 0.01;
    double bronze_sup_avg_cs = 1.1;
    double bronze_sup_avg_level = 0.43;

    // Silver
    double silver_mid_avg_kda = 3.4;
    double silver_mid_avg_deal = 690.9;
    double silver_mid_avg_dealtaken = 760.9;
    double silver_mid_avg_heal = 177.3;
    double silver_mid_avg_vision = 0.68;
    double silver_mid_avg_gold = 406.6;
    double silver_mid_avg_turret = 0.02;
    double silver_mid_avg_cs = 5.2;
    double silver_mid_avg_level = 0.52;

    double silver_top_avg_kda = 3.0;
    double silver_top_avg_deal = 685.5;
    double silver_top_avg_dealtaken = 908.3;
    double silver_top_avg_heal = 215.0;
    double silver_top_avg_vision = 0.58;
    double silver_top_avg_gold = 402.6;
    double silver_top_avg_turret = 0.04;
    double silver_top_avg_cs = 5.5;
    double silver_top_avg_level = 0.53;

    double silver_jungle_avg_kda = 3.7;
    double silver_jungle_avg_deal = 492.6;
    double silver_jungle_avg_dealtaken = 935.7;
    double silver_jungle_avg_heal = 365.9;
    double silver_jungle_avg_vision = 0.86;
    double silver_jungle_avg_gold = 374.7;
    double silver_jungle_avg_turret = 0.02;
    double silver_jungle_avg_cs = 1.5;
    double silver_jungle_avg_level = 0.48;

    double silver_bot_avg_kda = 3.9;
    double silver_bot_avg_deal = 668.6;
    double silver_bot_avg_dealtaken = 595.1;
    double silver_bot_avg_heal = 103.6;
    double silver_bot_avg_vision = 0.67;
    double silver_bot_avg_gold = 415.3;
    double silver_bot_avg_turret = 0.04;
    double silver_bot_avg_cs = 6.1;
    double silver_bot_avg_level = 0.48;

    double silver_sup_avg_kda = 3.6;
    double silver_sup_avg_deal = 321.0;
    double silver_sup_avg_dealtaken = 523.3;
    double silver_sup_avg_heal = 133.0;
    double silver_sup_avg_vision = 1.59;
    double silver_sup_avg_gold = 263.9;
    double silver_sup_avg_turret = 0.01;
    double silver_sup_avg_cs = 1.0;
    double silver_sup_avg_level = 0.41;

    // Gold
    double gold_mid_avg_kda = 3.9;
    double gold_mid_avg_deal = 642.8;
    double gold_mid_avg_dealtaken = 718.3;
    double gold_mid_avg_heal = 138.1;
    double gold_mid_avg_vision = 0.76;
    double gold_mid_avg_gold = 252.3;
    double gold_mid_avg_turret = 0.02;
    double gold_mid_avg_cs = 5.5;
    double gold_mid_avg_level = 0.51;

    double gold_top_avg_kda = 3.8;
    double gold_top_avg_deal = 563.3;
    double gold_top_avg_dealtaken = 810.0;
    double gold_top_avg_heal = 159.0;
    double gold_top_avg_vision = 0.69;
    double gold_top_avg_gold = 390.7;
    double gold_top_avg_turret = 0.03;
    double gold_top_avg_cs = 6.4;
    double gold_top_avg_level = 0.51;

    double gold_jungle_avg_kda = 4.5;
    double gold_jungle_avg_deal = 497.4;
    double gold_jungle_avg_dealtaken = 847.6;
    double gold_jungle_avg_heal = 323.5;
    double gold_jungle_avg_vision = 0.99;
    double gold_jungle_avg_gold = 238.7;
    double gold_jungle_avg_turret = 0.02;
    double gold_jungle_avg_cs = 1.8;
    double gold_jungle_avg_level = 0.49;

    double gold_bot_avg_kda = 4.3;
    double gold_bot_avg_deal = 696.1;
    double gold_bot_avg_dealtaken = 612.5;
    double gold_bot_avg_heal = 114.3;
    double gold_bot_avg_vision = 0.65;
    double gold_bot_avg_gold = 275.9;
    double gold_bot_avg_turret = 0.04;
    double gold_bot_avg_cs = 6.3;
    double gold_bot_avg_level = 0.48;

    double gold_sup_avg_kda = 3.4;
    double gold_sup_avg_deal = 291.8;
    double gold_sup_avg_dealtaken = 581.8;
    double gold_sup_avg_heal = 168.0;
    double gold_sup_avg_vision = 1.87;
    double gold_sup_avg_gold = 275.9;
    double gold_sup_avg_turret = 0.002;
    double gold_sup_avg_cs = 1.0;
    double gold_sup_avg_level = 0.43;

    // Platinum
    double platinum_mid_avg_kda = 3.9;
    double platinum_mid_avg_deal = 677.2;
    double platinum_mid_avg_dealtaken = 742.2;
    double platinum_mid_avg_heal = 179.3;
    double platinum_mid_avg_vision = 0.78;
    double platinum_mid_avg_gold = 410.0;
    double platinum_mid_avg_turret = 0.02;
    double platinum_mid_avg_cs = 5.6;
    double platinum_mid_avg_level = 0.54;

    double platinum_top_avg_kda = 3.2;
    double platinum_top_avg_deal = 659.0;
    double platinum_top_avg_dealtaken = 892.3;
    double platinum_top_avg_heal = 55638;
    double platinum_top_avg_vision = 0.64;
    double platinum_top_avg_gold = 414.1;
    double platinum_top_avg_turret = 0.03;
    double platinum_top_avg_cs = 5.8;
    double platinum_top_avg_level = 0.55;

    double platinum_jungle_avg_kda = 4.0;
    double platinum_jungle_avg_deal = 488.0;
    double platinum_jungle_avg_dealtaken = 914.7;
    double platinum_jungle_avg_heal = 374.1;
    double platinum_jungle_avg_vision = 0.98;
    double platinum_jungle_avg_gold = 380.4;
    double platinum_jungle_avg_turret = 0.02;
    double platinum_jungle_avg_cs = 1.4;
    double platinum_jungle_avg_level = 0.49;

    double platinum_bot_avg_kda = 4.4;
    double platinum_bot_avg_deal = 644.7;
    double platinum_bot_avg_dealtaken = 551.0;
    double platinum_bot_avg_heal = 96.5;
    double platinum_bot_avg_vision = 0.77;
    double platinum_bot_avg_gold = 421.0;
    double platinum_bot_avg_turret = 0.04;
    double platinum_bot_avg_cs = 6.7;
    double platinum_bot_avg_level = 0.49;

    double platinum_sup_avg_kda = 4.0;
    double platinum_sup_avg_deal = 300.0;
    double platinum_sup_avg_dealtaken = 520.9;
    double platinum_sup_avg_heal = 133.2;
    double platinum_sup_avg_vision = 1.93;
    double platinum_sup_avg_gold = 271.7;
    double platinum_sup_avg_turret = 0.01;
    double platinum_sup_avg_cs = 1.0;
    double platinum_sup_avg_level = 0.43;

    // Diamond
    double dia_mid_avg_kda = 4.0;
    double dia_mid_avg_deal = 609.4;
    double dia_mid_avg_dealtaken = 695.1;
    double dia_mid_avg_heal = 164.4;
    double dia_mid_avg_vision = 0.90;
    double dia_mid_avg_gold = 399.9;
    double dia_mid_avg_turret = 0.02;
    double dia_mid_avg_cs = 6.0;
    double dia_mid_avg_level = 0.53;

    double dia_top_avg_kda = 3.3;
    double dia_top_avg_deal = 581.2;
    double dia_top_avg_dealtaken = 823.9;
    double dia_top_avg_heal = 213.1;
    double dia_top_avg_vision = 0.76;
    double dia_top_avg_gold = 395.8;
    double dia_top_avg_turret = 0.03;
    double dia_top_avg_cs = 6.2;
    double dia_top_avg_level = 0.54;

    double dia_jungle_avg_kda = 4.4;
    double dia_jungle_avg_deal = 512.1;
    double dia_jungle_avg_dealtaken = 884.4;
    double dia_jungle_avg_heal = 360.9;
    double dia_jungle_avg_vision = 1.17;
    double dia_jungle_avg_gold = 391.2;
    double dia_jungle_avg_turret = 0.03;
    double dia_jungle_avg_cs = 1.4;
    double dia_jungle_avg_level = 0.50;

    double dia_bot_avg_kda = 4.2;
    double dia_bot_avg_deal = 630.7;
    double dia_bot_avg_dealtaken = 550.4;
    double dia_bot_avg_heal = 107.3;
    double dia_bot_avg_vision = 0.83;
    double dia_bot_avg_gold = 428.2;
    double dia_bot_avg_turret = 0.04;
    double dia_bot_avg_cs = 6.9;
    double dia_bot_avg_level = 0.50;

    double dia_sup_avg_kda = 3.9;
    double dia_sup_avg_deal = 269.7;
    double dia_sup_avg_dealtaken = 524.6;
    double dia_sup_avg_heal = 122.5;
    double dia_sup_avg_vision = 2.14;
    double dia_sup_avg_gold = 275.2;
    double dia_sup_avg_turret = 0.01;
    double dia_sup_avg_cs = 1.1;
    double dia_sup_avg_level = 0.44;

    // Master
    double master_mid_avg_kda = 4.1;
    double master_mid_avg_deal = 604.5;
    double master_mid_avg_dealtaken = 695.7;
    double master_mid_avg_heal = 173.4;
    double master_mid_avg_vision = 0.97;
    double master_mid_avg_gold = 400.0;
    double master_mid_avg_turret = 0.03;
    double master_mid_avg_cs = 6.2;
    double master_mid_avg_level = 0.52;

    double master_top_avg_kda = 3.5;
    double master_top_avg_deal = 593.1;
    double master_top_avg_dealtaken = 813.3;
    double master_top_avg_heal = 222.4;
    double master_top_avg_vision = 0.76;
    double master_top_avg_gold = 398.4;
    double master_top_avg_turret = 0.03;
    double master_top_avg_cs = 6.6;
    double master_top_avg_level = 0.53;

    double master_jungle_avg_kda = 4.1;
    double master_jungle_avg_deal = 517.4;
    double master_jungle_avg_dealtaken = 897.1;
    double master_jungle_avg_heal = 375.9;
    double master_jungle_avg_vision = 1.21;
    double master_jungle_avg_gold = 390.0;
    double master_jungle_avg_turret = 0.03;
    double master_jungle_avg_cs = 1.5;
    double master_jungle_avg_level = 0.49;

    double master_bot_avg_kda = 4.6;
    double master_bot_avg_deal = 631.7;
    double master_bot_avg_dealtaken = 547.3;
    double master_bot_avg_heal = 127.9;
    double master_bot_avg_vision = 0.84;
    double master_bot_avg_gold = 425.6;
    double master_bot_avg_turret = 0.04;
    double master_bot_avg_cs = 7.0;
    double master_bot_avg_level = 0.50;

    double master_sup_avg_kda = 4.2;
    double master_sup_avg_deal = 267.5;
    double master_sup_avg_dealtaken = 543.8;
    double master_sup_avg_heal = 118.9;
    double master_sup_avg_vision = 2.21;
    double master_sup_avg_gold = 273.3;
    double master_sup_avg_turret = 0.01;
    double master_sup_avg_cs = 1.2;
    double master_sup_avg_level = 0.43;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);
        String username = getIntent().getStringExtra("userid");
        Double db = 0.;
        String str;
        final List<String> result = new ArrayList<String>();
        OpenRiotAPITask t = new OpenRiotAPITask();
        try {
            str = t.execute(username).get();
            StringTokenizer st = new StringTokenizer(str, " ");
            while (st.hasMoreTokens()) {
                result.add(st.nextToken());
            }
            db = Double.parseDouble(result.get(0));
            Log.e("client", Double.toString(db));
        } catch (InterruptedException e) {
            e.printStackTrace();
        } catch (ExecutionException e) {
            e.printStackTrace();
        }
        TextView top = findViewById(R.id.top);
        top.setText(username + "님은 최근 경기에서");
        ImageView tier_image = findViewById(R.id.tier);
        RelativeLayout relativeLayout = findViewById(R.id.belowwrap);
        TextView below = findViewById(R.id.tiertext);
        TextView df = findViewById(R.id.text);
        Button detail = findViewById(R.id.details);
        String d_kda = result.get(1);
        String d_deal = result.get(2);
        String d_dealtaken = result.get(3);
        String d_heal = result.get(4);
        String d_vision = result.get(5);
        String d_gold = result.get(6);
        String d_turret = result.get(7);
        String d_cs = result.get(8);
        String d_level = result.get(9);

        if (db < IRON) {
            // IRON
            tier_image.setBackgroundResource(R.drawable.iron);
            below.setText("IRON");
        } else if (db < BRONZE) {
            // BRONZE
            tier_image.setBackgroundResource(R.drawable.bronze);
            below.setText("BRONZE");
        } else if (db < SILVER) {
            // SILVER
            tier_image.setBackgroundResource(R.drawable.silver);
            below.setText("SILVER");
        } else if (db < GOLD) {
            // GOLD
            tier_image.setBackgroundResource(R.drawable.gold);
            below.setText("GOLD");
        } else if (db < PLATINUM) {
            // PLATINUM
            tier_image.setBackgroundResource(R.drawable.platinum);
            below.setText("PLATINUM");
        } else if (db < DIA) {
            // DIAMOND
            tier_image.setBackgroundResource(R.drawable.dia);
            below.setText("DIAMOND");
        } else {
            // MASTER
            tier_image.setBackgroundResource(R.drawable.master);
            below.setText("MASTER");
        }

        detail.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                show(result);
            }
        });
    }

    void show(List<String> list) {
        AlertDialog.Builder builder = new AlertDialog.Builder(this);
        LayoutInflater inflater = getLayoutInflater();
        View view = inflater.inflate(R.layout.dialog_tier, null);
        builder.setView(view);
        final TextView title_text = (TextView) view.findViewById(R.id.title);
        final TextView kda_text = (TextView) view.findViewById(R.id.kda);
        final TextView deal_text = (TextView) view.findViewById(R.id.deal);
        final TextView dealtaken_text = (TextView) view.findViewById(R.id.dealtaken);
        final TextView heal_text = (TextView) view.findViewById(R.id.heal);
        final TextView vision_text = (TextView) view.findViewById(R.id.vision);
        final TextView gold_text = (TextView) view.findViewById(R.id.gold);
        final TextView turret_text = (TextView) view.findViewById(R.id.turret);
        final TextView cs_text = (TextView) view.findViewById(R.id.cs);
        final TextView level_text = (TextView) view.findViewById(R.id.level);

        Double tier = Double.parseDouble(list.get(0));
        String lane = list.get(10);
        String role = list.get(11);
//        Double kda = Double.parseDouble(list.get(1));
//        Double deal = Double.parseDouble(list.get(2));
//        Double dealtaken = Double.parseDouble(list.get(3));
//        Double heal = Double.parseDouble(list.get(4));
//        Double vision = Double.parseDouble(list.get(5));
//        Double gold = Double.parseDouble(list.get(6));
//        Double turret = Double.parseDouble(list.get(7));
//        Double cs = Double.parseDouble(list.get(8));
//        Double level = Double.parseDouble(list.get(9));

        if (tier < IRON) {
            // IRON
            if (lane.equals("TOP")) {
                kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(iron_top_avg_kda) + ")");
                deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(iron_top_avg_deal) + ")");
                dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(iron_top_avg_dealtaken) + ")");
                heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(iron_top_avg_heal) + ")");
                vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(iron_top_avg_vision) + ")");
                gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(iron_top_avg_gold) + ")");
                turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(iron_top_avg_turret) + ")");
                cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(iron_top_avg_cs) + ")");
                level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(iron_top_avg_level) + ")");
            }
            else if (lane.equals("mid")) {
                kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(iron_mid_avg_kda) + ")");
                deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(iron_mid_avg_deal) + ")");
                dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(iron_mid_avg_dealtaken) + ")");
                heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(iron_mid_avg_heal) + ")");
                vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(iron_mid_avg_vision) + ")");
                gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(iron_mid_avg_gold) + ")");
                turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(iron_mid_avg_turret) + ")");
                cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(iron_mid_avg_cs) + ")");
                level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(iron_mid_avg_level) + ")");
            }
            else if (lane.equals("JUNGLE")) {
                kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(iron_jungle_avg_kda) + ")");
                deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(iron_jungle_avg_deal) + ")");
                dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(iron_jungle_avg_dealtaken) + ")");
                heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(iron_jungle_avg_heal) + ")");
                vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(iron_jungle_avg_vision) + ")");
                gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(iron_jungle_avg_gold) + ")");
                turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(iron_jungle_avg_turret) + ")");
                cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(iron_jungle_avg_cs) + ")");
                level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(iron_jungle_avg_level) + ")");
            }
            else if (lane.equals("BOTTOM")) {
                if (role.equals("DUO_CARRY")) {
                    kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(iron_bot_avg_kda) + ")");
                    deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(iron_bot_avg_deal) + ")");
                    dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(iron_bot_avg_dealtaken) + ")");
                    heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(iron_bot_avg_heal) + ")");
                    vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(iron_bot_avg_vision) + ")");
                    gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(iron_bot_avg_gold) + ")");
                    turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(iron_bot_avg_turret) + ")");
                    cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(iron_bot_avg_cs) + ")");
                    level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(iron_bot_avg_level) + ")");
                }
                else if (role.equals("DUO_SUPPORT")) {
                    kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(iron_sup_avg_kda) + ")");
                    deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(iron_sup_avg_deal) + ")");
                    dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(iron_sup_avg_dealtaken) + ")");
                    heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(iron_sup_avg_heal) + ")");
                    vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(iron_sup_avg_vision) + ")");
                    gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(iron_sup_avg_gold) + ")");
                    turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(iron_sup_avg_turret) + ")");
                    cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(iron_sup_avg_cs) + ")");
                    level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(iron_sup_avg_level) + ")");
                }
            }
        } else if (tier < BRONZE) {
            // BRONZE
            if (lane.equals("TOP")) {
                kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(bronze_top_avg_kda) + ")");
                deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(bronze_top_avg_deal) + ")");
                dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(bronze_top_avg_dealtaken) + ")");
                heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(bronze_top_avg_heal) + ")");
                vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(bronze_top_avg_vision) + ")");
                gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(bronze_top_avg_gold) + ")");
                turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(bronze_top_avg_turret) + ")");
                cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(bronze_top_avg_cs) + ")");
                level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(bronze_top_avg_level) + ")");
            }
            else if (lane.equals("MIDDLE")) {
                kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(bronze_mid_avg_kda) + ")");
                deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(bronze_mid_avg_deal) + ")");
                dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(bronze_mid_avg_dealtaken) + ")");
                heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(bronze_mid_avg_heal) + ")");
                vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(bronze_mid_avg_vision) + ")");
                gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(bronze_mid_avg_gold) + ")");
                turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(bronze_mid_avg_turret) + ")");
                cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(bronze_mid_avg_cs) + ")");
                level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(bronze_mid_avg_level) + ")");
            }
            else if (lane.equals("JUNGLE")) {
                kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(bronze_jungle_avg_kda) + ")");
                deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(bronze_jungle_avg_deal) + ")");
                dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(bronze_jungle_avg_dealtaken) + ")");
                heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(bronze_jungle_avg_heal) + ")");
                vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(bronze_jungle_avg_vision) + ")");
                gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(bronze_jungle_avg_gold) + ")");
                turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(bronze_jungle_avg_turret) + ")");
                cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(bronze_jungle_avg_cs) + ")");
                level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(bronze_jungle_avg_level) + ")");
            }
            else if (lane.equals("BOTTOM")) {
                if (role.equals("DUO_CARRY")) {
                    kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(bronze_bot_avg_kda) + ")");
                    deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(bronze_bot_avg_deal) + ")");
                    dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(bronze_bot_avg_dealtaken) + ")");
                    heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(bronze_bot_avg_heal) + ")");
                    vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(bronze_bot_avg_vision) + ")");
                    gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(bronze_bot_avg_gold) + ")");
                    turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(bronze_bot_avg_turret) + ")");
                    cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(bronze_bot_avg_cs) + ")");
                    level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(bronze_bot_avg_level) + ")");
                }
                else if (role.equals("DUO_SUPPORT")) {
                    kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(bronze_sup_avg_kda) + ")");
                    deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(bronze_sup_avg_deal) + ")");
                    dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(bronze_sup_avg_dealtaken) + ")");
                    heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(bronze_sup_avg_heal) + ")");
                    vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(bronze_sup_avg_vision) + ")");
                    gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(bronze_sup_avg_gold) + ")");
                    turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(bronze_sup_avg_turret) + ")");
                    cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(bronze_sup_avg_cs) + ")");
                    level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(bronze_sup_avg_level) + ")");
                }
            }
        } else if (tier < SILVER) {
            // SILVER
            if (lane.equals("TOP")) {
                kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(silver_top_avg_kda) + ")");
                deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(silver_top_avg_deal) + ")");
                dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(silver_top_avg_dealtaken) + ")");
                heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(silver_top_avg_heal) + ")");
                vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(silver_top_avg_vision) + ")");
                gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(silver_top_avg_gold) + ")");
                turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(silver_top_avg_turret) + ")");
                cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(silver_top_avg_cs) + ")");
                level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(silver_top_avg_level) + ")");
            }
            else if (lane.equals("MIDDLE")) {
                kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(silver_mid_avg_kda) + ")");
                deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(silver_mid_avg_deal) + ")");
                dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(silver_mid_avg_dealtaken) + ")");
                heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(silver_mid_avg_heal) + ")");
                vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(silver_mid_avg_vision) + ")");
                gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(silver_mid_avg_gold) + ")");
                turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(silver_mid_avg_turret) + ")");
                cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(silver_mid_avg_cs) + ")");
                level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(silver_mid_avg_level) + ")");
            }
            else if (lane.equals("JUNGLE")) {
                kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(silver_jungle_avg_kda) + ")");
                deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(silver_jungle_avg_deal) + ")");
                dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(silver_jungle_avg_dealtaken) + ")");
                heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(silver_jungle_avg_heal) + ")");
                vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(silver_jungle_avg_vision) + ")");
                gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(silver_jungle_avg_gold) + ")");
                turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(silver_jungle_avg_turret) + ")");
                cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(silver_jungle_avg_cs) + ")");
                level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(silver_jungle_avg_level) + ")");
            }
            else if (lane.equals("BOTTOM")) {
                if (role.equals("DUO_CARRY")) {
                    kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(silver_bot_avg_kda) + ")");
                    deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(silver_bot_avg_deal) + ")");
                    dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(silver_bot_avg_dealtaken) + ")");
                    heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(silver_bot_avg_heal) + ")");
                    vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(silver_bot_avg_vision) + ")");
                    gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(silver_bot_avg_gold) + ")");
                    turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(silver_bot_avg_turret) + ")");
                    cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(silver_bot_avg_cs) + ")");
                    level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(silver_bot_avg_level) + ")");
                }
                else if (role.equals("DUO_SUPPORT")) {
                    kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(silver_sup_avg_kda) + ")");
                    deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(silver_sup_avg_deal) + ")");
                    dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(silver_sup_avg_dealtaken) + ")");
                    heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(silver_sup_avg_heal) + ")");
                    vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(silver_sup_avg_vision) + ")");
                    gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(silver_sup_avg_gold) + ")");
                    turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(silver_sup_avg_turret) + ")");
                    cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(silver_sup_avg_cs) + ")");
                    level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(silver_sup_avg_level) + ")");
                }
            }
        } else if (tier < GOLD) {
            // GOLD
            if (lane.equals("TOP")) {
                kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(gold_top_avg_kda) + ")");
                deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(gold_top_avg_deal) + ")");
                dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(gold_top_avg_dealtaken) + ")");
                heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(gold_top_avg_heal) + ")");
                vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(gold_top_avg_vision) + ")");
                gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(gold_top_avg_gold) + ")");
                turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(gold_top_avg_turret) + ")");
                cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(gold_top_avg_cs) + ")");
                level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(gold_top_avg_level) + ")");
            }
            else if (lane.equals("MIDDLE")) {
                kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(gold_mid_avg_kda) + ")");
                deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(gold_mid_avg_deal) + ")");
                dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(gold_mid_avg_dealtaken) + ")");
                heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(gold_mid_avg_heal) + ")");
                vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(gold_mid_avg_vision) + ")");
                gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(gold_mid_avg_gold) + ")");
                turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(gold_mid_avg_turret) + ")");
                cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(gold_mid_avg_cs) + ")");
                level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(gold_mid_avg_level) + ")");
            }
            else if (lane.equals("JUNGLE")) {
                kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(gold_jungle_avg_kda) + ")");
                deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(gold_jungle_avg_deal) + ")");
                dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(gold_jungle_avg_dealtaken) + ")");
                heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(gold_jungle_avg_heal) + ")");
                vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(gold_jungle_avg_vision) + ")");
                gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(gold_jungle_avg_gold) + ")");
                turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(gold_jungle_avg_turret) + ")");
                cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(gold_jungle_avg_cs) + ")");
                level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(gold_jungle_avg_level) + ")");
            }
            else if (lane.equals("BOTTOM")) {
                if (role.equals("DUO_CARRY")) {
                    kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(gold_bot_avg_kda) + ")");
                    deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(gold_bot_avg_deal) + ")");
                    dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(gold_bot_avg_dealtaken) + ")");
                    heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(gold_bot_avg_heal) + ")");
                    vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(gold_bot_avg_vision) + ")");
                    gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(gold_bot_avg_gold) + ")");
                    turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(gold_bot_avg_turret) + ")");
                    cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(gold_bot_avg_cs) + ")");
                    level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(gold_bot_avg_level) + ")");
                }
                else if (role.equals("DUO_SUPPORT")) {
                    kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(gold_sup_avg_kda) + ")");
                    deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(gold_sup_avg_deal) + ")");
                    dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(gold_sup_avg_dealtaken) + ")");
                    heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(gold_sup_avg_heal) + ")");
                    vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(gold_sup_avg_vision) + ")");
                    gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(gold_sup_avg_gold) + ")");
                    turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(gold_sup_avg_turret) + ")");
                    cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(gold_sup_avg_cs) + ")");
                    level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(gold_sup_avg_level) + ")");
                }
            }
        } else if (tier < PLATINUM) {
            // PLATINUM
            if (lane.equals("TOP")) {
                kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(platinum_top_avg_kda) + ")");
                deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(platinum_top_avg_deal) + ")");
                dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(platinum_top_avg_dealtaken) + ")");
                heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(platinum_top_avg_heal) + ")");
                vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(platinum_top_avg_vision) + ")");
                gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(platinum_top_avg_gold) + ")");
                turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(platinum_top_avg_turret) + ")");
                cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(platinum_top_avg_cs) + ")");
                level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(platinum_top_avg_level) + ")");
            }
            else if (lane.equals("MIDDLE")) {
                kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(platinum_mid_avg_kda) + ")");
                deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(platinum_mid_avg_deal) + ")");
                dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(platinum_mid_avg_dealtaken) + ")");
                heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(platinum_mid_avg_heal) + ")");
                vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(platinum_mid_avg_vision) + ")");
                gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(platinum_mid_avg_gold) + ")");
                turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(platinum_mid_avg_turret) + ")");
                cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(platinum_mid_avg_cs) + ")");
                level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(platinum_mid_avg_level) + ")");
            }
            else if (lane.equals("JUNGLE")) {
                kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(platinum_jungle_avg_kda) + ")");
                deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(platinum_jungle_avg_deal) + ")");
                dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(platinum_jungle_avg_dealtaken) + ")");
                heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(platinum_jungle_avg_heal) + ")");
                vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(platinum_jungle_avg_vision) + ")");
                gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(platinum_jungle_avg_gold) + ")");
                turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(platinum_jungle_avg_turret) + ")");
                cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(platinum_jungle_avg_cs) + ")");
                level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(platinum_jungle_avg_level) + ")");
            }
            else if (lane.equals("BOTTOM")) {
                if (role.equals("DUO_CARRY")) {
                    kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(platinum_bot_avg_kda) + ")");
                    deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(platinum_bot_avg_deal) + ")");
                    dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(platinum_bot_avg_dealtaken) + ")");
                    heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(platinum_bot_avg_heal) + ")");
                    vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(platinum_bot_avg_vision) + ")");
                    gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(platinum_bot_avg_gold) + ")");
                    turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(platinum_bot_avg_turret) + ")");
                    cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(platinum_bot_avg_cs) + ")");
                    level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(platinum_bot_avg_level) + ")");
                }
                else if (role.equals("DUO_SUPPORT")) {
                    kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(platinum_sup_avg_kda) + ")");
                    deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(platinum_sup_avg_deal) + ")");
                    dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(platinum_sup_avg_dealtaken) + ")");
                    heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(platinum_sup_avg_heal) + ")");
                    vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(platinum_sup_avg_vision) + ")");
                    gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(platinum_sup_avg_gold) + ")");
                    turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(platinum_sup_avg_turret) + ")");
                    cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(platinum_sup_avg_cs) + ")");
                    level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(platinum_sup_avg_level) + ")");
                }
            }
        } else if (tier < DIA) {
            // DIAMOND
            if (lane.equals("TOP")) {
                kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(dia_top_avg_kda) + ")");
                deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(dia_top_avg_deal) + ")");
                dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(dia_top_avg_dealtaken) + ")");
                heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(dia_top_avg_heal) + ")");
                vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(dia_top_avg_vision) + ")");
                gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(dia_top_avg_gold) + ")");
                turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(dia_top_avg_turret) + ")");
                cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(dia_top_avg_cs) + ")");
                level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(dia_top_avg_level) + ")");
            }
            else if (lane.equals("MIDDLE")) {
                kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(dia_mid_avg_kda) + ")");
                deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(dia_mid_avg_deal) + ")");
                dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(dia_mid_avg_dealtaken) + ")");
                heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(dia_mid_avg_heal) + ")");
                vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(dia_mid_avg_vision) + ")");
                gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(dia_mid_avg_gold) + ")");
                turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(dia_mid_avg_turret) + ")");
                cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(dia_mid_avg_cs) + ")");
                level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(dia_mid_avg_level) + ")");
            }
            else if (lane.equals("JUNGLE")) {
                kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(dia_jungle_avg_kda) + ")");
                deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(dia_jungle_avg_deal) + ")");
                dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(dia_jungle_avg_dealtaken) + ")");
                heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(dia_jungle_avg_heal) + ")");
                vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(dia_jungle_avg_vision) + ")");
                gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(dia_jungle_avg_gold) + ")");
                turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(dia_jungle_avg_turret) + ")");
                cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(dia_jungle_avg_cs) + ")");
                level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(dia_jungle_avg_level) + ")");
            }
            else if (lane.equals("BOTTOM")) {
                if (role.equals("DUO_CARRY")) {
                    kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(dia_bot_avg_kda) + ")");
                    deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(dia_bot_avg_deal) + ")");
                    dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(dia_bot_avg_dealtaken) + ")");
                    heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(dia_bot_avg_heal) + ")");
                    vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(dia_bot_avg_vision) + ")");
                    gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(dia_bot_avg_gold) + ")");
                    turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(dia_bot_avg_turret) + ")");
                    cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(dia_bot_avg_cs) + ")");
                    level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(dia_bot_avg_level) + ")");
                }
                else if (role.equals("DUO_SUPPORT")) {
                    kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(dia_sup_avg_kda) + ")");
                    deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(dia_sup_avg_deal) + ")");
                    dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(dia_sup_avg_dealtaken) + ")");
                    heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(dia_sup_avg_heal) + ")");
                    vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(dia_sup_avg_vision) + ")");
                    gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(dia_sup_avg_gold) + ")");
                    turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(dia_sup_avg_turret) + ")");
                    cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(dia_sup_avg_cs) + ")");
                    level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(dia_sup_avg_level) + ")");
                }
            }
        } else {
            // MASTER
            if (lane.equals("TOP")) {
                kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(master_top_avg_kda) + ")");
                deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(master_top_avg_deal) + ")");
                dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(master_top_avg_dealtaken) + ")");
                heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(master_top_avg_heal) + ")");
                vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(master_top_avg_vision) + ")");
                gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(master_top_avg_gold) + ")");
                turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(master_top_avg_turret) + ")");
                cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(master_top_avg_cs) + ")");
                level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(master_top_avg_level) + ")");
            }
            else if (lane.equals("MIDDLE")) {
                kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(master_mid_avg_kda) + ")");
                deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(master_mid_avg_deal) + ")");
                dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(master_mid_avg_dealtaken) + ")");
                heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(master_mid_avg_heal) + ")");
                vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(master_mid_avg_vision) + ")");
                gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(master_mid_avg_gold) + ")");
                turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(master_mid_avg_turret) + ")");
                cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(master_mid_avg_cs) + ")");
                level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(master_mid_avg_level) + ")");
            }
            else if (lane.equals("JUNGLE")) {
                kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(master_jungle_avg_kda) + ")");
                deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(master_jungle_avg_deal) + ")");
                dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(master_jungle_avg_dealtaken) + ")");
                heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(master_jungle_avg_heal) + ")");
                vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(master_jungle_avg_vision) + ")");
                gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(master_jungle_avg_gold) + ")");
                turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(master_jungle_avg_turret) + ")");
                cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(master_jungle_avg_cs) + ")");
                level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(master_jungle_avg_level) + ")");
            }
            else if (lane.equals("BOTTOM")) {
                if (role.equals("DUO_CARRY")) {
                    kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(master_bot_avg_kda) + ")");
                    deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(master_bot_avg_deal) + ")");
                    dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(master_bot_avg_dealtaken) + ")");
                    heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(master_bot_avg_heal) + ")");
                    vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(master_bot_avg_vision) + ")");
                    gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(master_bot_avg_gold) + ")");
                    turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(master_bot_avg_turret) + ")");
                    cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(master_bot_avg_cs) + ")");
                    level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(master_bot_avg_level) + ")");
                }
                else if (role.equals("DUO_SUPPORT")) {
                    kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(master_sup_avg_kda) + ")");
                    deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(master_sup_avg_deal) + ")");
                    dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(master_sup_avg_dealtaken) + ")");
                    heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(master_sup_avg_heal) + ")");
                    vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(master_sup_avg_vision) + ")");
                    gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(master_sup_avg_gold) + ")");
                    turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(master_sup_avg_turret) + ")");
                    cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(master_sup_avg_cs) + ")");
                    level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(master_sup_avg_level) + ")");
                }
            }
        }


        final AlertDialog dialog = builder.create();
        dialog.show();
    }
}
