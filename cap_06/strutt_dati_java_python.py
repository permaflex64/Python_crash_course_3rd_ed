'''
import java.util.*;

public class EsempioCollezioni {
    public static void main(String[] args) {
        
        // 1. HASHSET: Niente duplicati, ordine casuale (il più veloce)
        Set<String> invitati = new HashSet<>();
        invitati.add("Zaira");
        invitati.add("Marco");
        invitati.add("Andrea");
        invitati.add("Marco"); // Questo duplicato verrà ignorato
        System.out.println("HashSet (ordine casuale): " + invitati);
        // Output tipico: [Andrea, Zaira, Marco]

        // 2. TREESET: Niente duplicati, ordine ALFABETICO/NATURALE
        Set<String> invitatiOrdinati = new TreeSet<>(invitati);
        System.out.println("TreeSet (ordinato): " + invitatiOrdinati);
        // Output: [Andrea, Marco, Zaira]

        // 3. HASHMAP: Coppie Chiave-Valore (es. Nome -> Tavolo)
        Map<String, Integer> tavoli = new HashMap<>();
        tavoli.put("Marco", 5);
        tavoli.put("Andrea", 2);
        tavoli.put("Zaira", 5); // Due persone possono stare allo stesso tavolo
        
        System.out.println("HashMap (Chi siede dove): " + tavoli);
        System.out.println("Tavolo di Andrea: " + tavoli.get("Andrea"));
    }
}
'''