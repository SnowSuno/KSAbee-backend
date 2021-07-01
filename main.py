# This is a dummy api reference for frontend testing

from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    'http://ksabee.netlify.app',
    'https://ksabee.netlify.app',
    'http://localhost',
    'http://localhost:3000',
    'http://localhost:3001',
    'http://localhost:3002',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

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
        'level': 58,
        'profileImg': 'https://opgg-static.akamaized.net/images/profile_icons/profileIcon1394.jpg?image=q_auto:best&v=1518361200',
        'position': 'bottom',
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
        'level': 40,
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
        'level': 60,
        'profileImg': 'https://opgg-static.akamaized.net/images/profile_icons/profileIcon4903.jpg?image=q_auto:best&v=1518361200',
        'position': 'jungle',
        'tier': "Gold 4",
        'tierInfo': {
            'leaguePoints': 40,
            'wins': 10,
            'losses': 0,
            'winRate': 100
        }
    },
    {
        'index': 4,
        'studentID': "20-002",
        'studentName': "누군가",
        'nickName': "동명이인 테스트",
        'level': 100,
        'profileImg': 'https://opgg-static.akamaized.net/images/profile_icons/profileIcon4903.jpg?image=q_auto:best&v=1518361200',
        'position': 'mid',
        'tier': "Silver 3",
        'tierInfo': {
            'leaguePoints': 20,
            'wins': 5,
            'losses': 10,
            'winRate': 33
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
