#혼자서 해보기 7-1
library(ggplot2)
library(dplyr)
mpg <- as.data.frame(ggplot2::mpg)
mpg[c(65, 124, 131, 153, 212), "hwy"] <- NA
#Q1
table(is.na(mpg$drv))
table(is.na(mpg$hwy))
#Q2
mpg %>% 
  filter(!is.na(hwy)) %>%
  group_by(drv) %>%
  summarise(mean_hwy = mean(hwy)) %>%

#혼자서 해보기7-2
library(ggplot2)
library(dplyr)
mpg <- as.data.frame(ggplot2::mpg)
mpg[c(10, 14, 58, 93), "drv"] <- "k"
mpg[c(29, 43, 129, 203), "cty"] <- c(3, 4, 39, 42)
#Q1************
table(mpg$drv)
mpg$drv <- ifelse(mpg$drv == "k", NA, mpg$drv)
table(is.na(mpg$drv))
#Q2
boxplot(mpg$cty)
boxplot(mpg$cty)$stats
mpg$cty <- ifelse(mpg$cty < 9 | mpg$cty > 26, NA, mpg$cty)
boxplot(mpg$cty)
#Q3
mpg %>%
  filter(!is.na(mpg$cty) & !is.na(mpg$drv)) %>%
  group_by(drv) %>%
  summarise(mean_cty = mean(cty))
