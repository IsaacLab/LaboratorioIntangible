/*
UPF-IUA
 Màster d'Arts Digitals
 joan soler-adillon (www.joan.cat)
 
 Con un random() y un condicional, escogemos la dirección de la bola
 */
 
 int pos, vel;
int sz = 20;
float viento;

void setup(){
  size(300,150);
  pos = width/2;
  vel = 2;
  //vamos a crear un viento:
  viento = random(-1,1);
}

void draw(){

  background(0);

  //actualitzamos la posición según sople el viento:
  if(viento > 0){
    pos = pos+vel;
  } 
  else { //oséase si el viento es menor o igual a 0:
    pos = pos-vel;
  }
  //dibujamos
  ellipse(pos,height/2,sz,sz);

//para que se vaya repitiendo la misma acción:
  if(pos < 0 || pos > width){
    //reiniciamos posicion:
    pos = width/2;
    //creamos un viento:
    viento = random(-1,1);
    //println(viento);
  }
}


