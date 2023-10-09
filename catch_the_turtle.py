import turtle
import random


def calculate_grade(score):  # Verilen skora göre bir not ve mesaj döndürür.
    if score >= 50:
        return "A+", "You're a legend now. Congratulations! :))"
    elif score >= 45:
        return "A", "You did great. Are you up for another fight to become a legend?"
    elif score >= 30:
        return "B", "The highest score is waiting for you. You should be faster."
    elif score >= 15:
        return "C", "You can do better. Try harder."
    elif score > 0:
        return "D", "Try a bit more. There's still hope."
    else:
        return "F", "don't stop continue"


def setup_display(display, x_pos, align):  # Bir metin göstermek için kullanılacak kaplumbağa nesnesinin
    # görünümünü ayarlamak için kullanılır.
    display.hideturtle()  # hideturtle() ile kaplumbağa görünmez hale getiriliyor.
    display.penup()  # penup() ile kalem kaldırılıyor.
    display.goto(x_pos, 250)  # goto(x_pos, 250) ile konumu belirleniyor.
    display.write("", align=align, font=("Arial", 16, "normal"))  # write("", align=align, font=("Arial", 16,
    # "normal")) ile başlangıç metni, hizalama ve font ayarlanıyor.


class TurtleGame:
    def __init__(self, time_limit):
        self.screen = turtle.Screen()  # turtle.Screen() ile bir ekran oluşturuluyor
        self.screen.title("Catch The Turtle")  # başlık "Turtle Catcher Game" olarak ayarlanıyor.

        self.score = 0
        self.time_limit = time_limit
        self.game_over = False

        self.turtle = turtle.Turtle()  # turtle.Turtle() ile bir kaplumbağa nesnesi oluşturuluyor
        self.turtle.shape("turtle")  # sekli "turtle"
        self.turtle.color("green")  # rengi "green"
        self.turtle.penup()  # Kaplumbağa'nın kalemini kaldırmak için penup() kullanılıyor
        self.create_turtle()  # create_turtle metodu çağrılarak rastgele bir konuma yerleştiriliyor.

        self.score_display = turtle.Turtle()  # score icin metin olusturur
        setup_display(self.score_display, -150, "left")  # metnin gorunumlerini ayarlar

        self.time_display = turtle.Turtle()  # zaman icin metin olusturur
        setup_display(self.time_display, 150, "right")  # metnin gorunumlerini ayarlar

        self.screen.onclick(self.click_event)  # Fare tıklama olayını yakalamak için screen.onclick(self.click_event)
        # kullanilir

        self.update()  # update metodu çağrılarak oyunun zaman içinde güncellenmesi sağlanıyor.

    def create_turtle(self):  # Rastgele bir konuma gitmeye çalışırken Terminator hatası oluşursa, ekranın
        # kapatılmadığı kontrol ediliyor. Eğer kapatılmamışsa yeni bir kaplumbağa oluşturuluyor.
        try:
            x = random.randint(-190, 190)
            y = random.randint(-190, 190)
            self.turtle.goto(x, y)
        except turtle.Terminator:
            if not self.screen.bye():
                # Eğer ekran kapatılmamışsa, yeni bir kaplumbağa oluştur
                self.create_turtle()

    def click_event(self, x, y):  # Fare tıklamasını yakalar.
        if self.is_inside_turtle(x, y):
            self.score += 1
            self.update_score_display()
            self.create_turtle()
            # Eğer tıklanan yer kaplumbağa içindeyse, skoru artırır, ekrandaki skor göstergesini günceller ve yeni bir
            # kaplumbağa oluşturur.
            grade, _ = calculate_grade(self.score)  # puanlama sistemini uygular ve bir mesajı ekrana yazdırır.
            print(f"Congratulations! the turtle {self.score} you caught it . your note: {grade}")
        else:
            print("Oh No! You couldn't catch me. :(")

    def is_inside_turtle(self, x, y):  # Verilen koordinatların kaplumbağa içinde olup olmadığını kontrol eder.
        turtle_x, turtle_y = self.turtle.position()
        return abs(x - turtle_x) < 20 and abs(y - turtle_y) < 20

    def update(self):  # Oyunun süresi bitene kadar (time_limit > 0) sürekli olarak kendisini çağırır
        if not self.game_over:
            if self.time_limit > 0:
                self.time_limit -= 1  # Her çağrıda zaman limitini azaltır ve güncellenmiş zaman göstergesini ekrana
                # yazar.
                self.update_time_display()
                self.screen.ontimer(self.update, 1000)
            else:
                if not self.game_over:  # Kontrol bayrağı ekleniyor
                    self.show_final_message()
                    self.game_over = True  # Bayrağı işaretle

    def update_score_display(self):  # skor gostergesini duzenler
        self.score_display.clear()
        self.score_display.write(f"Score: {self.score}", align="left", font=("Arial", 16, "normal"))

    def update_time_display(self):  # zaman gostergesini duzenler
        self.time_display.clear()
        self.time_display.write(f"Time Left: {self.time_limit}", align="right", font=("Arial", 16, "normal"))

    def show_final_message(self):  # Oyun bittiğinde çağrılır.
        final_grade, final_comment = calculate_grade(self.score)
        final_message = f"Game over! Your total score: {self.score}. Your note: {final_grade}. {final_comment}"
        turtle.clear()
        turtle.write(final_message, align="center", font=("Arial", 18, "normal"))

        # Son notu ve mesajı ekrana yazdırır.


if __name__ == "__main__":
    game = TurtleGame(time_limit=30)  # oyunun süresini belirler.
    turtle.done()  # turtle.done() ise turtle modülünün pencerenin kapanmasını engeller. Bu, oyunun süresi dolduktan
    # sonra ekrandaki mesajın görünmesini sağlar ve kullanıcının pencereyi elle kapatmasına kadar bekler.
