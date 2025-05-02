from abc import ABC, abstractmethod

class Hewan(ABC): 
    @abstractmethod
    def describe(self):
        pass

class Herbivora(Hewan):
    def describe(self):
        return "merupakan Hewan pemakan tumbuh-tumbuhan atau Herbivora."

class Karnivora(Hewan):
    def describe(self):
        return "merupakan Hewan pemakan daging atau Karnivora."

class Omnivora(Hewan):
    def describe(self):
        return "merupakan Hewan pemakan segalanya atau Omnivora."

class Factory:
    @staticmethod
    def buat_hewan(jenis_hewan):
        if jenis_hewan == "Sapi":
            return Herbivora()
        elif jenis_hewan == "Singa":
            return Karnivora()
        elif jenis_hewan == "Beruang":
            return Omnivora()
        else:
            raise ValueError("Jenis hewan tidak dikenal")
        
jenis_hewan = input("Hewan apa yang ingin anda masukkan? [Sapi, Singa, Beruang]")
hewan = Factory.buat_hewan(jenis_hewan)
print(f"Hewan {hewan.__class__.__name__} ")
print("Jenis mempunyai deskripsi:")
print(hewan.describe())