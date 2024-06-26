from flask import Flask, request, jsonify, render_template
from youtube_transcript_api import YouTubeTranscriptApi

# Dummy function TRANS.get_transcript
def get_transcript(id, preserve_formatting=True):
    # Dummy data
    result = YouTubeTranscriptApi.get_transcript(id, languages=['hi', 'en', 'de'])
    # result = YouTubeTranscriptApi.list_transcripts(id)
    
    return result

app = Flask(__name__)

@app.route('/')
def extract_id_and_get_transcript():
    # Extract the 'id' parameter from the query string
    id_value = request.args.get('id')

    if id_value:
        # Call TRANS.get_transcript function to get the transcript
        result = get_transcript(id_value, preserve_formatting=True)
        return render_template('index.html', json_data=result)
        # Convert the transcript to JSON format
        # return jsonify(result)

        
    
    else:
        return "Error: 'id' parameter not found in URL", 400

if __name__ == "__main__":
    app.run(debug=True)














# from flask import Flask, render_template_string, jsonify
# from youtube_transcript_api import YouTubeTranscriptApi
# from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

# app = Flask(__name__)

# # HTML template to display the results
# HTML_TEMPLATE = """
# <!DOCTYPE html>
# <html>
# <head>
#     <title>YouTube Transcript API</title>
# </head>
# <body>
#     {% if transcript %}
#         <h2>Transcript for Video ID: {{ video_id }}</h2>
#         <pre>{{ transcript|safe }}</pre>
#     {% else %}
#         <p>Error: {{ error }}</p>
#     {% endif %}
# </body>
# </html>
# """

# @app.route('/<video_id>', methods=['GET'])
# def get_transcript(video_id):
#     try:
#         transcript = YouTubeTranscriptApi.get_transcript(video_id)
#         # Convert the transcript list to pretty JSON format
#         pretty_transcript = jsonify(transcript).json
#         return render_template_string(HTML_TEMPLATE, transcript=pretty_transcript, video_id=video_id)
#     except (TranscriptsDisabled, NoTranscriptFound) as e:
#         return render_template_string(HTML_TEMPLATE, error=str(e), video_id=video_id)

# if __name__ == '__main__':
#     app.run(debug=True)
