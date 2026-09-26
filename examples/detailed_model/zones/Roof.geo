*Geometry 1.1,GEN,Roof # tag version, format, zone name
*date Mon Aug 17 19:18:34 2020  # latest file modification 
Roof describes a death space
*previous_rotate   180.00,  13.120,  10.600  # prior rotation angle X Y
# tag, X co-ord, Y co-ord, Z co-ord
*vertex,0.00000,-0.40001,3.00000  #   1
*vertex,16.25000,-0.40001,3.00000  #   2
*vertex,16.25000,11.80701,4.36110  #   3
*vertex,0.00000,11.80702,4.36110  #   4
*vertex,16.25000,11.80701,4.13640  #   5
*vertex,0.00000,11.80702,4.13640  #   6
*vertex,16.25000,11.50000,3.00000  #   7
*vertex,-0.00002,11.50002,3.00000  #   8
*vertex,11.84999,9.29998,3.00000  #   9
*vertex,10.75000,9.30000,3.00000  #  10
*vertex,10.75000,7.30000,3.00000  #  11
*vertex,10.75002,6.30000,3.00000  #  12
*vertex,11.85000,6.30001,3.00000  #  13
*vertex,9.55001,9.30001,3.00000  #  14
*vertex,9.55000,7.30000,3.00000  #  15
*vertex,16.25002,11.30000,3.00000  #  16
*vertex,11.84999,11.29998,3.00000  #  17
*vertex,15.15000,6.30000,3.00000  #  18
*vertex,16.25002,6.30000,3.00000  #  19
*vertex,11.85000,3.80000,3.00000  #  20
*vertex,11.85000,0.00001,3.00000  #  21
*vertex,16.25000,0.00000,3.00000  #  22
*vertex,16.25000,3.79999,3.00000  #  23
*vertex,14.15000,3.79999,3.00000  #  24
*vertex,14.15000,5.25000,3.00000  #  25
*vertex,15.15000,5.25000,3.00000  #  26
*vertex,7.20001,9.30001,3.00000  #  27
*vertex,7.20000,6.29999,3.00000  #  28
*vertex,4.00000,6.30001,3.00000  #  29
*vertex,3.99998,5.64999,3.00000  #  30
*vertex,2.50000,5.65000,3.00000  #  31
*vertex,2.50000,3.65000,3.00000  #  32
*vertex,4.00001,3.64999,3.00000  #  33
*vertex,3.99999,0.00000,3.00000  #  34
*vertex,3.99999,9.30001,3.00000  #  35
*vertex,0.00000,9.30000,3.00000  #  36
*vertex,0.00001,5.65000,3.00000  #  37
*vertex,0.00000,3.65001,3.00000  #  38
*vertex,0.00000,0.00001,3.00000  #  39
*vertex,13.87024,1.38767,3.19933  #  40
*vertex,10.99763,1.38767,3.19933  #  41
*vertex,10.99761,5.70353,3.68055  #  42
*vertex,13.87024,5.70353,3.68055  #  43
*vertex,13.87024,10.01933,4.16177  #  44
*vertex,10.99761,10.01932,4.16177  #  45
*vertex,8.12499,10.01932,4.16177  #  46
*vertex,8.12501,5.70353,3.68055  #  47
*vertex,8.12500,1.38766,3.19933  #  48
*vertex,5.25239,1.38767,3.19933  #  49
*vertex,5.25239,5.70353,3.68055  #  50
*vertex,5.25239,10.01933,4.16177  #  51
*vertex,2.37976,10.01933,4.16177  #  52
*vertex,2.37976,5.70353,3.68055  #  53
*vertex,2.37976,1.38767,3.19933  #  54
*vertex,11.67000,6.15000,3.00000  #  55
*vertex,4.17000,6.15000,3.00000  #  56
*vertex,4.17000,0.15000,3.00000  #  57
*vertex,11.67000,0.15000,3.00000  #  58
# 
# tag, number of vertices followed by list of associated vert
*edges,18,1,2,3,4,52,51,46,45,44,43,40,41,48,49,54,53,52,4  #   1
*edges,4,4,3,5,6  #   2
*edges,4,6,5,7,8  #   3
*edges,5,10,9,13,12,11  #   4
*edges,4,14,10,11,15  #   5
*edges,6,17,16,19,18,13,9  #   6
*edges,9,13,18,26,25,24,23,22,21,20  #   7
*edges,6,18,19,23,24,25,26  #   8
*edges,4,35,27,28,29  #   9
*edges,6,36,35,29,30,31,37  #  10
*edges,5,38,32,33,34,39  #  11
*edges,4,37,31,32,38  #  12
*edges,6,2,1,39,34,21,22  #  13
*edges,10,8,7,16,17,9,10,14,27,35,36  #  14
*edges,8,3,2,22,23,19,16,7,5  #  15
*edges,8,1,4,6,8,36,37,38,39  #  16
*edges,4,41,40,43,42  #  17
*edges,4,43,44,45,42  #  18
*edges,4,45,46,47,42  #  19
*edges,4,42,47,48,41  #  20
*edges,4,48,47,50,49  #  21
*edges,4,50,47,46,51  #  22
*edges,4,51,52,53,50  #  23
*edges,4,50,53,54,49  #  24
*edges,4,56,55,58,57  #  25
*edges,21,27,14,15,11,12,13,20,21,34,33,32,31,30,29,56,57,58,55,56,29,28  #  26
# 
# surf attributes:
#  surf name, surf position VERT/CEIL/FLOR/SLOP/UNKN
#  child of (surface name), useage (pair of tags) 
#  construction name, optical name
#  boundary condition tag followed by two data items
*surf,Roof_top,SLOP,-,ROOF,FLAT,CT_Wall_Roof,OPAQUE,EXTERIOR,00,000  #   1 ||< external
*surf,Roof_S1,VERT,-,WALL,-,CT_Wall_Roof,OPAQUE,EXTERIOR,00,000  #   2 ||< external
*surf,Roof_S2,SLOP,-,WALL,-,CT_Wall_Roof,OPAQUE,EXTERIOR,00,000  #   3 ||< external
*surf,Ceil-Cel,FLOR,-,PARTN,-,CT_Ceiling_inv,OPAQUE,ANOTHER,006,006  #   4 ||< Ceil-Cel:Cellar
*surf,Ceil-WC,FLOR,-,PARTN,-,CT_Ceiling_inv,OPAQUE,ANOTHER,004,004  #   5 ||< Ceil-WC:WC
*surf,Ceil_gar,FLOR,-,PARTN,-,CT_Ceiling_inv,OPAQUE,ANOTHER,006,006  #   6 ||< Ceil_gar:Garage
*surf,Ceil_Bd1,FLOR,-,PARTN,-,CT_Ceiling_inv,OPAQUE,ANOTHER,009,009  #   7 ||< Ceil_Bd1:BedRoom_1
*surf,Ceil_Bath1,FLOR,-,PARTN,-,CT_Ceiling_inv,OPAQUE,ANOTHER,002,002  #   8 ||< Ceil_Bath1:Bath1
*surf,Ceil_Kitc,FLOR,-,PARTN,-,CT_Ceiling_inv,OPAQUE,ANOTHER,003,003  #   9 ||< Ceil_Kitc:Kitchen
*surf,Ceil_Bd3,FLOR,-,PARTN,-,CT_Ceiling_inv,OPAQUE,ANOTHER,004,004  #  10 ||< Ceil_Bd3:BedRoom_3
*surf,Ceil_Bd2,FLOR,-,PARTN,-,CT_Ceiling_inv,OPAQUE,ANOTHER,004,004  #  11 ||< Ceil_Bd2:BedRoom_2
*surf,Ceil_Bth2,FLOR,-,PARTN,-,CT_Ceiling_inv,OPAQUE,ANOTHER,002,002  #  12 ||< Ceil_Bth2:BathRoom_2
*surf,Ceil_Grd2,FLOR,-,PARTN,-,CT_Ceil_external,OPAQUE,EXTERIOR,00,000  #  13 ||< external
*surf,Ceil_Grd1,FLOR,-,FLOOR,EXTGRND,CT_Ceil_external,OPAQUE,EXTERIOR,00,000  #  14 ||< external
*surf,roof_W,VERT,-,WALL,-,CT_Wall_Roof,OPAQUE,EXTERIOR,00,000  #  15 ||< external
*surf,roof_E,VERT,-,WALL,-,CT_Wall_Roof,OPAQUE,EXTERIOR,00,000  #  16 ||< external
*surf,pvt_R_1,SLOP,-,ROOF,FLAT,CT_Wall_Roof,OPAQUE,ANOTHER,001,018  #  17 ||< pvt_1_R:R_Pvt_1
*surf,pvt_R_2,SLOP,-,ROOF,FLAT,CT_Wall_Roof,OPAQUE,ANOTHER,001,019  #  18 ||< pvt_2_R:R_Pvt_2
*surf,pvt_R_3,SLOP,-,ROOF,FLAT,CT_Wall_Roof,OPAQUE,ANOTHER,001,020  #  19 ||< pvt_3_R:R_Pvt_3
*surf,pvt_R_4,SLOP,-,ROOF,FLAT,CT_Wall_Roof,OPAQUE,ANOTHER,001,021  #  20 ||< pvt_4_R:R_Pvt_4
*surf,pvt_R_5,SLOP,-,ROOF,FLAT,CT_Wall_Roof,OPAQUE,ANOTHER,001,022  #  21 ||< pvt_5_R:R_Pvt_5
*surf,pvt_R_6,SLOP,-,ROOF,FLAT,CT_Wall_Roof,OPAQUE,ANOTHER,001,023  #  22 ||< pvt_6_R:R_Pvt_6
*surf,pvt_R_7,SLOP,-,ROOF,FLAT,CT_Wall_Roof,OPAQUE,ANOTHER,001,024  #  23 ||< pvt_7_R:R_Pvt_7
*surf,pvt_R_8,SLOP,-,ROOF,FLAT,CT_Wall_Roof,OPAQUE,ANOTHER,001,025  #  24 ||< pvt_8_R:R_Pvt_8
*surf,PCM_option,FLOR,Ceil_Sal,PARTN,-,CT_Ceiling_inv,OPAQUE,ANOTHER,028,025  #  25 ||< PCM_option:Salon
*surf,Ceil_Sal,FLOR,-,PARTN,-,CT_Ceiling_inv,OPAQUE,ANOTHER,010,010  #  26 ||< Ceil_Sal:Salon
# 
*insol,3,0,0,0  # default insolation distribution
# 
# shading directives
*shad_calc,none  # no temporal shading requested
# 
*insol_calc,none  # no insolation requested
# 
*base_list,0,193.38,0  # zone base
