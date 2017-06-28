/*
UPF-IUA
 Màster d'Arts Digitals
 joan soler-adillon (www.joan.cat)
 
 Una función que retorna un int
 */

//declaramos variables
int sumaDeBlancos; 
PFont letra; //objeto PFont para utilizar texto
void setup() 
{
  noSmooth();
  size(300,200);
  background(0);
  letra = loadFont("ArialMT-24.vlw"); //cargamos la FONT
  textFont(letra);//y tal y como con fill, le decimos a p5 qué font utilizaremos la próxima vez a escribir algo
  //dibujamos el 0
  fill(255,127,13,255);
  text(0, 20,60);
}


void draw() 
{ 

  //sólo pasan cosas si le damos al mouse:
  if(mousePressed){ //mousePressed aquí es una variable
    dibuijaEllipseMouse(); //invocamos nuestra función elipsera
    //invocamos la función que cuenta los píxels blancos y RETORNA la suma de éstos
    //el RETORNO de la función, se lo asignamos a una variable que llamamos "num"
    int num = cuantosPixelsBlancos();

    //dibujamos un rectangulo negro donde pondremos el texto
    fill(0);
    rect(18,45,40,18);
    //y el texto con el número de píxels blancos
    fill(255,127,13,255);
    text(num, 20,60);
  }

}
/////////////////////////////
// funciones:

int cuantosPixelsBlancos(){
    loadPixels();
  //resetejeteamos el contador:
  int contador=0;
  //loop anidado para recorrer todos los píxels
  for(int i=0;i<width;i++){
    for(int j=0;j<height;j++){
      //cogemos el color del píxel donde estamos
      //color c = get(i,j);
      color c = pixels[j*width+i];
      //y si es blanco, aumentamos el contador
      if(c == color(255)){
        contador++;
      }
    }
  }
  //y DEVOLVEMOS el valor de CONTADOR
  updatePixels();
  return contador;
}

//función que dibuja elipses
void dibuijaEllipseMouse(){
  //noStroke();
  fill(255);
  int x = mouseX;
  int y = mouseY;
  //el tamaño de la elipse dependerá de la VELOCIDAD con la que movemos el mouse
  int sz = int(dist(mouseX,mouseY,pmouseX,pmouseY));
  sz *=1.5; //aumentamos el tamaño un 50%
  ellipse(x,y,sz,sz);
}

