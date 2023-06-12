from plyer import notification
import time

def bildirim_goster():
    notification.notify(
        title="Su İçme Zamanı!",
        message="Lütfen bir bardak su için.",
        timeout=10
    )

# Kullanıcıdan bildirim süresini dakika cinsinden alın
bekleme_suresi = int(input("Bildirim süresini dakika cinsinden girin: ")) * 60

while True:
    bildirim_goster()
    time.sleep(bekleme_suresi)
