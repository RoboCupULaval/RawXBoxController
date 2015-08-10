/**
 * Simple Write. 
 * 
 * Check if the mouse is over a rectangle and writes the status to the serial port. 
 * This example works with the Wiring / Arduino program that follows below.
 */


import processing.serial.*;

boolean packetSent = false;

Serial myPort;  // Create object from Serial class
int val;        // Data received from the serial port
char inByte = '0';


void setup() 
{
  size(200, 200);
  // I know that the first port in the serial list on my mac
  // is always my  FTDI adaptor, so I open Serial.list()[0].
  // On Windows machines, this generally opens COM1.
  // Open whatever port is the one you're using.
  String portName = Serial.list()[0];
  myPort = new Serial(this, "/dev/ttyACM0", 9600);
  myPort.buffer(1);
  frameRate(60);
  
}

void draw() {
  //sendPacket();
  if (mousePressed) {
    if (!packetSent){
      sendPacket();
      println("Packet sent!!!");
      packetSent = true;
    }
  } else {
    packetSent = false;
  }
  background(0);
  text("Last Received: " + inByte, 10, 130);
}

void sendPacket(){
  myPort.write(126);  
  myPort.write(0);
  myPort.write(1);
  
  myPort.write(65);
  myPort.write(3);
  myPort.write(0);
  myPort.write(124);
  
  myPort.write(67);
  myPort.write(0);
  myPort.write(0); 
  myPort.write(8);

  myPort.write(67);
  myPort.write(8);
  myPort.write(0);
  myPort.write(8);
  
  myPort.write(127); 

}

void serialEvent(Serial myPort) {
  inByte = char(myPort.read());
  print(inByte + "");
}
