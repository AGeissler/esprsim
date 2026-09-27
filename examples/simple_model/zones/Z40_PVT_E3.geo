*Geometry 1.1,GEN,Z40_PVT_E3 # tag version, format, zone name
*date Sun Sep 27 21:11:22 2026  # latest file modification 
Z40_PVT_E3 describes the PVT E3 air channel zone
# tag, X co-ord, Y co-ord, Z co-ord
*vertex,13.50000,3.06418,5.27115  #   1
*vertex,15.00000,3.06418,5.27115  #   2
*vertex,15.00000,4.59627,6.55673  #   3
*vertex,13.50000,4.59627,6.55673  #   4
*vertex,13.50000,3.06418,5.32115  #   5
*vertex,15.00000,3.06418,5.32115  #   6
*vertex,15.00000,4.59627,6.60673  #   7
*vertex,13.50000,4.59627,6.60673  #   8
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
*surf,Wall-1,VERT,-,-,-,fictitious,SC_fictit,ANOTHER,20,003  #   1 ||< Wall-3:Z40_PVT_E2
*surf,Wall-2,VERT,-,-,-,PVT_sideplate,OPAQUE,EXTERIOR,00,000  #   2 ||< external
*surf,Wall-3,VERT,-,-,-,fictitious,SC_fictit,EXTERIOR,00,000  #   3 ||< external
*surf,Wall-4,VERT,-,-,-,PVT_sideplate,OPAQUE,ANOTHER,18,002  #   4 ||< Wall-2:Z40_PVT_W3
*surf,Top-5,SLOP,-,-,-,PVT_type1,PVT_opt,EXTERIOR,00,000  #   5 ||< external
*surf,Base-6,FLOR,-,-,-,Douala_roof_inv,OPAQUE,ANOTHER,15,011  #   6 ||< Z40_PVT_E3:Z40
# 
*insol,3,0,0,0  # default insolation distribution
# 
# shading directives
*shad_calc,none  # no temporal shading requested
# 
*insol_calc,none  # no insolation requested
# 
*base_list,0,3.00,0  # zone base
