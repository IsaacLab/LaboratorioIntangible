/*
UPF-IUA
 Máster d'Arts Digitals
 joan soler-adillon (www.joan.cat)
 
 Pelotitas de colores!
 */

int sz = 9;
int numeroBolas = 200;

//creamos un array de posicionesX con "numeroBolas" elementos:
int[] posicionesX = new int[numeroBolas];
//y creamos un array de posicionesY:
int[] posicionesY = new int[numeroBolas];
//creamos un array de velocidadesX con "numeroBolas" elementos:
float[] velocidadesX = new float[numeroBolas];
//y creamos un array de velocidadesY:
float[] velocidadesY = new float[numeroBolas];

void setup(){
  size(300,200);
  frameRate(30);
  //inicializamos las posiciones y velocidades:
  for(int i = 0; i<numeroBolas; i++){
    posicionesX[i] = int(random(width));
    posicionesY[i] = int(random(height));
    velocidadesX[i] = random(2,10);
    velocidadesY[i] = random(2,10);
  }
  noStroke();
}

void draw(){
  //background(0);
  colorMode(RGB,255);
  fill(255,25);
  rect(0,0,width,height);


  //actualitzamos las posiciones
  for(int i = 0; i<numeroBolas; i++){
    posicionesX[i] += velocidadesX[i];
    posicionesY[i] += velocidadesY[i];


    //comprobamos las posiciones X
    if((posicionesX[i]<0)||(posicionesX[i]>width)){
      velocidadesX[i] = -velocidadesX[i];
    } 
    //comprobamos las posiciones Y
    if((posicionesY[i]<0)||(posicionesY[i]>height)){
      velocidadesY[i] = -velocidadesY[i];
    } 
  }


  //dibujamos las elipses:
  for(int i = 0; i<numeroBolas; i++){
    colorMode(HSB,numeroBolas);
    fill(i,i,i);
    ellipse(posicionesX[i],posicionesY[i],sz,sz);
  }
}

void mousePressed(){
  //reinicializamos las velocidades:
  for(int i = 0; i<numeroBolas; i++){
    velocidadesX[i] = random(2,10);
    velocidadesY[i] = random(2,10);
  }
}


