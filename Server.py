from flask import Flask, request, jsonify
import pusher

app = Flask(__name__)

pusher_client = pusher.Pusher(
  app_id='1999240',
  key='77cff9cdb8c9ef87672d',
  secret='0561a90f80bde7d80dfc',
  cluster='eu',
  ssl=True
)

shared_data = {}

@app.route('/sendData', methods=['POST'])
def send_data():
    data = request.json
    player_id = data.get('playerId')
    print(f"Received data for playerId={player_id}: {data}")

    shared_data[player_id] = data  # store whole data

    pusher_client.trigger('my-channel', 'my-event', data)
    return jsonify({'status': 'success'})


@app.route('/getData', methods=['GET'])
def get_data():
    player_id = request.args.get('playerId')
    data = shared_data.get(player_id)
    print(f"GET data for playerId={player_id}: {data}")
    return jsonify(data or {})



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)

