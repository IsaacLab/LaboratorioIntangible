/*
 MUAD-UPF
 Máster d'Arts Digitals
 
 La cuadratura del círculo: el rebicho rebota!
 
 Más limpito.
 */
int posX, posY, velX, velY;

void setup(){
  size(250,150);
  frameRate(30);
  rectMode(CENTER);
  //smooth();
  posX = width/2;
  posY = height/2;
  velX = 2;
  velY = 2;
}

void draw(){
  dibujaFondo();

  actualiza();
  compruebaBordes();
  dibujaReBicho();
}
  
void compruebaBordes(){
  //comprobamos la posición X
  if((posX<0)||(posX>width)){
    velX = -velX;
  } 
  //comprobamos la posición Y
  if((posY<0)||(posY>height)){
    velY = -velY;
  } 
}


void dibujaFondo(){
   //background(255,127,127);
 noStroke();
 fill(255,127,0,32);
 rect(width/2,height/2,width,height);
 }

void actualiza(){
  //actualitzamos las posiciones
  posX = posX+velX;
  posY = posY+velY;
}


void dibujaReBicho(){
  //una función también pué tener sus variablecillas:
  int tamanoCuerpoX=24;
  int tamanoCuerpoY=40;
  int largoPatas=tamanoCuerpoY;
  int separacionPatas = tamanoCuerpoY/5;
  int diametroPies=4;
  int diametroOjos=6;
  int diametroPupilas=2;
  int separacionOjos=10;
  //colores
  fill(127,127,255);
  stroke(127,255,127);
  //patas
  line(posX-largoPatas/2,posY-separacionPatas*2,posX+largoPatas/2,posY-separacionPatas*2);
  line(posX-largoPatas/2,posY-separacionPatas,posX+largoPatas/2,posY-separacionPatas);
  line(posX-largoPatas/2,posY,posX+largoPatas/2,posY);
  line(posX-largoPatas/2,posY+separacionPatas,posX+largoPatas/2,posY+separacionPatas);
  line(posX-largoPatas/2,posY+separacionPatas*2,posX+largoPatas/2,posY+separacionPatas*2);
  //cuerpo
  rect(posX,posY,tamanoCuerpoX,tamanoCuerpoY);
  //pies
  ellipse(posX-largoPatas/2,posY-separacionPatas*2,diametroPies,diametroPies);
  ellipse(posX+largoPatas/2,posY-separacionPatas*2,diametroPies,diametroPies);
  ellipse(posX-largoPatas/2,posY-separacionPatas,diametroPies,diametroPies);
  ellipse(posX+largoPatas/2,posY-separacionPatas,diametroPies,diametroPies);
  ellipse(posX-largoPatas/2,posY,diametroPies,diametroPies);
  ellipse(posX+largoPatas/2,posY,diametroPies,diametroPies);
  ellipse(posX-largoPatas/2,posY+separacionPatas,diametroPies,diametroPies);
  ellipse(posX+largoPatas/2,posY+separacionPatas,diametroPies,diametroPies);
  ellipse(posX-largoPatas/2,posY+separacionPatas*2,diametroPies,diametroPies);
  ellipse(posX+largoPatas/2,posY+separacionPatas*2,diametroPies,diametroPies);
  //ojos
  stroke(0);
  fill(255);
  ellipse(posX-separacionOjos/2,posY-tamanoCuerpoY/2,diametroOjos,diametroOjos);
  ellipse(posX+separacionOjos/2,posY-tamanoCuerpoY/2,diametroOjos,diametroOjos);
  fill(0);
  ellipse(posX-separacionOjos/2,posY-tamanoCuerpoY/2,diametroPupilas,diametroPupilas);
  ellipse(posX+separacionOjos/2,posY-tamanoCuerpoY/2,diametroPupilas,diametroPupilas);
}

