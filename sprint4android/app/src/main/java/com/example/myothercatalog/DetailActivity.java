package com.example.myothercatalog;

import android.os.Bundle;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

public class DetailActivity extends AppCompatActivity {
    /*Inicializo mi DetailActivity y lo apunto en mi manifesto*/
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.detail_activity);
    }
}
