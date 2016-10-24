
int led = 13;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(led,OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
    if (Serial.available() > 0){
         if (Serial.read() == 97){ // letra a

            digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
            delay(500); // wait for a second
            digitalWrite(led, LOW); 
            
         }
     }
}
