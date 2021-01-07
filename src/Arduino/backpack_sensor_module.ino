#include<Wire.h>
#include<I2Cdev.h>
#include<MPU6050.h>


MPU6050 mpu;

const int MPU=0x68;                       // Gy-521's default address
const int acSensitivityScale = 16384;     // Scale factor for acceleration range of +/-2g
const int gySensitivityScale = 131;       // Scale factor for angular velocity range of +/- 250 degrees/s
float accX,accY,accZ,gyX,gyY,gyZ;

// SDA - A4
// SCL - A5

// Optimal offsets
// X-axis: [311,311] --> [-717,364]
// Y-axis: [1061,1061] --> [-243,9]
// Z-axis: [1029,1029] --> [16374,16385]
// X-Gy: [140,140] --> [-1,27]
// Y-Gy: [14,15] --> [-31,20]
// Z-Gy: [31,31] --> [-58,61]


void setup(){
  Wire.begin();

  Serial.begin(9600);
  while (!Serial);

  // initialize device
  /* Serial.println(F("Initializing I2C devices..."));
  mpu.initialize();

  Serial.println(F("Testing device connections..."));
  Serial.println(F("MPU6050 connetion "));
  Serial.print(mpu.testConnection() ? F("successful") : F("failed"));

  Serial.println(F("\nSend any character to begin DMP programming and demo: "));
  while (Serial.available() && Serial.read());
  while (!Serial.available());
  */
  Wire.beginTransmission(MPU);
  Wire.write(0x6B); 
  Wire.write(0);    
  Wire.endTransmission(true);
  Serial.begin(9600);
}

// This function loops continually while the Arduino is running
void loop(){
  Wire.beginTransmission(MPU);
  Wire.write(0x3B);  
  Wire.endTransmission(false);
  Wire.requestFrom(MPU,12,true);  
  accX=Wire.read()<<8|Wire.read() + 311;    
  accY=Wire.read()<<8|Wire.read() + 1061;  
  accZ=Wire.read()<<8|Wire.read()+ 1029;  
  gyX=Wire.read()<<8|Wire.read() + 140;  
  gyY=Wire.read()<<8|Wire.read() + 14;  
  gyZ=Wire.read()<<8|Wire.read() + 31;  

  Serial.print(accX / acSensitivityScale);
  Serial.print(", "); Serial.print(accY);
  Serial.print(", "); Serial.print(accZ); 
  Serial.print(", "); Serial.print(gyX);
  Serial.print(", "); Serial.print(gyY);
  Serial.print(", "); Serial.println(gyZ);
  Serial.println("");
  delay(100);
}
