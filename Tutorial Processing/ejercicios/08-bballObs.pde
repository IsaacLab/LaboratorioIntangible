/*
UPF :: IUA-IDEC
 Màster d'Arts Digitals
 joan soler-adillon (www.joan.cat)
 
 
 El condicional nos permite hacer rebotar la pelota
 en los ejes X e Y
 Random() hace que cada vez las velocidades X e Y sean distintas
 */

float posX, posY, velX, velY;
int sz = 25;
int obstacleX, obstacleY;


void setup(){
  size(300,200);
  posX = width/2;
  posY = height/2;
  velX = random(1,10);
  velY = random(1,10);
  fill(255,255,192);
  smooth();
  stroke(255,192,192);
}

void draw(){
  background(0);

  //actualitzamos las posiciones
  posX = posX+velX;
  posY = posY+velY;

  //dibujamos
  ellipse(posX,posY,sz,sz);

  //comprobamos la posición X
  if((posX<0)||(posX>width)){
    velX = -velX;
  } 
  //comprobamos la posición Y
  if((posY<0)||(posY>height)){
    velY = -velY;
  } 

  //actulizamos obstáculo, según el mouse:
  obstacleX = mouseX;
  obstacleY = mouseY;
  
  //dibujamos obstaculo:
  line(obstacleX,0,obstacleX,height);
  //COMPROBAMOS OBSTÁCULO:
  if(abs(posX-obstacleX) < sz/2){
    velX = -velX;
  }
}


