from fastapi import FastAPI
from pydantic import BaseModel

from diet import kalori_hesapla, bmi_hesapla, bmi_durumu, makro_stratejisi

app = FastAPI()


class ProfileRequest(BaseModel):
    cinsiyet: str
    kilo: float
    boy: float
    yas: int
    aktivite: str
    hedef: str


@app.get("/")
def home():
    return {
        "message": "AI Diyet Asistanı API çalışıyor"
    }


@app.post("/calculate")
def calculate_profile(data: ProfileRequest):
    bmi = bmi_hesapla(data.kilo, data.boy)
    durum = bmi_durumu(bmi)

    kalori = kalori_hesapla(
        data.cinsiyet,
        data.kilo,
        data.boy,
        data.yas,
        data.aktivite,
        data.hedef
    )

    makro = makro_stratejisi(data.hedef)

    return {
        "bmi": bmi,
        "bmi_durumu": durum,
        "kalori": kalori,
        "makro": makro
    }