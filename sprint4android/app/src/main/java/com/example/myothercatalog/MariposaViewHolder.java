package com.example.myothercatalog;

import android.app.Activity;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;
import com.bumptech.glide.Glide;
public class MariposaViewHolder extends RecyclerView.ViewHolder {
//implemento las celdas donde mostrare mis imagenes y nombres de mariposas
    private  TextView textView;
    private  ImageView imageView;

    public MariposaViewHolder(@NonNull View itemView) {
        super(itemView);

        textView =  (TextView) itemView.findViewById(R.id.mariposa_name);
        imageView= (ImageView)  itemView.findViewById(R.id.mariposa_image);

    }

    public  void showData (MariposaData mariposa, Activity activity){
        textView.setText(mariposa.getName());
        Glide.with(itemView.getContext()).load(mariposa.getImage_url()).into(imageView);
    }
}
