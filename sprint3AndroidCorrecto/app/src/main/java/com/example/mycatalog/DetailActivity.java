package com.example.mycatalog;

import android.os.Bundle;
import android.widget.Button;

import androidx.appcompat.app.AppCompatActivity;

public class DetailActivity extends AppCompatActivity {



    //Llamo a mi button desde el xml  y lo identifico por su Id
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.detail_activity);

    }

}