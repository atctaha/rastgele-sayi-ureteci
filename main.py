import time

class CollatzRNG:
    """
    Collatz Sanısı (3x+1 Problemi) tabanlı Sözde Rastgele Sayı Üreteci.
    
    
    - Sayı çift ise: x / 2
    - Sayı tek ise: 3x + 1
    """

    def __init__(self, seed=None):
        """
        Başlangıç tohumu (seed) belirlenir.
        """
        if seed is None:
            # Zamanı tohum olarak al (Sıfır olmamasını garanti et)
            self.state = int(time.time_ns())
            if self.state == 0: self.state = 12345
        else:
            self.state = seed

    def next_collatz(self):
        
        if self.state % 2 == 0:
            # Sayı Çiftse: İkiye böl
            self.state = self.state // 2
        else:
            # Sayı Tekse: 3 ile çarp 1 ekle
            self.state = 3 * self.state + 1
        
        # Collatz dizisi 1'e ulaştığında döngüye girer (4-2-1).
        # Rastgeleliği sürdürmek için eğer 1 olursa state'i yeniden tohumluyoruz
        # veya büyük bir sayıyla modifiye ediyoruz.
        if self.state == 1:
            self.state = int(time.time_ns()) & 0xFFFFFFFF # Yeniden karıştır
            
        return self.state

    def randint(self, min_val, max_val):
        """
        Üretilen Collatz sayısını istenilen aralığa (min-max) sıkıştırır.
        """
        ham_sayi = self.next_collatz()
        return min_val + (ham_sayi % (max_val - min_val + 1))

# --- ÖRNEK KULLANIM ---
if __name__ == "__main__":
    rng = CollatzRNG()
    
    print(f"Başlangıç Tohumu (Seed): {rng.state}")
    print("--- Collatz Mantığıyla 300 Sayı Üretimi (İlk 10'u) ---")
    
    # Hoca tahtada 300 RSÜ demiş, 300 tane üretilebilir.
    liste = []
    for _ in range(300):
        sayi = rng.randint(0, 100)
        liste.append(sayi)
    
    # İlk 10 tanesini yazdıralım
    print(liste[:10])
    print("...")
