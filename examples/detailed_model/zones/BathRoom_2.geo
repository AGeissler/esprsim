*Geometry 1.1,GEN,BathRoom_2 # tag version, format, zone name
*date Mon Aug 17 19:18:34 2020  # latest file modification 
BathRoom_2 describes a room for bath
*previous_rotate   180.00,  13.120,  10.600  # prior rotation angle X Y
# tag, X co-ord, Y co-ord, Z co-ord
*vertex,2.50000,5.65000,0.00000  #   1
*vertex,0.00001,5.65000,0.00000  #   2
*vertex,0.00000,3.65001,0.00000  #   3
*vertex,2.50000,3.65000,0.00000  #   4
*vertex,2.50000,5.65000,3.00000  #   5
*vertex,0.00001,5.65000,3.00000  #   6
*vertex,0.00000,3.65001,3.00000  #   7
*vertex,2.50000,3.65000,3.00000  #   8
*vertex,2.50001,5.15000,0.00000  #   9
*vertex,2.50001,5.15000,2.25000  #  10
*vertex,2.50000,4.15000,2.25000  #  11
*vertex,2.50000,4.15000,0.00000  #  12
# 
# tag, number of vertices followed by list of associated vert
*edges,4,2,3,7,6  #   1
*edges,4,5,6,7,8  #   2
*edges,6,1,9,12,4,3,2  #   3
*edges,4,1,2,6,5  #   4
*edges,4,3,4,8,7  #   5
*edges,8,9,1,5,8,4,12,11,10  #   6
*edges,4,12,9,10,11  #   7
# 
# surf attributes:
#  surf name, surf position VERT/CEIL/FLOR/SLOP/UNKN
#  child of (surface name), useage (pair of tags) 
#  construction name, optical name
#  boundary condition tag followed by two data items
*surf,Bth2_W,VERT,-,WALL,-,CT_Ext_Wall,OPAQUE,EXTERIOR,00,000  #   1 ||< external
*surf,Ceil_Bth2,CEIL,-,PARTN,-,CT_Ceiling,OPAQUE,ANOTHER,012,012  #   2 ||< Ceil_Bth2:Roof
*surf,Grd_Bth2,FLOR,-,-,-,CT_Ground,OPAQUE,GROUND,0,002  #   3 ||< user def grnd profile  2
*surf,Bd3_Bth2,VERT,-,PARTN,-,CT_Int_Wall,OPAQUE,ANOTHER,003,004  #   4 ||< Bd3_Bth2:BedRoom_3
*surf,Bd2_Bth2,VERT,-,PARTN,-,CT_Int_Wall,OPAQUE,ANOTHER,001,005  #   5 ||< Bd2_Bth2:BedRoom_2
*surf,Sal_Bth2,VERT,-,PARTN,-,CT_Int_Wall,OPAQUE,ANOTHER,006,006  #   6 ||< Sal_Bth2:Salon
*surf,Dr_Sal_Bth2,VERT,Sal_Bth2,PARTN,-,CT_Int_Door,OPAQUE,ANOTHER,024,007  #   7 ||< Dr_Sal_Bth22:Salon
# 
*insol,3,0,0,0  # default insolation distribution
# 
# shading directives
*shad_calc,none  # no temporal shading requested
# 
*insol_calc,none  # no insolation requested
# 
*base_list,0,5.00,0  # zone base
