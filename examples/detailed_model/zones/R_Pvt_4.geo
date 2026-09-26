*Geometry 1.1,GEN,R_Pvt_4 # tag version, format, zone name
*date Wed Jul 22 18:20:52 2020  # latest file modification 
Photovoltaic thermal system part 4
*previous_rotate   180.00,  13.120,  10.600  # prior rotation angle X Y
# tag, X co-ord, Y co-ord, Z co-ord
*vertex,10.99761,5.70353,3.68055  #   1
*vertex,8.12501,5.70353,3.68055  #   2
*vertex,8.12500,1.38766,3.19933  #   3
*vertex,10.99763,1.38767,3.19933  #   4
*vertex,10.99761,5.69466,3.76006  #   5
*vertex,8.12501,5.69466,3.76006  #   6
*vertex,8.12501,1.37880,3.27884  #   7
*vertex,10.99764,1.37880,3.27884  #   8
# 
# tag, number of vertices followed by list of associated vert
*edges,4,2,1,4,3  #   1
*edges,4,7,8,5,6  #   2
*edges,4,3,4,8,7  #   3
*edges,4,4,1,5,8  #   4
*edges,4,1,2,6,5  #   5
*edges,4,2,3,7,6  #   6
# 
# surf attributes:
#  surf name, surf position VERT/CEIL/FLOR/SLOP/UNKN
#  child of (surface name), useage (pair of tags) 
#  construction name, optical name
#  boundary condition tag followed by two data items
*surf,pvt_4_R,SLOP,-,-,-,CT_Wall_Roof,OPAQUE,ANOTHER,020,020  #   1 ||< pvt_R_4:Roof
*surf,pvt_4,SLOP,-,-,-,CT_PVT_semi_Tr,PVmod_opt,EXTERIOR,00,000  #   2 ||< external
*surf,pvt_4_S,SLOP,-,-,-,CT_Wall_Roof,OPAQUE,EXTERIOR,00,000  #   3 ||< external
*surf,pvt_4_1,VERT,-,-,-,CT_Wall_Roof,OPAQUE,ANOTHER,006,004  #   4 ||< pvt_1_4:R_Pvt_1
*surf,pvt_4_3,SLOP,-,-,-,CT_Wall_Roof,OPAQUE,ANOTHER,003,005  #   5 ||< pvt_3_4:R_Pvt_3
*surf,pvt_4_5,VERT,-,-,-,CT_Wall_Roof,OPAQUE,ANOTHER,006,006  #   6 ||< pvt_5_4:R_Pvt_5
# 
*insol,3,0,0,0  # default insolation distribution
# 
# shading directives
*shad_calc,none  # no temporal shading requested
# 
*insol_calc,none  # no insolation requested
# 
*base_list,0,0.00,0  # zone base
