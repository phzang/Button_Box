#include <SimpleRotary.h>
#include <Button.h>
#include "misc_header.h"

bool DEBUG = 0;

// init buttons
Button button_A(7);
Button button_B(6);
Button button_C(5);
Button button_D(4);
Button button_E(3);

Button but_ign(13);
Button but_acc(12);
Button but_bat(11);

// init rotary turn
byte rotary_A_turn = 0;
byte rotary_B_turn = 0;
byte rotary_C_turn = 0;
byte rotary_D_turn = 0;
byte rotary_E_turn = 0;
byte rotary_F_turn = 0;
byte rotary_G_turn = 0;
byte rotary_H_turn = 0;
byte rotary_I_turn = 0;
byte rotary_J_turn = 0;

byte rotary_pushed = 0;

// Pin A, Pin B, Button Pin
SimpleRotary rotary_A(24,25,43);
SimpleRotary rotary_B(26,27,44);
SimpleRotary rotary_C(28,29,45);
SimpleRotary rotary_D(30,31,46);
SimpleRotary rotary_E(22,23,42);
SimpleRotary rotary_F(32,33,47);
SimpleRotary rotary_G(34,35,48);
SimpleRotary rotary_H(36,37,49);
SimpleRotary rotary_I(38,39,50);
SimpleRotary rotary_J(40,41,51);


void setup() {
  // put your setup code here, to run once:
  button_A.begin();
  button_B.begin();
  button_C.begin();
  button_D.begin();
  button_E.begin();

  but_ign.begin();
  but_acc.begin();
  but_bat.begin();




  Serial.begin(9600);

}

