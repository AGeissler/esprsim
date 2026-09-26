*Geometry 1.1,GEN,R_Pvt_5 # tag version, format, zone name
*date Wed Jul 22 18:20:52 2020  # latest file modification 
Photovolaic thermal system part 5
*previous_rotate   180.00,  13.120,  10.600  # prior rotation angle X Y
# tag, X co-ord, Y co-ord, Z co-ord
*vertex,8.12500,1.38766,3.19933  #   1
*vertex,8.12501,5.70353,3.68055  #   2
*vertex,5.25239,5.70353,3.68055  #   3
*vertex,5.25239,1.38767,3.19933  #   4
*vertex,8.12501,1.37880,3.27884  #   5
*vertex,8.12501,5.69466,3.76006  #   6
*vertex,5.25239,5.69466,3.76006  #   7
*vertex,5.25240,1.37880,3.27884  #   8
# 
# tag, number of vertices followed by list of associated vert
*edges,4,2,1,4,3  #   1
*edges,4,7,8,5,6  #   2
*edges,4,3,4,8,7  #   3
*edges,4,2,3,7,6  #   4
*edges,4,4,1,5,8  #   5
*edges,4,1,2,6,5  #   6
# 
# surf attributes:
#  surf name, surf position VERT/CEIL/FLOR/SLOP/UNKN
#  child of (surface name), useage (pair of tags) 
#  construction name, optical name
#  boundary condition tag followed by two data items
*surf,pvt_5_R,SLOP,-,-,-,CT_Wall_Roof,OPAQUE,ANOTHER,021,021  #   1 ||< pvt_R_5:Roof
*surf,pvt_5,SLOP,-,-,-,CT_PVT_semi_Tr,PVmod_opt,EXTERIOR,00,000  #   2 ||< external
*surf,pvt_5_8,VERT,-,-,-,CT_Wall_Roof,OPAQUE,ANOTHER,006,003  #   3 ||< pvt_8_5:R_Pvt_8
*surf,pvt_5_6,SLOP,-,-,-,CT_Wall_Roof,OPAQUE,ANOTHER,006,004  #   4 ||< pvt_6_5:R_Pvt_6
*surf,pvt_5_S,SLOP,-,-,-,CT_Wall_Roof,OPAQUE,EXTERIOR,00,000  #   5 ||< external
*surf,pvt_5_4,VERT,-,-,-,CT_Wall_Roof,OPAQUE,ANOTHER,006,006  #   6 ||< pvt_4_5:R_Pvt_4
# 
*insol,3,0,0,0  # default insolation distribution
# 
# shading directives
*shad_calc,none  # no temporal shading requested
# 
*insol_calc,none  # no insolation requested
# 
*base_list,0,0.00,0  # zone base
