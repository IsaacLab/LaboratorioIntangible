/*
UPF-IUA
 Màster d'Arts Digitals
 joan soler-adillon (www.joan.cat)
 
 Follow me!
 */
float xPos, xVel;
float yPos, yVel;
float sz = 20;

void setup(){
  size(300,200);
  xPos = width/2;
  yPos = height/2;
  xVel = 40;
  yVel = 40;
  smooth();
  noStroke();
}

void draw(){
  //fondo con alfa
  fill(255,255,0,2);
  rect(0,0,width,height);

  actualizar();
  dibujar();
}

void actualizar(){
  //calculamos la distáncia entre el mouse y la bola en los 2 ejes
  float distanceX = mouseX-xPos;
  float distanceY = mouseY-yPos;
  //ho imprimim així que és maco:
  //println("dx: "+distanceX+" dy: "+distanceY);

  //y actualizamos la posición de manera que la bola no acabe de llegar nunca...
  xPos += distanceX/xVel;
  yPos += distanceY/yVel;
//  println("xp: "+xPos+" yp: "+yPos);
}

void dibujar(){
  fill(0,16);
  ellipse(xPos,yPos,sz,sz);
}

