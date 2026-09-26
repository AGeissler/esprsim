*Geometry 1.1,GEN,Cellar # tag version, format, zone name
*date Mon Aug 17 19:18:34 2020  # latest file modification 
Cellar describes a place in which the provision are kept
*previous_rotate   180.00,  13.120,  10.600  # prior rotation angle X Y
# tag, X co-ord, Y co-ord, Z co-ord
*vertex,11.84999,9.29998,0.00000  #   1
*vertex,10.75000,9.30000,0.00000  #   2
*vertex,10.75000,7.30000,0.00000  #   3
*vertex,10.75002,6.30000,0.00000  #   4
*vertex,11.85000,6.30001,0.00000  #   5
*vertex,11.84999,9.29998,3.00000  #   6
*vertex,10.75000,9.30000,3.00000  #   7
*vertex,10.75000,7.30000,3.00000  #   8
*vertex,10.75002,6.30000,3.00000  #   9
*vertex,11.85000,6.30001,3.00000  #  10
*vertex,10.75000,7.20000,0.00000  #  11
*vertex,10.75000,6.40000,0.00000  #  12
*vertex,10.75000,6.40000,2.25000  #  13
*vertex,10.75000,7.20000,2.25000  #  14
*vertex,11.84999,6.57500,0.00000  #  15
*vertex,11.85000,7.57500,0.00000  #  16
*vertex,11.85000,7.57500,2.25000  #  17
*vertex,11.84999,6.57500,2.25000  #  18
# 
# tag, number of vertices followed by list of associated vert
*edges,4,1,2,7,6  #   1
*edges,4,2,3,8,7  #   2
*edges,8,3,11,14,13,12,4,9,8  #   3
*edges,4,4,5,10,9  #   4
*edges,8,5,15,18,17,16,1,6,10  #   5
*edges,5,6,7,8,9,10  #   6
*edges,9,1,16,15,5,4,12,11,3,2  #   7
*edges,4,11,12,13,14  #   8
*edges,4,15,16,17,18  #   9
# 
# surf attributes:
#  surf name, surf position VERT/CEIL/FLOR/SLOP/UNKN
#  child of (surface name), useage (pair of tags) 
#  construction name, optical name
#  boundary condition tag followed by two data items
*surf,Cel_frt,VERT,-,WALL,-,CT_Ext_Wall,OPAQUE,EXTERIOR,00,000  #   1 ||< external
*surf,Cel-WC,VERT,-,PARTN,-,CT_Int_Wall,OPAQUE,ANOTHER,006,002  #   2 ||< Cel-WC:WC
*surf,Sal-Cel_1,VERT,-,PARTN,-,CT_Int_Wall,OPAQUE,ANOTHER,014,003  #   3 ||< Sal-Cel_1:Salon
*surf,Sal-Cal_2,VERT,-,PARTN,-,CT_Int_Wall,OPAQUE,ANOTHER,015,004  #   4 ||< Sal-Cal_2:Salon
*surf,Cel-Gar,VERT,-,PARTN,-,CT_Int_Wall,OPAQUE,ANOTHER,010,005  #   5 ||< Cel-Gar:Garage
*surf,Ceil-Cel,CEIL,-,PARTN,-,CT_Ceiling,OPAQUE,ANOTHER,004,004  #   6 ||< Ceil-Cel:Roof
*surf,Grd_cellar,FLOR,-,-,-,CT_Ground,OPAQUE,GROUND,0,002  #   7 ||< user def grnd profile  2
*surf,door-Sal_Cel,VERT,Sal-Cel_1,DOOR,UNDERCUT,CT_Int_Door,OPAQUE,ANOTHER,019,008  #   8 ||< door-Sal_Cel:Salon
*surf,door-Cel_Gar,VERT,Cel-Gar,DOOR,UNDERCUT,CT_Int_Door,OPAQUE,ANOTHER,011,009  #   9 ||< door-Cel_Gar:Garage
# 
*insol,3,0,0,0  # default insolation distribution
# 
# shading directives
*shad_calc,none  # no temporal shading requested
# 
*insol_calc,none  # no insolation requested
# 
*base_list,0,3.30,0  # zone base
