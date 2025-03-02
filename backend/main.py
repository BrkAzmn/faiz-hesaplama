from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from calculator import calculate_compound_interest
from fetch_prices import get_gold_price, get_silver_price

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "API çalışıyor!"}

@app.get("/calculate_interest")
def interest(principal: float, rate: float, years: int, compound_frequency: int = 1):
    result = calculate_compound_interest(principal, rate, years, compound_frequency)
    return {"future_value": result}

@app.get("/compare_investment")
def compare(year: int, investment: float):
    gold_return = get_gold_price(year, investment)
    silver_return = get_silver_price(year, investment)
    
    best_investment = "Altın" if gold_return > silver_return else "Gümüş"
    
    return {
        "gold_return": gold_return,
        "silver_return": silver_return,
        "best_investment": best_investment
    }
