library(ggplot2)
library(dplyr)
require(maps)
require(viridis)
theme_set(
  theme_void()
)


world_map <- map_data("world")
ggplot(world_map, aes(x = long, y = lat, group = group)) +
  geom_polygon(fill="lightgray", colour = "white")

some.countries <- c(
  "Cuba", "Honduras", "Brazil", "Guinea", "DRC",
  "Mozambique", "Madagascar", "Ethiopia", "Egypt",
  "Turkey", "Russia", "Kazakhstan", "Kyrgyzstan",
  "Uzbekistan", "China", "India", "Pakistan",
  "Oman", "Sri Lanka", "Kyrgystan", "Tajikistan", "Nepal", "Bangladesh",
  "Myanmar", "Vietnam", "Cambodia", "Australia"
)
some.maps <- map_data("world", region = some.countries)

region.lab.data <- ()

ggplot(some.maps, aes(x = long, y = lat)) +
  geom_polygon(aes( group = group, fill = region))+
  geom_text(aes(label = region), data = region.lab.data,  size = 3, hjust = 0.5)+
  scale_fill_viridis_d()+
  theme_void()+
  theme(legend.position = "none")
