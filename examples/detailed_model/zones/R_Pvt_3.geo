*Geometry 1.1,GEN,R_Pvt_3 # tag version, format, zone name
*date Wed Jul 22 18:20:52 2020  # latest file modification 
Photovoltaic thermal system part 3
*previous_rotate   180.00,  13.120,  10.600  # prior rotation angle X Y
# tag, X co-ord, Y co-ord, Z co-ord
*vertex,10.99761,10.01932,4.16177  #   1
*vertex,8.12499,10.01932,4.16177  #   2
*vertex,8.12501,5.70353,3.68055  #   3
*vertex,10.99761,5.70353,3.68055  #   4
*vertex,10.99761,10.01044,4.24128  #   5
*vertex,8.12499,10.01046,4.24128  #   6
*vertex,8.12501,5.69466,3.76006  #   7
*vertex,10.99761,5.69466,3.76006  #   8
# 
# tag, number of vertices followed by list of associated vert
*edges,4,2,1,4,3  #   1
*edges,4,7,8,5,6  #   2
*edges,4,3,4,8,7  #   3
*edges,4,2,3,7,6  #   4
*edges,4,1,2,6,5  #   5
*edges,4,4,1,5,8  #   6
# 
# surf attributes:
#  surf name, surf position VERT/CEIL/FLOR/SLOP/UNKN
#  child of (surface name), useage (pair of tags) 
#  construction name, optical name
#  boundary condition tag followed by two data items
*surf,pvt_3_R,SLOP,-,-,-,CT_Wall_Roof,OPAQUE,ANOTHER,019,019  #   1 ||< pvt_R_3:Roof
*surf,pvt_3,SLOP,-,-,-,CT_PVT_semi_Tr,PVmod_opt,EXTERIOR,00,000  #   2 ||< external
*surf,pvt_3_4,SLOP,-,-,-,CT_Wall_Roof,OPAQUE,ANOTHER,005,003  #   3 ||< pvt_4_3:R_Pvt_4
*surf,pvt_3_6,VERT,-,-,-,CT_Wall_Roof,OPAQUE,ANOTHER,005,004  #   4 ||< pvt_6_3:R_Pvt_6
*surf,pvt_3_N,SLOP,-,-,-,CT_Wall_Roof,OPAQUE,EXTERIOR,00,000  #   5 ||< external
*surf,pvt_3_2,VERT,-,-,-,CT_Wall_Roof,OPAQUE,ANOTHER,003,006  #   6 ||< pvt_2_3:R_Pvt_2
# 
*insol,3,0,0,0  # default insolation distribution
# 
# shading directives
*shad_calc,none  # no temporal shading requested
# 
*insol_calc,none  # no insolation requested
# 
*base_list,0,0.00,0  # zone base
