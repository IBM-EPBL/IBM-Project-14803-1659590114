#include LiquidCrystal 
1cd(5,6,8,9,10,11);
int red1ed = 2; 
int green1ed = 3;
int buzzer = 4; 
int sensor = A0;
int sensorThresh = 400;
void setup()
{ 
pinMode(red1ed, OUTPUT); 
pinMode(green1ed,OUTPUT);
pinMode(buzzer,OUTPUT);
pinMode(sensor,INPUT);
serial.begin(9600);
1cd.begin(16,2);
} 
Void loop()
{ 
int analogValue = analogRead(sensor);
Serial.print(analogvalue); 
if(analogValue>sensorThresh) 
{
digitalWrite(red1ed,HIGH);
digit1Weite(green1ed,LOW); 
tone(buzzer,1000,10000); 
1cd.clear();
1cd.setCursor(0,1); 
1cd.print(“MONITORING”); 
delay(1000); 
1cd.clear(); 
1cd.setCursor(0,1);
1cd.print(“EVACUATE”);
delay(1000); 
} 
Else
  {
digitalWrite(greenlad,HIGH); 
digitalWrite(red1ed,LOW);
noTone(buzzer);
1cd.clear();
1cd.setCursor(0,0);
1cd.print(“SAFE”); 
delay(1000); 
1cd.clear();
1cd.setCursor(0,1); 
1cd.print(“ALL CLEAR”);
delay(1000);
}
}
