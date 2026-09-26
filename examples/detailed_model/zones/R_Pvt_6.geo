*Geometry 1.1,GEN,R_Pvt_6 # tag version, format, zone name
*date Wed Jul 22 18:20:52 2020  # latest file modification 
Photovoltaic thermal system part 6
*previous_rotate   180.00,  13.120,  10.600  # prior rotation angle X Y
# tag, X co-ord, Y co-ord, Z co-ord
*vertex,8.12501,5.70353,3.68055  #   1
*vertex,5.25239,5.70353,3.68055  #   2
*vertex,5.25239,10.01933,4.16177  #   3
*vertex,8.12499,10.01932,4.16177  #   4
*vertex,5.25239,5.69466,3.76006  #   5
*vertex,8.12501,5.69466,3.76006  #   6
*vertex,8.12499,10.01046,4.24128  #   7
*vertex,5.25239,10.01043,4.24128  #   8
# 
# tag, number of vertices followed by list of associated vert
*edges,4,1,2,3,4  #   1
*edges,4,7,8,5,6  #   2
*edges,4,4,3,8,7  #   3
*edges,4,3,2,5,8  #   4
*edges,4,1,4,7,6  #   5
*edges,4,2,1,6,5  #   6
# 
# surf attributes:
#  surf name, surf position VERT/CEIL/FLOR/SLOP/UNKN
#  child of (surface name), useage (pair of tags) 
#  construction name, optical name
#  boundary condition tag followed by two data items
*surf,pvt_6_R,SLOP,-,-,-,CT_Wall_Roof,OPAQUE,ANOTHER,022,022  #   1 ||< pvt_R_6:Roof
*surf,pvt_6,SLOP,-,-,-,CT_PVT_semi_Tr,PVmod_opt,EXTERIOR,00,000  #   2 ||< external
*surf,pvt_6_N,SLOP,-,-,-,CT_Wall_Roof,OPAQUE,EXTERIOR,00,000  #   3 ||< external
*surf,pvt_6_7,VERT,-,-,-,CT_Wall_Roof,OPAQUE,ANOTHER,005,006  #   4 ||< pvt_7_6:R_Pvt_7
*surf,pvt_6_3,VERT,-,-,-,CT_Wall_Roof,OPAQUE,ANOTHER,004,005  #   5 ||< pvt_3_6:R_Pvt_3
*surf,pvt_6_5,SLOP,-,-,-,CT_Wall_Roof,OPAQUE,ANOTHER,004,006  #   6 ||< pvt_5_6:R_Pvt_5
# 
*insol,3,0,0,0  # default insolation distribution
# 
# shading directives
*shad_calc,none  # no temporal shading requested
# 
*insol_calc,none  # no insolation requested
# 
*base_list,0,0.00,0  # zone base
