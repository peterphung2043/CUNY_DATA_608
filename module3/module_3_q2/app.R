rm(list=ls())
library(tidyverse)
library(shiny)

# Crude death rate definition: https://www-doh.state.nj.us/doh-shad/view/sharedstatic/CrudeDeathRate.pdf
# We can determine national crude death rate by summing all the deaths
# and all of the populations and then dividing the summed deaths
# by the populations and then multiplying by 1e5..
cdc_mortality_data <- read.csv("https://raw.githubusercontent.com/charleyferrari/CUNY_DATA_608/master/module3/data/cleaned-cdc-mortality-1999-2010-2.csv") %>%
  group_by(Year, ICD.Chapter) %>%
  mutate(national_average_crude_death_rate = (sum(Deaths)/sum(Population))*100000)

# cdc_mortality_data %>%
#   filter(State == 'AL' & ICD.Chapter == "Certain infectious and parasitic diseases") %>%
#   ggplot(aes(x = Year)) +
#   geom_line(aes(y = Crude.Rate, color = "Crude Rate for State")) +
#   geom_line(aes(y = national_average_crude_death_rate, color = "National Average Crude Death Rate")) +
#   scale_color_manual(values = c("blue", "red")) +
#   theme(legend.position = 'bottom')

# See above for the definitions of ui and server
ui <- fluidPage(
  titlePanel("Crude Mortality for Each Cause of Death for Each State vs. National Average"),
  
  sidebarLayout(
    sidebarPanel(
      helpText("Select the cause of death and a state, and a line plot
                will be generated showing the crude death mortality for 
                the state and average crude death mortality for the 
                entire country from 1999 to 2010."),
      selectInput("cause_of_death",
                  label = "Choose a cause of death",
                  choices = unique(cdc_mortality_data$ICD.Chapter)),
      selectInput("state",
                  label = "Choose a state",
                  choices = unique(cdc_mortality_data$State))
    ),
    mainPanel(
      plotOutput("line_chart")
    )
  )
  
)

server <- function(input, output){
  output$line_chart <- renderPlot({
    crude_death_data <- cdc_mortality_data %>%
      filter(State == input$state & ICD.Chapter == input$cause_of_death)
    
    crude_death_data %>%
    ggplot(aes(x = Year)) +
      geom_line(aes(y = Crude.Rate, color = "State Crude Death Rate")) +
      geom_line(aes(y = national_average_crude_death_rate, color = "National Average Crude Death Rate")) +
      scale_color_manual(values = c("blue", "red")) +
      theme(legend.position = 'bottom') +
      theme(text = element_text(size = 20)) +
      guides(color=guide_legend(nrow=2, byrow=TRUE))
  })
}

shinyApp(ui = ui, server = server)