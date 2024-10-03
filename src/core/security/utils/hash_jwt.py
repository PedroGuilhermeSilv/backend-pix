import os
from datetime import datetime, timedelta

import jwt
from dotenv import load_dotenv
from zoneinfo import ZoneInfo

load_dotenv()


def create_jwt(payload: dict[str], expires_in: int) -> dict:
    timezone = ZoneInfo("America/Sao_Paulo")
    payload["exp"] = datetime.now(tz=timezone) + timedelta(minutes=expires_in)
    return jwt.encode(
        payload=payload,
        key=os.getenv("SECRET_KEY"),
        algorithm=os.getenv("ALGORITHM"),
    )


def decode_jwt(token: str) -> dict | None:
    timezone = ZoneInfo("America/Sao_Paulo")
    decoded = jwt.decode(
        jwt=token,
        key=os.getenv("SECRET_KEY"),
        algorithms=[os.getenv("ALGORITHM")],
    )
    if decoded.get("email") is None:
        return None

    current_time = datetime.now(tz=timezone)

    exp_time = datetime.fromtimestamp(decoded["exp"], tz=timezone)

    minutes = (exp_time - current_time).total_seconds() / 60

    decoded["exp"] = round(minutes)

    if minutes < 0:
        return None

    return decoded

def refresh_jwt(token: str) -> dict | None:
    timezone = ZoneInfo("America/Sao_Paulo")
    decoded = jwt.decode(
        jwt=token,
        key=os.getenv("SECRET_KEY"),
        algorithms=[os.getenv("ALGORITHM")],
    )
    if decoded.get("email") is None:
        return None

    current_time = datetime.now(tz=timezone)

    exp_time = datetime.fromtimestamp(decoded["exp"], tz=timezone)

    minutes = (exp_time - current_time).total_seconds() / 60

    decoded["exp"] = round(minutes)

    if minutes < 0:
        return None

    payload = {"email": decoded["email"]}
    new_token = create_jwt(payload, 60)

    return {"token": new_token, "exp": 60}
