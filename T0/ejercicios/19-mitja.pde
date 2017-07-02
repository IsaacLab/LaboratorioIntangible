/*
 MUAD - UPF
 MÃ ster d'Arts Digitals
 joan soler-adillon (www.joan.cat)
 
 Con un array, podemos tener las pelotitas que querramos,
 sÃ¯Â¿Â½lo hay que cambiar el valor de numeroBolas
 */

int sz = 15;
int numeroBolas = 4;

//creamos un array de posicionesX con "numeroBolas" elementos:
float[] posicionesX = new float[numeroBolas];
//y creamos un array de posicionesY:
float[] posicionesY = new float[numeroBolas];
//creamos un array de velocidadesX con "numeroBolas" elementos:
float[] velocidadesX = new float[numeroBolas];
//y creamos un array de velocidadesY:
float[] velocidadesY = new float[numeroBolas];


void setup() {
  size(300, 200);
  //inicializamos las posiciones y velocidades:
  for (int i = 0; i<numeroBolas; i++) {
    posicionesX[i] = width/2;
    posicionesY[i] = height/2;
    velocidadesX[i] = random(1, 3);
    velocidadesY[i] = random(1, 3);
  }
}

void draw() {
  background(0);

  //primero, dibujamos toda las bolas:
  dibujaBolas();
  //y finalmente, dibujamos el marcador de la posiciÃ³n media:
}

//////////////FUNCIONES(///////////////////////////////////

void dibujaBolas() {
  stroke(0);
  fill(255);

  //iniciamos un bucle para que realize la acciÃ¯Â¿Â½n para todos los
  //elementos del array:
  for (int i = 0; i<numeroBolas; i++) {
    //actualitzamos las posiciones
    posicionesX[i] += velocidadesX[i];
    posicionesY[i] += velocidadesY[i];

    //comprobamos los bordes X
    if ((posicionesX[i]<0)||(posicionesX[i]>width)) {
      velocidadesX[i] = -velocidadesX[i];
    } 
    //comprobamos los bordes Y
    if ((posicionesY[i]<0)||(posicionesY[i]>height)) {
      velocidadesY[i] = -velocidadesY[i];
    } 

    //dibujamos las elipses:
    ellipse(posicionesX[i], posicionesY[i], sz, sz);
  }
  //acabado esto, dibujamos una elipse que represente la posición media:
    //y dibujamos el elemento
  noFill();
  stroke(200,0,0);
  float xMedia = dameLaMedia(posicionesX);
  float yMedia = dameLaMedia(posicionesY);
  
  ellipse(xMedia,yMedia,sz,sz);
  line(xMedia-sz/4,yMedia,xMedia+sz/4,yMedia);
  line(xMedia,yMedia-sz/4,xMedia,yMedia+sz/4);
}

float dameLaMedia(float[] _a) {
  float suma=0, media =0;
 
  //sumamos todas las posiciones 
  for (int i = 0; i<numeroBolas; i++) {
   suma += _a[i];
  }
  //...y las dividimos por el nÃºmero de bolas:
  media = suma/numeroBolas;
  return media;
}

void mousePressed(){
   for (int i = 0; i<numeroBolas; i++) {
    posicionesX[i] = mouseX;
    posicionesY[i] = mouseY;
    velocidadesX[i] = random(1, 5);
    velocidadesY[i] = random(1, 5);
  } 
}




