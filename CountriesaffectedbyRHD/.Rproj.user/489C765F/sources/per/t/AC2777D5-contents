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


# Some EU Contries
some.eu.countries <- c(
  "Portugal", "Spain", "France", "Switzerland", "Germany",
  "Austria", "Belgium", "UK", "Netherlands",
  "Denmark", "Poland", "Italy", 
  "Croatia", "Slovenia", "Hungary", "Slovakia",
  "Czech republic"
)
# Retrievethe map data
some.eu.maps <- map_data("world", region = some.eu.countries)

# Compute the centroid as the mean longitude and lattitude
# Used as label coordinate for country's names
region.lab.data <- some.eu.maps %>%
  group_by(region) %>%
  summarise(long = mean(long), lat = mean(lat))
ggplot(some.eu.maps, aes(x = long, y = lat)) +
  geom_polygon(aes( group = group, fill = region))+
  geom_text(aes(label = region), data = region.lab.data,  size = 3, hjust = 0.5)+
  scale_fill_viridis_d()+
  theme_void()+
  theme(legend.position = "none")





library("WHO")
library("dplyr")
life.exp <- get_data("WHOSIS_000001")             # Retrieve the data
life.exp <- life.exp %>%
  filter(year == 2015 & sex == "Both sexes") %>%  # Keep data for 2015 and for both sex
  select(country, value) %>%                      # Select the two columns of interest
  rename(region = country, lifeExp = value) %>%   # Rename columns
  # Replace "United States of America" by USA in the region column
  mutate(
    region = ifelse(region == "United States of America", "USA", region)
  )   

world_map <- map_data("world")
life.exp.map <- left_join(life.exp, world_map, by = "region")

ggplot(life.exp.map, aes(map_id = region, fill = lifeExp))+
  geom_map(map = life.exp.map,  color = "white")+
  expand_limits(x = life.exp.map$long, y = life.exp.map$lat)+
  scale_fill_viridis_c(option = "C")