void setup(){
  size(300,300);
  frameRate(30);
  smooth();
  fill(255,32);
  noStroke();
}

void draw(){
  background(255,0,0);
  
for(int i=0; i<width; i+=4){
     float tamano = random (i);
    ellipse(i,i,tamano,tamano);
  }
}

