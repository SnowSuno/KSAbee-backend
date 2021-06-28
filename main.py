# This is a dummy api reference for frontend testing

from typing import Optional

from fastapi import FastAPI

app = FastAPI()



dummy_data = [
    {
        'index': 1,
        'studentID': "19-079",
        'studentName': "이지원",
        'nickName': "마리마리착마리",
        'level': 50,
        'profileImg': 'https://opgg-static.akamaized.net/images/profile_icons/profileIcon4903.jpg?image=q_auto:best&v=1518361200',
        'position': 'top',
        'tier': "Bronze 1",
        'tierInfo': {
            'leaguePoints': 20,
            'wins': 15,
            'losses': 20,
            'winRate': 43
        }
    },
    {
        'index': 0,
        'studentID': "19-006",
        'studentName': "권순호",
        'nickName': "침대에서 뒹굴",
        'level': 50,
        'profileImg': 'https://opgg-static.akamaized.net/images/profile_icons/profileIcon4903.jpg?image=q_auto:best&v=1518361200',
        'position': 'adc',
        'tier': "Challenger",
        'tierInfo': {
            'leaguePoints': 99,
            'wins': 100,
            'losses': 100,
            'winRate': 50
        }
    },
    {
        'index': 2,
        'studentID': "19-001",
        'studentName': "강라엘",
        'nickName': "리듬타지마",
        'level': 50,
        'profileImg': 'https://opgg-static.akamaized.net/images/profile_icons/profileIcon4903.jpg?image=q_auto:best&v=1518361200',
        'position': 'mid',
        'tier': "Unranked",
        'tierInfo': {
            'leaguePoints': 0,
            'wins': 0,
            'losses': 0,
            'winRate': 0
        }
    },
    {
        'index': 3,
        'studentID': "20-001",
        'studentName': "누군가",
        'nickName': "나롤개잘함",
        'level': 50,
        'profileImg': 'https://opgg-static.akamaized.net/images/profile_icons/profileIcon4903.jpg?image=q_auto:best&v=1518361200',
        'position': 'mid',
        'tier': "Iron 4",
        'tierInfo': {
            'leaguePoints': 2,
            'wins': 0,
            'losses': 10,
            'winRate': 0
        }
    },
    {
        'index': 4,
        'studentID': "21-001",
        'studentName': "누군가",
        'nickName': "동명이인 테스트",
        'level': 50,
        'profileImg': 'https://opgg-static.akamaized.net/images/profile_icons/profileIcon4903.jpg?image=q_auto:best&v=1518361200',
        'position': 'mid',
        'tier': "Iron 4",
        'tierInfo': {
            'leaguePoints': 2,
            'wins': 0,
            'losses': 9,
            'winRate': 0
        }
    },
]



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get('/users')
def get_all_users():
    return dummy_data

# @app.get('/user')
# def get_user(**kwargs):
#     params = {'studentId', 'name', 'nickname'}
#     if not params.intersection(set(kwargs.keys())):
#         return  # KeyError
#
# @app.get('/register')
# def register_user(name: str, studentId: str, pw: int):
#     return {'name': name, 'sid': studentId, 'pw': pw}
#
#
#
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}
