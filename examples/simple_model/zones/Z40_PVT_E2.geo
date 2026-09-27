*Geometry 1.1,GEN,Z40_PVT_E2 # tag version, format, zone name
*date Sun Sep 27 17:02:36 2026  # latest file modification 
Z40_PVT_E2 describes the PVT E2 air channel zone
# tag, X co-ord, Y co-ord, Z co-ord
*vertex,13.50000,1.53209,3.98557  #   1
*vertex,15.00000,1.53209,3.98557  #   2
*vertex,15.00000,3.06418,5.27115  #   3
*vertex,13.50000,3.06418,5.27115  #   4
*vertex,13.50000,1.53209,4.03557  #   5
*vertex,15.00000,1.53209,4.03557  #   6
*vertex,15.00000,3.06418,5.32115  #   7
*vertex,13.50000,3.06418,5.32115  #   8
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
*surf,Wall-1,VERT,-,-,-,fictitious,SC_fictit,ANOTHER,19,003  #   1 ||< Wall-3:Z40_PVT_E1
*surf,Wall-2,VERT,-,-,-,PVT_sideplate,OPAQUE,EXTERIOR,00,000  #   2 ||< external
*surf,Wall-3,VERT,-,-,-,fictitious,SC_fictit,ANOTHER,21,001  #   3 ||< Wall-1:Z40_PVT_E3
*surf,Wall-4,VERT,-,-,-,PVT_sideplate,OPAQUE,ANOTHER,17,002  #   4 ||< Wall-2:Z40_PVT_W2
*surf,Top-5,CEIL,-,-,-,PVT_type1,PVT_opt,EXTERIOR,00,000  #   5 ||< external
*surf,Base-6,FLOR,-,-,-,Douala_roof_inv,OPAQUE,ANOTHER,15,010  #   6 ||< Z40_PVT_E2:Z40
# 
*insol,3,0,0,0  # default insolation distribution
# 
# shading directives
*shad_calc,none  # no temporal shading requested
# 
*insol_calc,none  # no insolation requested
# 
*base_list,0,3.00,0  # zone base
