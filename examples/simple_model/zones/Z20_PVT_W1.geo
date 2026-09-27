*Geometry 1.1,GEN,Z20_PVT_W1 # tag version, format, zone name
*date Sun Sep 27 17:02:36 2026  # latest file modification 
Z20_PVT_W1 describes the PVT W1 air channel zone
# tag, X co-ord, Y co-ord, Z co-ord
*vertex,6.00000,0.00000,2.70000  #   1
*vertex,7.50000,0.00000,2.70000  #   2
*vertex,7.50000,1.87938,3.38404  #   3
*vertex,6.00000,1.87938,3.38404  #   4
*vertex,6.00000,0.00000,2.75000  #   5
*vertex,7.50000,0.00000,2.75000  #   6
*vertex,7.50000,1.87938,3.43404  #   7
*vertex,6.00000,1.87938,3.43404  #   8
# 
# tag, number of vertices followed by list of associated vert
*edges,4,1,2,6,5  #   1
*edges,4,2,3,7,6  #   2
*edges,4,3,4,8,7  #   3
*edges,4,4,1,5,8  #   4
*edges,4,5,6,7,8  #   5
*edges,4,1,4,3,2  #   6
# 
# surf attributes:
#  surf name, surf position VERT/CEIL/FLOR/SLOP/UNKN
#  child of (surface name), useage (pair of tags) 
#  construction name, optical name
#  boundary condition tag followed by two data items
*surf,Wall-1,VERT,-,-,-,fictitious,SC_fictit,EXTERIOR,00,000  #   1 ||< external
*surf,Wall-2,VERT,-,-,-,PVT_sideplate,OPAQUE,ANOTHER,12,004  #   2 ||< Wall-4:Z20_PVT_E1
*surf,Wall-3,VERT,-,-,-,fictitious,SC_fictit,ANOTHER,10,001  #   3 ||< Wall-1:Z20_PVT_W2
*surf,Wall-4,VERT,-,-,-,PVT_sideplate,OPAQUE,EXTERIOR,00,000  #   4 ||< external
*surf,Top-5,SLOP,-,-,-,PVT_type1,PVT_opt,EXTERIOR,00,000  #   5 ||< external
*surf,Base-6,FLOR,-,-,-,Douala_roof_inv,OPAQUE,ANOTHER,08,006  #   6 ||< Z20_PVT_W1:Z20
# 
*insol,3,0,0,0  # default insolation distribution
# 
# shading directives
*shad_calc,none  # no temporal shading requested
# 
*insol_calc,none  # no insolation requested
# 
*base_list,0,3.00,0  # zone base
