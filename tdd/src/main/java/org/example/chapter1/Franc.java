package org.example.chapter1;

public class Franc extends Money{
    public Franc(int amount){
        this.amount = amount;
    }

    public Money times(int multiplier){
        return new Franc(this.amount * multiplier);
    }
}
