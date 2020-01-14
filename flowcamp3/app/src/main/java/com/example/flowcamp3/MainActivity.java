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

        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                final EditText editText = (EditText)findViewById(R.id.editText);
                final String username = editText.getText().toString();
                Intent intent = new Intent(getApplicationContext(), Main2Activity.class);
                intent.putExtra("userid", username);
                startActivity(intent);
                finish();
            }
        });
    }
}
