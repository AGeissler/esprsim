*Geometry 1.1,GEN,Kitchen # tag version, format, zone name
*date Mon Aug 17 19:18:34 2020  # latest file modification 
Kitchen describes a room for food
*previous_rotate   180.00,  13.120,  10.600  # prior rotation angle X Y
# tag, X co-ord, Y co-ord, Z co-ord
*vertex,7.20001,9.30001,0.00000  #   1
*vertex,3.99999,9.30001,0.00000  #   2
*vertex,4.00000,6.30001,0.00000  #   3
*vertex,7.20000,6.29999,0.00000  #   4
*vertex,7.20001,9.30001,3.00000  #   5
*vertex,3.99999,9.30001,3.00000  #   6
*vertex,4.00000,6.30001,3.00000  #   7
*vertex,7.20000,6.29999,3.00000  #   8
*vertex,6.60000,9.30000,1.00000  #   9
*vertex,4.60000,9.30000,1.00000  #  10
*vertex,4.60000,9.30000,2.25000  #  11
*vertex,6.60000,9.30000,2.25000  #  12
*vertex,7.20000,7.57500,0.00000  #  13
*vertex,7.20000,7.57500,2.25000  #  14
*vertex,7.20000,6.57500,2.25000  #  15
*vertex,7.20000,6.57500,0.00000  #  16
# 
# tag, number of vertices followed by list of associated vert
*edges,10,1,2,6,11,10,9,12,11,6,5  #   1
*edges,4,2,3,7,6  #   2
*edges,4,5,6,7,8  #   3
*edges,6,1,13,16,4,3,2  #   4
*edges,4,9,10,11,12  #   5
*edges,8,13,1,5,8,4,16,15,14  #   6
*edges,4,3,4,8,7  #   7
*edges,4,16,13,14,15  #   8
# 
# surf attributes:
#  surf name, surf position VERT/CEIL/FLOR/SLOP/UNKN
#  child of (surface name), useage (pair of tags) 
#  construction name, optical name
#  boundary condition tag followed by two data items
*surf,Kitc_N,VERT,-,WALL,-,CT_Ext_Wall,OPAQUE,EXTERIOR,00,000  #   1 ||< external
*surf,Kitc_Bd3,VERT,-,PARTN,-,CT_Int_Wall,OPAQUE,ANOTHER,008,002  #   2 ||< Kitc_Bd3:BedRoom_3
*surf,Ceil_Kitc,CEIL,-,PARTN,-,CT_Ceiling,OPAQUE,ANOTHER,009,009  #   3 ||< Ceil_Kitc:Roof
*surf,Grd_Kitc,FLOR,-,-,-,CT_Ground,OPAQUE,GROUND,0,002  #   4 ||< user def grnd profile  2
*surf,Win_Kitc,VERT,Kitc_N,C-WINDOW,CRACK,CT_Ext_Window,SCF8783_06nb,EXTERIOR,00,000  #   5 ||< external
*surf,Sal_Kitc_1,VERT,-,PARTN,-,CT_Int_Wall,OPAQUE,ANOTHER,002,006  #   6 ||< Sal_Kitc_1:Salon
*surf,Sal_Kitc_2,VERT,-,PARTN,-,CT_Int_Wall,OPAQUE,ANOTHER,003,007  #   7 ||< Sal_Kitc_2:Salon
*surf,Door_Sal_Kit,VERT,Sal_Kitc_1,DOOR,UNDERCUT,CT_Int_Door,OPAQUE,ANOTHER,022,008  #   8 ||< Door_Sal_Kit:Salon
# 
*insol,3,0,0,0  # default insolation distribution
# 
# shading directives
*shad_calc,all_applicable   2 # list of surfs
  1  5
# 
*insol_calc,all_applicable   1 # insolation sources
  5
# 
*base_list,0,9.60,0  # zone base
# 
# block entities:
#  *obs = obstructions
*block_start, 20 20 # geometric blocks
*obs,0.0000,9.3000,2.9500,11.4900,2.0000,0.0500,0.00,1.00,kitc_obs CT_wall_obs  # block   1
*end_block
