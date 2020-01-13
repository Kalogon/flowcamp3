package com.example.flowcamp3;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import java.util.concurrent.ExecutionException;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Button button = (Button) findViewById(R.id.button1);
        String str = "";
        OpenRiotAPITask t = new OpenRiotAPITask();
        try {
            str = t.execute("hide on bush").get();
            Log.e("client", str);
        } catch (InterruptedException e) {
            e.printStackTrace();
        } catch (ExecutionException e) {
            e.printStackTrace();
        }
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                EditText editText = (EditText)findViewById(R.id.editText);
                Intent intent = new Intent(getApplicationContext(), Main2Activity.class);
                intent.putExtra("userid", editText.getText());
                startActivity(intent);
                finish();
            }
        });
    }
}
