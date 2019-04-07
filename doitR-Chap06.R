#06-02 133쪽 혼자서 해보기
#Q1
library(ggplot2)
library(dplyr)
mpg <- as.data.frame(ggplot2::mpg)
View(mpg)
mpg_displ4 <- mpg %>% filter(displ<=4)
mpg_displ5 <- mpg %>% filter(displ>=5)
mean(mpg_displ4$hwy)
mean(mpg_displ5$hwy)
#Q2
mpg_audi <- mpg %>% filter(manufacturer=="audi")
mpg_toyota <- mpg %>% filter(manufacturer=="toyota")
mean(mpg_audi$cty)
mean(mpg_toyota$cty)
#Q3
mpg_new <- mpg %>% filter(manufacturer %in% c("chevrolet", "ford", "honda"))
mean(mpg_new$hwy)

#06-03 138쪽 혼자서 해보기
#Q1
library(ggplot2)
library(dplyr)
mpg <- as.data.frame(ggplot2::mpg)
mpg_1 <- mpg %>% select(class, cty)
head(mpg_1, 3)
#Q2
mpg_suv <- mpg_1 %>% filter(class=="suv")
mpg_compact <- mpg_1 %>% filter(class=="compact")
mean(mpg_suv$cty)
mean(mpg_compact$cty)

#06-04 141쪽 혼자서 해보기
#Q1
library(ggplot2)
library(dplyr)
mpg <- as.data.frame(ggplot2::mpg)
mpg %>% 
  filter(manufacturer=="audi") %>%
  select(manufacturer, hwy) %>%
  arrange(desc(hwy)) %>%
  head(5)

#06-05 144쪽 혼자서 해보기
#Q1
library(ggplot2)
library(dplyr)
mpg <- as.data.frame(ggplot2::mpg)
mpg_new <- mpg
mpg_new %>%
  mutate(total = hwy + cty)
#Q2
mpg_new %>%
  mutate(total_mean = total/2)
#Q3
mpg_new %>%
  arrange(desc(total_mean)) %>%
  head(3)
#Q4
mpg %>%
  mutate(total = hwy + cty,
         total_mean = (hwy + cty)/2) %>%
  arrange(desc(total_mean)) %>%
  head(3)

#06-06 150쪽 혼자서 해보기
#Q1
library(ggplot2)
library(dplyr)
mpg <- as.data.frame(ggplot2::mpg)
mpg %>%
  group_by(class) %>%
  summarise(mean = mean(cty))
#Q2
mpg %>% arrange(desc(cty))
#Q3
mpg %>%
  group_by(class) %>%
  summarise(mean_hwy = mean(hwy))
  arrange(desc(hwy))
  head(3)
#Q4
mpg %>%
  filter(class=="compact") %>%
  group_by(manufacturer) %>%
  summarise(count = n()) %>%
  arrange(desc(count))

#06-07 157쪽 혼자서 해보기
library(ggplot2)
library(dplyr)
fuel <- data.frame(f1 = c("c", "d", "e", "p", "r"),
                   price_f1 = c(2.35, 2.38, 2.11, 2.76, 2.22),
                   stringsAsFactors = F)
fuel
#Q1
mpg <- as.data.frame(ggplot2::mpg)
mpg_new %>% left_join(mpg, fuel, by = "f1")
#Q2
mpg_new %>% select(model, f1, price_f1) %>% head(5)