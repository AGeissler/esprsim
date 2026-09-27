*Geometry 1.1,GEN,Z00 # tag version, format, zone name
*date Sun Sep 27 21:05:13 2026  # latest file modification 
Z00 describes the flat PVT orientation
# tag, X co-ord, Y co-ord, Z co-ord
*vertex,0.00000,-0.00000,0.00000  #   1
*vertex,3.00000,-0.00000,0.00000  #   2
*vertex,3.00000,6.00000,0.00000  #   3
*vertex,-0.00000,6.00000,0.00000  #   4
*vertex,0.00000,-0.00000,2.70000  #   5
*vertex,3.00000,-0.00000,2.70000  #   6
*vertex,3.00000,6.00000,2.70000  #   7
*vertex,-0.00000,6.00000,2.70000  #   8
*vertex,1.50000,-0.00000,2.70000  #   9
*vertex,1.50000,6.00000,2.70000  #  10
*vertex,0.00000,2.00000,2.70000  #  11
*vertex,0.00000,4.00000,2.70000  #  12
*vertex,3.00000,4.00000,2.70000  #  13
*vertex,3.00000,2.00000,2.70000  #  14
*vertex,1.50000,2.00000,2.70000  #  15
*vertex,1.50000,4.00000,2.70000  #  16
# 
# tag, number of vertices followed by list of associated vert
*edges,5,1,2,6,9,5  #   1
*edges,6,2,3,7,13,14,6  #   2
*edges,5,3,4,8,10,7  #   3
*edges,6,4,1,5,11,12,8  #   4
*edges,4,1,4,3,2  #   5
*edges,4,5,9,15,11  #   6
*edges,4,11,15,16,12  #   7
*edges,4,12,16,10,8  #   8
*edges,4,9,6,14,15  #   9
*edges,4,15,14,13,16  #  10
*edges,4,16,13,7,10  #  11
# 
# surf attributes:
#  surf name, surf position VERT/CEIL/FLOR/SLOP/UNKN
#  child of (surface name), useage (pair of tags) 
#  construction name, optical name
#  boundary condition tag followed by two data items
*surf,Wall-1,VERT,-,-,-,extern_wall,OPAQUE,EXTERIOR,00,000  #   1 ||< external
*surf,Wall-2,VERT,-,-,-,extern_wall,OPAQUE,EXTERIOR,00,000  #   2 ||< external
*surf,Wall-3,VERT,-,-,-,extern_wall,OPAQUE,EXTERIOR,00,000  #   3 ||< external
*surf,Wall-4,VERT,-,-,-,extern_wall,OPAQUE,EXTERIOR,00,000  #   4 ||< external
*surf,Base-6,FLOR,-,-,-,grnd_floor,OPAQUE,GROUND,01,0  #   5 ||< ground profile  1
*surf,Z00_PVT_W1,CEIL,-,-,-,Douala_roof,OPAQUE,ANOTHER,02,006  #   6 ||< Base-6:Z00_PVT_W1
*surf,Z00_PVT_W2,CEIL,-,-,-,Douala_roof,OPAQUE,ANOTHER,03,006  #   7 ||< Base-6:Z00_PVT_W2
*surf,Z00_PVT_W3,CEIL,-,-,-,Douala_roof,OPAQUE,ANOTHER,04,006  #   8 ||< Base-6:Z00_PVT_W3
*surf,Z00_PVT_E1,CEIL,-,-,-,Douala_roof,OPAQUE,ANOTHER,05,006  #   9 ||< Base-6:Z00_PVT_E1
*surf,Z00_PVT_E2,CEIL,-,-,-,Douala_roof,OPAQUE,ANOTHER,06,006  #  10 ||< Base-6:Z00_PVT_E2
*surf,Z00_PVT_E3,CEIL,-,-,-,Douala_roof,OPAQUE,ANOTHER,07,006  #  11 ||< Base-6:Z00_PVT_E3
# 
*insol,3,0,0,0  # default insolation distribution
# 
# shading directives
*shad_calc,none  # no temporal shading requested
# 
*insol_calc,none  # no insolation requested
# 
*base_list,0,18.00,0  # zone base
