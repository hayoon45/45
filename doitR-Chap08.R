#p.188
library(ggplot2)
#Q1
ggplot(data = mpg, aes(x = cty, y = hwy)) + geom_point()
#Q2
View(midwest)
ggplot(data = midwest, aes(x = poptotal, y = popasian)) + geom_point() + xlim(0, 500000) + ylim(0, 10000)

#p,193
#Q1
library(ggplot2)
library(dplyr)
df <- mpg %>%
  filter(class=="suv") %>%
  group_by(manufacturer) %>%
  summarise(mean_cty = mean(cty)) %>%
  arrange(desc(mean_cty)) %>%
  head(5)
ggplot(data = df, aes(x = reorder(manufacturer, -mean_cty), y = mean_cty)) + geom_col()
#Q2
ggplot(data = mpg, aes(x = class)) + geom_bar()

#p.195
#Q1
View(economics)
ggplot(data = economics, aes(x = date, y = psavert)) + geom_line()

#p.198
#Q1
dfdf <- mpg %>%
  filter(class=="compact" | class=="subcompact" | class=="suv")
   #filter(class %in% c("compact", "subcompact", "suv"))
ggplot(data = dfdf, aes(x = class, y = cty)) + geom_boxplot()