void checkButtons(){

    // -------- Buttons Pressed --------
    if (button_A.pressed())
      Serial.write(Button_A_Pressed);
    if (button_A.released())
      Serial.write(Button_A_Released);

    if (button_B.pressed())
      Serial.write(Button_B_Pressed);
    if (button_B.released())
      Serial.write(Button_B_Released);

    if (button_C.pressed())
      Serial.write(Button_C_Pressed);
    if (button_C.released())
      Serial.write(Button_C_Released);

    if (button_D.pressed())
      Serial.write(Button_D_Pressed);
    if (button_D.released())
      Serial.write(Button_D_Released);

    if (button_E.pressed())
      Serial.write(Button_E_Pressed);
    if (button_E.released())
      Serial.write(Button_E_Released);

    if (but_ign.pressed())
      Serial.write(but_ign_Pressed);

    if (but_acc.pressed())
      Serial.write(but_acc_Pressed);


    if (but_bat.pressed())
      Serial.write(but_bat_Pressed);


    // -------- Rotary A --------
    rotary_A_turn = rotary_A.rotate();
    rotary_pushed = rotary_A.push();
    if ( rotary_A_turn == 1 ) {
      Serial.write(Rotary_A_CW);
      rotary_A_turn = 0;
    }
    if ( rotary_A_turn == 2 ) {
      Serial.write(Rotary_A_CCW);
      rotary_A_turn = 0;
    }
    if (rotary_pushed) {
      Serial.write(Rotary_A_Button_Pressed);
      rotary_pushed = 0;
    }

    // -------- Rotary B --------
    rotary_B_turn = rotary_B.rotate();
    rotary_pushed = rotary_B.push();
    if ( rotary_B_turn == 1 ) {
      Serial.write(Rotary_B_CW);
      rotary_B_turn = 0;
    }
    if ( rotary_B_turn == 2 ) {
      Serial.write(Rotary_B_CCW);
      rotary_B_turn = 0;
    }
    if (rotary_pushed) {
      Serial.write(Rotary_B_Button_Pressed);
      rotary_pushed = 0;
    }

    // -------- Rotary C --------
    rotary_C_turn = rotary_C.rotate();
    rotary_pushed = rotary_C.push();
    if ( rotary_C_turn == 1 ) {
      Serial.write(Rotary_C_CW);
      rotary_C_turn = 0;
    }
    if ( rotary_C_turn == 2 ) {
      Serial.write(Rotary_C_CCW);
      rotary_C_turn = 0;
    }
    if (rotary_pushed) {
      Serial.write(Rotary_C_Button_Pressed);
      rotary_pushed = 0;
    }

    // -------- Rotary D --------
    rotary_D_turn = rotary_D.rotate();
    rotary_pushed = rotary_D.push();
    if ( rotary_D_turn == 1 ) {
      Serial.write(Rotary_D_CW);
      rotary_D_turn = 0;
    }
    if ( rotary_D_turn == 2 ) {
      Serial.write(Rotary_D_CCW);
      rotary_D_turn = 0;
    }
    if (rotary_pushed) {
      Serial.write(Rotary_D_Button_Pressed);
      rotary_pushed = 0;
    }

    // -------- Rotary E --------
    rotary_E_turn = rotary_E.rotate();
    rotary_pushed = rotary_E.push();
    if ( rotary_E_turn == 1 ) {
      Serial.write(Rotary_E_CW);
      rotary_E_turn = 0;
    }
    if ( rotary_E_turn == 2 ) {
      Serial.write(Rotary_E_CCW);
      rotary_E_turn = 0;
    }
    if (rotary_pushed) {
      Serial.write(Rotary_E_Button_Pressed);
      rotary_pushed = 0;
    }

    // -------- Rotary F --------
    rotary_F_turn = rotary_F.rotate();
    rotary_pushed = rotary_F.push();
    if ( rotary_F_turn == 1 ) {
      Serial.write(Rotary_F_CW);
      rotary_F_turn = 0;
    }
    if ( rotary_F_turn == 2 ) {
      Serial.write(Rotary_F_CCW);
      rotary_F_turn = 0;
    }
    if (rotary_pushed) {
      Serial.write(Rotary_F_Button_Pressed);
      rotary_pushed = 0;
    }

    // -------- Rotary G --------
    rotary_G_turn = rotary_G.rotate();
    rotary_pushed = rotary_G.push();
    if ( rotary_G_turn == 1 ) {
      Serial.write(Rotary_G_CW);
      rotary_G_turn = 0;
    }
    if ( rotary_G_turn == 2 ) {
      Serial.write(Rotary_G_CCW);
      rotary_G_turn = 0;
    }
    if (rotary_pushed) {
      Serial.write(Rotary_G_Button_Pressed);
      rotary_pushed = 0;
    }

    // -------- Rotary H --------
    rotary_H_turn = rotary_H.rotate();
    rotary_pushed = rotary_H.push();
    if ( rotary_H_turn == 1 ) {
      Serial.write(Rotary_H_CW);
      rotary_H_turn = 0;
    }
    if ( rotary_H_turn == 2 ) {
      Serial.write(Rotary_H_CCW);
      rotary_H_turn = 0;
    }
    if (rotary_pushed) {
      Serial.write(Rotary_H_Button_Pressed);
      rotary_pushed = 0;
    }


    // -------- Rotary I --------
    rotary_I_turn = rotary_I.rotate();
    rotary_pushed = rotary_I.push();
    if ( rotary_I_turn == 1 ) {
      Serial.write(Rotary_I_CW);
      rotary_I_turn = 0;
    }
    if ( rotary_I_turn == 2 ) {
      Serial.write(Rotary_I_CCW);
      rotary_I_turn = 0;
    }
    if (rotary_pushed) {
      Serial.write(Rotary_I_Button_Pressed);
      rotary_pushed = 0;
    }

    // -------- Rotary J --------
    rotary_J_turn = rotary_J.rotate();
    rotary_pushed = rotary_J.push();
    if ( rotary_J_turn == 1 ) {
      Serial.write(Rotary_J_CW);
      rotary_J_turn = 0;
    }
    if ( rotary_J_turn == 2 ) {
      Serial.write(Rotary_J_CCW);
      rotary_J_turn = 0;
    }
    if (rotary_pushed) {
      Serial.write(Rotary_J_Button_Pressed);
      rotary_pushed = 0;
    }

}

void loop() {
    // put your main code here, to run repeatedly:
   checkButtons();

}
