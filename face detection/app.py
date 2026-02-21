from flask import Flask,render_template,Response
import cv2
app=Flask(__name__)

face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

camera=cv2.VideoCapture(0)

def generate_frames():
  while True:
    success,frame=camera.read()
    if not success:
        break
    else:
        #conver to gray scale
        gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #detect faces
        faces=face_cascade.detectMultiScale(gray,1.3,5)

        #Draw rectangles around faces
        for(x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        
        #encode frame as jpeg
        ret,buffer=cv2.imencode('.jpg',frame)
        frame=buffer.tobytes()

        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')





@app.route('/')
def base():
    return render_template('index.html')

@app.route('/video')
def video():
   return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=='__main__':
    app.run(debug=True)
