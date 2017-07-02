/*
Autor: Joan Soler-Adillon (www.joan.cat)
 Tutorial de Processing. Números aleatoris. 
 */

float posX, posY, velX, velY;
int sz = 20;

void setup(){
  size(300,200);
  posX = width/2;
  posY = height/2;
  velX = random(1,10);
  velY = random(1,10);
}

void draw(){
  background(0);

  //actualitzem posicions
  posX = posX+velX;
  posY = posY+velY;

  //dibuixem
  ellipse(posX,posY,sz,sz);

  //comprovem posició X
  if((posX<0)||(posX>width)){
    velX = -velX;
  } 
  //comprovem posició Y
  if((posY<0)||(posY>height)){
    velY = -velY;
  } 
}

void mousePressed(){
    posX = mouseX;
  posY = mouseY;
  velX = random(1,10);
  velY = random(1,10);
}

