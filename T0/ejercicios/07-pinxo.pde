/*
 Autor: Joan Soler-Adillon (www.joan.cat)
 Tutorial de Processing: Condicionals
 */


int sz = 20; //mida del globus: inicialment 20
int creixement = 1; //variable de creixement del globus
int midaPunxa = 35; //mida de la punxa

void setup(){
  size(200,200);
  fill(255,255,127);
  smooth();
  stroke(255,127,127);
}

void draw(){
  background(0);

  //dibuixem la punxa:
  stroke(255,127,127);
  line(0,height/2,midaPunxa,height/2);

  if(mousePressed){ //si estem clicant
    sz = sz + creixement; //size creixerà segons la variable "creixement"
  } 

  /*abans de dibuixar el globes, cal comprobar si toca o no la punxa.
   Sabem que el globus toca la punxa si la meitat del seu diàmetre
   és menor a la meitat de WIDTH menys la mida de la punxa */

  if(sz/2 > (width/2)-midaPunxa){
    //com que ha tocat la punxa, dibuixem el recuadre vermell:
    fill(255,0,0);
    rect(0,0,width,height);
  } 
  else { //com que no el toca, dibuixem la bola
    //primer el globus
    //sense stroke
    noStroke();
    ellipse(width/2,height/2,sz,sz);
    //println(sz);
  }

}

