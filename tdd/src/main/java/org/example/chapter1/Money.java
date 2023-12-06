package org.example.chapter1;

public abstract class Money {
    protected int amount;

    public static Dollar dollar(int amount){
        return new Dollar(amount);
    }

    public static Franc franc(int amount){
        return new Franc(amount);
    }

    public abstract Money times(int multiplier);

    public boolean equals(Object object){
        Money money = (Money) object;
        return this.amount == money.amount
                && getClass().equals(money.getClass());

    }
}
