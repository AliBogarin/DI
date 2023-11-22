package com.example.myothercatalog;

import android.app.Activity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

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