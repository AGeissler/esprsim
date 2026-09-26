*Geometry 1.1,GEN,BedRoom_3 # tag version, format, zone name
*date Mon Aug 17 19:18:34 2020  # latest file modification 
BedRoom_3 describes a room for bed
*previous_rotate   180.00,  13.120,  10.600  # prior rotation angle X Y
# tag, X co-ord, Y co-ord, Z co-ord
*vertex,3.99999,9.30001,0.00000  #   1
*vertex,0.00000,9.30000,0.00000  #   2
*vertex,0.00001,5.65000,0.00000  #   3
*vertex,2.50000,5.65000,0.00000  #   4
*vertex,3.99998,5.64999,0.00000  #   5
*vertex,4.00000,6.30001,0.00000  #   6
*vertex,3.99999,9.30001,3.00000  #   7
*vertex,0.00000,9.30000,3.00000  #   8
*vertex,0.00001,5.65000,3.00000  #   9
*vertex,2.50000,5.65000,3.00000  #  10
*vertex,3.99998,5.64999,3.00000  #  11
*vertex,4.00000,6.30001,3.00000  #  12
*vertex,3.75000,5.65000,0.00000  #  13
*vertex,3.75000,5.65000,2.25000  #  14
*vertex,2.75000,5.65000,2.25000  #  15
*vertex,2.75000,5.65000,0.00000  #  16
*vertex,3.10000,9.30000,1.00000  #  17
*vertex,1.10000,9.30000,1.00000  #  18
*vertex,1.10000,9.30000,2.25000  #  19
*vertex,3.10000,9.30000,2.25000  #  20
# 
# tag, number of vertices followed by list of associated vert
*edges,10,1,2,8,7,20,19,18,17,20,7  #   1
*edges,4,2,3,9,8  #   2
*edges,4,3,4,10,9  #   3
*edges,6,7,8,9,10,11,12  #   4
*edges,8,1,6,5,13,16,4,3,2  #   5
*edges,4,5,6,12,11  #   6
*edges,8,13,5,11,10,4,16,15,14  #   7
*edges,4,6,1,7,12  #   8
*edges,4,16,13,14,15  #   9
*edges,4,17,18,19,20  #  10
# 
# surf attributes:
#  surf name, surf position VERT/CEIL/FLOR/SLOP/UNKN
#  child of (surface name), useage (pair of tags) 
#  construction name, optical name
#  boundary condition tag followed by two data items
*surf,Bd3_S,VERT,-,WALL,-,CT_Ext_Wall,OPAQUE,EXTERIOR,00,000  #   1 ||< external
*surf,Bd3_W,VERT,-,WALL,-,CT_Ext_Wall,OPAQUE,EXTERIOR,00,000  #   2 ||< external
*surf,Bd3_Bth2,VERT,-,PARTN,-,CT_Int_Wall,OPAQUE,ANOTHER,004,004  #   3 ||< Bd3_Bth2:BathRoom_2
*surf,Ceil_Bd3,CEIL,-,PARTN,-,CT_Ceiling,OPAQUE,ANOTHER,010,010  #   4 ||< Ceil_Bd3:Roof
*surf,Grd_Bd3,FLOR,-,-,-,CT_Ground,OPAQUE,GROUND,0,003  #   5 ||< user def grnd profile  3
*surf,Sal_Bd3_1,VERT,-,PARTN,-,CT_Int_Wall,OPAQUE,ANOTHER,004,006  #   6 ||< Sal_Bd3_1:Salon
*surf,Sal_Bd3_2,VERT,-,PARTN,-,CT_Int_Wall,OPAQUE,ANOTHER,005,007  #   7 ||< Sal_Bd3_2:Salon
*surf,Kitc_Bd3,VERT,-,PARTN,-,CT_Int_Wall,OPAQUE,ANOTHER,002,008  #   8 ||< Kitc_Bd3:Kitchen
*surf,Dr_Sal_Bd3,VERT,Sal_Bd3_2,DOOR,UNDERCUT,CT_Int_Door,OPAQUE,ANOTHER,023,009  #   9 ||< Door_Sal_Bd3:Salon
*surf,Win_Bd3,VERT,Bd3_S,C-WINDOW,CRACK,CT_Ext_Window,SCF8783_06nb,EXTERIOR,00,000  #  10 ||< external
# 
*insol,3,0,0,0  # default insolation distribution
# 
# shading directives
*shad_calc,all_applicable   3 # list of surfs
  1  2 10
# 
*insol_calc,all_applicable   1 # insolation sources
 10
# 
*base_list,0,14.60,0  # zone base
# 
# block entities:
#  *obs = obstructions
*block_start, 20 20 # geometric blocks
*obs,0.0000,9.3000,2.9500,11.4900,2.0000,0.0500,0.00,1.00,bed3_obs CT_wall_obs  # block   1
*end_block
