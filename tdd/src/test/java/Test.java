import org.example.chapter1.Dollar;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class Test {

    @org.junit.jupiter.api.Test
    public void multipleTest(){
        Dollar dollar = new Dollar(5);
        int result = dollar.times(2);
        assertEquals(10,result);
    }
}
