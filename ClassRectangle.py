class Rectangle:
    def __init__(self, length: float, width: float):
        # Validasi input tidak boleh 0 atau negatif
        if length <= 0 or width <= 0:
            raise ValueError("Panjang dan lebar harus lebih besar dari 0.")
        self.length = length
        self.width = width

    def calculate_circumference(self) -> float:
        """Menghitung keliling persegi panjang."""
        return 2 * (self.length + self.width)    

    def calculate_area(self) -> float:
        """Menghitung luas persegi panjang."""
        return self.length * self.width

    def __str__(self) -> str:
        """Mengembalikan representasi string dari objek."""
        return f"rectangle, {self.length} cm long, and {self.width} cm wide"


 # --- Menjalankan dan Menguji Kelas Rectangle ---
if __name__ == "__main__":
    try:
        # Membuat objek Rectangle
        rect = Rectangle(length=3, width=2)