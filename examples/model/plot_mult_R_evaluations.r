#!/usr/bin/env Rscript
#
# Last changed: 14/12/2017
# Status: development
# Generate various evaluations by call to external R scripts.
# Basis for all selected variables is h3k (.csv) file from simulation
# run.
#
# Expects 1 parameter(s) on call!
#   <file>  The results file (.csv)
#
suppressMessages(library(tools, quietly = T))
suppressMessages(library(plyr, quietly = T))
suppressMessages(library(crop, quietly = T))

args = commandArgs(trailingOnly=TRUE)

# Test if there is (at least) one argument: if not, return an error
if (length(args)==0) {
  stop("** Input file name(s) must be supplied (input file).n", call.=FALSE)
}
##else if (length(args)==1) {
##  # default output file
##  args[2] = "out.txt"
##}

## Define "calendar"
#https://stackoverflow.com/questions/29199181/boxplot-by-date-in-r
Sys.setenv(TZ="Europe/Berlin")

writeLines(" ")
cat("   R postprocessing, reading input file")

##filenam <- strsplit(args[1], "\\.")[[1]]
file_base <- file_path_sans_ext(args[1])

if (length(args)==1) {
    cat(" ...")
    df<-read.csv(file=args[1],header=T,sep=",")
    df[,"thedate"]<-as.Date(df$building.day.number.present..days.,origin = "2017-01-01")
} else {
    cat("s ...")
    df1<-read.csv(file=args[1],header=T,sep=",")
    df2<-read.csv(file=args[2],header=T,sep=",")

    df1[,"thedate"]<-as.Date(mv1$building.day.number.present..days.,origin = "2017-01-01")
    df2[,"thedate"]<-as.Date(mv2$building.day.number.present..days.,origin = "2016-01-01")
    df<-rbind(df2,df1)
}

writeLines(" done.")

## Monthly box plots
#https://togaware.com/datamining/survivor/Grouping_Time.html
mons<-c("January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November",
        "December")
smons<-c("Jan", "Feb", "Mar", "Apr", "May", "Jun",
         "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

observer.months <- ordered(months(df$thedate),
                           levels=mons,
                           labels=smons)

bZoneTemps<-F
bSolRad<-F
bPVeff<-T
bNodeTemps<-F
bqInt<-F
btandq<-F
bmeteo<-F

## Choose if fixed scales should be used
bFixedScales<-T

###############################################
## Zone air temperature color maps
if (bZoneTemps==T) {
  cat("   Creating colour field plots for indoor air temperatures ...")
  outputfile <- paste(file_base,"_zoneTmaps.png", sep="")
  source("plot_mult_zoneT_maps.r")
  writeLines(" done.")
}

###############################################
## Solar radiation incidence color maps
if (bSolRad==T) {
    cat("   Creating colour field plots for direct and diffuse incident solar radiation ...")
    outputfile <- paste(file_base,"_solRadmaps.png", sep="")
    outputfile2 <- paste(file_base,"_solTotRadmaps.png", sep="")
    source("plot_mult_rad_maps.r")
    writeLines(" done.")
}

################################################
## Surface convective coefficients of interest
if (bPVeff==T) {
  cat("   Creating plots for PV efficiency ...")
  outputfile <- paste(file_base,"_PVeff", sep="")
  source("plot_PV_efficiency.r")
  writeLines(" done.")
}

#################################################
## Vertical section temperature range
if (bNodeTemps==T) {
  cat("   Creating node temperature plot ...")
  outputfile <- paste(file_base,"_NodeTemps", sep="")
  source("plot_t_xsec.r")
  writeLines(" done.")
}

#################################################
## Internal glass pane heat flux
if (bqInt==T) {
    cat("   Creating internal glass pane heat flux plot ...")
    outputfile <- paste(file_base,"_qInt", sep="")
    source("plot_q_int.r")
    writeLines(" done.")
}

#################################################
## Zone air temperatures and cooling load
if (btandq==T) {
    cat("   Creating zone air temperature and cooling load plots ...")
    outputfile <- paste(file_base,"", sep="")
    source("plot_q_and_tair.r")
    writeLines(" done.")
}

#################################################
## Ambient air temperature and total solar on facade
if (bmeteo==T) {
    cat("   Creating ambient air temperature and solar incidence plot ...")
    outputfile <- paste(file_base,"_meteo", sep="")
    source("plot_meteo.r")
    writeLines(" done.")
}

###### Multiple time-series plots at once ...
#https://cran.r-project.org/web/packages/timelineR/vignettes/plot_timeline.html

writeLines(" ")

# Clean up (?)
rm(list = ls(all.names = TRUE))
