rm(list=ls())
library(tidyverse)
library(shiny)
library(rsconnect)

# Import data and only use data from 2010.
cdc_mortality_data <- read.csv("https://raw.githubusercontent.com/charleyferrari/CUNY_DATA_608/master/module3/data/cleaned-cdc-mortality-1999-2010-2.csv")
cdc_mortality_data_2010 <- cdc_mortality_data %>%
  filter(Year == 2010) %>%
  group_by(ICD.Chapter)

# See above for the definitions of ui and server
ui <- fluidPage(
  titlePanel("Crude Mortality for Each Cause of Death for America in 2010"),
  
  sidebarLayout(
    sidebarPanel(
      helpText("Select the cause of death, and a bar plot
                will be generated showing the Crude Mortality
                by state for 2010."),
      selectInput("cause_of_death",
                  label = "Choose a cause of death",
                  choices = unique(cdc_mortality_data_2010$ICD.Chapter))
    ),
    mainPanel(
      plotOutput("bar_chart")
    )
  )
  
)

server <- function(input, output){
  output$bar_chart <- renderPlot({
    cause_of_death_data <- filter(cdc_mortality_data_2010,
                                  ICD.Chapter == input$cause_of_death)
    
    cause_of_death_data %>%
      ggplot(aes(x = reorder(State, Crude.Rate), y = Crude.Rate)) +
      geom_bar(stat = "identity") +
      coord_flip() +
      theme(text = element_text(size = 20)) +
      xlab("State") +
      ylab("Crude Mortality")
  }, height = 1000)
}

shinyApp(ui = ui, server = server)