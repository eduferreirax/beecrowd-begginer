a = str(input())
b = str(input())
c = str(input())

animais = {
          
          ("vertebrado", "ave", "carnivoro" ): "aguia",
          ("vertebrado", "ave", "onivoro"): "pomba" ,
          ("vertebrado", "mamifero", "onivoro"): "homem",
          ("vertebrado", "mamifero", "herbivoro"): "vaca",
          ("invertebrado", "inseto", "hematofago"): "pulga",
          ("invertebrado", "inseto", "herbivoro"): "lagarta",
          ("invertebrado", "anelideo", "hematofago"): "sanguessuga",
          ("invertebrado", "anelideo", "onivoro"): "minhoca",
          
          }
          
          
print(animais[a,b,c])