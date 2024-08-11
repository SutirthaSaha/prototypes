from flask import Flask, Response, render_template
import time

app = Flask(__name__)


@app.route('/')
def index():
    # Render the index.html template
    return render_template('index.html')


@app.route('/events')
def stream():
    def event_stream():
        while True:
            # Send a message event every second
            yield f"data: Server time is {time.ctime()}\n\n"
            time.sleep(1)

            # Return a response with the appropriate headers for SSE

    return Response(event_stream(), content_type='text/event-stream')


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
