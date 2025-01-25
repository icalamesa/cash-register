from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.post("/cart/add")
def add_to_cart(item: int, quantity: int):
    try:
        # add to cart logic
        return {"message": f"Added {quantity} of {item} to the cart"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    