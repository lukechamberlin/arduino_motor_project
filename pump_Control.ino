//pinout for motor 1
#define speedPin_M1 3
#define dirA_M1 4
#define dirB_M1 5

// data for the serial recieving
boolean newData = false;
boolean loopComplete = true;
const byte numChars = 64;
char receivedChars[numChars];

//data for setting speed of motor 1
int speed_M1;  // 0-255 speed for PWM
char speed_M1HunCalc; //recieved data from the serial port
char speed_M1TenCalc;
char speed_M1OneCalc;

int M1HunMultiple; //char to int conversion for speed control ---> must subtract 48 for ASCII conversion
int M1TenMultiple;
int M1OneMultiple;


void setup() {
  Serial.begin(9600);
  pinMode (speedPin_M1, OUTPUT);
  pinMode (dirA_M1, OUTPUT);
  pinMode (dirA_M1, OUTPUT);

// start with motors off
  digitalWrite(dirA_M1, LOW);
  digitalWrite(dirB_M1, LOW);
}

void loop() {
  recvWithStartEndMarkers();
  useNewData();
  motorMovement();
}

void recvWithStartEndMarkers() {
    static boolean recvInProgress = false;
    static byte ndx = 0;
    char startMarker = '<';
    char endMarker = '>';
    char rc;
    while (Serial.available() > 0 && newData == false) {
        rc = Serial.read();
        if (recvInProgress == true) {
            if (rc != endMarker) {
                receivedChars[ndx] = rc;
                ndx++;
                if (ndx >= numChars) {
                    ndx = numChars - 1;
                }
            }
            else {
                receivedChars[ndx] = '\0'; // terminate the string
                recvInProgress = false;
                ndx = 0;
                newData = true;
            }
        }
        else if (rc == startMarker) {
            recvInProgress = true;
        }
    }
}

void useNewData() {
  if (newData == true) {
    speed_M1HunCalc = receivedChars[0];
    speed_M1TenCalc = receivedChars[1];
    speed_M1OneCalc = receivedChars[2];

    M1HunMultiple = (100*(speed_M1HunCalc-48));
    M1TenMultiple = (10*(speed_M1TenCalc-48));
    M1OneMultiple = (1*(speed_M1OneCalc-48));

    speed_M1 = (M1HunMultiple+M1TenMultiple+M1OneMultiple);
    Serial.println(speed_M1);
    if (speed_M1 > 255) {
      speed_M1 == 0;
      Serial.println("You are going too fast");
    }
  }
newData = false;
loopComplete = false;
}

void motorMovement(){
  analogWrite(speedPin_M1, speed_M1); //set motor speed
  digitalWrite(dirA_M1, HIGH); // turn motor on
  digitalWrite(dirB_M1, LOW);
  delay(2000);
  digitalWrite(dirA_M1, LOW); // turn motor off
  digitalWrite(dirB_M1, LOW); 
}
