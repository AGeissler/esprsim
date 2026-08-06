#
# Last changed: 11/07/2019
# Status: usable
#
# Generate
#
# Expects dataframe "df" to be defined/filled/available!
#

# building:spmatl:Z00 W1:misc data:efficiency %
grx <- glob2rx("building.spmatl.Z*0.W1.misc.data.efficiency..")
pveff<-df[,c("building.time.present..hours.",
           "building.day.number.present..days.",
           "thedate",
           grep(grx, names(df), ignore.case = TRUE, value = TRUE, perl = TRUE))]

## Set column names
colnames(pveff)<-c("hour","day","thedate",sapply(strsplit(colnames(pveff[4:length(pveff)]),"\\."),
                 FUN=function(x){paste(x[3],x[4],x[7], sep="_")},
                 simplify = TRUE, USE.NAMES = TRUE))

# building:spmatl:Z00 W1:misc data:total incident irradiance:unit area (W/m^2)
grx <- glob2rx("building.spmatl.Z*0.W1.misc.data.total.incident.irradiance.unit.area..W.m.2.")
irrad<-df[,c(grep(grx, names(df), ignore.case = TRUE, value = TRUE, perl = TRUE))]

## Set column names
colnames(irrad)<-c(sapply(strsplit(colnames(irrad[1:length(irrad)]),"\\."),
                 FUN=function(x){paste(x[3],x[4],x[9], sep="_")},
                 simplify = TRUE, USE.NAMES = TRUE))

# building:Z00 PVT W1:Top-5:node 04:temperature (oC)
grx <- glob2rx("building.Z*0.PVT.W1.Top.5.node.04.temperature..oC.")
pvtemp<-df[,c(grep(grx, names(df), ignore.case = TRUE, value = TRUE, perl = TRUE))]

## Set column names
colnames(pvtemp)<-c(sapply(strsplit(colnames(pvtemp[1:length(pvtemp)]),"\\."),
                 FUN=function(x){paste(x[2],x[4],x[8],x[9], sep="_")},
                 simplify = TRUE, USE.NAMES = TRUE))

## Add irrad and pvtemp to pveff ...
pveff<-cbind(pveff,irrad,pvtemp)

## Set plot output file to type png
nrow<-1
ncol<-1

outputfile <- paste(outputfile,".png", sep="")
png(file = outputfile, width=6*ncol, height=6*nrow, units= "in", res=300, type="quartz", bg = "transparent")

## Possibly set slightly more space for y-label because of exponent?
## (https://stackoverflow.com/questions/8100765/y-axis-label-falling-outside-graphics-window)
#mar.default <- c(5,4,4,2) + 0.1
#par(mar = mar.default + c(0, 4, 0, 0))

## Filter the efficiency data by total incident radiation on the PV panel
pveff_low<-subset(pveff, Z00_W1_irradiance>190.0 & Z00_W1_irradiance <220.0)
pveff_high<-subset(pveff, Z00_W1_irradiance>700.0 & Z00_W1_irradiance <800.0)

## Create multiple graphs on single pane (here: one row, two columns)
old.par<-par(mfrow = c(nrow, ncol))

## Plot
plot(pveff_low$Z00_W1_04_temperatur,pveff_low$Z00_W1_efficiency,
            main="",
            xlab="temperature [°C]",
#            ylab=expression("h"[ci]*" [W/(m"^2*"K)]"),
            ylab="efficiency [%]",
            col="blue",pch=21,cex=0.7,
            ylim=c(0,20),
            xlim=c(20,90),
            las=1,xaxs="i",yaxs="i")

# Add grid
grid(nx = 8, ny = 10,
     col = "lightgray",
     lty = "dotted",
     lwd = 1.25,
     equilogs = TRUE)

points(pveff_high$Z00_W1_04_temperatur,pveff_high$Z00_W1_efficiency,  col="red",  pch=22,cex=0.7)

#points(flow$blind_gap/bgapcross/3600.,hci$blind_gap_baffle_HCi,col="green",pch=23,cex=0.7)

reg1 <- lm(pveff_low$Z00_W1_efficiency ~ pveff_low$Z00_W1_04_temperatur,data=pveff_low)
reg2 <- lm(pveff_high$Z00_W1_efficiency ~ pveff_high$Z00_W1_04_temperatur, data=pveff_high)

text(21.0, 4.0, paste("intercept = ", round(coef(reg1)[1],2),
                      "\n   slope = ", round(coef(reg1)[2],3)
                ),
               cex = 1.0,
               adj = 0,
               col = "blue")

text(21.0, 2.0, paste("intercept = ", round(coef(reg2)[1],2),
                      "\n   slope = ", round(coef(reg2)[2],3)
                ),
               cex = 1.0,
               adj = 0,
               col = "red")

clip(25,55, -100, 100)
abline(reg1, col="blue")

clip(70,85, -100, 100)
abline(reg2, col="red")

#text(2.0, 4.5, expression(h[ci]*" ext_gap"),
#               cex = 1.0,
#               adj = 0,
#               col = "red")
#
#text(2.0, 3.0, expression(h[ci]*" blind_gap"),
#               cex = 1.0,
#               adj = 0,
#               col = "green")
#
#text(0.1, 13.2,paste(case,
#                     "\nctl      : ",ctl,
#                     "\nsetp hx: ",setp," \u00B0C",
#                     "\nvmax   : ",vmax," l/s",
#                     "\nintld  :",intld,
#                     "\nsim-per:",per
#                   ),
#               cex = 0.7,
#               adj = 0,
#               col = "black")

# Clean up (?)
#rm(list = ls(all.names = TRUE))

dev.off.crop(file=outputfile)
#system(paste("pdfcrop", filename, filename))
