package com.example.myothercatalog;

import android.app.Activity;
import android.content.Intent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;
//Este es mi adaptador donde visualizare la información que visualizaré desde mi json
public class MariposaViewAdapter extends RecyclerView.Adapter<MariposaViewHolder> {

    private List<MariposaData> allData;
    private Activity activity;

    public MariposaViewAdapter(List<MariposaData> dataset, Activity activity) {
        this.allData = dataset;
        this.activity = activity;
    }

    @NonNull
    @Override
    public MariposaViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        LayoutInflater inflater = LayoutInflater.from(parent.getContext());
        View cellView = inflater.inflate(R.layout.mariposa_view, parent, false);
        return new MariposaViewHolder(cellView);
    }

    @Override
    public void onBindViewHolder(@NonNull MariposaViewHolder holder, int position) {
        MariposaData positionData = allData.get(position);
        holder.showData(positionData, activity);

        //Aqui inicializare el DetailActivity cuando haga click en alguna celda
        holder.itemView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent  = new Intent(activity, DetailActivity.class);
                activity.startActivity(intent);
            }
        });
    }

    @Override
    public int getItemCount() {
        return allData.size();
    }

    public void setData(List<MariposaData> newData) {
        allData.clear();
        allData.addAll(newData);
       notifyDataSetChanged();
    }
}