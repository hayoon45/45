#07-01 p.170
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

#07-02 p.178
library(ggplot2)
library(dplyr)
mpg <- as.data.frame(ggplot2::mpg)
mpg[c(10, 14, 58, 93), "drv"] <- "k"
mpg[c(29, 43, 129, 203), "cty"] <- c(3, 4, 39, 42)
#Q1
table(mpg$drv)
#%in% not use and use case.
mpg$drv <- ifelse(mpg$drv == "k", NA, mpg$drv)
mpg$drv <- ifelse(mpg$drv %in% c("4", "f", "r"), mpg$drv, NA)
table(mpg$drv)
#Q2
boxplot(mpg$cty)$stats
mpg$cty <- ifelse(mpg$cty < 9 | mpg$cty > 26, NA, mpg$cty)
boxplot(mpg$cty)
#Q3
mpg %>%
  filter(!is.na(cty) & !is.na(drv)) %>%
  group_by(drv) %>%
  summarise(mean_cty = mean(cty))
