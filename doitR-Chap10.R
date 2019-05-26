install.packages("rJava")
install.packages("memorise")
install.packages("KoNLP")
install.packages("wordcloud")

library(KoNLP)
library(dplyr)
library(wordcloud)
library(RColorBrewer)

useNIADic()

txt <- readLines("hiphop.txt")
head(txt)

install.packages("stringr")
library(stringr)

txt <- str_replace_all(txt, "\\W", " ")
noun <- extractNoun(txt)
wordcount <- table(unlist(noun))
df_word <- as.data.frame(wordcount, stringsAsFactors = F)
View(df_word)
df_word <- rename(df_word, word = Var1, freq = Freq)

df_word <- filter(df_word, nchar(word) >=2 )

pal <- brewer.pal(8, "Dark2")
set.seed(1234)

wordcloud(words = df_word$word,
          freq = df_word$freq,
          min.freq = 2,
          max.words = 200,
          random.order = F,
          rot.per = .1,
          scale = c(4, 0.3),
          colors = pal)
