install.packages("ggiraphExtra")
install.packages("maps")
install.packages("mapproj")

library(ggiraphExtra)
library(ggplot2)
library(maps)
library(tibble)

str(USArrests)
crime <- rownames_to_column(USArrests, var = "state")
crime$state <- tolower(crime$state)
str(crime)
states_map <- map_data("state")
str(states_map)
ggChoropleth(data = crime,
             aes(fill = Murder,
                 map_id = state),
             map = states_map,
             interactive = T)
