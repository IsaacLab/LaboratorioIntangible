/*
MUAD - UPF
 Màster d'Arts Digitals
 Autor: joan soler-adillon (www.joan.cat)
 
 Una función nos sirve para agrupar una serie de líneas de código
 que se ejecutarán cada vez que dicha función sea invocada.
 
 Esto nos sirve para organizar el código y hacerlo reciclable...
 */


float pos = 20;
float vel = 1;

void setup() {
  size(300, 150);
  smooth();
  background(0);
}

void draw() {
  background(0);
  dibujaUnSputnik(pos, height/2);

  pos += vel;

  if (pos > width) {
    pos = random(width-50);
  }
}


//He aquí una función que dibuja un SPUTNIK:
void dibujaUnSputnik(int x_, int y_) {
  strokeWeight(3);
  stroke(255);
  fill(255, 0, 0);
  line(x_-30, y_-30, x_+30, y_+30);
  line(x_-30, y_+30, x_+30, y_-30);
  ellipse(x_, y_, 35, 35);
}


