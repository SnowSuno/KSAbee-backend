# This is a dummy api reference for frontend testing

from typing import Optional

from fastapi import FastAPI

app = FastAPI()


# DUMMY_DB = [
#     {
#         'studentId': '19-006',
#         'name': '권순호',
#     },
#     {
#         'studentId': '19-079',
#         'name': '이지원',
#         'data': {
#             'nickname': '마리마리 착마리',
#             'summonerId': '',
#             'tier': 'Bronze 1',
#
#         }
#     },  # Registerd students
#     {
#         'studentId': '19-000',
#         'name': '홍길동',
#     }  # Unregistered student
# ]

dummy_data = [
    {
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
        'studentID': "19-006",
        'studentName': "권순호",
        'nickName': "침대에서 뒹굴",
        'level': 50,
        'profileImg': 'https://opgg-static.akamaized.net/images/profile_icons/profileIcon4903.jpg?image=q_auto:best&v=1518361200',
        'position': 'mid',
        'tier': "Challenger",
        'tierInfo': {
            'leaguePoints': 99,
            'wins': 100,
            'losses': 100,
            'winRate': 50
        }
    }
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
