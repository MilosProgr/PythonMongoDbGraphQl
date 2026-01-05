import pytest
import asyncio
loop: asyncio.AbstractEventLoop

from app.service import create_user


@pytest.mark.asyncio(loop_scope="module")
async def test_create_user():
    
    global loop

    user = await create_user({
        "email": "email@gmail.com",
        "name": "Marko",
        "age": 25
    })

    assert user["name"] == "Marko" is loop