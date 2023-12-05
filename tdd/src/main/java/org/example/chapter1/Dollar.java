package org.example.chapter1;

public class Dollar {
    public int amount;
    public Dollar(int amount){
        this.amount = amount;
    }
    public int times(int multiplier){
        amount *= multiplier;
        return amount;
    }

}
