*Geometry 1.1,GEN,R_Pvt_1 # tag version, format, zone name
*date Thu Aug 13 11:46:38 2020  # latest file modification 
Photovoltaic thermal system part 1
*previous_rotate   180.00,  13.120,  10.600  # prior rotation angle X Y
# tag, X co-ord, Y co-ord, Z co-ord
*vertex,13.87024,1.38767,3.19933  #   1
*vertex,10.99763,1.38767,3.19933  #   2
*vertex,10.99761,5.70353,3.68055  #   3
*vertex,13.87024,5.70353,3.68055  #   4
*vertex,10.99764,1.37880,3.27884  #   5
*vertex,13.87023,1.37880,3.27884  #   6
*vertex,13.87024,5.69466,3.76006  #   7
*vertex,10.99761,5.69466,3.76006  #   8
# 
# tag, number of vertices followed by list of associated vert
*edges,4,1,2,3,4  #   1
*edges,4,7,8,5,6  #   2
*edges,4,4,3,8,7  #   3
*edges,4,1,4,7,6  #   4
*edges,4,2,1,6,5  #   5
*edges,4,3,2,5,8  #   6
# 
# surf attributes:
#  surf name, surf position VERT/CEIL/FLOR/SLOP/UNKN
#  child of (surface name), useage (pair of tags) 
#  construction name, optical name
#  boundary condition tag followed by two data items
*surf,pvt_1_R,SLOP,-,-,-,CT_Wall_Roof,OPAQUE,ANOTHER,017,017  #   1 ||< pvt_R_1:Roof
*surf,pvt_1,SLOP,-,-,-,CT_PVT_semi_Tr,PVmod_opt,EXTERIOR,00,000  #   2 ||< external
*surf,pvt_1_2,SLOP,-,-,-,CT_Wall_Roof,OPAQUE,ANOTHER,006,003  #   3 ||< pvt_2_1:R_Pvt_2
*surf,pvt_1_E,VERT,-,-,-,CT_Wall_Roof,OPAQUE,EXTERIOR,00,000  #   4 ||< external
*surf,pvt_1_S,SLOP,-,-,-,CT_Wall_Roof,OPAQUE,EXTERIOR,00,000  #   5 ||< external
*surf,pvt_1_4,VERT,-,-,-,CT_Wall_Roof,OPAQUE,ANOTHER,004,006  #   6 ||< pvt_4_1:R_Pvt_4
# 
*insol,3,0,0,0  # default insolation distribution
# 
# shading directives
*shad_calc,none  # no temporal shading requested
# 
*insol_calc,none  # no insolation requested
# 
*base_list,0,0.00,0  # zone base
