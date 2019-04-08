library(dplyr)
exam <- read.csv("csv_exam.csv")
exam
exam %>% filter(class==2 & (math > 80 | english > 70))
exam %>% filter(class==2 & math>80 | english > 70)
exam %>% filter(class==1 | class==2 | class==4)
exam %>% filter(class %in% c(1, 2, 4))
exam %>% select(math)
exam %>% select(-math)
exam %>% select(class, english)
exam %>% filter(class==3) %>% select(math)
exam %>% filter(math>=70) %>% select(english)
exam %>% select(english) %>% filter(math>=70)
exam %>% 
  filter(math>=70) %>%
  select(english)
exam %>%
  select(id, math) %>%
  head(3)
exam %>% select(math) %>% filter(math>=70) %>% head(3)
exam %>%
  mutate(total = math + english + science) %>%
  head(3)
exam %>%
  mutate(total = math + english + science,
         mean = (math + english + science)/3) %>%
  arrange(total, mean) %>%
  head(3)
exam %>% mutate(result = ifelse(math>=80 & english>=80 & science >= 80, "pass", "fail"))
exam %>% mutate(mean_new = mean(math))
exam %>% summarise(mean_new = mean(math))
exam %>%
  group_by(class) %>%
  summarise(mean_english = mean(english),
            sum_english = sum(english),
            median_english = median(english),
            n = n())

  
  
  