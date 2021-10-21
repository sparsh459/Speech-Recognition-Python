from flask import Flask, render_template, request, redirect
import speech_recognition as sr  # used for analyzing teh audio file we have uploaded
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    transcript = ""
    if request.method == "POST":
        print("Form Data Recieved")
    # what if someone pings my website with post request with no file info whatsoever
        if "file" not in request.files:
            return redirect(request.url)
    # accessing the file uploaded on website, if a file exist it will give me the file
        file = request.files["file"]
    # what if someone submits a blank file
        if file.filename == "":
            return redirect(request.url)
    # analzying the audio file uploaded
        if file:
            # this will initialize the speech instance of our class
            recognizer = sr.Recognizer()
            # creating an audiofile object the file that was intially created
            audiofile = sr.AudioFile(file)
            # opening up this audio file and reading it through recognizer
            with audiofile as source:
                # passing teh audiofile abouve created in to teh recognizer module
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, key=None)

    # reson why we don't have to specify template/index.html is cause flsak automatically understands to look in
    # templates when rendring template
    return render_template('index.html', transcript=transcript)


if __name__ == '__main__':
    # debug allows us t control S this file and flask instance will refresh with latest update
    # threaded is true because when we're dealing with file upload we want to have some threaded bases so that our
    # computer doesn't overload and handle multiple request overtime
    app.run(debug=True, threaded=True)
