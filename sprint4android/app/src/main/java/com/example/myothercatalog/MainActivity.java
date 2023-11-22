package com.example.myothercatalog;

import android.content.Context;
import android.os.Bundle;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.constraintlayout.widget.ConstraintLayout;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    private RequestQueue queue;
    private Context context = this;
    private ConstraintLayout mainLayout;
    private RecyclerView recyclerView;
    private MariposaViewAdapter adapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        this.queue = Volley.newRequestQueue(context);
        this.mainLayout = findViewById(R.id.main_layout);
        this.recyclerView = findViewById(R.id.recycler_view);
        this.adapter = new MariposaViewAdapter(new ArrayList<>(), this);

        recyclerView.setLayoutManager(new LinearLayoutManager(this));
        recyclerView.setAdapter(adapter);

        String url = "https://raw.githubusercontent.com/AliBogarin/DWES/main/sprint1Tkinter/catalog/data/catalog.json";

        JsonArrayRequest request = new JsonArrayRequest(
                Request.Method.GET,
                url,
                null,
                new Response.Listener<JSONArray>() {
                    @Override
                    public void onResponse(JSONArray response) {
                        List<MariposaData> allMariposas = new ArrayList<>();

                        // Éxito
                        for (int i = 0; i < response.length(); i++) {
                            try {
                                JSONObject object = response.getJSONObject(i);
                                MariposaData mariposaData = new MariposaData(object);
                                allMariposas.add(mariposaData);
                            } catch (JSONException e) {
                                throw new RuntimeException(e);
                            }
                        }

                        // Actualizar el adaptador con los datos obtenidos
                        adapter.setData(allMariposas);
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        // Error o fallo
                        Toast.makeText(context, "Fallito bueno", Toast.LENGTH_SHORT).show();
                    }
                }
        );

        queue.add(request);
    }
}