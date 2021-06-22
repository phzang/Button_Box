# Keyboard Press lookups
# Hex : Button Press

# ------ Lookup Table Buttons -------

keypress_dictionary = {
"00": 'TOGGLE_PRIMER', #Button_A_Pressed
"01": 'NONE', #Button_A_Released
"02": 'DISCORD_PRESSED', #Button_B_Pressed
"03": 'DISCORD_RELEASED', #Button_B_Released
"04": 'VATSIM_PRESSED', #Button_C_Pressed
"05": 'VATSIM_RELEASED', #Button_C_Released
"06": "sim/radios/com1_standy_flip", #Button_D_Pressed
"07": 'NONE', #Button_D_Released
"08": "sim/radios/nav1_standy_flip", #Button_E_Pressed
"09": 'NONE', #Button_E_Released

# ------ Lookup Table Rotary -------

"10": 'F6', #Rotary_A_CW
"11": 'F5', #Rotary_A_CCW
"12": 'NONE', #Rotary_A_Button_Pressed
"13": 'NONE', #Rotary_A_Button_Released

"14": "NONE", #Rotary_B_CW VOR1
"15": 'NONE', #Rotary_B_CCW
"16": 'NONE', #Rotary_B_Button_Pressed
"17": 'NONE', #Rotary_B_Button_Released

"18": 'FAKE_COM', #Rotary_C_CW          com.py will fill in a real value
"19": 'FAKE_COM', #Rotary_C_CCW         for SimConnect
"20": 'FAKE_COM', #Rotary_C_Button_Pressed
"21": 'NONE', #Rotary_C_Button_Released

"22": 'FAKE_COM', #Rotary_D_CW          com.py will fill in a real value
"23": 'FAKE_COM', #Rotary_D_CCW         for SimConnect
"24": 'FAKE_COM', #Rotary_D_Button_Pressed
"25": 'NONE', #Rotary_D_Button_Released

"26": 'F6', #Rotary_E_CW      INOP AGAIN GRR
"27": 'F5', #Rotary_E_CCW
"28": 'NONE', #Rotary_E_Button_Pressed
"29": 'NONE', #Rotary_E_Button_Released

"30": 'shift+b', #Rotary_F_CW      Altimiter Adjustment
"31": 'ctrl+b', #Rotary_F_CCW
"32": 'NONE', #Rotary_F_Button_Pressed
"33": 'NONE', #Rotary_F_Button_Released

"34": 'VOR2_OBI_INC', #Rotary_G_CW
"35": 'VOR2_OBI_DEC', #Rotary_G_CCW
"36": 'NONE', #Rotary_G_Button_Pressed
"37": 'NONE', #Rotary_G_Button_Released

"38": 'FAKE_TRANSPONDER', #Rotary_H_CW   transponder.py will fill in a real
"39": 'FAKE_TRANSPONDER', #Rotary_H_CCW  value to SimConnect
"40": 'FAKE_TRANSPONDER', #Rotary_H_Button_Pressed
"41": 'NONE', #Rotary_H_Button_Released

"42": 'FAKE_NAV', #Rotary_I_CW           nav.py will fill in a real value
"43": 'FAKE_NAV', #Rotary_I_CCW          to SimConnect
"44": 'FAKE_NAV', #Rotary_I_Button_Pressed
"45": 'NONE', #Rotary_I_Button_Released

"46": 'FAKE_NAV', #Rotary_J_CW           nav.py will fill in a real value
"47": 'FAKE_NAV', #Rotary_J_CCW          to SimConnect
"48": 'FAKE_NAV', #Rotary_J_Button_Pressed
"49": 'NONE', #Rotary_J_Button_Released

"50": 'FAKE_MAG', #Rotary_J_Button_Pressed
"51": 'FAKE_MAG1', #Rotary_J_Button_Released
"52": 'FAKE_MAG2'

}
