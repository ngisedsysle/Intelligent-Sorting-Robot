uint32_t value =0;
uint32_t index=0;
uint32_t cmd=0;
uint8_t data_store[5];
uint16_t data=0;
uint16_t previous_data=0;
uint32_t current_position=0;
uint32_t initial_position=0;


#include <BioloidController.h>
BioloidController bioloid = BioloidController(1000000);


void setup(){

Serial.begin(9600);
pinMode(25,OUTPUT);

  ax12SetRegister2(0,32,100);
  ax12SetRegister2(1,32,70);
  ax12SetRegister2(2,32,70);   

  ax12SetRegister2(3,32,100);
  ax12SetRegister2(4,32,100);  
 
  ax12SetRegister2(5,32,100);
  ax12SetRegister2(6,32,100);
  ax12SetRegister2(7,32,100);  

  //Serial.setTimeout(1);
}

// Calcul pose moteur 3

int pos_moteur3(int moteur4){
  int val;
  int diff=509-moteur4;
  if(diff<0){
    val = 509-abs(diff);
    return val;
  }
  else{
    val = 509+diff;
    return val;
  }
}

// Calcul pose moteur 2

int pos_moteur2(int moteur1){
  return moteur1-293;
}


void loop(){

  int moteur0, moteur1,moteur2,moteur3,moteur4,moteur5,moteur6, moteur7;
   if(Serial.available() > 0) { 
     value = Serial.read();
     data_store[index]=value;
     Serial.println(data_store[index]);
     index++;
   }
 //Serial.println(index);
   
   
 if (index == 5){
   Serial.println(index);
   index=0;
   // If the byte sequence received is correct
   if (data_store[0] == 18 && data_store[1]== 18){
     cmd = data_store[2];
     
   //Treating the data
     data= data_store[3] <<8 | data_store[4];
     Serial.println(data);

   //Switch case, depending on the command received
   
   switch(cmd){
     
     case 9: //Pose condensateur
     
         /////////////////////////////////////////////// MOTEUR 1,2,3 et 4 Initialize the position /////////////////////////////////////////////// 
      Serial.write("I am about to move the cube...");
      
      //Initial position
      
        moteur0 = 977; //position de départ imposée
       
      /////////////////////////////////////////Premier mouvement: Aller chercher le cube
        //moteur0=current_position;
        moteur1= 750; //650;
        moteur2=pos_moteur2(moteur1);
        moteur4=509; //490;
        moteur3=pos_moteur3(moteur4);
        moteur5=509;
        moteur6=507;
        moteur7= 512; 
        delay(100);
      ////  
      
        SetPosition(7,moteur7);
        delay(1000);
      
        SetPosition(6,moteur6);
        delay(1000);
      
        SetPosition(5,moteur5);
        delay(1000);
        
        SetPosition(4,moteur4);
        SetPosition(3,moteur3);
        delay(1000);
      
        SetPosition(2,moteur2);
        SetPosition(1,moteur1);
        delay(1000);
        
        SetPosition(0,moteur0); 
        delay(3000);
        
        /////////////////////////////////////// Placement moteur 5 et fermeture de la pince sur le cube
        moteur5= 300; //370;
        moteur7=670;
      //  
        SetPosition(5,moteur5);
        delay(1000);
      ////  
        SetPosition(7,moteur7);
        delay(1000);
           
      ////////////////////////////////////////Second mouvement:remonte le bras et l'orienter vers l'endroit où l'on veut poser le cube
      //
        moteur1=830;
        moteur2=pos_moteur2(moteur1);
        delay(100);
        
        SetPosition(2,moteur2);
        SetPosition(1,moteur1);
        delay(1000);
        
        moteur0=data;
        SetPosition(0,moteur0); 
        delay(3000);
      
      /////////////////////////////////////// 3 eme mouvement: dépose le cube en ouvrant la pince
      //
        moteur1=750; //650;
        moteur2=pos_moteur2(moteur1);
        moteur7=512;
      // 
        SetPosition(2,moteur2);
        SetPosition(1,moteur1);
        delay(1000); 
      //  
      //  
        SetPosition(7,moteur7);
        delay(1000);
      
      //////////////////////////////////////// 4 eme mouvement: relève le bras
      //
        moteur1=830;
        moteur2=pos_moteur2(moteur1);
        delay(100);
      //  
        SetPosition(1,moteur1);
        SetPosition(2,moteur2);
        delay(1000); 
        
        break;
      case 0:
                    /////////////////////////////////////////////// MOTEUR 1,2,3 et 4 Initialize the position /////////////////////////////////////////////// 
         Serial.write("I am about to move the thing which has been detected...");
                
         //Initial position
         
          moteur0 = 977; //position de de départ imposée
          
        /////////////////////////////////////////Premier mouvement: Aller chercher le cube
        
          moteur1= 750; //650;
          moteur2=pos_moteur2(moteur1);
          moteur4=509; //490;
          moteur3=pos_moteur3(moteur4);
          moteur5=509;
          moteur6=507;
          moteur7= 512; 
          delay(100);
                ////  
                
          SetPosition(7,moteur7);
          delay(1000);
                
          SetPosition(6,moteur6);
          delay(1000);
                
          SetPosition(5,moteur5);
          delay(1000);
                  
          SetPosition(4,moteur4);
          SetPosition(3,moteur3);
          delay(1000);
                
          SetPosition(2,moteur2);
          SetPosition(1,moteur1);
          delay(1000);
                  
          SetPosition(0,moteur0); 
          delay(3000);
                  
           /////////////////////////////////////// Placement moteur 5 et fermeture de la pince sur le cube
           moteur5= 300; //370;
           moteur7=670;
             //  
           SetPosition(5,moteur5);
           delay(1000);
                ////  
           SetPosition(7,moteur7);
           delay(1000);
                     
                ////////////////////////////////////////Second mouvement:remonte le bras et l'orienter vers l'endroit où l'on veut poser le cube
                //
           moteur1=830;
           moteur2=pos_moteur2(moteur1);
           delay(100);
                  
           SetPosition(2,moteur2);
           SetPosition(1,moteur1);
           delay(1000);
                  
           moteur0=data;
           SetPosition(0,moteur0); 
           delay(3000);
                
         /////////////////////////////////////// 3 eme mouvement: dépose le cube en ouvrant la pince
                //
           moteur1=750; //650;
           moteur2=pos_moteur2(moteur1);
           moteur7=512;
                // 
           SetPosition(2,moteur2);
           SetPosition(1,moteur1);
           delay(1000); 
            
           SetPosition(7,moteur7);
           delay(1000);
                
                //////////////////////////////////////// 4 eme mouvement: relève le bras
                //
           moteur1=830;
           moteur2=pos_moteur2(moteur1);
           delay(100);
                //  
           SetPosition(1,moteur1);
           SetPosition(2,moteur2);
           delay(1000); 
           
           break;     
        
                 
         default:
               
           Serial.println("error...");
           break;
             
               
             }
   
      
   }
 
 }
}
 
