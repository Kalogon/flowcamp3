package com.example.flowcamp3;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import org.w3c.dom.Text;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;
import java.util.concurrent.ExecutionException;

public class Main2Activity extends AppCompatActivity {
    double IRON = 1.0;
    double BRONZE = 2.0;
    double SILVER = 3.0;
    double GOLD = 4.0;
    double PLATINUM = 5.0;
    double DIA = 6.0;
    double MASTER = 7.0;

    // Iron
    double iron_avg_kda;
    double iron_avg_deal;
    double iron_avg_dealtaken;
    double iron_avg_heal;
    double iron_avg_vision;
    double iron_avg_gold;
    double iron_avg_turret;
    double iron_avg_cs;
    double iron_avg_level;

    // Bronze
    double bronze_avg_kda;
    double bronze_avg_deal;
    double bronze_avg_dealtaken;
    double bronze_avg_heal;
    double bronze_avg_vision;
    double bronze_avg_gold;
    double bronze_avg_turret;
    double bronze_avg_cs;
    double bronze_avg_level;

    // Silver
    double silver_avg_kda;
    double silver_avg_deal;
    double silver_avg_dealtaken;
    double silver_avg_heal;
    double silver_avg_vision;
    double silver_avg_gold;
    double silver_avg_turret;
    double silver_avg_cs;
    double silver_avg_level;

    // Gold
    double gold_avg_kda;
    double gold_avg_deal;
    double gold_avg_dealtaken;
    double gold_avg_heal;
    double gold_avg_vision;
    double gold_avg_gold;
    double gold_avg_turret;
    double gold_avg_cs;
    double gold_avg_level;

    // Platinum
    double platinum_avg_kda;
    double platinum_avg_deal;
    double platinum_avg_dealtaken;
    double platinum_avg_heal;
    double platinum_avg_vision;
    double platinum_avg_gold;
    double platinum_avg_turret;
    double platinum_avg_cs;
    double platinum_avg_level;

    // Diamond
    double dia_avg_kda;
    double dia_avg_deal;
    double dia_avg_dealtaken;
    double dia_avg_heal;
    double dia_avg_vision;
    double dia_avg_gold;
    double dia_avg_turret;
    double dia_avg_cs;
    double dia_avg_level;

    // Master
    double master_avg_kda;
    double master_avg_deal;
    double master_avg_dealtaken;
    double master_avg_heal;
    double master_avg_vision;
    double master_avg_gold;
    double master_avg_turret;
    double master_avg_cs;
    double master_avg_level;

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
            kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(iron_avg_kda) + ")");
            deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(iron_avg_deal) + ")");
            dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(iron_avg_dealtaken) + ")");
            heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(iron_avg_heal) + ")");
            vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(iron_avg_vision) + ")");
            gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(iron_avg_gold) + ")");
            turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(iron_avg_turret) + ")");
            cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(iron_avg_cs) + ")");
            level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(iron_avg_level) + ")");
        } else if (tier < BRONZE) {
            // BRONZE
            kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(bronze_avg_kda) + ")");
            deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(bronze_avg_deal) + ")");
            dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(bronze_avg_dealtaken) + ")");
            heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(bronze_avg_heal) + ")");
            vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(bronze_avg_vision) + ")");
            gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(bronze_avg_gold) + ")");
            turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(bronze_avg_turret) + ")");
            cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(bronze_avg_cs) + ")");
            level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(bronze_avg_level) + ")");
        } else if (tier < SILVER) {
            // SILVER
            kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(silver_avg_kda) + ")");
            deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(silver_avg_deal) + ")");
            dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(silver_avg_dealtaken) + ")");
            heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(silver_avg_heal) + ")");
            vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(silver_avg_vision) + ")");
            gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(silver_avg_gold) + ")");
            turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(silver_avg_turret) + ")");
            cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(silver_avg_cs) + ")");
            level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(silver_avg_level) + ")");
        } else if (tier < GOLD) {
            // GOLD
            kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(gold_avg_kda) + ")");
            deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(gold_avg_deal) + ")");
            dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(gold_avg_dealtaken) + ")");
            heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(gold_avg_heal) + ")");
            vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(gold_avg_vision) + ")");
            gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(gold_avg_gold) + ")");
            turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(gold_avg_turret) + ")");
            cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(gold_avg_cs) + ")");
            level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(gold_avg_level) + ")");
        } else if (tier < PLATINUM) {
            // PLATINUM
            kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(platinum_avg_kda) + ")");
            deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(platinum_avg_deal) + ")");
            dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(platinum_avg_dealtaken) + ")");
            heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(platinum_avg_heal) + ")");
            vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(platinum_avg_vision) + ")");
            gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(platinum_avg_gold) + ")");
            turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(platinum_avg_turret) + ")");
            cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(platinum_avg_cs) + ")");
            level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(platinum_avg_level) + ")");
        } else if (tier < DIA) {
            // DIAMOND
            kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(dia_avg_kda) + ")");
            deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(dia_avg_deal) + ")");
            dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(dia_avg_dealtaken) + ")");
            heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(dia_avg_heal) + ")");
            vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(dia_avg_vision) + ")");
            gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(dia_avg_gold) + ")");
            turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(dia_avg_turret) + ")");
            cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(dia_avg_cs) + ")");
            level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(dia_avg_level) + ")");
        } else {
            // MASTER
            kda_text.setText("KDA : " + list.get(1) + " (" + Double.toString(master_avg_kda) + ")");
            deal_text.setText("딜량 : " + list.get(2) + " (" + Double.toString(master_avg_deal) + ")");
            dealtaken_text.setText("받은 딜량 : " + list.get(3) + " (" + Double.toString(master_avg_dealtaken) + ")");
            heal_text.setText("힐량 : " + list.get(4) + " (" + Double.toString(master_avg_heal) + ")");
            vision_text.setText("시야 점수 : " + list.get(5) + " (" + Double.toString(master_avg_vision) + ")");
            gold_text.setText("골드 : " + list.get(6) + " (" + Double.toString(master_avg_gold) + ")");
            turret_text.setText("포탑 : " + list.get(7) + " (" + Double.toString(master_avg_turret) + ")");
            cs_text.setText("CS : " + list.get(8) + " (" + Double.toString(master_avg_cs) + ")");
            level_text.setText("레벨 : " + list.get(9) + " (" + Double.toString(master_avg_level) + ")");
        }


        final AlertDialog dialog = builder.create();
        dialog.show();
    }
}
