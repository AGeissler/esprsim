*Geometry 1.1,GEN,WC # tag version, format, zone name
*date Mon Aug 17 19:18:34 2020  # latest file modification 
WC describes a water closet
*previous_rotate   180.00,  13.120,  10.600  # prior rotation angle X Y
# tag, X co-ord, Y co-ord, Z co-ord
*vertex,10.75000,9.30000,0.00000  #   1
*vertex,9.55001,9.30001,0.00000  #   2
*vertex,9.55000,7.30000,0.00000  #   3
*vertex,10.75000,7.30000,0.00000  #   4
*vertex,10.75000,9.30000,3.00000  #   5
*vertex,9.55001,9.30001,3.00000  #   6
*vertex,9.55000,7.30000,3.00000  #   7
*vertex,10.75000,7.30000,3.00000  #   8
*vertex,10.65000,9.30000,1.75000  #   9
*vertex,9.65000,9.30000,1.75000  #  10
*vertex,9.65000,9.30000,2.25000  #  11
*vertex,10.65000,9.30000,2.25000  #  12
*vertex,9.55001,8.59998,0.00000  #  13
*vertex,9.55000,7.60000,0.00000  #  14
*vertex,9.55000,7.60000,2.25000  #  15
*vertex,9.55001,8.59998,2.25000  #  16
# 
# tag, number of vertices followed by list of associated vert
*edges,10,1,2,6,11,10,9,12,11,6,5  #   1
*edges,8,2,13,16,15,14,3,7,6  #   2
*edges,4,3,4,8,7  #   3
*edges,4,5,6,7,8  #   4
*edges,6,1,4,3,14,13,2  #   5
*edges,4,4,1,5,8  #   6
*edges,4,9,10,11,12  #   7
*edges,4,13,14,15,16  #   8
# 
# surf attributes:
#  surf name, surf position VERT/CEIL/FLOR/SLOP/UNKN
#  child of (surface name), useage (pair of tags) 
#  construction name, optical name
#  boundary condition tag followed by two data items
*surf,WC_frt,VERT,-,WALL,-,CT_Ext_Wall,OPAQUE,EXTERIOR,00,000  #   1 ||< external
*surf,Sal-WC_1,VERT,-,PARTN,-,CT_Int_Wall,OPAQUE,ANOTHER,016,002  #   2 ||< Sal-WC_1:Salon
*surf,Sal-WC_2,VERT,-,PARTN,-,CT_Int_Wall,OPAQUE,ANOTHER,017,003  #   3 ||< Sal-WC_2:Salon
*surf,Ceil-WC,CEIL,-,PARTN,-,CT_Ceiling,OPAQUE,ANOTHER,005,005  #   4 ||< Ceil-WC:Roof
*surf,Grd-WC,FLOR,-,-,-,CT_Ground,OPAQUE,GROUND,0,001  #   5 ||< user def grnd profile  1
*surf,Cel-WC,VERT,-,PARTN,-,CT_Int_Wall,OPAQUE,ANOTHER,002,006  #   6 ||< Cel-WC:Cellar
*surf,Win_WC,VERT,WC_frt,C-WINDOW,CRACK,CT_Ext_Window,SCF8783_06nb,EXTERIOR,00,000  #   7 ||< external
*surf,door-Sal_WC,VERT,Sal-WC_1,DOOR,UNDERCUT,CT_Int_Door,OPAQUE,ANOTHER,020,008  #   8 ||< door-Sal_WC:Salon
# 
*insol,3,0,0,0  # default insolation distribution
# 
# shading directives
*shad_calc,all_applicable   2 # list of surfs
  1  7
# 
*insol_calc,all_applicable   1 # insolation sources
  7
# 
*base_list,0,2.40,0  # zone base
# 
# block entities:
#  *obs = obstructions
*block_start, 20 20 # geometric blocks
*obs,0.0000,9.3000,2.9500,11.4900,2.0000,0.0500,0.00,1.00,WC_obs_N NONE  # block   1
*end_block
