objects = [];
status="";
video="";

function perload(){
    video = createVideo('video.mp4');
    video.hide();
}

function setup(){
    canvas= createCanvas(480,380);
    canvas.center();
}


function start(){
    ObjectDetector= ml5.objectDetector('cocossd',modelLoaded);
    document.getElementById("status").innerHTML="Status Loading: Detecting Objects";
}

function modelLoaded(){
    console.log('modelLoaded');
    status=true;
    video.loop();
    video.speed(1);
    video.volume(0);
}

function draw(){
    image(video ,0 ,0 ,480 ,380);
    if(status != "")
    {
    objectDetector.detect(video, gotResults());
    
    console.log(results);
    for (i = 0; i < object.length; i++) {
        document.getElementById("status").innerHTML = "Status : Objects Detected";
        document.getElementById("number_of_objects").innerHTML = "Number of objects detected are : " + object.length;
        
        fill("red");
        percent =floor(objects[i].confidence * 100);
        text(objects[i].label + "" + percent + "%", objects[i].x + 15, objects[i].y + 15);
        noFill();
        stroke("red");
        rect(objects[i].x, objects[i].y, objects[i].width, objects[i].height);
    }
    }
}