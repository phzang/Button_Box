# Keyboard Press lookups
# Hex : Button Press

# ------ Lookup Table Buttons -------

keypress_dictionary = {
"00": 'TOGGLE_PRIMER', #Button_A_Pressed
"01": 'NONE', #Button_A_Released
"02": 'NONE', #Button_B_Pressed
"03": 'NONE', #Button_B_Released
"04": 'NONE', #Button_C_Pressed
"05": 'NONE', #Button_C_Released
"06": 'COM_STBY_RADIO_SWAP', #Button_D_Pressed
"07": 'NONE', #Button_D_Released
"08": 'NAV1_RADIO_SWAP', #Button_E_Pressed
"09": 'NONE', #Button_E_Released

# ------ Lookup Table Rotary -------

"10": 'NONE', #Rotary_A_CW              inop due to wireing
"11": 'NONE', #Rotary_A_CCW             inop due to wireing
"12": 'NONE', #Rotary_A_Button_Pressed  inop due to wireing
"13": 'NONE', #Rotary_A_Button_Released inop due to wireing

"14": "z", #Rotary_B_CW VOR1
"15": 'ctrl+shift+z', #Rotary_B_CCW
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

"26": 'ctrl+z', #Rotary_E_CW      inop due to wireing
"27": 'alt+ctrl+z', #Rotary_E_CCW     inop due to wireing
"28": 'NONE', #Rotary_E_Button_Pressed  inop due to wireing
"29": 'NONE', #Rotary_E_Button_Released inop due to wireing

"30": 'KOHLSMAN_INC', #Rotary_F_CW      Altimiter Adjustment
"31": 'KOHLSMAN_DEC', #Rotary_F_CCW
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

"50": 'but_13', # pin 13
"51": 'but_12', # pin 12
"52": 'but_11', # pin 11
    
"53": 'BOTH'

}
