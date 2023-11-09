package com.example.mycatalog.ui.home;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

public class HomeViewModel extends ViewModel {

    private final MutableLiveData<String> mText;
//Mi texto de la ventana pricipal
    public HomeViewModel() {
        mText = new MutableLiveData<>();
        mText.setValue("Bienvenidos a mi pequeño mundo de luz y de color!");
    }

    public LiveData<String> getText() {
        return mText;
    }
}