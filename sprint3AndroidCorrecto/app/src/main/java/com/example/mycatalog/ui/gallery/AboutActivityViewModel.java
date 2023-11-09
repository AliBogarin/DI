package com.example.mycatalog.ui.gallery;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

public class AboutActivityViewModel extends ViewModel {

    private final MutableLiveData<String> mText;
 //Creo el texto que se verá
    public AboutActivityViewModel() {
        mText = new MutableLiveData<>();
        mText.setValue("Este es mi pequeño texto, solo digo que después de estas " +
                "tropecientas horas encima para entender solo un poco," +
                "solo quiero aprobar por Dioooo!!!");
    }

    public LiveData<String> getText() {
        return mText;
    }
}