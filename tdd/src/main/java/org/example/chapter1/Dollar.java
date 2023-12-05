package org.example.chapter1;

public class Dollar {
    private int amount;
    public Dollar(int amount){
        this.amount = amount;
    }

    public Dollar times(int multiplier){
        return new Dollar(this.amount * multiplier);
    }

    @Override
    public boolean equals(Object object){
        Dollar d = (Dollar) object;
        return this.amount == d.amount;

    }
}
