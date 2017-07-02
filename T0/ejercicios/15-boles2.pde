void setup(){
  size(200,200);
  frameRate(1);
}

void draw(){
  background(255,0,0);
  
for(int i=0; i<100; i++){
    float posX = random(width);
    float posY = random(height);
    float tamano = random (60);
    ellipse(posX,posY,tamano,tamano);
  }
}

