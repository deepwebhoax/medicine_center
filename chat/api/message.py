from fastapi import WebSocket



@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        
        await websocket.send_text(f"Message text was: {data}")











async def send_message



async def get_messages(sender, doctor_id, patient_id)
    """
    """


    return messages