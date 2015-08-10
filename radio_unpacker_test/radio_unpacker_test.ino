#include "unpacker.h"
#include "circularBuffer.h"

const int redout =  9;
const int blueout =  10;
const int greenout =  11;

UnPacker_Handle unpacker;
CB_Handle cbuffer;
bool flag = false;

union u_tag {
   byte b[4];
   float fval;
} u;

void setup() {
  //unpacker = UnPacker_init();
  cbuffer = CB_init();
  //CB_flush(&cbuffer);
  pinMode(redout, OUTPUT);
  pinMode(greenout, OUTPUT);
  pinMode(blueout, OUTPUT);
  Serial.begin(9600);
  blank();
}

void loop() {
    bool notfull = true;
    
    while (Serial.available() > 0) {
        notfull = CB_write(&cbuffer, Serial.read()); 
    }
    
    flag = Unpacker_parseBuffer(&unpacker, &cbuffer);
    for (int i = 0; i < NUMBER_OF_PLAYER; i++){
      if(unpacker.playerReady[i]){
        //blue();
        if(i == 0){
          
          u.b[3] = unpacker.playerBuffer[i][1];
          u.b[2] = unpacker.playerBuffer[i][2];
          u.b[1] = unpacker.playerBuffer[i][3];
          u.b[0] = unpacker.playerBuffer[i][4];
          float x = u.fval;
          u.b[3] = unpacker.playerBuffer[i][5];
          u.b[2] = unpacker.playerBuffer[i][6];
          u.b[1] = unpacker.playerBuffer[i][7];
          u.b[0] = unpacker.playerBuffer[i][8];
          float y = u.fval;
          u.b[3] = unpacker.playerBuffer[i][9];
          u.b[2] = unpacker.playerBuffer[i][10];
          u.b[1] = unpacker.playerBuffer[i][11];
          u.b[0] = unpacker.playerBuffer[i][12];
          float theta = u.fval;
          Serial.print("X: ");
          Serial.print(x, 5);
          Serial.print(" Y: ");
          Serial.print(y, 5);
          Serial.print(" Theta: ");
          Serial.print(theta, 5);
          Serial.print("\n");
          analogWrite(redout, 127 + 127.0 * (x));
          analogWrite(blueout, 127 + 127.0 * (y));
        }
        Unpacker_cleanPlayerBuffer(&unpacker, i);
      }

    }
    
    
    
}

void blank(){
    digitalWrite(redout, HIGH);
    digitalWrite(greenout, HIGH);
    digitalWrite(blueout, HIGH);
}

void red(){
    digitalWrite(redout, LOW);
    digitalWrite(greenout, HIGH);
    digitalWrite(blueout, HIGH);
}

void blue(){
    digitalWrite(redout, HIGH);
    digitalWrite(greenout, HIGH);
    digitalWrite(blueout, LOW);
}

void green(){
    digitalWrite(redout, HIGH);
    digitalWrite(greenout, LOW);
    digitalWrite(blueout, HIGH);
}

void yellow(){
    analogWrite(redout, 0);
    analogWrite(greenout, 0);
    analogWrite(blueout, 255);
}
