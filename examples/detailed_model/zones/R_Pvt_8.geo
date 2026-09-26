*Geometry 1.1,GEN,R_Pvt_8 # tag version, format, zone name
*date Wed Jul 22 18:20:52 2020  # latest file modification 
Photovoltaic thermal system part 8
*previous_rotate   180.00,  13.120,  10.600  # prior rotation angle X Y
# tag, X co-ord, Y co-ord, Z co-ord
*vertex,5.25239,5.70353,3.68055  #   1
*vertex,2.37976,5.70353,3.68055  #   2
*vertex,2.37976,1.38767,3.19933  #   3
*vertex,5.25239,1.38767,3.19933  #   4
*vertex,5.25239,5.69466,3.76006  #   5
*vertex,2.37977,5.69466,3.76006  #   6
*vertex,2.37976,1.37880,3.27884  #   7
*vertex,5.25240,1.37880,3.27884  #   8
# 
# tag, number of vertices followed by list of associated vert
*edges,4,2,1,4,3  #   1
*edges,4,7,8,5,6  #   2
*edges,4,3,4,8,7  #   3
*edges,4,2,3,7,6  #   4
*edges,4,5,1,2,6  #   5
*edges,4,4,1,5,8  #   6
# 
# surf attributes:
#  surf name, surf position VERT/CEIL/FLOR/SLOP/UNKN
#  child of (surface name), useage (pair of tags) 
#  construction name, optical name
#  boundary condition tag followed by two data items
*surf,pvt_8_R,SLOP,-,-,-,CT_Wall_Roof,OPAQUE,ANOTHER,024,024  #   1 ||< pvt_R_8:Roof
*surf,pvt_8,SLOP,-,-,-,CT_PVT_semi_Tr,PVmod_opt,EXTERIOR,00,000  #   2 ||< external
*surf,pvt_8_S,SLOP,-,-,-,CT_Wall_Roof,OPAQUE,EXTERIOR,00,000  #   3 ||< external
*surf,pvt_8_W,VERT,-,-,-,CT_Wall_Roof,OPAQUE,EXTERIOR,00,000  #   4 ||< external
*surf,pvt_8_7,SLOP,-,-,-,CT_Wall_Roof,OPAQUE,ANOTHER,006,005  #   5 ||< pvt_7_8:R_Pvt_7
*surf,pvt_8_5,VERT,-,-,-,CT_Wall_Roof,OPAQUE,ANOTHER,003,006  #   6 ||< pvt_5_8:R_Pvt_5
# 
*insol,3,0,0,0  # default insolation distribution
# 
# shading directives
*shad_calc,none  # no temporal shading requested
# 
*insol_calc,none  # no insolation requested
# 
*base_list,0,0.00,0  # zone base
