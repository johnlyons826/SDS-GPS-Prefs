from RoomSearch.SelectRooms import pickRooms

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def pick_rooms():
    if not request.is_json:
        # Error
        pass
    else:
        req_dict = request.get_json()
        print(f'{req_dict}')
        user_ids = req_dict['users']
        start_time = req_dict['start']

        room_scores = pickRooms(user_ids, start_time)

        return jsonify(room_scores)

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)
