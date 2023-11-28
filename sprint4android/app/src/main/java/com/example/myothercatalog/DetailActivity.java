package com.example.myothercatalog;

import android.content.Intent;
import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import com.bumptech.glide.Glide;


public class DetailActivity extends AppCompatActivity {
    /*Inicializo mi DetailActivity y lo apunto en mi manifesto*/
    private TextView name_v;
    private  TextView description_v;
    private ImageView image_v;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.detail_activity);

       image_v = findViewById(R.id.view_image_detail);
       name_v = findViewById(R.id.title_detail);
       description_v = findViewById(R.id.textView_description_detail);

       Intent intent = getIntent();
    //Cargo la actividad por medio de una Intent()
       String name = intent.getStringExtra("name");
       String description = intent.getStringExtra("description");
       String url = intent.getStringExtra("image_url");
        //Utilizo Glide() para visualizar la imgen
       Glide.with(DetailActivity.this).load(url).into(image_v);
       name_v.setText(name);
       description_v.setText(description);

       //este glide lo utilizo para visualizar la imgen en circulo
        Glide.with(DetailActivity.this)
                .load(url)
                .circleCrop()
                .into(image_v);

    }
}
