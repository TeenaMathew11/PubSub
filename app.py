from flask import Flask, jsonify, request

app = Flask(__name__)

# topics available
topics = [
    {
        'name': 'Python',
        'note': ['Python is an interpreted high-level programming language for general-purpose programming.']
    },
    {
        'name': 'Java',
        'note': ['Java is a general-purpose computer-programming language.']
    }
]

# topics subscribed by the subscriber
sub_topics = []

# topics registered by the publisher
pub_topics = []

#Register/Unregister a subscriber to a topic - can be a string
@app.route('/topics/subscriber/<string:name>')
def reg_sub_topic(name):
    for topic in topics:
        if topic['name'] == name:
            if name in sub_topics:
                return jsonify({'message': 'Already subscribing to topic'})
            else:
                sub_topics.append(name)
                return jsonify({'message': 'Subscribed'})
    return jsonify({'message': 'Topic not found'})

#Register/Unregister a publisher to a topic
@app.route('/topics/publisher/<string:name>')
def reg_pub_topic(name):
    for topic in topics:
        if topic['name'] == name:
            if name in pub_topics:
                return jsonify({'message': 'Already registered for topic'})
            else:
                pub_topics.append(name)
                return jsonify({'message': 'Registered'})
    return jsonify({'message': 'Topic not found'})

#Publish a note to a topic
@app.route('/topics/publish/<string:name>', methods=['POST'])
def add_note_to_topic(name):
    request_topic = request.get_json()
    for topic in topics:
        if topic['name'] == name:
            if name in pub_topics:
                topic['note'].append(request_topic['note'])
                return jsonify(topic)
            else:
                return jsonify({'message': 'Not registered for topic'})
    return jsonify({'message': 'Topic not found'})

#Receive a published note as a subscriber
@app.route('/topics/subscribe/<string:name>')
def get_subcribe_topic(name):
    for topic in topics:
        if topic['name'] == name:
            if name in sub_topics:
                return jsonify(topic)
            else:
                return jsonify({'message': 'Not subscribing to topic'})
    return jsonify({'message': 'Topic not found'})

#Show all topics
@app.route('/topics')
def get_topics():
    return jsonify({'topics': topics})

app.run(port=5000)
