package org.example.chapter1;

// 환율 해시 테이블의 key 를 위한 클래스
public class Pair {
    private String from;
    private String to;

    Pair(String from, String to){
        this.from = from;
        this.to = to;
    }

    @Override
    public boolean equals(Object object){
        Pair pair = (Pair) object;
        return from.equals(pair.from) && to.equals(pair.to);
    }

    @Override
    public int hashCode() {
        return 0;
    }
}
