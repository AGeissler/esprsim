*Geometry 1.1,GEN,R_Pvt_2 # tag version, format, zone name
*date Wed Jul 22 18:20:52 2020  # latest file modification 
Photovolaic thermal system part 4
*previous_rotate   180.00,  13.120,  10.600  # prior rotation angle X Y
# tag, X co-ord, Y co-ord, Z co-ord
*vertex,10.99761,5.70353,3.68055  #   1
*vertex,13.87024,5.70353,3.68055  #   2
*vertex,13.87024,10.01933,4.16177  #   3
*vertex,10.99761,10.01932,4.16177  #   4
*vertex,13.87024,5.69466,3.76006  #   5
*vertex,13.87024,10.01046,4.24128  #   6
*vertex,10.99761,10.01044,4.24128  #   7
*vertex,10.99761,5.69466,3.76006  #   8
# 
# tag, number of vertices followed by list of associated vert
*edges,4,3,2,1,4  #   1
*edges,4,7,8,5,6  #   2
*edges,4,4,1,8,7  #   3
*edges,4,3,4,7,6  #   4
*edges,4,2,3,6,5  #   5
*edges,4,1,2,5,8  #   6
# 
# surf attributes:
#  surf name, surf position VERT/CEIL/FLOR/SLOP/UNKN
#  child of (surface name), useage (pair of tags) 
#  construction name, optical name
#  boundary condition tag followed by two data items
*surf,pvt_2_R,SLOP,-,-,-,CT_Wall_Roof,OPAQUE,ANOTHER,018,018  #   1 ||< pvt_R_2:Roof
*surf,pvt_2,SLOP,-,-,-,CT_PVT_semi_Tr,PVmod_opt,EXTERIOR,00,000  #   2 ||< external
*surf,pvt_2_3,VERT,-,-,-,CT_Wall_Roof,OPAQUE,ANOTHER,006,003  #   3 ||< pvt_3_2:R_Pvt_3
*surf,pvt_2_N,SLOP,-,-,-,CT_Wall_Roof,OPAQUE,EXTERIOR,00,000  #   4 ||< external
*surf,pvt_2_E,VERT,-,-,-,CT_Wall_Roof,OPAQUE,EXTERIOR,00,000  #   5 ||< external
*surf,pvt_2_1,SLOP,-,-,-,CT_Wall_Roof,OPAQUE,ANOTHER,003,006  #   6 ||< pvt_1_2:R_Pvt_1
# 
*insol,3,0,0,0  # default insolation distribution
# 
# shading directives
*shad_calc,none  # no temporal shading requested
# 
*insol_calc,none  # no insolation requested
# 
*base_list,0,0.00,0  # zone base
