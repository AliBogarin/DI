package com.example.mycatalog;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import androidx.appcompat.app.AppCompatActivity;

public class CatalogActivity extends AppCompatActivity {

    private Button button;
    Context context = this;

    //Llamo a mi button desde el xml  y lo identifico por su Id
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.catalog_activity);

        button = findViewById(R.id.botton_Navigate_To_Detail);

        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(context, DetailActivity.class);
                //inicializo  DetailActivity en CatalogActivity, a traves del boton
                startActivity(intent);
            }
        });

    }
}
